from tkinter import *
import sqlite3

# GUI Setup

class Questionnaire(Frame):

    def __init__(self, master):

        Frame.__init__(self, master)
        self.grid()
        self.create_scroll()
        self.create_buttons()
        self.create_labels()
        self.create_options()

    def create_buttons(self):

        buttonViewQuestions = Button(self, text='View Stored Questions', font=('Helvetica', 18), justify="center")
        buttonViewQuestions.grid(row=0, column=1, columnspan=2, padx=20, pady=20)

        buttonSubmit = Button(self, text='Submit', font=('Helvetica', 18), justify="center")
        # buttonViewQuestions['command']=self.storeResponse
        buttonSubmit.grid(row=10, column=1, columnspan=2, padx=20, pady=20)

    def create_scroll(self):

        self.listProg = Listbox(self, width=100, height=5)
        scroll = Scrollbar(self, command=self.listProg.yview)
        self.listProg.configure(yscrollcommand=scroll.set)

        self.listProg.grid(row=1, column=2, columnspan=3)
        scroll.grid(row=1, column=2, sticky=E)

        conn = sqlite3.connect('mc_question.db')
        c = conn.cursor ()

        with conn:
            cur = conn.execute("SELECT * FROM mc_question")
            for item in (cur.fetchall()):
                self.listProg.insert(END, "ID: " + str(item[0]) + ", Question: " + item[1])
        conn.commit()

        self.listProg.selection_set(END)

    def create_labels(self):

        lblSpecifyID = Label(self, text="Please specify the Question ID you wish to amend/delete (use the Scrollbar"
                                        + " above to view stored questions):", font=("Helvetica", 14, "bold"))
        lblSpecifyID.grid(row=2, column=1, columnspan=2, padx=20, pady=20)

        lblSpecifyOption = Label(self, text="Please specify whether you wish to amend or delete this Question:", font=("Helvetica", 14, "bold"))
        lblSpecifyOption.grid(row=5, column=1, columnspan=2, padx=20, pady=20)

    def create_options(self):

        self.entID = Entry(self)
        self.entID.grid(row=3, column=1, columnspan=2, rowspan=2)

        specifyOptionAmend = Label(self, text="Amend (edit)", font=("Helvetica", 12))
        specifyOptionAmend.grid(row=7, column=1)
        specifyOptionDelete = Label(self, text="Delete", font=("Helvetica", 12))
        specifyOptionDelete.grid(row=7, column=2)

        self.varAmendDelete = IntVar()
        R1AmendDelete = Radiobutton(self, variable=self.varAmendDelete, value=1)
        R1AmendDelete.grid(row=8, column=1)

        R2AmendDelete = Radiobutton(self, variable=self.varAmendDelete, value=2)
        R2AmendDelete.grid(row=8, column=2)



# Main

root = Tk()
root.title("Amend/Delete Questions")
root.geometry("1000x500")
app = Questionnaire(root)
root.mainloop()
