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
            self.question = questionMCClass()
            self.outgoingQuestion = questionMCClass()
            with conn:
                cur = conn.execute("SELECT * FROM MC_QUESTION WHERE PID = {i}".format(i=qID))
                for i in (cur.fetchall()):
                    self.question.qID = i[0]
                    self.question.question = (str(i[1]))
                    self.question.category = (str(i[2]))
                    self.question.difficulty = (str(i[3]))
                    self.question.correct = (str(i[4]))
                    self.question.wrong1 = (str(i[5]))
                    self.question.wrong2 = (str(i[6]))
                    self.question.wrong3 = (str(i[7]))

                cur = conn.execute("SELECT PID FROM MC_QUESTION")
                for i in (cur.fetchall()):
                    idList.append(i[0])

            self.newID = max(idList) + 1


        elif (self.Ans.radioValType == 2):
            self.question = questionTFClass()
            self.outgoingQuestion = questionTFClass()
            with conn:
                cur = conn.execute("SELECT * FROM TF_QUESTION WHERE PID = {i}".format(i=qID))
                for i in (cur.fetchall()):
                    self.question.qID = i[0]
                    self.question.question = (str(i[1]))
                    self.question.category = (str(i[2]))
                    self.question.difficulty = (str(i[3]))
                    self.question.answer = (str(i[4]))

                cur = conn.execute("SELECT PID FROM TF_QUESTION")
                for i in (cur.fetchall()):
                    idList.append(i[0])

            self.newID = max(idList) + 1

        conn.commit()

        self.grid()

        if (self.Ans.radioValType == 1):
            self.create_labelsMC()
            self.create_inputsMC()
        if (self.Ans.radioValType == 2):
            self.create_labelsTF()
            self.create_inputsTF()

        self.create_buttons()

    def create_buttons(self):

        buttonAmend = Button(self, text='Amend Question', font=('Helvetica', 15), justify="center")
        buttonAmend.grid(row=13, column=2, padx=10, pady=10)

        if (self.question.type == "Multiple Choice"):
            buttonAmend['command']=self.addOutgoingMC

        elif (self.question.type == "True/ False"):
            buttonAmend['command']=self.createOutgoingTF

    def create_labelsMC(self):

        lblInfo = Label (self, text="A list of details associated with the question ID specified previously are" +
                        " summarised below.\n" "You may edit (or leave untouced) some of these details and amend/create a revised verison.\n" +
                        " This can be added to the database by clicking the button below.\n" + "A new question ID will be generated, however "
                        + "the former ID will not be deleted.", font=("Helvetica", 10))
        lblInfo.grid(row=1, column=2, padx=10, pady=10)

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

    def create_labelsTF(self):

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

    def create_inputsMC(self):

        lblFQID = Label(self, text=str(self.question.qID), font=("Helvetica", 12))
        lblFQID.grid(row=2, column=2, padx=10, pady=10)

        lblNQID = Label(self, text=self.newID, font=("Helvetica", 12))
        lblNQID.grid(row=3, column=2, padx=10, pady=10)

        lblCI = Label(self, text=self.question.category, font=("Helvetica", 12))
        lblCI.grid(row=4, column=2, padx=10, pady=10)

        lblTI = Label(self, text=self.question.type, font=("Helvetica", 12))
        lblTI.grid(row=5, column=2, padx=10, pady=10)

        self.entDifficulty = Entry(self, width=100)
        self.entDifficulty.grid(row=6, column=2)
        self.entDifficulty.insert(0, self.question.difficulty)

        self.entQuestion = Entry(self, width=100)
        self.entQuestion.grid(row=7, column=2)
        self.entQuestion.insert(0, self.question.question)

        self.entCorrect = Entry(self, width=100)
        self.entCorrect.grid(row=8, column=2)
        self.entCorrect.insert(0, self.question.correct)

        self.entWrong1 = Entry(self, width=100)
        self.entWrong1.grid(row=9, column=2)
        self.entWrong1.insert(0, self.question.wrong1)

        self.entWrong2 = Entry(self, width=100)
        self.entWrong2.grid(row=10, column=2)
        self.entWrong2.insert(0, self.question.wrong2)

        self.entWrong3 = Entry(self, width=100)
        self.entWrong3.grid(row=11, column=2)
        self.entWrong3.insert(0, self.question.wrong3)

    def create_inputsTF(self):

        lblFQID = Label(self, text=str(self.question.qID), font=("Helvetica", 12))
        lblFQID.grid(row=2, column=2, padx=10, pady=10)

        lblNQID = Label(self, text=self.newID, font=("Helvetica", 12))
        lblNQID.grid(row=3, column=2, padx=10, pady=10)

        lblCI = Label(self, text=self.question.category, font=("Helvetica", 12))
        lblCI.grid(row=4, column=2, padx=10, pady=10)

        lblTI = Label(self, text=self.question.type, font=("Helvetica", 12))
        lblTI.grid(row=5, column=2, padx=10, pady=10)

        self.entDifficulty = Entry(self, width=100)
        self.entDifficulty.grid(row=6, column=2)
        self.entDifficulty.insert(0, self.question.difficulty)

        self.entQuestion = Entry(self, width=100)
        self.entQuestion.grid(row=7, column=2)
        self.entQuestion.insert(0, self.question.question)

        if (self.question.answer == "1"):
            self.question.answer = "True"

        if (self.question.answer == "0"):
            self.question.answer ="False"

        self.entCorrect = Entry(self, width=100)
        self.entCorrect.grid(row=8, column=2)
        self.entCorrect.insert(0, self.question.answer)

    def createOutgoingMC(self):

        self.outgoingQuestion.qID = self.newID
        self.outgoingQuestion.category = self.question.category
        self.outgoingQuestion.difficulty = self.entDifficulty.get()
        self.outgoingQuestion.question = self.entQuestion.get()
        self.outgoingQuestion.correct = self.entCorrect.get()
        self.outgoingQuestion.wrong1 = self.entWrong1.get()
        self.outgoingQuestion.wrong2 = self.entWrong2.get()
        self.outgoingQuestion.wrong3 = self.entWrong3.get()

    def createOutgoingTF(self):

        self.outgoingQuestion.qID = self.newID
        self.outgoingQuestion.category = self.question.category
        self.outgoingQuestion.difficulty = self.entDifficulty.get()
        self.outgoingQuestion.question = self.entQuestion.get()
        self.outgoingQuestion.answer = self.entCorrect.get()

    def addOutgoingMC(self):

        createOutgoingMC()

        conn = sqlite3.connect('system.db')
        c = conn.cursor ()

        with conn:
            cur = conn.execute('''INSERT INTO MC_QUESTION (PID, QUESTION,
            CATEGORY, DIFFICULTY, CORRECT, WRONG1, WRONG2,
            WRONG3) VALUES (?,?,?,?,
            ?,?,?)'''

            1=self.outgoingQuestion.qID,
            1=self.outgoingQuestion.category,
            2=self.outgoingQuestion.difficulty,
            3=self.outgoingQuestion.question,
            4=self.outgoingQuestion.correct,
            5=self.outgoingQuestion.wrong1,
            6=self.outgoingQuestion.wrong2,
            7=self.outgoingQuestion.wrong3

        conn.commit()
