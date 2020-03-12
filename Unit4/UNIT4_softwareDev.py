# Unit 4: Elaine
# Enable pupil to take part in a quiz
# Initially the pupil selects the type of quiz i.e. multiple choice or true/false
# The system then randomly picks the questions from the database.

# https://pythonprogramming.net/tkinter-python-3-tutorial-adding-buttons/?completed=/python-3-tkinter-basics-tutorial/

import tkinter as tk
from tkinter import ttk
from tkinter import *
import sqlite3

difficulty = 'Easy'
num_of_quest = 5


class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.question_radio = IntVar()
        self.init_window()

    def init_window(self):
        self.master.title("Pupil - Choose type of quiz")
        self.pack(fill=BOTH, expand=1)
        Label(self, text = "Please choose what type of quiz you would like: ").grid(row=0, sticky=W)
        #Button(self, text="Quit/Back??").grid(row=5, sticky=W)
        Radiobutton(self, text= "True or False Quiz", value = 1, variable = self.question_radio).grid(row=1, sticky=W)
        Radiobutton(self, text= "Multiple Choice Quiz", value = 2, variable = self.question_radio).grid(row=2, sticky=W)
        Button(self, text="Submit choice", command= self.select_questions).grid(row=3, sticky=W)


    def select_questions(self):
        print("select questions function")
        if self.question_radio.get()==1:
            print("ToF selected")
            self.tof_database()
        elif self.question_radio.get()==2:
            print("multiple choice question selected")
            self.mc_database()


    def mc_database(self):
        print("get MC database function")
        db = sqlite3.connect("mc_question.db")
        cursor = db.cursor()
        #cursor.execute("SELECT * FROM MC_QUESTION WHERE DIFFICULTY='Easy' ORDER BY RANDOM() LIMIT 2")
        cursor.execute("SELECT * FROM MC_QUESTION ORDER BY RANDOM() LIMIT 5")
        x = cursor.fetchall()
        cursor.close()
        #return x
        print(x)

    def tof_database(self):
        print("get ToF database function")
        db = sqlite3.connect("tf_question.db")
        cursor = db.cursor()
        cursor.execute("SELECT * FROM TF_QUESTION")
        # i should try to bring back the number of q, type and difficulty level above but need this info from ryann
        x = cursor.fetchall()
        cursor.close()
        return x


root = Tk()

root.geometry("400x300")

app = Window(root)
root.mainloop()

# mc_question = [
#     {
#         'question': 'question1'
#         'answers':['a1','a2','a3'],
#         'correct_answer':'a1'
#     }
# ]
#what type of question e.g. easy or hard etc