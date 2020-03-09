#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/8 15:58
# @Author : Tian ZHANG
# @Site : 
# @File : add_question.py
# @Software: PyCharm
# @Version: 1.0


# imports
import tkinter as tk
from tkinter import ttk


class GUI:
    def __init__(self):
        # Create instance
        self.win = tk.Tk()
        # Add a title
        self.win.title('Add Questions')
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
        # TODO: Complete the instruction paragraph.
        self.instruction_r = ttk.Label(self.record_tab, text='You can record a question manually in this tab.')
        self.instruction_r.grid(column=0, row=0, padx=8, pady=2)
        # Create a label frame to contain the 2 buttons of choosing question type
        self.q_type_choose = ttk.LabelFrame(self.record_tab, text='Type of the question')
        self.q_type_choose.grid(column=0, row=1, padx=8, pady=5)
        # Create 2 buttons to change the question input format
        self.sc_button = ttk.Button(self.q_type_choose, text='Create a Single Choice question', command=self.remove_tf)
        self.sc_button.grid(column=0, row=0, padx=8, pady=5)
        self.tf_button = ttk.Button(self.q_type_choose, text='Create a True or False question', command=self.remove_sc)
        self.tf_button.grid(column=1, row=0, padx=8, pady=5)

        # Create another labelFrame to contain the detail input of the question
        self.record_q = ttk.LabelFrame(self.record_tab, text='Details of the question')
        self.record_q.grid(column=0, row=3, padx=10, pady=8)

        # Widgets for Single Choice questions
        self.sc_text = ttk.Label(self.record_q, text='Enter the question: ')
        self.sc_text.grid(column=0, row=0, sticky='W')
        self.sc_question = tk.StringVar()
        self.sc_entered = ttk.Entry(self.record_q, width=50, textvariable=self.sc_question)
        self.sc_entered.grid(column=0, row=1, sticky='W', columnspan=2)
        self.sc_correct_answer_text = ttk.Label(self.record_q, text='Enter the correct answer: ')
        self.sc_correct_answer_text.grid(column=0, row=2, sticky='W')
        self.sc_correct_answer = tk.StringVar()
        self.sc_correct_entry = ttk.Entry(self.record_q, width=50, textvariable=self.sc_correct_answer)
        self.sc_correct_entry.grid(column=0, row=3, sticky='W', columnspan=2)
        self.sc_wrong1_text = ttk.Label(self.record_q, text='Enter the 1st wrong answer: ')
        self.sc_wrong1_text.grid(column=0, row=4, sticky="W")
        self.sc_wrong1 = tk.StringVar()
        self.sc_wrong1_entry = ttk.Entry(self.record_q, width=50, textvariable=self.sc_wrong1)
        self.sc_wrong1_entry.grid(column=0, row=5, sticky="W", columnspan=2)
        self.sc_wrong2_text = ttk.Label(self.record_q, text='Enter the 2nd wrong answer: ')
        self.sc_wrong2_text.grid(column=0, row=6, sticky="W")
        self.sc_wrong2 = tk.StringVar()
        self.sc_wrong2_entry = ttk.Entry(self.record_q, width=50, textvariable=self.sc_wrong2)
        self.sc_wrong2_entry.grid(column=0, row=7, sticky="W", columnspan=2)
        self.sc_wrong3_text = ttk.Label(self.record_q, text='Enter the 3rd wrong answer: ')
        self.sc_wrong3_text.grid(column=0, row=8, sticky="W")
        self.sc_wrong3 = tk.StringVar()
        self.sc_wrong3_entry = ttk.Entry(self.record_q, width=50, textvariable=self.sc_wrong3)
        self.sc_wrong3_entry.grid(column=0, row=9, sticky="W", columnspan=2)

        self.gen_sc_btn = ttk.Button(self.record_q, text='Generate!')
        self.gen_sc_btn.grid(column=0, row=10, padx=8, pady=5, sticky="W")
        self.clr_sc_btn = ttk.Button(self.record_q, text="Clear", command=self.clear_sc)
        self.clr_sc_btn.grid(column=1, row=10, padx=8, pady=5, sticky="W")

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

    # initialize the record_tab with single choice, hide the t&f record widgets
    def initial_record_status(self):
        self.tf_text.grid_remove()
        self.tf_entered.grid_remove()
        self.tf_correct_text.grid_remove()
        self.tf_rad1.grid_remove()
        self.tf_rad2.grid_remove()
        self.gen_tf_btn.grid_remove()
        self.clr_tf_btn.grid_remove()

    def remove_sc(self):
        self.sc_text.grid_remove()
        self.sc_entered.grid_remove()
        self.sc_correct_answer_text.grid_remove()
        self.sc_correct_entry.grid_remove()
        self.sc_wrong1_text.grid_remove()
        self.sc_wrong1_entry.grid_remove()
        self.sc_wrong2_text.grid_remove()
        self.sc_wrong2_entry.grid_remove()
        self.sc_wrong3_text.grid_remove()
        self.sc_wrong3_entry.grid_remove()
        self.gen_sc_btn.grid_remove()
        self.clr_sc_btn.grid_remove()

        self.tf_text.grid()
        self.tf_entered.grid()
        self.tf_correct_text.grid()
        self.tf_rad1.grid()
        self.tf_rad2.grid()
        self.gen_tf_btn.grid()
        self.clr_tf_btn.grid()

    def remove_tf(self):
        self.sc_text.grid()
        self.sc_entered.grid()
        self.sc_correct_answer_text.grid()
        self.sc_correct_entry.grid()
        self.sc_wrong1_text.grid()
        self.sc_wrong1_entry.grid()
        self.sc_wrong2_text.grid()
        self.sc_wrong2_entry.grid()
        self.sc_wrong3_text.grid()
        self.sc_wrong3_entry.grid()
        self.gen_sc_btn.grid()
        self.clr_sc_btn.grid()

        self.tf_text.grid_remove()
        self.tf_entered.grid_remove()
        self.tf_correct_text.grid_remove()
        self.tf_rad1.grid_remove()
        self.tf_rad2.grid_remove()
        self.gen_tf_btn.grid_remove()
        self.clr_tf_btn.grid_remove()

    def clear_sc(self):
        self.sc_entered.delete(0, 'end')
        self.sc_correct_entry.delete(0, 'end')
        self.sc_wrong1_entry.delete(0, 'end')
        self.sc_wrong2_entry.delete(0, 'end')
        self.sc_wrong3_entry.delete(0, 'end')

    def clear_tf(self):
        self.tf_entered.delete(0, 'end')


gui = GUI()
gui.win.mainloop()
