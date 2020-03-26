# Unit 4: Elaine
# Enable pupil to take part in a quiz
# Initially the pupil selects the type of quiz i.e. multiple choice or true/false
# The system then randomly picks the questions from the database.

import sqlite3
import tkinter as tk
from random import shuffle
from tkinter import *
from tkinter import messagebox as msg
from tkinter import ttk

import new_homepage as home
import quiz_button as quiz


def error_popup():
    msg.showerror("Error", "Administrator needs to add questions to the quiz")


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
        ttk.Label(self.root, text="Welcome to the Cardiff University Computer Science Quiz!").grid(row=0, columnspan=2,
                                                                                                   padx=10, pady=8,
                                                                                                   sticky=W)
        ttk.Label(self.root, text="Please choose what type of quiz you would like to take:").grid(row=1, columnspan=2,
                                                                                                  padx=10, pady=8,
                                                                                                  sticky=W)
        self.tf_radio = ttk.Radiobutton(self.root, text="True or False", value=1, variable=self.question_radio).grid(
            column=0, row=2,
            padx=10, pady=8,
            sticky=W)
        self.mc_radio = ttk.Radiobutton(self.root, text="Multiple Choice", value=2, variable=self.question_radio).grid(
            column=1, row=2,
            padx=10,
            pady=8, sticky=W)
        self.button1 = ttk.Button(self.root, text="Submit choice", command=self.select_questions)
        self.button1.grid(row=3, padx=10, pady=8, sticky=W)
        self.label1 = Label(self.root, text=None)
        self.label1.grid(row=3, column=1, padx=10, pady=8, sticky=W)
        self.login_btn = ttk.Button(self.root, text="Back to Homepage", command=self.back_to_home).grid(row=4, column=0,
                                                                                                        padx=10,
                                                                                                        pady=8,
                                                                                                        sticky=W)

    # The following function is called one the 'submit button is clicked'.
    # If True or False or Multiple choice is clicked then the button is then disabled so that multiple request to
    # the database are not made.
    # If submit button is clicked without any radio button selected it will prompt the pupil to select a radio button

    def select_questions(self):
        if self.question_radio.get() == 1:
            self.tof_database()
            # self.label1.config(text="You have chosen a True or False Quiz", fg="Black")
            self.button1.config(state="disabled")
        elif self.question_radio.get() == 2:
            self.mc_database()
            # self.label1.config(text="You have chosen a Multiple Choice Quiz", fg="Black")
            self.button1.config(state="disabled")
        else:
            self.label1.config(text="Remember to choose the type of quiz before you click submit.", fg="Red")

    # The following code brings back either multiple choice or True or False questions from the database in a random
    # order. they are then turned into a list of dictionaries which is the format that is needed for the next unit.
    # multiple choice will also ensure that the answers are shuffled so the correct answer is always at a different
    # index

    def mc_database(self):
        try:
            db = sqlite3.connect("system.db")
            cursor = db.cursor()
            cursor.execute("SELECT * FROM MC_QUESTION ORDER BY RANDOM()")
            x = cursor.fetchall()
            cursor.close()
            question_mockup = []
            for i in x:
                q_dict = {"id": i[0], "question": i[1], "answers": [i[5], i[6], i[7], i[4]], "correct_answer": i[4]}
                a = q_dict["answers"]
                shuffle(a)
                question_mockup.append(q_dict)
            print(question_mockup)
            msg.showinfo("Multiple Choice Quiz", "You have chosen a Multiple Choice Quiz")
            self.quiz_chosen = question_mockup
            self.take_quiz()
        except sqlite3.DatabaseError:
            error_popup()

    def tof_database(self):
        try:
            db = sqlite3.connect("system.db")
            cursor = db.cursor()
            cursor.execute("SELECT * FROM TF_QUESTION ORDER BY RANDOM()")
            x = cursor.fetchall()
            cursor.close()
            question_mockup = []
            for i in x:
                q_dict = {"id": i[0], "question": i[1], "correct_answer": i[4]}
                if q_dict["correct_answer"] == 1:
                    q_dict["correct_answer"] = "True"
                else:
                    q_dict["correct_answer"] = "False"
                question_mockup.append(q_dict)
            # print(question_mockup)
            msg.showinfo("True or False Quiz", "You have chosen a True or False Quiz")
            self.quiz_chosen = question_mockup
            self.take_quiz()
        except sqlite3.DatabaseError:
            error_popup()

    def quit(self):
        self.root.destroy()

    def back_to_home(self):
        self.quit()
        self.back_login = home.Homepage()
        self.root.mainloop()

    def take_quiz(self):
        self.quit()
        self.window = tk.Tk()
        self.quiz = quiz.RenderQuestions(self.window, self.quiz_chosen)
        self.quiz.start_quiz()
        self.window.mainloop()


if __name__ == "__main__":
    app = Window()
    app.root.mainloop()
