#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/8 15:58
# @Author : Tian ZHANG
# @Site : 
# @File : add_question.py
# @Software: PyCharm
# @Version: 1.1


# imports
import tkinter as tk
from tkinter import Menu
from tkinter import messagebox as msg
from tkinter import ttk


class GUI:
    def __init__(self):
        # Create instance
        self.win = tk.Tk()
        # Add a title
        self.win.title('Add Questions')
        # Change the icon
        self.win.iconbitmap('add_q.ico')
        # Create a menu bar with author info
        self.menu_bar = Menu(self.win)
        self.win.config(menu=self.menu_bar)
        self.help_menu = Menu(self.menu_bar, tearoff=0)
        self.help_menu.add_command(label='About', command=self._about_msg)
        self.menu_bar.add_cascade(label='Help', menu=self.help_menu)
        # Create tab control
        self.tab_control = ttk.Notebook(self.win)
        # Create 2 tabs
        self.record_tab = ttk.Frame(self.tab_control)
        self.import_tab = ttk.Frame(self.tab_control)
        # Make the tabs visible
        self.tab_control.add(self.record_tab, text='Record manually')
        self.tab_control.add(self.import_tab, text='Import from file')
        #  Pack to make visible
        self.tab_control.pack(expand=1, fill='both')

        # Text instruction
        self.instruction_r = ttk.Label(self.record_tab, text='You can record a question manually in this tab.\n'
                                                             'Press the buttons below to choose the type of the '
                                                             'question.\n '
                                                             'Press "Generate!" to record the question.')
        self.instruction_r.grid(column=0, row=0, padx=10, pady=8)

        # Create a labelFrame to contain the 2 buttons of choosing question type
        self.record_type = ttk.LabelFrame(self.record_tab, text='Type of the question')
        self.record_type.grid(column=0, row=1, padx=10, pady=8)
        # Create 2 buttons to change the question input format
        self.mc_button = ttk.Button(self.record_type, text='Create a Multiple Choice question', command=self.remove_tf)
        self.mc_button.grid(column=0, row=0, padx=8, pady=5)
        self.tf_button = ttk.Button(self.record_type, text='Create a True or False question', command=self.remove_mc)
        self.tf_button.grid(column=1, row=0, padx=8, pady=5)

        # Create a labelFrame to contain category and difficulty selection
        self.record_cate_diff = ttk.LabelFrame(self.record_tab, text='Category and difficulty level')
        self.record_cate_diff.grid(column=0, row=3, padx=10, pady=8)

        # Widgets for category and difficulty selection
        self.cate_diff_text = ttk.Label(self.record_cate_diff, text='Choose the category:')
        self.cate_diff_text.grid(column=0, row=0, padx=8, pady=5, sticky="W")
        self.category = tk.StringVar()
        self.category_selected = ttk.Combobox(self.record_cate_diff, width=20, textvariable=self.category,
                                              state='readonly')
        self.category_selected['values'] = ("Computer Science", "Cookery", "Nature")
        self.category_selected.grid(column=0, row=1, padx=8, pady=5, sticky="W")
        self.category_selected.current(0)
        self.cate_diff_text = ttk.Label(self.record_cate_diff, text='Choose the difficulty level:')
        self.cate_diff_text.grid(column=1, row=0, padx=8, pady=5, sticky="W")
        self.difficulty_lvl = tk.StringVar()
        self.difficulty_selected = ttk.Combobox(self.record_cate_diff, width=20, textvariable=self.difficulty_lvl,
                                                state='readonly')
        self.difficulty_selected['values'] = ("Easy", "Medium", "Hard")
        self.difficulty_selected.grid(column=1, row=1, padx=8, pady=5, sticky="W")
        self.difficulty_selected.current(0)

        # Create another labelFrame to contain the detail input of the question
        self.record_q = ttk.LabelFrame(self.record_tab, text='Details of the question')
        self.record_q.grid(column=0, row=4, padx=10, pady=8)

        # Widgets for Multiple Choice questions
        self.mc_text = ttk.Label(self.record_q, text='Enter the question: ')
        self.mc_text.grid(column=0, row=0, sticky='W')
        self.mc_question = tk.StringVar()
        self.mc_entered = ttk.Entry(self.record_q, width=50, textvariable=self.mc_question)
        self.mc_entered.grid(column=0, row=1, sticky='W', columnspan=2)
        self.mc_correct_answer_text = ttk.Label(self.record_q, text='Enter the correct answer: ')
        self.mc_correct_answer_text.grid(column=0, row=2, sticky='W')
        self.mc_correct_answer = tk.StringVar()
        self.mc_correct_entry = ttk.Entry(self.record_q, width=50, textvariable=self.mc_correct_answer)
        self.mc_correct_entry.grid(column=0, row=3, sticky='W', columnspan=2)
        self.mc_wrong1_text = ttk.Label(self.record_q, text='Enter the 1st wrong answer: ')
        self.mc_wrong1_text.grid(column=0, row=4, sticky="W")
        self.mc_wrong1 = tk.StringVar()
        self.mc_wrong1_entry = ttk.Entry(self.record_q, width=50, textvariable=self.mc_wrong1)
        self.mc_wrong1_entry.grid(column=0, row=5, sticky="W", columnspan=2)
        self.mc_wrong2_text = ttk.Label(self.record_q, text='Enter the 2nd wrong answer: ')
        self.mc_wrong2_text.grid(column=0, row=6, sticky="W")
        self.mc_wrong2 = tk.StringVar()
        self.mc_wrong2_entry = ttk.Entry(self.record_q, width=50, textvariable=self.mc_wrong2)
        self.mc_wrong2_entry.grid(column=0, row=7, sticky="W", columnspan=2)
        self.mc_wrong3_text = ttk.Label(self.record_q, text='Enter the 3rd wrong answer: ')
        self.mc_wrong3_text.grid(column=0, row=8, sticky="W")
        self.mc_wrong3 = tk.StringVar()
        self.mc_wrong3_entry = ttk.Entry(self.record_q, width=50, textvariable=self.mc_wrong3)
        self.mc_wrong3_entry.grid(column=0, row=9, sticky="W", columnspan=2)

        self.gen_mc_btn = ttk.Button(self.record_q, text='Generate!')
        self.gen_mc_btn.grid(column=0, row=10, padx=8, pady=5, sticky="W")
        self.clr_mc_btn = ttk.Button(self.record_q, text="Clear", command=self.clear_mc)
        self.clr_mc_btn.grid(column=1, row=10, padx=8, pady=5, sticky="W")

        # Widgets for True of False questions
        self.tf_text = ttk.Label(self.record_q, text='Enter the question:')
        self.tf_text.grid(column=0, row=0, sticky="W")
        self.tf_question = tk.StringVar()
        self.tf_entered = ttk.Entry(self.record_q, width=50, textvariable=self.tf_question)
        self.tf_entered.grid(column=0, row=1, sticky='W', columnspan=2)
        self.tf_correct_text = ttk.Label(self.record_q, text='Choose the correct selection:')
        self.tf_correct_text.grid(column=0, row=2, sticky="W")

        self.tf_answer = tk.IntVar()
        self.tf_rad1 = tk.Radiobutton(self.record_q, text="True", variable=self.tf_answer, value=1)
        self.tf_rad1.grid(column=0, row=3, padx=8, pady=5, sticky="W")
        self.tf_rad2 = tk.Radiobutton(self.record_q, text="False", variable=self.tf_answer, value=0)
        self.tf_rad2.grid(column=1, row=3, padx=8, pady=5, sticky="W")

        self.gen_tf_btn = ttk.Button(self.record_q, text='Generate!')
        self.gen_tf_btn.grid(column=0, row=4, padx=8, pady=5, sticky="W")
        self.clr_tf_btn = ttk.Button(self.record_q, text='Clear', command=self.clear_tf)
        self.clr_tf_btn.grid(column=1, row=4, padx=8, pady=5, sticky="W")

        self.initial_record_status()

    @staticmethod
    def _about_msg():
        msg.showinfo('Team 8 - Portfolio B', 'Unit 1 - Add Question\n'
                                             'Version 1.1'
                                             'Unit created by Tian ZHANG.')

    # initialize the record_tab with multiple choice, hide the t&f record widgets
    def initial_record_status(self):
        self.tf_text.grid_remove()
        self.tf_entered.grid_remove()
        self.tf_correct_text.grid_remove()
        self.tf_rad1.grid_remove()
        self.tf_rad2.grid_remove()
        self.gen_tf_btn.grid_remove()
        self.clr_tf_btn.grid_remove()
        self.mc_entered.focus()

    def remove_mc(self):
        self.mc_text.grid_remove()
        self.mc_entered.grid_remove()
        self.mc_correct_answer_text.grid_remove()
        self.mc_correct_entry.grid_remove()
        self.mc_wrong1_text.grid_remove()
        self.mc_wrong1_entry.grid_remove()
        self.mc_wrong2_text.grid_remove()
        self.mc_wrong2_entry.grid_remove()
        self.mc_wrong3_text.grid_remove()
        self.mc_wrong3_entry.grid_remove()
        self.gen_mc_btn.grid_remove()
        self.clr_mc_btn.grid_remove()

        self.tf_text.grid()
        self.tf_entered.grid()
        self.tf_entered.focus()
        self.tf_correct_text.grid()
        self.tf_rad1.grid()
        self.tf_rad2.grid()
        self.gen_tf_btn.grid()
        self.clr_tf_btn.grid()

    def remove_tf(self):
        self.mc_text.grid()
        self.mc_entered.grid()
        self.mc_entered.focus()
        self.mc_correct_answer_text.grid()
        self.mc_correct_entry.grid()
        self.mc_wrong1_text.grid()
        self.mc_wrong1_entry.grid()
        self.mc_wrong2_text.grid()
        self.mc_wrong2_entry.grid()
        self.mc_wrong3_text.grid()
        self.mc_wrong3_entry.grid()
        self.gen_mc_btn.grid()
        self.clr_mc_btn.grid()

        self.tf_text.grid_remove()
        self.tf_entered.grid_remove()
        self.tf_correct_text.grid_remove()
        self.tf_rad1.grid_remove()
        self.tf_rad2.grid_remove()
        self.gen_tf_btn.grid_remove()
        self.clr_tf_btn.grid_remove()

    def clear_mc(self):
        self.mc_entered.delete(0, 'end')
        self.mc_correct_entry.delete(0, 'end')
        self.mc_wrong1_entry.delete(0, 'end')
        self.mc_wrong2_entry.delete(0, 'end')
        self.mc_wrong3_entry.delete(0, 'end')

    def clear_tf(self):
        self.tf_entered.delete(0, 'end')


gui = GUI()
gui.win.mainloop()
