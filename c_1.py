from tkinter import *
import sqlite3
import tkinter.messagebox
from c_1response import submitResponse
from c_1amendWindow import *

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
        buttonViewQuestions.grid(row=1, column=1, columnspan=2, padx=10, pady=10)

        buttonSubmit = Button(self, text='Submit', font=('Helvetica', 15), justify="center")
        buttonSubmit['command']=self.storeResponse
        buttonSubmit.grid(row=12, column=1, columnspan=2, padx=10, pady=10)

    def create_scroll(self):

        self.listQuestions = Listbox(self, width=58, height=7)
        scroll = Scrollbar(self, command=self.listQuestions.yview)
        self.listQuestions.configure(yscrollcommand=scroll.set)

        self.listQuestions.grid(row=3, column=1, columnspan=2)
        scroll.grid(row=3, column=2, columnspan=2)

    def refreshQuestions(self):

        self.listQuestions.delete(0, END)

        conn = sqlite3.connect('system.db')
        c = conn.cursor ()

        with conn:
            cur = conn.execute("SELECT * FROM MC_QUESTION")
            for item in (cur.fetchall()):
                self.listQuestions.insert(END, "ID: " + str(item[0]) + ", Type: Multiple Choice" ", Question: " + item[1])
            cur = conn.execute("SELECT * FROM TF_QUESTION")
            for item in (cur.fetchall()):
                self.listQuestions.insert(END, "ID: " + str(item[0]) + ", Type: True/ False" ", Question: " + item[1])
        conn.commit()

        self.listQuestions.selection_set(END)

    def create_labels(self):

        lblSpecifyID = Label(self, text="Please note, Question ID's are also associated with Question Type. Hence"
                                        + " why some questions may appear to have the same ID's.", font=("Helvetica", 8))
        lblSpecifyID.grid(row=2, column=1, columnspan=2, padx=10, pady=10)

        lblSpecifyID = Label(self, text="Please specify the Question ID you wish to amend/delete (use the Scrollbar"
                                        + " above to view stored questions):", font=("Helvetica", 12, "bold"))
        lblSpecifyID.grid(row=4, column=1, columnspan=2, padx=10, pady=10)

        lblSpecifyType = Label(self, text="Please specify the Question Type:", font=("Helvetica", 12, "bold"))
        lblSpecifyType.grid(row=6, column=1, columnspan=2, padx=10, pady=10)

        lblSpecifyOption = Label(self, text="Please specify whether you wish to amend or delete this Question:", font=("Helvetica", 12, "bold"))
        lblSpecifyOption.grid(row=9, column=1, columnspan=2, padx=10, pady=10)

    def create_options(self):

        self.entID = Entry(self)
        self.entID.grid(row=5, column=1, columnspan=2)

        specifyOptionMC = Label(self, text="Multiple Choice", font=("Helvetica", 12))
        specifyOptionMC.grid(row=7, column=1)
        specifyOptionTF = Label(self, text="True/ False", font=("Helvetica", 12))
        specifyOptionTF.grid(row=7, column=2)

        self.varType = IntVar()
        R1Type = Radiobutton(self, variable=self.varType, value=1)
        R1Type.grid(row=8, column=1)

        R2Type = Radiobutton(self, variable=self.varType, value=2)
        R2Type.grid(row=8, column=2)

        specifyOptionAmend = Label(self, text="Amend (edit)", font=("Helvetica", 12))
        specifyOptionAmend.grid(row=10, column=1)
        specifyOptionDelete = Label(self, text="Delete", font=("Helvetica", 12))
        specifyOptionDelete.grid(row=10, column=2)

        self.varAmendDelete = IntVar()
        R1AmendDelete = Radiobutton(self, variable=self.varAmendDelete, value=1)
        R1AmendDelete.grid(row=11, column=1)

        R2AmendDelete = Radiobutton(self, variable=self.varAmendDelete, value=2)
        R2AmendDelete.grid(row=11, column=2)

    def storeResponse(self):

        strEntID = self.entID.get()
        strMsg=""

        if strEntID == "":
            strMsg = "You need to specify a Question ID. "

        if (self.varType.get() == 0):
            strMsg = strMsg + "You need to select a Question Type. "

        if (self.varAmendDelete.get() == 0):
            strMsg = strMsg + "You need to select Amend or Delete. "

        if strMsg == "":

            import shelve
            db = shelve.open("responsedb")

            Ans = submitResponse( self.entID.get(), self.varType.get(), self.varAmendDelete.get())

            db["0"] = Ans
            db.close()

            if (self.varAmendDelete.get() == 2) and (self.varType.get() == 1):

                self.removeMCQuestion(Ans)
                self.clearResponse()

            if (self.varAmendDelete.get() == 2) and (self.varType.get() == 2):

                self.removeTFQuestion(Ans)
                self.clearResponse()

            else:

                self.openAmendWindow(Ans)

        else:

            tkinter.messagebox.showwarning("Entry Error", strMsg)

    def clearResponse(self):

        self.varAmendDelete.set(0)
        self.varType.set(0)

        self.entID.delete(0, END)

    def removeMCQuestion(self, Ans):

        qID = int(Ans.qID)

        conn = sqlite3.connect('system.db')
        c = conn.cursor ()

        with conn:
            cur = conn.execute("SELECT * FROM MC_QUESTION WHERE PID = {i}".format(i=qID))
            if len(cur.fetchall()) == 0:
                tkinter.messagebox.showwarning("Question Delete", "Question (ID: " + str(qID) + ") NOT FOUND. Enter a valid Multiple Choice ID")
            else:
                cur = conn.execute("DELETE FROM MC_QUESTION WHERE PID = {i}".format(i=qID))
                tkinter.messagebox.showinfo("Question Delete", "Question (ID: " + str(qID) + ") deleted. Use 'Refresh Stored Questions' button to clarify'")

        conn.commit()

    def removeTFQuestion(self, Ans):

        qID = int(Ans.qID)

        conn = sqlite3.connect('system.db')
        c = conn.cursor ()

        with conn:
            cur = conn.execute("SELECT * FROM TF_QUESTION WHERE PID = {i}".format(i=qID))
            if len(cur.fetchall()) == 0:
                tkinter.messagebox.showwarning("Question Delete", "Question (ID: " + str(qID) + ") NOT FOUND. Enter a valid True/ False ID")
            else:
                cur = conn.execute("DELETE FROM TF_QUESTION WHERE PID = {i}".format(i=qID))
                tkinter.messagebox.showinfo("Question Delete", "Question (ID: " + str(qID) + ") deleted. Use 'Refresh Stored Questions' button to clarify'")

        conn.commit()

    def openAmendWindow(self, Ans):

        qID = int(Ans.qID)

        conn = sqlite3.connect('system.db')
        c = conn.cursor ()

        with conn:
            if (Ans.radioValType == 1):
                cur = conn.execute("SELECT * FROM MC_QUESTION WHERE PID = {i}".format(i=qID))
                if len(cur.fetchall()) == 0:
                    tkinter.messagebox.showwarning("Question Amend", "Question (ID: " + str(qID) + ") NOT FOUND. Enter a valid Multiple Choice ID")
                else:
                    t1 = Toplevel()
                    t1.title("Amend Question")
                    t1.geometry("1000x500")
                    amendQuestion(t1)

            if (Ans.radioValType == 2):
                cur = conn.execute("SELECT * FROM TF_QUESTION WHERE PID = {i}".format(i=qID))
                if len(cur.fetchall()) == 0:
                    tkinter.messagebox.showwarning("Question Amend", "Question (ID: " + str(qID) + ") NOT FOUND. Enter a valid True/ False ID")
                else:
                    t1 = Toplevel()
                    t1.title("Amend Question")
                    t1.geometry("1000x500")
                    amendQuestion(t1)

        conn.commit()



# Main

root = Tk()
root.title("Amend/Delete Questions")
root.geometry("1000x800")
app = Questionnaire(root)
root.mainloop()
