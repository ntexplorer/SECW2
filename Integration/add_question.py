#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/12 20:12
# @Author : Tian ZHANG
# @Site : 
# @File : add_question.py
# @Software: PyCharm
# @Version: 2.2

# Imports
import csv
import sqlite3
import tkinter as tk
from time import sleep
from tkinter import Menu
from tkinter import filedialog
from tkinter import messagebox as msg
from tkinter import ttk

# Import template file for next and last GUI
import backstage_index as index


# import next_GUI_sample as unit2


class GUI:
    def __init__(self):
        # Create instance
        self.win = tk.Tk()
        # Add a title
        self.win.title('Add Questions - Quiz System by Team G')
        # Change the icon
        # This function is not supported on School laptop, so have to remove it
        # self.win.iconbitmap('add_q.ico')
        # Create a menu bar with author info
        self.menu_bar = Menu(self.win)
        self.win.config(menu=self.menu_bar)
        self.sys_menu = Menu(self.menu_bar, tearoff=0)
        self.sys_menu.add_command(label='Go to question operation Unit', command=self.goto_op)
        self.sys_menu.add_command(label='Return to Index', command=self.goto_index)
        self.menu_bar.add_cascade(label='System', menu=self.sys_menu)
        self.help_menu = Menu(self.menu_bar, tearoff=0)
        self.help_menu.add_command(label='About', command=self._about_msg)
        self.menu_bar.add_cascade(label='Help', menu=self.help_menu)
        # Create tab control
        self.tab_control = ttk.Notebook(self.win)
        # Create 3 tabs
        self.record_tab = ttk.Frame(self.tab_control)
        self.import_tab = ttk.Frame(self.tab_control)
        self.display_tab = ttk.Frame(self.tab_control)
        # Make the tabs visible
        self.tab_control.add(self.record_tab, text='Record manually')
        self.tab_control.add(self.import_tab, text='Import from file')
        self.tab_control.add(self.display_tab, text='Question display')
        #  Pack to make visible
        self.tab_control.pack(expand=1, fill='both')

        # ====================== Element for record tab ========================
        # Text instruction for record tab
        self.instruction_r = ttk.Label(self.record_tab, text='* Record a question manually in this tab.\n'
                                                             '* Press the buttons below to select the type of '
                                                             'question.\n'
                                                             '* Press "Generate!" button to record question.\n'
                                                             '* Press "Clear" button to clear the input.')
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
        self.category_selected['values'] = ("Computer Science", "Art", "Nature", "Food", "History", "Language",
                                            "Sports", "Video Game", "Music")
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
        # 2 buttons to generate database and clear input
        self.gen_mc_btn = ttk.Button(self.record_q, text='Generate!', command=self.gen_mc_db)
        self.gen_mc_btn.grid(column=0, row=10, padx=8, pady=5, sticky="W")
        self.clr_mc_btn = ttk.Button(self.record_q, text="Clear", command=self.clear_mc)
        self.clr_mc_btn.grid(column=1, row=10, padx=8, pady=5, sticky="W")

        # Widgets for True of False questions
        self.tf_text = ttk.Label(self.record_q, text='Enter the question:')
        self.tf_text.grid(column=0, row=0, sticky="W")
        self.tf_question = tk.StringVar()
        self.tf_entered = ttk.Entry(self.record_q, width=50, textvariable=self.tf_question)
        self.tf_entered.grid(column=0, row=1, sticky='W', columnspan=2)
        self.tf_correct_text = ttk.Label(self.record_q, text='Choose the correct answer:')
        self.tf_correct_text.grid(column=0, row=2, sticky="W")
        # Using 2 radio buttons for True and False selection
        self.tf_answer = tk.IntVar()
        self.tf_rad1 = tk.Radiobutton(self.record_q, text="True", variable=self.tf_answer, value=1)
        self.tf_rad1.grid(column=0, row=3, padx=8, pady=5, sticky="W")
        self.tf_rad2 = tk.Radiobutton(self.record_q, text="False", variable=self.tf_answer, value=0)
        self.tf_rad2.grid(column=1, row=3, padx=8, pady=5, sticky="W")
        # Create 2 buttons for generating database and clear input
        self.gen_tf_btn = ttk.Button(self.record_q, text='Generate!', command=self.gen_tf_db)
        self.gen_tf_btn.grid(column=0, row=4, padx=8, pady=5, sticky="W")
        self.clr_tf_btn = ttk.Button(self.record_q, text='Clear', command=self.clear_tf)
        self.clr_tf_btn.grid(column=1, row=4, padx=8, pady=5, sticky="W")

        # initialize with this function to hide widgets for TF question input
        self.initial_record_status()
        # ====================== End of record tab ========================

        # ====================== Element for import tab ========================
        # Text instruction for import tab
        self.instruction_i = ttk.Label(self.import_tab, text='* Import data file with questions in this tab.\n'
                                                             '* Both .csv and .txt file could be accepted.\n'
                                                             '* Please make sure the file is in right format.\n'
                                                             '* Please operate within the related area.')
        self.instruction_i.grid(column=0, row=0, padx=10, pady=8)

        # Create a labelFrame to contain the widgets to import mc questions from file
        self.import_mc_labelframe = ttk.LabelFrame(self.import_tab, text='Import multiple choice questions from file')
        self.import_mc_labelframe.grid(column=0, row=1, padx=10, pady=8)

        # Create a button using filedialog.askopenfilename to get the path of data file
        self.mc_imp_btn = ttk.Button(self.import_mc_labelframe, width=30, text='Import Multiple Choice data file',
                                     command=self.mc_file_import)
        self.mc_imp_btn.grid(column=0, row=0, padx=8, pady=5, sticky="W")
        self.mc_file_path = ttk.Label(self.import_mc_labelframe, width=55, wraplength=380, text='File opened: ')
        self.mc_file_path.grid(column=0, row=1, padx=8, pady=5, sticky="W")
        # Create a progress bar for importing mc
        self.mc_progress_bar = ttk.Progressbar(self.import_mc_labelframe, orient="horizontal", length=400,
                                               mode='determinate')
        self.mc_progress_bar.grid(column=0, row=2, padx=8, pady=5, sticky="W")

        # Generate button to transfer the data into db file
        self.mc_gen_imp_btn = ttk.Button(self.import_mc_labelframe, width=30, text='Import Questions!',
                                         command=self.gen_mc_db_imp)
        self.mc_gen_imp_btn.grid(column=0, row=3, padx=8, pady=5, sticky="W")
        # Using a list to contain all pieces of question data
        # ** notice that every single piece must be a tuple to be recorded into a db file
        self.mc_import_ls = []

        # Another labelFrame for TF data file import
        self.import_tf_labelframe = ttk.LabelFrame(self.import_tab, text='Import true or false questions from file')
        self.import_tf_labelframe.grid(column=0, row=2, padx=10, pady=8)

        # Create a button using filedialog.askopenfile to open a file
        self.tf_imp_btn = ttk.Button(self.import_tf_labelframe, width=30, text='Import True or False data file',
                                     command=self.tf_file_import)
        self.tf_imp_btn.grid(column=0, row=0, padx=8, pady=5, sticky="W")
        self.tf_file_path = ttk.Label(self.import_tf_labelframe, width=55, wraplength=380, text='File opened: ')
        self.tf_file_path.grid(column=0, row=1, padx=8, pady=5, sticky="W")

        # Create a progress bar for importing tf
        self.tf_progress_bar = ttk.Progressbar(self.import_tf_labelframe, orient="horizontal", length=400,
                                               mode='determinate')
        self.tf_progress_bar.grid(column=0, row=2, padx=8, pady=5, sticky="W")

        self.tf_gen_imp_btn = ttk.Button(self.import_tf_labelframe, width=30, text='Import Questions!',
                                         command=self.gen_tf_db_imp)
        self.tf_gen_imp_btn.grid(column=0, row=3, padx=8, pady=5, sticky="W")
        self.tf_import_ls = []
        # ====================== End of import tab ========================

        # ====================== Element for display tab ========================
        # Create 2 labelFrame for table display
        self.display_mc_labelframe = ttk.LabelFrame(self.display_tab, text='Current Multiple Choice questions')
        self.display_mc_labelframe.grid(column=0, row=0, padx=10, pady=8)
        self.display_tf_labelframe = ttk.LabelFrame(self.display_tab, text='Current True or False questions')
        self.display_tf_labelframe.grid(column=0, row=1, padx=10, pady=8)
        # 2 buttons to generate latest question data
        self.display_mc_btn = ttk.Button(self.display_mc_labelframe, text='Display Multiple Choice questions',
                                         command=self.display_mc)
        self.display_mc_btn.grid(column=0, row=0, padx=8, pady=5, sticky="W")
        self.display_tf_btn = ttk.Button(self.display_tf_labelframe, text='Display True or False questions',
                                         command=self.display_tf)
        self.display_tf_btn.grid(column=0, row=0, padx=8, pady=5, sticky="W")
        # Create a tree element for mc table
        self.mc_tree = ttk.Treeview(self.display_mc_labelframe, height=5, show="headings", selectmode="browse")
        self.mc_tree.grid(column=0, row=1, padx=8, pady=5)
        # Setting columns for mc_tree
        self.mc_tree["columns"] = ("PID", "QST", "CTG", "DFC", "CA", "WA1", "WA2", "WA3")
        for i in self.mc_tree["columns"]:
            self.mc_tree.column(i, width=50, anchor='center')
            self.mc_tree.heading(i, text=i)
        # Creating a scrollbar for viewing table
        self.mc_vbar = ttk.Scrollbar(self.display_mc_labelframe, orient="vertical", command=self.mc_tree.yview)
        self.mc_vbar.grid(column=1, row=1, sticky="NS")
        self.mc_tree.configure(yscrollcommand=self.mc_vbar.set)
        # Binding left click with showing data
        self.mc_tree.bind("<ButtonRelease-1>", self.mc_click_view)
        self.mc_display_text = tk.StringVar()
        self.mc_display_text.set("Data selected:\n"
                                 "PID:\n"
                                 "Question:\n"
                                 "Category:\n"
                                 "Difficulty:\n"
                                 "Correct Answer:\n"
                                 "Wrong Answer 1:\n"
                                 "Wrong Answer 2:\n"
                                 "Wrong Answer 3:")
        # Create a label to display single piece of data
        self.mc_display_data = ttk.Label(self.display_mc_labelframe, width=55, wraplength=380,
                                         textvariable=self.mc_display_text)
        self.mc_display_data.grid(column=0, row=2, padx=8, pady=5)

        # Create a tree element for tf table
        self.tf_tree = ttk.Treeview(self.display_tf_labelframe, height=5, show="headings", selectmode="browse")
        self.tf_tree.grid(column=0, row=1, padx=8, pady=5)
        # Setting columns for tf_tree
        self.tf_tree["columns"] = ("PID", "QST", "CTG", "DFC", "CA")
        for i in self.tf_tree["columns"]:
            self.tf_tree.column(i, width=70, anchor='center')
            self.tf_tree.heading(i, text=i)
        # Creating a scrollbar for viewing table
        self.tf_vbar = ttk.Scrollbar(self.display_tf_labelframe, orient="vertical", command=self.tf_tree.yview)
        self.tf_vbar.grid(column=1, row=1, sticky="NS")
        self.tf_tree.configure(yscrollcommand=self.tf_vbar.set)
        # Binding left click with showing data
        self.tf_tree.bind("<ButtonRelease-1>", self.tf_click_view)
        self.tf_display_text = tk.StringVar()
        self.tf_display_text.set("Data selected:\n"
                                 "PID:\n"
                                 "Question:\n"
                                 "Category:\n"
                                 "Difficulty:\n"
                                 "Correct Answer:")
        # Create a label to display single piece of data
        self.tf_display_data = ttk.Label(self.display_tf_labelframe, width=55, wraplength=380,
                                         textvariable=self.tf_display_text)
        self.tf_display_data.grid(column=0, row=2, padx=8, pady=5)

    # ====================== End of display tab ========================

    @staticmethod
    # Pop up message box of About info
    def _about_msg():
        msg.showinfo('Team G - Portfolio B', 'Unit 1 - Add Question\n'
                                             'Version 2.2\n'
                                             'Unit created by Tian ZHANG.')

    # ====================== Function for record tab ========================
    # initialize the record_tab with multiple choice widgets, hide the t&f record widgets
    def initial_record_status(self):
        self.tf_text.grid_remove()
        self.tf_entered.grid_remove()
        self.tf_correct_text.grid_remove()
        self.tf_rad1.grid_remove()
        self.tf_rad2.grid_remove()
        self.gen_tf_btn.grid_remove()
        self.clr_tf_btn.grid_remove()
        self.mc_entered.focus()

    # when clicking the tf btn, remove the widgets for mc
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
        # Show the widgets for tf recording
        self.tf_text.grid()
        self.tf_entered.grid()
        self.tf_entered.focus()
        self.tf_correct_text.grid()
        self.tf_rad1.grid()
        self.tf_rad2.grid()
        self.gen_tf_btn.grid()
        self.clr_tf_btn.grid()

    # when clicking the mc btn, remove all the widgets for tf
    def remove_tf(self):
        # show the mc widgets
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
        # remove all widgets for tf recording
        self.tf_text.grid_remove()
        self.tf_entered.grid_remove()
        self.tf_correct_text.grid_remove()
        self.tf_rad1.grid_remove()
        self.tf_rad2.grid_remove()
        self.gen_tf_btn.grid_remove()
        self.clr_tf_btn.grid_remove()

    # clear all the mc input
    def clear_mc(self):
        self.mc_entered.delete(0, 'end')
        self.mc_correct_entry.delete(0, 'end')
        self.mc_wrong1_entry.delete(0, 'end')
        self.mc_wrong2_entry.delete(0, 'end')
        self.mc_wrong3_entry.delete(0, 'end')

    # clear all the tf input
    def clear_tf(self):
        self.tf_entered.delete(0, 'end')

    '''
    Using a tuple to store all the mc input.
    Then generate a database if not exist.
    Insert all the data of the question into the database file.
    After generation clear all the input with clear_mc function.
    Then pop up a msg box, close the cursor to end.
    And pop up msg box for error exceptions.
    '''

    def gen_mc_db(self):
        # Initialize mc_question database with sqlite3
        mc_q = self.mc_entered.get()
        mc_c = self.category_selected.get()
        mc_d = self.difficulty_selected.get()
        mc_ca = self.mc_correct_entry.get()
        mc_w1 = self.mc_wrong1_entry.get()
        mc_w2 = self.mc_wrong2_entry.get()
        mc_w3 = self.mc_wrong3_entry.get()
        if not mc_q:
            # If question is empty
            msg.showerror('Error', 'Question cannot be empty, please try again.')
        elif not mc_ca:
            # if correct answer is empty
            msg.showerror('Error', 'Correct answer cannot be empty! Please try again.')
        elif not (mc_w1 and mc_w2 and mc_w3):
            # if any of the wrong answers is empty
            msg.showerror('Error', 'Three wrong answers are required, please try again.')
        else:
            # store the question into a tuple
            self.mc_question_ls = (mc_q, mc_c, mc_d, mc_ca, mc_w1, mc_w2, mc_w3)
            '''
            Connecting the db file and create cursor must be done in the function.
            Otherwise it can't generate for a second time cause the cursor is closed!
            So can't move it to __init__.
            '''
            self.conn = sqlite3.connect("system.db")
            self.c = self.conn.cursor()
            self.c.execute('''CREATE TABLE IF NOT EXISTS MC_QUESTION (PID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
            QUESTION TEXT NOT NULL, CATEGORY TEXT NOT NULL, DIFFICULTY TEXT NOT NULL, CORRECT TEXT NOT NULL,
            WRONG1 TEXT NOT NULL, WRONG2 TEXT NOT NULL, WRONG3 TEXT NOT NULL)''')

            self.c.execute("INSERT INTO MC_QUESTION (QUESTION, CATEGORY, DIFFICULTY, CORRECT, WRONG1,"
                           "WRONG2, WRONG3) VALUES (?, ?, ?, ?, ?, ?, ?)", self.mc_question_ls)
            self.conn.commit()
            self.conn.close()
            self.clear_mc()
            msg.showinfo('Success', 'Question recorded successfully!')

    def gen_tf_db(self):
        # Initialize tf_question database with sqlite3
        tf_q = self.tf_entered.get()
        tf_c = self.category_selected.get()
        tf_d = self.difficulty_selected.get()
        tf_ca = self.tf_answer.get()
        if not tf_q:
            # if the question is empty
            msg.showerror('Error', 'Question cannot be empty, please try again.')
        else:
            self.tf_question_ls = (tf_q, tf_c, tf_d, tf_ca)
            '''
            Connecting the db file and create cursor must be done in the function.
            Otherwise it can't generate for a second time cause the cursor is closed!
            So can't move it to __init__.
            '''
            self.conn = sqlite3.connect("system.db")
            self.c = self.conn.cursor()
            self.c.execute('''CREATE TABLE IF NOT EXISTS TF_QUESTION (PID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
            QUESTION TEXT NOT NULL, CATEGORY TEXT NOT NULL, DIFFICULTY TEXT NOT NULL, CORRECT INTEGER NOT NULL)''')

            self.c.execute("INSERT INTO TF_QUESTION (QUESTION, CATEGORY, DIFFICULTY, CORRECT) VALUES (?, ?, ?, ?)",
                           self.tf_question_ls)
            self.conn.commit()
            self.conn.close()
            self.clear_tf()
            msg.showinfo('Success', 'Question recorded successfully!')

    # ====================== End of function for record tab ========================

    # ====================== Function for import tab ========================
    def mc_file_import(self):
        # using askopenfilename to get the full path of selected file
        self.mc_ask_open_file = tk.filedialog.askopenfilename()
        # display the path on GUI for user to see
        self.mc_file_path['text'] = 'File opened: ' + self.mc_ask_open_file
        # if the filename ends with csv then proceed with module csv
        if self.mc_ask_open_file[-3:] == "csv":
            with open(self.mc_ask_open_file, 'r') as mc_csv:
                self.mc_reader = csv.reader(mc_csv)
                for row in self.mc_reader:
                    self.mc_import_ls.append(row)
                # delete the head of table
                del (self.mc_import_ls[0])
        # if the filename ends with txt then use 'readlines' to read the data
        elif self.mc_ask_open_file[-3:] == 'txt':
            with open(self.mc_ask_open_file, 'r') as mc_txt:
                self.mc_txt_data = mc_txt.readlines()
                for line in self.mc_txt_data:
                    # remove \n
                    new_line = line.replace("\n", "")
                    # split the string by ","
                    str_to_ls = new_line.split(',')
                    # turn the list into a tuple
                    gen_tuple = tuple(str_to_ls)
                    # append to the list to proceed
                    self.mc_import_ls.append(gen_tuple)
                # delete head row of the table afterward
                del (self.mc_import_ls[0])
        elif not self.mc_ask_open_file:
            # if no file chosen
            msg.showinfo('No file chosen', 'Please choose a csv or txt file to proceed.')
        else:
            # if the file chosen is not the right type, pop up a error box
            self.mc_ask_open_file = ''
            self.mc_file_path['text'] = 'File opened: '
            msg.showerror('Error', 'File type not supported!\nPlease try again.')

    def gen_mc_db_imp(self):
        # if the list is empty (no data)
        if not self.mc_import_ls:
            msg.showerror('Error', 'No data imported!\nPlease try again.')
        else:
            # Initialize mc_question database with sqlite3
            self.conn = sqlite3.connect("system.db")
            self.c = self.conn.cursor()
            self.c.execute('''CREATE TABLE IF NOT EXISTS MC_QUESTION (PID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
            QUESTION TEXT NOT NULL, CATEGORY TEXT NOT NULL, DIFFICULTY TEXT NOT NULL, CORRECT TEXT NOT NULL,
            WRONG1 TEXT NOT NULL, WRONG2 TEXT NOT NULL, WRONG3 TEXT NOT NULL)''')

            self.c.executemany("INSERT INTO MC_QUESTION (QUESTION, CATEGORY, DIFFICULTY, CORRECT, WRONG1,"
                               "WRONG2, WRONG3) VALUES (?, ?, ?, ?, ?, ?, ?)", self.mc_import_ls)
            self.conn.commit()
            self.conn.close()
            # progress bar go up
            self.mc_progress_bar['maximum'] = 100
            for i in range(101):
                sleep(0.01)
                self.mc_progress_bar['value'] = i
                self.mc_progress_bar.update()
            # show msg box as a feedback
            msg.showinfo('Success', 'Question imported successfully!')
            # Empty the list after importing
            self.mc_import_ls = []
            # reset the path storage and display
            self.mc_ask_open_file = ''
            self.mc_file_path['text'] = 'File opened: '
            self.mc_progress_bar['value'] = 0

    def tf_file_import(self):
        # see self.mc_file_import()
        self.tf_ask_open_file = tk.filedialog.askopenfilename()
        self.tf_file_path['text'] = 'File opened: ' + self.tf_ask_open_file
        if self.tf_ask_open_file[-3:] == 'csv':
            with open(self.tf_ask_open_file, 'r') as tf_csv:
                self.tf_reader = csv.reader(tf_csv)
                for row in self.tf_reader:
                    self.tf_import_ls.append(row)
                # delete head row of the table afterward
                del (self.tf_import_ls[0])
        elif self.tf_ask_open_file[-3:] == 'txt':
            with open(self.tf_ask_open_file, 'r') as tf_txt:
                self.tf_txt_data = tf_txt.readlines()
                for line in self.tf_txt_data:
                    new_line_2 = line.replace("\n", "")
                    str_to_ls_2 = new_line_2.split(',')
                    gen_tuple_2 = tuple(str_to_ls_2)
                    self.tf_import_ls.append(gen_tuple_2)
                # delete head row of the table afterward
                del (self.tf_import_ls[0])
        elif not self.tf_ask_open_file:
            msg.showinfo('No file chosen', 'Please choose a csv or txt file to proceed.')
        else:
            self.tf_ask_open_file = ''
            self.tf_file_path['text'] = 'File opened: '
            msg.showerror('Error', 'File type not supported!\nPlease try again.')

    def gen_tf_db_imp(self):
        if not self.tf_import_ls:
            msg.showerror('Error', 'No data imported!\nPlease try again.')
        else:
            # Initialize mc_question database with sqlite3
            self.conn = sqlite3.connect("system.db")
            self.c = self.conn.cursor()
            self.c.execute('''CREATE TABLE IF NOT EXISTS TF_QUESTION (PID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
            QUESTION TEXT NOT NULL, CATEGORY TEXT NOT NULL, DIFFICULTY TEXT NOT NULL, CORRECT INTEGER NOT NULL)''')

            self.c.executemany("INSERT INTO TF_QUESTION (QUESTION, CATEGORY, DIFFICULTY, CORRECT) VALUES (?, ?, ?, ?)",
                               self.tf_import_ls)
            self.conn.commit()
            self.conn.close()
            # progress bar go up
            self.tf_progress_bar['maximum'] = 100
            for i in range(101):
                sleep(0.01)
                self.tf_progress_bar['value'] = i
                self.tf_progress_bar.update()
            msg.showinfo('Success', 'Question imported successfully!')
            # Empty the list after importing
            self.tf_import_ls = []
            self.tf_ask_open_file = ''
            self.tf_file_path['text'] = 'File opened: '
            self.tf_progress_bar['value'] = 0

    # ====================== End of function for import tab ========================

    # ====================== Function for display tab ========================
    def get_mc_data(self, database="system.db"):
        # Empty the list every time retrieve data
        self.mc_data_ls = []
        self.conn = sqlite3.connect(database)
        self.c = self.conn.cursor()
        self.c.execute("SELECT * FROM MC_QUESTION ORDER BY PID")
        self.mc_data_ls = self.c.fetchall()
        self.conn.commit()
        self.conn.close()
        return self.mc_data_ls

    def display_mc(self):
        # Empty the table evert time user click the button
        for i in self.mc_tree.get_children():
            self.mc_tree.delete(i)
        self.mc_data = self.get_mc_data()
        i = 0
        # insert the data
        for data in self.mc_data:
            self.mc_tree.insert('', i, values=data)
            i += 1

    def mc_click_view(self, event):
        # get the item selected
        for item in self.mc_tree.selection():
            self.item_text = self.mc_tree.item(item, "values")
        self.mc_display_text.set("Data selected:"
                                 "\nPID: " + self.item_text[0] +
                                 "\nQuestion: " + self.item_text[1] +
                                 "\nCategory: " + self.item_text[2] +
                                 "\nDifficulty: " + self.item_text[3] +
                                 "\nCorrect Answer: " + self.item_text[4] +
                                 "\nWrong Answer 1: " + self.item_text[5] +
                                 "\nWrong Answer 2: " + self.item_text[6] +
                                 "\nWrong Answer 3: " + self.item_text[7])

    def get_tf_data(self, database="system.db"):
        self.tf_data_ls = []
        self.conn = sqlite3.connect(database)
        self.c = self.conn.cursor()
        self.c.execute("SELECT * FROM TF_QUESTION ORDER BY PID")
        self.tf_data_ls = self.c.fetchall()
        self.conn.commit()
        self.conn.close()
        return self.tf_data_ls

    def display_tf(self):
        for i in self.tf_tree.get_children():
            self.tf_tree.delete(i)
        self.tf_data = self.get_tf_data()
        i = 0
        for data in self.tf_data:
            # transfer tuple to list
            data_ls = list(data)
            # if value is 1 set it to True, otherwise set to False
            if data_ls[4] == 1:
                data_ls[4] = "True"
            else:
                data_ls[4] = "False"
            self.tf_tree.insert('', i, values=data_ls)
            i += 1

    def tf_click_view(self, event):
        for item in self.tf_tree.selection():
            self.item_text = list(self.tf_tree.item(item, "values"))
        self.tf_display_text.set("Data selected:"
                                 "\nPID: " + self.item_text[0] +
                                 "\nQuestion: " + self.item_text[1] +
                                 "\nCategory: " + self.item_text[2] +
                                 "\nDifficulty: " + self.item_text[3] +
                                 "\nCorrect Answer: " + self.item_text[4])

    # ====================== End of function for display tab ========================

    # Quit current GUI
    def quit(self):
        self.win.destroy()

    # Function to connect to next Unit
    def goto_op(self):
        # self.quit()
        # self.unit1 = unit2.GUI()
        # self.win.mainloop()
        pass

    # Function to return to last interface
    def goto_index(self):
        self.quit()
        self.index = index.GUI()
        self.win.mainloop()


if __name__ == "__main__":
    gui = GUI()
    gui.win.mainloop()

