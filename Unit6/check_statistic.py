import os
import sqlite3
import time
import pickle
import tkinter as tk
import quiz_button as unit5
from tkinter import Menu
from tkinter import messagebox as msg
from tkinter import ttk


# import backstage_index as index
"""
final_data = [
            {"id": 1, "question": "q1", "if_correct": 0},
            {"id": 2, "question": "q2", "if_correct": 1},
            {"id": 3, "question": "q3", "if_correct": 0},
            {"id": 4, "question": "q4", "if_correct": 1},
            {"id": 5, "question": "q5", "if_correct": 1},
        ]

class test():  # test for Unit5 get_final_data
    file_number = 7  # file_name is set for answer sheet's number

    def __init__(self):
        self.final_data = [
            {"id": 1, "question": "q1", "if_correct": 1},
            {"id": 2, "question": "q2", "if_correct": 1},
            {"id": 3, "question": "q3", "if_correct": 0},
            {"id": 4, "question": "q4", "if_correct": 1},
            {"id": 5, "question": "q5", "if_correct": 1},
        ]

    def output(self):
        quizdata_folder = "result_data"  # create folder for storing answer sheets

        if quizdata_folder not in os.listdir(os.getcwd()):  # check whether the folder is available
            os.mkdir("result_data")
            os.chdir("result_data")  # make and change to new folder
            # write file end with sequenced number
            asw_data = open("{}.pk".format(self.file_number, "wb"))
            pickle.dump(self.final_data, asw_data)
            asw_data.close()

            # data = open("{}.pk".format(self.file_number), "rb")
            # review_data = pickle.load(data)
            # print(review_data)
            # # print(self.file_number)
        else:
            os.chdir("result_data")
            asw_data = open("{}.pk".format(self.file_number), "wb")
            pickle.dump(self.final_data, asw_data)
            asw_data.close()

            # data = open("{}.pk".format(self.file_number), "rb")
            # review_data = pickle.load(data)
            # print(review_data)
            # # print(self.file_number)

    # def add_one(self):
    #     if test.file_number == 0:
    #         print(self.file_number)
    #         test.file_number += 1
    #         print(self.file_number)
    #     else:
    #         print(self.file_number)
    #         test.file_number += 1
    #         print(self.file_number)

# dict_a = {"id": 1, "question": "q1", "if_correct": 0}
# dict_b = dict_a.copy()
# print(type(dict_b), "\nb: ", dict_b, "\na: ", dict_a, "\nis a = b?", dict_a==dict_b)

test01 = test()
test01.output()
"""
class ckStat():
    files = 0  # file_name is set for answer sheet's number

    def __init__(self):
        # create gui
        self.win = tk.Tk()
        self.win.title("Check  Statistic - Team G")
        self.win.resizable(False, False)

        # set menus
        menu_bar = Menu(self.win)
        self.win.config(menu=menu_bar)
        file_menu = Menu(menu_bar, tearoff=0)

        # create "File" bar
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Back", command=self.go_back)

        # create Tabs
        tabCtrl = ttk.Notebook(self.win, padding=2)
        tab1 = ttk.Frame(tabCtrl)
        tabCtrl.add(tab1, text="Score")
        tabCtrl.pack(expand=1, fill="both")

        # set "Score" Tab
        average_score_Frame = ttk.LabelFrame(tab1, text="Score Display")
        average_score_Frame.grid(column=0, row=0, padx=20, pady=15)

        # display Label:"Score"
        ttk.Label(average_score_Frame, text="This person's Score (%) : ") \
            .grid(column=0, row=1, padx=15, pady=10, sticky="e")

        # set person's score here
        self.average_score = tk.StringVar()
        ttk.Label(average_score_Frame, textvariable=self.average_score, width=20, anchor="center",
                  relief="groove").grid(column=1, row=1, padx=20, pady=10)

        # create "Show Score" Button
        show_score_button = ttk.Button(average_score_Frame, text="Average Score",
                                       command=self.all_score)
        show_score_button.grid(column=0, row=2, padx=10, pady=10)

        # create "Back" Button
        back_button = ttk.Button(average_score_Frame, text="Back", command=self.go_back)
        back_button.grid(column=1, row=2, padx=10, pady=10)

        self.win.mainloop()

    # ============== Functions for GUI ======================

    # quit current window
    def quit(self):
        self.win.destroy()

    # back to homepage
    def go_back(self):
        self.quit()
        # self.back_index = index.GUI()
        # self.win.mainloop()

    # show all score
    def all_score(self):
        self.folder_name = "result_data"
        if self.folder_name in os.listdir(os.getcwd()):
            os.chdir("result_data")
            self.current_score()
        else:
            pass

    # show current score
    def current_score(self):
        self.questionID_list = []  # appeared question id
        self.question_list = []  # appeared questions

        self.correct_answer_num = 0  # show how many answer correct
        # self.question_answer_list = []  # store question answer in sequence
        self.correct_answer_Qid_list = []  # store the correct question's id

        self.correct_id_dict = {}  # store correct id
        self.all_id_list = []  # store all question id

        self.accuracy = 0  # accuracy
        question_counter = 0  # add a question counter

        # count how many .pk files in "result_data"
        for lists in os.listdir(os.getcwd()):
            sub_path = os.path.join(os.getcwd(), lists)
            if os.path.isfile(sub_path):
                self.files += 1

        # get data through those files
        try:
            for file_name in range(self.files):
                data = open("{}.pk".format(file_name), "rb")
                self.review_data = pickle.load(data)
                # print(self.review_data)

                # get each question in quiz
                for x in self.review_data:
                    # print(x)
                    self.questionID_list.append(x.get("id"))
                    if_correct = x.get("if_correct")
                    if if_correct == 1:
                        self.correct_answer_num += 1
                    else:
                        pass

                    # get all question's  id
                    self.all_id_list.append(x.get("id"))
                    # print(self.all_id_list)
        except FileNotFoundError:
            print("Done")
        self.accuracy = self.correct_answer_num / len(self.all_id_list)
        self.average_score.set("{:.2%}".format(self.accuracy))

        # print(self.accuracy)
    # def retrieve_data(self):
    #     self.conn = sqlite3.connect("system.db")
    #     self.c = self.conn.cursor()
    #     self.c.execute("SELECT * FROM STATISTICS")
    #     self.x = self.c.fetchall()
    #     self.conn.commit()
    #     self.conn.close()
    #     self.statistics_mockup = []
    #     for i in self.x:
    #         s_dict = {"id": i[0], "q": i[1], "isCorrect": i[2]}
    #         self.statistics_mockup.append(s_dict)
    #     print(self.statistics_mockup)
    #     return self.statistics_mockup


test01 = ckStat()
test01.current_score()
