from tkinter import *
import sqlite3
import tkinter.messagebox
from c_1questionClass import *

class amendQuestion(Frame):

    def __init__(self, master):

        Frame.__init__(self, master)

        import shelve
        db = shelve.open("responsedb")
        self.Ans = db["0"]
        db.close()

        conn = sqlite3.connect('system.db')
        c = conn.cursor ()

        qID = self.Ans.qID

        idList = []
        self.newID = 0

        if (self.Ans.radioValType == 1):
            question = questionMCClass()
            with conn:
                cur = conn.execute("SELECT * FROM MC_QUESTION WHERE PID = {i}".format(i=qID))
                for i in (cur.fetchall()):
                    question.qID = i[0]
                    question.question = (str(i[1]))
                    question.category = (str(i[2]))
                    question.difficulty = (str(i[3]))
                    question.correct = (str(i[4]))
                    question.wrong1 = (str(i[5]))
                    question.wrong2 = (str(i[6]))
                    question.wrong3 = (str(i[7]))

                cur = conn.execute("SELECT PID FROM MC_QUESTION")
                for i in (cur.fetchall()):
                    idList.append(i[0])

            self.newID = max(idList) + 1


        elif (self.Ans.radioValType == 2):
            question = questionTFClass()
            with conn:
                cur = conn.execute("SELECT * FROM TF_QUESTION WHERE PID = {i}".format(i=qID))
                for i in (cur.fetchall()):
                    question.qID = i[0]
                    question.question = (str(i[1]))
                    question.category = (str(i[2]))
                    question.difficulty = (str(i[3]))
                    question.answer = (str(i[4]))

                cur = conn.execute("SELECT PID FROM TF_QUESTION")
                for i in (cur.fetchall()):
                    idList.append(i[0])

            self.newID = max(idList) + 1

        conn.commit()

        self.grid()
        self.create_buttons()

        if (self.Ans.radioValType == 1):
            self.create_labelsMC(question)
            self.create_inputsMC(question)
        if (self.Ans.radioValType == 2):
            self.create_labelsTF(question)
            self.create_inputsTF(question)

    def create_buttons(self):

        buttonAmend = Button(self, text='Amend Question', font=('Helvetica', 15), justify="center")
        # buttonAmend['command']=self.submitAmend
        buttonAmend.grid(row=13, column=2, padx=10, pady=10)

    def create_labelsMC(self, question):

        lblFormerID = Label(self, text="Former ID:", font=("Helvetica", 12, "bold"))
        lblFormerID.grid(row=2, column=1, padx=10, pady=10)

        lblNewID = Label(self, text="New ID:", font=("Helvetica", 12, "bold"))
        lblNewID.grid(row=3, column=1, padx=10, pady=10)

        lblCategory = Label(self, text="Category:", font=("Helvetica", 12, "bold"))
        lblCategory.grid(row=4, column=1, padx=10, pady=10)

        lblType = Label(self, text="Question Type:", font=("Helvetica", 12, "bold"))
        lblType.grid(row=5, column=1, padx=10, pady=10)

        lblDifficulty = Label(self, text="Difficulty Level:", font=("Helvetica", 12, "bold"))
        lblDifficulty.grid(row=6, column=1, padx=10, pady=10)

        lblQuestion = Label(self, text="Question:", font=("Helvetica", 12, "bold"))
        lblQuestion.grid(row=7, column=1, padx=10, pady=10)

        lblCorrectAnswer = Label(self, text="Correct Answer:", font=("Helvetica", 12, "bold"))
        lblCorrectAnswer.grid(row=8, column=1, padx=10, pady=10)

        lblWrongAnswer1 = Label(self, text="Wrong Answer 1:", font=("Helvetica", 12, "bold"))
        lblWrongAnswer1.grid(row=9, column=1, padx=10, pady=10)

        lblWrongAnswer2 = Label(self, text="Wrong Answer 2:", font=("Helvetica", 12, "bold"))
        lblWrongAnswer2.grid(row=10, column=1, padx=10, pady=10)

        lblWrongAnswer3 = Label(self, text="Wrong Answer 3:", font=("Helvetica", 12, "bold"))
        lblWrongAnswer3.grid(row=11, column=1, padx=10, pady=10)

    def create_labelsTF(self, question):

        lblFormerID = Label(self, text="Former ID:", font=("Helvetica", 12, "bold"))
        lblFormerID.grid(row=2, column=1, padx=10, pady=10)

        lblNewID = Label(self, text="New ID:", font=("Helvetica", 12, "bold"))
        lblNewID.grid(row=3, column=1, padx=10, pady=10)

        lblCategory = Label(self, text="Category:", font=("Helvetica", 12, "bold"))
        lblCategory.grid(row=4, column=1, padx=10, pady=10)

        lblType = Label(self, text="Question Type:", font=("Helvetica", 12, "bold"))
        lblType.grid(row=5, column=1, padx=10, pady=10)

        lblDifficulty = Label(self, text="Difficulty Level:", font=("Helvetica", 12, "bold"))
        lblDifficulty.grid(row=6, column=1, padx=10, pady=10)

        lblQuestion = Label(self, text="Question:", font=("Helvetica", 12, "bold"))
        lblQuestion.grid(row=7, column=1, padx=10, pady=10)

        lblTFAnswer = Label(self, text="Answer:", font=("Helvetica", 12, "bold"))
        lblTFAnswer.grid(row=8, column=1, padx=10, pady=10)

    def create_inputsMC(self, question):

        lblFQID = Label(self, text=str(question.qID), font=("Helvetica", 12))
        lblFQID.grid(row=2, column=2, padx=10, pady=10)

        lblNQID = Label(self, text=self.newID, font=("Helvetica", 12))
        lblNQID.grid(row=3, column=2, padx=10, pady=10)

        lblCI = Label(self, text=question.category, font=("Helvetica", 12))
        lblCI.grid(row=4, column=2, padx=10, pady=10)

        lblTI = Label(self, text=question.type, font=("Helvetica", 12))
        lblTI.grid(row=5, column=2, padx=10, pady=10)

        self.entDifficulty = Entry(self, width=100)
        self.entDifficulty.grid(row=6, column=2)
        self.entDifficulty.insert(0, question.difficulty)

        self.entQuestion = Entry(self, width=100)
        self.entQuestion.grid(row=7, column=2)
        self.entQuestion.insert(0, question.question)

        self.entCorrect = Entry(self, width=100)
        self.entCorrect.grid(row=8, column=2)
        self.entCorrect.insert(0, question.correct)

        self.entWrong1 = Entry(self, width=100)
        self.entWrong1.grid(row=9, column=2)
        self.entWrong1.insert(0, question.wrong1)

        self.entWrong2 = Entry(self, width=100)
        self.entWrong2.grid(row=10, column=2)
        self.entWrong2.insert(0, question.wrong2)

        self.entWrong3 = Entry(self, width=100)
        self.entWrong3.grid(row=11, column=2)
        self.entWrong3.insert(0, question.wrong3)

    def create_inputsTF(self, question):

        lblFQID = Label(self, text=str(question.qID), font=("Helvetica", 12))
        lblFQID.grid(row=2, column=2, padx=10, pady=10)

        lblNQID = Label(self, text=self.newID, font=("Helvetica", 12))
        lblNQID.grid(row=3, column=2, padx=10, pady=10)

        lblCI = Label(self, text=question.category, font=("Helvetica", 12))
        lblCI.grid(row=4, column=2, padx=10, pady=10)

        lblTI = Label(self, text=question.type, font=("Helvetica", 12))
        lblTI.grid(row=5, column=2, padx=10, pady=10)

        self.entDifficulty = Entry(self, width=100)
        self.entDifficulty.grid(row=6, column=2)
        self.entDifficulty.insert(0, question.difficulty)

        self.entQuestion = Entry(self, width=100)
        self.entQuestion.grid(row=7, column=2)
        self.entQuestion.insert(0, question.question)

        self.entCorrect = Entry(self, width=100)
        self.entCorrect.grid(row=8, column=2)
        self.entCorrect.insert(0, question.answer)
