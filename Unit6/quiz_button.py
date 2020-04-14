# coding=utf-8
<<<<<<< HEAD:Unit5/quiz_button.py
<<<<<<< HEAD
import os
import tkinter as tk
import tkinter.font as tf

from tkinter import messagebox
from tkinter import simpledialog
from tkinter import filedialog

[
    {
     "id" : 1,
     "isCorrect": 1
     },
    {
        "id": 2,
        "isCorrect": 0
    },
]

question_mockup = [
    {
        'id': 1,
        'question': 'question1',
        'answers': ['a1', 'a2', 'A computer that has been broken by being flatted and crushed into another object', 'a4'],
        'correct_answer': 'a1'
    },
    {
        'id': 2,
        'question': 'question2',
        'answers': ['a1.1', 'a2', 'a3'],
        'correct_answer': 'a2'
    },
    {
        'id': 3,
        'question': 'question3',
        'answers': ['a1.3', 'a2', 'a3'],
        'correct_answer': 'a3'
    },
    {
        'id': 4,
        'question': 'question4',
        'answers': ['a1.4', 'a2', 'a3'],
        'correct_answer': 'a3'
    },
    {
        'id': 5,
        'question': 'question3',
        'answers': ['a1.5', 'a2', 'a3'],
        'correct_answer': 'a3'
    }
]
=======
import tkinter as tk
import tkinter.font as tf
from tkinter import messagebox

import choose_quiz as unit4


# [
#     {
#      "id" : 1,
#      "isCorrect": 1
#      },
#     {
#         "id": 2,
#         "isCorrect": 0
#     },
# ]
#
=======
import sqlite3
import tkinter as tk
import tkinter.font as tf
import pickle  # Robert edit
import os  # Robert edit
# import check_statistic as unit6  # Robert edit

from tkinter import messagebox

# import choose_quiz as unit4


>>>>>>> Ellie:Unit6/quiz_button.py
# question_mockup = [
#     {
#         'id': 1,
#         'question': 'question1',
<<<<<<< HEAD:Unit5/quiz_button.py
#         'answers': ['a1', 'a2', 'A computer that has been broken by being flatted and crushed into another object', 'a4'],
=======
#         'answers': ['a1', 'a2', 'A computer that has been broken by being flatted and crushed into another object',
#                     'a4'],
>>>>>>> Ellie:Unit6/quiz_button.py
#         'correct_answer': 'a1'
#     },
#     {
#         'id': 2,
#         'question': 'question2',
#         'answers': ['a1.1', 'a2', 'a3'],
#         'correct_answer': 'a2'
#     },
#     {
#         'id': 3,
#         'question': 'question3',
#         'answers': ['a1.3', 'a2', 'a3'],
#         'correct_answer': 'a3'
#     },
#     {
#         'id': 4,
#         'question': 'question4',
#         'answers': ['a1.4', 'a2', 'a3'],
#         'correct_answer': 'a3'
#     },
#     {
#         'id': 5,
<<<<<<< HEAD:Unit5/quiz_button.py
#         'question': 'question3',
=======
#         'question': 'question5',
>>>>>>> Ellie:Unit6/quiz_button.py
#         'answers': ['a1.5', 'a2', 'a3'],
#         'correct_answer': 'a3'
#     }
# ]
<<<<<<< HEAD:Unit5/quiz_button.py
>>>>>>> e94a3e6569b1b1d930c8c0ea7532c731b77ebf33
=======
>>>>>>> Ellie:Unit6/quiz_button.py

# 模块化开发，统一标准，预留接口

class RenderQuestions():

    def __init__(self, window, quiz_list):

        self.window = window
        self.quiz_list = quiz_list
        self.q_length = len(quiz_list)  # The length of quiz
        self.index = 0  # Initial index is 0 to retreive the first question
        self.q_id = 0
        self.question_frame = tk.Frame(window)
        self.l_style = tf.Font(family='Helvetica', size=14)
        self.b_style = tf.Font(family='Helvetica', size=13)
        self.ipad_x = 10  # Padding
        self.ipad_y = 5
        self.corrected_answer = 0
        self.q_title = ''
        self.final_data = []
<<<<<<< HEAD:Unit5/quiz_button.py
<<<<<<< HEAD
                
    def get_question_answer(self):
        question_show = self.quiz_list[self.index]['question']
        answer_show = self.quiz_list[self.index]['answers'] if self.quiz_list[self.index].__contains__('answers') else ['True', 'False']
        correct_answer = self.quiz_list[self.index]['correct_answer']
        self.q_id = self.quiz_list[self.index]['id']  
=======
=======
        # Robert edit
        self.file_number = 0  # file_name is set for answer sheet's number
        # R edit finished
>>>>>>> Ellie:Unit6/quiz_button.py

    def get_question_answer(self):
        question_show = self.quiz_list[self.index]['question']
        answer_show = self.quiz_list[self.index]['answers'] if self.quiz_list[self.index].__contains__('answers') else [
            'True', 'False']
        correct_answer = self.quiz_list[self.index]['correct_answer']
        self.q_id = self.quiz_list[self.index]['id']
<<<<<<< HEAD:Unit5/quiz_button.py
>>>>>>> e94a3e6569b1b1d930c8c0ea7532c731b77ebf33
=======
>>>>>>> Ellie:Unit6/quiz_button.py
        # When get_question_answer is called, index plus one each time in order to go to next question
        self.index += 1
        return question_show, answer_show, correct_answer

    def start_quiz(self):
        self.window.title('Start Quiz')
<<<<<<< HEAD:Unit5/quiz_button.py
<<<<<<< HEAD
        self.window.geometry('650x450')
        quiz_data = self.get_question_answer()
        
        self.question_frame.pack(pady=20)
        # Display quiz question
        tk.Label(self.question_frame, text=quiz_data[0], font=self.l_style, width=30, height=2).pack(pady=10)
        # Display question answers
        choices = quiz_data[1]
        
            
        for i in range(len(choices)):
            button = tk.Button(self.question_frame,
                               text=choices[i], width=30, font=self.b_style, wraplength=200, pady=10, padx=5,
                                command=lambda chosen_answer=choices[i], correct=quiz_data[2]: self.option_click(chosen_answer, correct))
            i += 1
            button.pack(pady=5)
        
        
        # Skip the question
        tk.Button(self.question_frame, text='Skip', font=self.b_style, 
                  command=lambda: self.next_click('skip')).pack(pady=40,side='right', ipadx=self.ipad_x, ipady=self.ipad_y)
        # Finish the quiz
        tk.Button(self.question_frame, text='Finish', font=self.b_style,
                  command=lambda: self.next_click('finish')).pack(pady=40, side='left', ipadx=self.ipad_x, ipady=self.ipad_y)
        
        
=======
=======
>>>>>>> Ellie:Unit6/quiz_button.py
        self.window.minsize(650, 450)
        quiz_data = self.get_question_answer()

        self.question_frame.pack(pady=20)
        # Display quiz question
<<<<<<< HEAD:Unit5/quiz_button.py
        tk.Label(self.question_frame, text=quiz_data[0], font=self.l_style, width=50, wraplength=300).pack(pady=10)
=======
        self.q_title = quiz_data[0]
        tk.Label(self.question_frame, text=self.q_title, font=self.l_style, width=50, wraplength=300).pack(pady=10)
>>>>>>> Ellie:Unit6/quiz_button.py
        # Display question answers
        choices = quiz_data[1]

        for i in range(len(choices)):
            button = tk.Button(self.question_frame,
                               text=choices[i], width=30, font=self.b_style, wraplength=200, pady=10, padx=5,
                               command=lambda chosen_answer=choices[i], correct=quiz_data[2]: self.option_click(
                                   chosen_answer, correct))
            i += 1
            button.pack(pady=5)

        # Skip the question
        tk.Button(self.question_frame, text='Skip', font=self.b_style,
                  command=lambda: self.next_click('skip')).pack(pady=40, side='right', ipadx=self.ipad_x,
                                                                ipady=self.ipad_y)
        # Finish the quiz
        tk.Button(self.question_frame, text='Finish', font=self.b_style,
                  command=lambda: self.next_click('finish')).pack(pady=40, side='left', ipadx=self.ipad_x,
                                                                  ipady=self.ipad_y)

<<<<<<< HEAD:Unit5/quiz_button.py
>>>>>>> e94a3e6569b1b1d930c8c0ea7532c731b77ebf33
=======
>>>>>>> Ellie:Unit6/quiz_button.py
    def option_click(self, chosen_answer, correct):
        if chosen_answer == correct:
            self.corrected_answer += 1
            self.clear_frame()
<<<<<<< HEAD:Unit5/quiz_button.py
            tk.Label(self.question_frame, text='Congradulations! Correct Answer :)', font=self.l_style).pack(pady=20)
<<<<<<< HEAD
            tk.Button(self.question_frame, text='Next', command=lambda:self.next_click('next')).pack(ipadx=self.ipad_x, ipady=self.ipad_y)
=======
            tk.Button(self.question_frame, text='Next', command=lambda: self.next_click('next')).pack(ipadx=self.ipad_x,
                                                                                                      ipady=self.ipad_y)
>>>>>>> e94a3e6569b1b1d930c8c0ea7532c731b77ebf33
            self.data_collection(self.q_id, 1)
=======
            tk.Label(self.question_frame, text='Congratulations! Correct Answer :)', font=self.l_style).pack(pady=20)
            tk.Button(self.question_frame, text='Next', command=lambda: self.next_click('next')).pack(ipadx=self.ipad_x,
                                                                                                      ipady=self.ipad_y)
            self.data_collection(self.q_id, self.q_title, 1)
>>>>>>> Ellie:Unit6/quiz_button.py
        else:
            self.clear_frame()
            i_pady = 0
            tk.Label(self.question_frame, text='Oops, Wrong Answer', font=self.l_style).pack(pady=i_pady)
<<<<<<< HEAD:Unit5/quiz_button.py
<<<<<<< HEAD
            tk.Label(self.question_frame, text='The correct answer is %s' % correct, font=self.l_style).pack(pady=i_pady)
            tk.Label(self.question_frame,text='Good luck with next time!', font=self.l_style).pack(pady=i_pady)
            tk.Button(self.question_frame, text='Next', font=self.b_style, command=lambda: self.next_click('next')).pack(pady=10, ipadx=self.ipad_x, ipady=self.ipad_y)
            self.data_collection(self.q_id, 0)
            
    def next_click(self, status):        
=======
=======
>>>>>>> Ellie:Unit6/quiz_button.py
            tk.Label(self.question_frame, text='The correct answer is %s' % correct, font=self.l_style).pack(
                pady=i_pady)
            tk.Label(self.question_frame, text='Good luck with next time!', font=self.l_style).pack(pady=i_pady)
            tk.Button(self.question_frame, text='Next', font=self.b_style,
                      command=lambda: self.next_click('next')).pack(pady=10, ipadx=self.ipad_x, ipady=self.ipad_y)
            self.data_collection(self.q_id, self.q_title, 0)

    def next_click(self, status):
<<<<<<< HEAD:Unit5/quiz_button.py
>>>>>>> e94a3e6569b1b1d930c8c0ea7532c731b77ebf33
=======
>>>>>>> Ellie:Unit6/quiz_button.py
        # Determine if the current question index smaller than the quiz length to continue or finish
        if status == 'skip' and self.index < self.q_length:
            self.data_collection(self.q_id, self.q_title, 0)
            self.clear_frame()
            self.start_quiz()
        elif status == 'next' and self.index < self.q_length:
            self.clear_frame()
            self.start_quiz()
        elif status == 'finish':  # When user clicks finish button
            self.finish_quiz('finish_clicked')
        elif not self.index < self.q_length:
            self.finish_quiz('main')
<<<<<<< HEAD:Unit5/quiz_button.py
<<<<<<< HEAD
            
=======

>>>>>>> e94a3e6569b1b1d930c8c0ea7532c731b77ebf33
=======

>>>>>>> Ellie:Unit6/quiz_button.py
    def finish_quiz(self, type):
        # Alert pops up when user try to finish the whole quiz
        if type == 'finish_clicked':
            if_finish = tk.messagebox.askyesno(title='Confirmation', message='Are you sure to finish the whole quiz?')
            if if_finish:
                self.clear_frame()
                self.result_display()
<<<<<<< HEAD:Unit5/quiz_button.py
<<<<<<< HEAD
                #拿到目前的题目ID，用总长度减去目前的得到剩余的题目长度来循环
                #循环的时候让目前题目ID加上增量 i ，以把剩下的题目都判断为错
=======
                # 拿到目前的题目ID，用总长度减去目前的得到剩余的题目长度来循环
                # 循环的时候让目前题目ID加上增量 i ，以把剩下的题目都判断为错
>>>>>>> e94a3e6569b1b1d930c8c0ea7532c731b77ebf33
                # When pupil chose finish, the rest of questions are all marked as wrong 
                # Get the current question ID and use the total length of quiz question subtract 
=======
                # 拿到目前的题目ID，用总长度减去目前的得到剩余的题目长度来循环
                # 循环的时候让目前题目ID加上增量 i ，以把剩下的题目都判断为错
                # When pupil chose finish, the rest of questions are all marked as wrong
                # Get the current question ID and use the total length of quiz question subtract
>>>>>>> Ellie:Unit6/quiz_button.py
                # the current ID to get the remaining question length to loop as wrong answers
                current_id = self.q_id
                left_question = self.q_length - current_id + 1
                # * 拿到目前的题目下标，然后用总长度减去目前的看还剩几个
                # * 用剩的题目循环，从目前的标下开始传题目问题

                for i in range(left_question):
                    temp = self.quiz_list[current_id + i - 1]['question']  # Current question
                    self.data_collection(current_id + i, temp, 0)
                print(self.final_data)

                # for current_id in range(len(self.quiz_list)):
                #     new_index = current_id + 1
                #     if len(self.quiz_list) - current_id > 0:
                #         print(self.quiz_list[current_id]['question'])
                #     print(new_index)

            else:
                return False
        else:
            self.clear_frame()
            self.result_display()

<<<<<<< HEAD:Unit5/quiz_button.py
<<<<<<< HEAD
            
    def result_display(self):
        tk.Label(self.question_frame, text='You finished all the questions!', font=self.l_style).pack()
        tk.Label(self.question_frame, text='You\'ve got %d answer(s) corrected' % self.corrected_answer, font=self.l_style).pack()
        tk.Label(self.question_frame, text='Thank you for taking this quiz :)', font=self.l_style).pack()
        tk.Button(self.question_frame, text='Restart', command=self.restart).pack(pady=10, ipadx=5, ipady=3)
        print(self.final_data)
            
            
    def restart(self):
        # need API from unit 4
        # Initialize this below when start a nee quiz
        self.corrected_answer = 0 
        self.clear_frame()
        self.index = 0
        self.final_data = []
        
        self.start_quiz()
    
=======
=======
>>>>>>> Ellie:Unit6/quiz_button.py
    def result_display(self):
        tk.Label(self.question_frame, text='You finished all the questions!', font=self.l_style).pack()
        tk.Label(self.question_frame, text='You\'ve got %d answer(s) correct' % self.corrected_answer,
                 font=self.l_style).pack()
        tk.Label(self.question_frame, text='Thank you for taking this quiz :)', font=self.l_style).pack()
        tk.Button(self.question_frame, text='Restart', command=self.restart).pack(pady=10, ipadx=5, ipady=3)
        print(self.final_data)

    def restart(self):
        # need API from unit 4
        # Initialize this below when start a nee quiz
        # self.corrected_answer = 0
        # self.clear_frame()
        # self.index = 0
        # self.final_data = []
<<<<<<< HEAD:Unit5/quiz_button.py
=======
        self.get_final_data()
>>>>>>> Ellie:Unit6/quiz_button.py
        self.window.destroy()
        self.choose = unit4.Window()
        self.choose.root.mainloop()

<<<<<<< HEAD:Unit5/quiz_button.py
>>>>>>> e94a3e6569b1b1d930c8c0ea7532c731b77ebf33
    def data_collection(self, passed_id, if_correct):
        temp = {'id': passed_id, "if_correct": if_correct}
        self.final_data.append(temp.copy())
        print(self.final_data)
<<<<<<< HEAD
        
    def get_final_data(self):
        return self.final_data
             
    def clear_frame(self):
         for widget in self.question_frame.winfo_children():  # clear widgets in frame
                widget.destroy()
=======

    def get_final_data(self):
        return self.final_data
=======
    def data_collection(self, passed_id, passed_title, if_correct):
        temp = {'id': passed_id, 'question': passed_title, 'if_correct': if_correct}
        self.final_data.append(temp.copy())
        # print(self.final_data)

    # ========= Robert edit ===========
    def get_final_data(self):

        quizdata_folder = "result_data"  # create folder for storing answer sheets

        # the "file_name" below is set for answer sheet's number
        if quizdata_folder not in os.listdir(os.getcwd()):  # check whether the folder is available
            os.mkdir("result_data")
            os.chdir("result_data")  # make and change to new folder
            # write file end with sequenced number
            asw_data = open("{}.pk".format(self.file_number, "wb"))
            pickle.dump(self.final_data, asw_data)
            asw_data.close()
        else:
            os.chdir("result_data")
            asw_data = open("{}.pk".format(self.file_number), "wb")
            pickle.dump(self.final_data, asw_data)
            asw_data.close()
        self.file_number += 1

        # self.final_data_ls = []
        # self.temp_ls = []
        # for item in self.final_data:
        #     self.temp_ls.append(item["id"])
        #     self.temp_ls.append(item["question"])
        #     self.temp_ls.append(item["if_correct"])
        #     self.final_data_ls.append(tuple(self.temp_ls))
        #     self.temp_ls = []
        #     print(self.final_data_ls)
        # self.conn = sqlite3.connect("system.db")
        # self.c = self.conn.cursor()
        # self.c.execute('''CREATE TABLE IF NOT EXISTS STATISTICS (ID INTEGER NOT NULL, QUESTION
        # TEXT NOT NULL, IF_CORRECT INTEGER NOT NULL)''')
        # self.c.executemany("INSERT INTO STATISTICS (ID, QUESTION, IF_CORRECT) VALUES (?, ?, ?)", self.final_data_ls)
        # self.conn.commit()
        # self.conn.close()
        # =======================================================
        # save each answer sheet data in a single file
        # ========== R Edit finished ============
>>>>>>> Ellie:Unit6/quiz_button.py

    def clear_frame(self):
        for widget in self.question_frame.winfo_children():  # clear widgets in frame
            widget.destroy()
<<<<<<< HEAD:Unit5/quiz_button.py
>>>>>>> e94a3e6569b1b1d930c8c0ea7532c731b77ebf33

=======
>>>>>>> Ellie:Unit6/quiz_button.py

if __name__ == '__main__':
    window = tk.Tk()
    # Render interface
    render = RenderQuestions(window, question_mockup)
    render.start_quiz()
<<<<<<< HEAD:Unit5/quiz_button.py
<<<<<<< HEAD
    
=======

>>>>>>> e94a3e6569b1b1d930c8c0ea7532c731b77ebf33
=======

>>>>>>> Ellie:Unit6/quiz_button.py
    window.mainloop()
