from tkinter import *
import sqlite3
import tkinter.messagebox
from c_1response import submitResponse

# GUI Setup

class Questionnaire(Frame):

    def __init__(self, master):

        Frame.__init__(self, master)
        self.grid()
        self.create_scroll()
        self.create_buttons()
        self.create_labels()
        self.create_options()
        self.storeResponse()

    def create_buttons(self):

        buttonViewQuestions = Button(self, text='Refresh Stored Questions', font=('Helvetica', 15), justify="center")
        buttonViewQuestions['command']=self.refreshQuestions
        buttonViewQuestions.grid(row=0, column=1, columnspan=2, padx=10, pady=10)

        buttonSubmit = Button(self, text='Submit', font=('Helvetica', 15), justify="center")
        buttonSubmit['command']=self.storeResponse
        buttonSubmit.grid(row=7, column=1, columnspan=2, padx=10, pady=10)

    def create_scroll(self):

        self.listQuestions = Listbox(self, width=58, height=7)
        scroll = Scrollbar(self, command=self.listQuestions.yview)
        self.listQuestions.configure(yscrollcommand=scroll.set)

        self.listQuestions.grid(row=1, column=1, columnspan=2)
        scroll.grid(row=1, column=2, columnspan=2)

    def refreshQuestions(self):

        self.listQuestions.delete(0, END)

        conn = sqlite3.connect('mc_question.db')
        c = conn.cursor ()

        with conn:
            cur = conn.execute("SELECT * FROM mc_question")
            for item in (cur.fetchall()):
                self.listQuestions.insert(END, "ID: " + str(item[0]) + ", Question: " + item[1])
        conn.commit()

        self.listQuestions.selection_set(END)

    def create_labels(self):

        lblSpecifyID = Label(self, text="Please specify the Question ID you wish to amend/delete (use the Scrollbar"
                                        + " above to view stored questions):", font=("Helvetica", 12, "bold"))
        lblSpecifyID.grid(row=2, column=1, columnspan=2, padx=10, pady=10)

        lblSpecifyOption = Label(self, text="Please specify whether you wish to amend or delete this Question:", font=("Helvetica", 12, "bold"))
        lblSpecifyOption.grid(row=4, column=1, columnspan=2, padx=10, pady=10)

    def create_options(self):

        self.entID = Entry(self)
        self.entID.grid(row=3, column=1, columnspan=2)

        specifyOptionAmend = Label(self, text="Amend (edit)", font=("Helvetica", 12))
        specifyOptionAmend.grid(row=5, column=1)
        specifyOptionDelete = Label(self, text="Delete", font=("Helvetica", 12))
        specifyOptionDelete.grid(row=5, column=2)

        self.varAmendDelete = IntVar()
        R1AmendDelete = Radiobutton(self, variable=self.varAmendDelete, value=1)
        R1AmendDelete.grid(row=6, column=1)

        R2AmendDelete = Radiobutton(self, variable=self.varAmendDelete, value=2)
        R2AmendDelete.grid(row=6, column=2)

    def storeResponse(self):

        strEntID = self.entID.get()
        strMsg=""

        if strEntID == "":
            strMsg = "You need to specify a Question ID."

        if (self.varAmendDelete.get() == 0):
            strMsg = strMsg + "You need to select Amend or Delete"

        if strMsg == "":

            import shelve
            db = shelve.open("responsedb")

            Ans = submitResponse( self.entID.get(), self.varAmendDelete.get())

            db["0"] = Ans
            db.close()

            if (self.varAmendDelete.get() == 2):

                self.removeQuestion(Ans)
                self.clearResponse()

            else:

                print("Amend selected")

        else:

            tkinter.messagebox.showwarning("Entry Error", strMsg)

    def clearResponse(self):

        self.varAmendDelete.set(0)

        self.entID.delete(0, END)

    def removeQuestion(self, Ans):

        qID = int(Ans.qID)

        conn = sqlite3.connect('mc_question.db')
        c = conn.cursor ()

        with conn:
            cur = conn.execute("SELECT * FROM mc_question WHERE PID = {i}".format(i=qID))
            if len(cur.fetchall()) == 0:
                tkinter.messagebox.showwarning("Question Delete", "Question (ID: " + str(qID) + ") NOT FOUND. Enter a valid ID")
            else:
                cur = conn.execute("DELETE FROM mc_question WHERE PID = {i}".format(i=qID))
                tkinter.messagebox.showinfo("Question Delete", "Question (ID: " + str(qID) + ") deleted. Use 'Refresh Stored Questions' button to clarify'")

        conn.commit()



# Main

root = Tk()
root.title("Amend/Delete Questions")
root.geometry("1000x500")
app = Questionnaire(root)
root.mainloop()
