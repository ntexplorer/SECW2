# Unit 4: Elaine
# Enable pupil to take part in a quiz
# Initially the pupil selects the type of quiz i.e. multiple choice or true/false
# The system then randomly picks the questions from the database.

import sqlite3
import tkinter as tk
from random import shuffle
from tkinter import *
from tkinter import messagebox as msg

import login


class Window:
    def __init__(self):
        self.root = tk.Tk()
        # Add a title
        self.root.title('Choose your quiz! by Team G')
        self.root.geometry("600x400")
        self.question_radio = IntVar()
        self.init_window()

    # the following function sets out the GUI layout. Radiobutton as been used for selection so that only one choice
    # can be made to reduce potential errors.

    def init_window(self):
        Label(self.root, text="Welcome to the Cardiff University Computer Science Quiz!").grid(row=0, padx=8, pady=20,
                                                                                               sticky=W)
        Label(self.root, text="Please choose what type of quiz you would like to take:").grid(row=2, padx=8, pady=8,
                                                                                              sticky=W)
        Radiobutton(self.root, text="True or False", value=1, variable=self.question_radio).grid(row=4, padx=8, pady=8,
                                                                                                 sticky=W)
        Radiobutton(self.root, text="Multiple Choice", value=2, variable=self.question_radio).grid(row=5, padx=8,
                                                                                                   pady=8, sticky=W)
        self.button1 = Button(self.root, text="Submit choice", command=self.select_questions)
        self.button1.grid(row=7, padx=8, pady=8, sticky=W)
        self.label1 = Label(self.root, text=None)
        self.label1.grid(row=9, padx=8, pady=8, sticky=W)
        self.login_btn = Button(self.root, text="Login as Admin", command=self.goto_login).grid(row=10, padx=8, pady=40,
                                                                                                sticky=W)

    # The following fuction is called one the 'submit button is clicked'.
    # If True or False or Multiple choice is clicked then the button is then disabled so that multiple request to
    # the database are not made.
    #If submit button is clicked without any radio button selected it will prompt the pupil to select a radio button

    def select_questions(self):
        if self.question_radio.get() ==1:
            self.tof_database()
            self.label1.config(text="You have chosen a True or False Quiz", fg="Black")
            self.button1.config(state="disabled")
        elif self.question_radio.get() ==2:
            self.mc_database()
            self.label1.config(text="You have chosen a Multiple Choice Quiz", fg="Black")
            self.button1.config(state="disabled")
        else:
            self.label1.config(text="Remember to choose the type of quiz before you click submit.", fg="Red")

    # The following code brings back either multiple choice or True or False questions from the database in a random order.
    # they are then turned into a list of dictionarys which is the format that is needed for the next unit.
    #multiple choice will also ensure that the answers are shuffled so the correct answer is always at a different index

    def mc_database(self):
        try:
            db = sqlite3.connect("system.db")
            cursor = db.cursor()
            cursor.execute("SELECT * FROM MC_QUESTION ORDER BY RANDOM()")
            x = cursor.fetchall()
            cursor.close()
            question_mockup = []
            for i in x:
                dict = {"id": i[0], "question": i[2], "answers": [i[5], i[6], i[7], i[4]], "correct_answer": i[4]}
                a = dict["answers"]
                shuffle(a)
                question_mockup.append(dict)
            print(question_mockup)
            return question_mockup
        except:
            self.error_popup()

    def tof_database(self):
        try:
            db = sqlite3.connect("system.db")
            cursor = db.cursor()
            cursor.execute("SELECT * FROM TF_QUESTION ORDER BY RANDOM()")
            x = cursor.fetchall()
            cursor.close()
            question_mockup = []
            for i in x:
                dict = {"id": i[0], "question": i[1], "correct_answer": i[4]}
                if dict["correct_answer"] == 1:
                    dict["correct_answer"] = "True"
                else:
                    dict["correct_answer"] = "False"
                question_mockup.append(dict)
            # print(question_mockup)
            return question_mockup
        except:
            self.error_popup()

    def error_popup(self):
        msg.showerror("Error", "Administrator needs to add questions to the quiz")

    def quit(self):
        self.root.destroy()

    def goto_login(self):
        self.quit()
        self.back_login = login.GUI()
        self.root.mainloop()


if __name__ == "__main__":
    app = Window()
    app.root.mainloop()
