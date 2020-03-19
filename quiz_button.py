# coding=utf-8
import os
import tkinter as tk
import tkinter.font as tf

from tkinter import messagebox
from tkinter import simpledialog
from tkinter import filedialog

question_mockup = [
    {
        'id': 1,
        'question': 'question1',
        'answers': ['a1', 'a2', 'a3'],
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
]

# 模块化开发，统一标准，预留接口
# restart 直接把前面的类 import 进来
# 按钮点击的时候也会有点击的效果
# * radio要点击了之后才会把数据传到变量里面，所以值不能通过command传，要在command的函数里面才能拿到
# todo 收集答题数据

class RenderQuestions():
    def __init__(self, window, quiz_list):
        self.window = window
        self.quiz_list = quiz_list
        self.q_length = len(quiz_list)  # 问题的长度（一共多少个）
        self.index = 0  # 初始的下标是 0，来获得第quiz的第一个文件
        self.question_frame = tk.Frame(window)
        self.l_style = tf.Font(family='Helvetica', size=14)
        self.b_style = tf.Font(family='Helvetica', size=13)
        self.ipad_x = 10  #内边距
        self.ipad_y = 5
        self.corrected_answer = 0
        self.q_data = []

                
    def get_question_answer(self):
        question_show = self.quiz_list[self.index]['question']
        answer_show = self.quiz_list[self.index]['answers'] if self.quiz_list[self.index].__contains__('answers') else ['True', 'False']
        correct_answer = self.quiz_list[self.index]['correct_answer']
        self.index += 1  # 每一次调用 get_question_answer 下标就加一
        return question_show, answer_show, correct_answer

    def start_quiz(self):
        self.window.title('Start Quiz')
        self.window.geometry('600x400')
        quiz_data = self.get_question_answer()
        
        self.question_frame.pack(pady=20)
        # 展示 quiz 问题
        tk.Label(self.question_frame, text=quiz_data[0], font=self.l_style, width=30, height=2).pack()
        # 显示问题的可选答案，并传入正确答案
        choices = quiz_data[1]
        
            
        for i in range(len(choices)):
            button = tk.Button(self.question_frame,
                                text=choices[i], width=20, height=2, font=self.b_style,
                                command=lambda chosen_answer=choices[i], correct=quiz_data[2]: self.option_click(chosen_answer, correct))
            i += 1
            button.pack(pady=5)
        
        
        # 跳过问题
        tk.Button(self.question_frame, text='Skip', font=self.b_style, 
                  command=lambda: self.next_click('skip')).pack(pady=40,side='right', ipadx=self.ipad_x, ipady=self.ipad_y)
        tk.Button(self.question_frame, text='Finish', font=self.b_style,
                  command=lambda: self.next_click('finish')).pack(pady=40, side='left', ipadx=self.ipad_x, ipady=self.ipad_y)
        
        

    def option_click(self, chosen_answer, correct):
        # print(chosen_answer)
        # correct_answer = quiz_data[2]
        if_confirm = tk.messagebox.askyesno(title='Confirmation', message='Are you sure to choose %s?' % chosen_answer)
        if if_confirm:
            if chosen_answer == correct:
                self.corrected_answer += 1
                self.clear_frame()
                tk.Label(self.question_frame, text='Congradulations! Correct Answer :)', font=self.l_style).pack(pady=20)
                tk.Button(self.question_frame, text='Next', command=lambda:self.next_click('next')).pack(ipadx=self.ipad_x, ipady=self.ipad_y)
            else:
                self.clear_frame()
                i_pady = 0
                tk.Label(self.question_frame, text='Oops, Wrong Answer', font=self.l_style).pack(pady=i_pady)
                tk.Label(self.question_frame, text='The correct answer is %s' % correct, font=self.l_style).pack(pady=i_pady)
                tk.Label(self.question_frame,text='Good luck with next time!', font=self.l_style).pack(pady=i_pady)
                tk.Button(self.question_frame, text='Next', font=self.b_style, command=lambda: self.next_click('next')).pack(pady=10, ipadx=self.ipad_x, ipady=self.ipad_y)
        else:
            return False
        
        print('-------')
        print(chosen_answer)
        print(correct)
        print(self.corrected_answer)
            
    def next_click(self, status):
        if status == 'skip' or status == 'next':
            #判断当前的题目是否大于总题目长度
            if self.index < self.q_length:
                self.clear_frame()
                self.start_quiz()
            else:
                self.finish_quiz('main')
        else:
            self.finish_quiz('alter')
    
    def finish_quiz(self, type):
        # 当用户直接跳过的时候弹出确认信息
        if type == 'alter':
            if_finish = tk.messagebox.askyesno(title='Confirmation', message='Are you sure to finish the whole quiz?')
            if if_finish:
                self.clear_frame()
                self.result_display()
            else:
                return False
        else:
            self.clear_frame()
            self.result_display()

            
    def result_display(self):
        tk.Label(self.question_frame, text='You finished all the questions!', font=self.l_style).pack()
        tk.Label(self.question_frame, text='You\'ve got %d answer(s) corrected' % self.corrected_answer, font=self.l_style).pack()
        tk.Label(self.question_frame, text='Thank you for taking this quiz :)', font=self.l_style).pack()
        tk.Button(self.question_frame, text='Restart', command=self.restart).pack(pady=10, ipadx=5, ipady=3)
            
            
    def restart(self):
        # need API from unit 4
        self.corrected_answer = 0  #重新开始的时候把上局的正确答案清零
        self.clear_frame()
        self.index = 0
        self.start_quiz()
    
    def quiz_data(self):
        # 不要重复命名
        return self.q_data  # data for next unit 
             
    def clear_frame(self):
         for widget in self.question_frame.winfo_children():  # clear widgets in frame
                widget.destroy()


if __name__ == '__main__':
    window = tk.Tk()
    # 渲染界面
    render = RenderQuestions(window, question_mockup)
    render.start_quiz()
    
    window.mainloop()
