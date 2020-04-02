#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/23 20:14
# @Author : Tian ZHANG
# @Site : 
# @File : backstage_index.py
# @Software: PyCharm
# @Version: 1.2

import tkinter as tk
from tkinter import ttk

import add_question as unit1
import amend_delete_home as unit2
import check_statistics as unit6
import new_homepage as home
import quiz_gen as unit3


class GUI:
    def __init__(self):
        # Create instance
        self.win = tk.Tk()
        # Add a title
        self.win.title('Backstage Index - Quiz System by Team G')
        self.instruction = ttk.Label(self.win, text='Welcome to the backstage of the quiz system,\n'
                                                    'choose a option.')
        self.instruction.grid(column=0, row=0, padx=10, pady=8, sticky="W")
        self.index_lf = ttk.LabelFrame(self.win, text='Backstage')
        self.index_lf.grid(column=0, row=1, padx=10, pady=8, sticky="W")

        self.goto_unit1_btn = ttk.Button(self.index_lf, text='Create Question',
                                         width=30, command=self.goto_unit1)
        self.goto_unit1_btn.grid(column=0, row=0, padx=10, pady=8, sticky="W")
        self.goto_unit2_btn = ttk.Button(self.index_lf, text='Manage Question',
                                         width=30, command=self.goto_unit2)
        self.goto_unit2_btn.grid(column=1, row=0, padx=10, pady=8, sticky="W")
        self.goto_unit3_btn = ttk.Button(self.index_lf, text='Manage Quiz',
                                         width=30, command=self.goto_unit3)
        self.goto_unit3_btn.grid(column=2, row=0, padx=10, pady=8, sticky="W")
        self.goto_unit4_btn = ttk.Button(self.index_lf, text="Back to Homepage",
                                         width=30, command=self.goto_unit4)
        self.goto_unit4_btn.grid(column=1, row=1, padx=10, pady=8, sticky="W")
        self.goto_unit6_btn = ttk.Button(self.index_lf, text="Check Statistics",
                                         width=30, command=self.goto_unit6)
        self.goto_unit6_btn.grid(column=0, row=1, padx=10, pady=8, sticky="W")

    def quit(self):
        self.win.destroy()

    def goto_unit1(self):
        self.quit()
        self.unit1 = unit1.GUI()
        self.win.mainloop()

    def goto_unit2(self):
        self.quit()
        root = tk.Tk()
        root.title("Amend/Delete Questions")
        root.geometry("900x700")
        app = unit2.amendDeleteQuestions(root)
        root.mainloop()

    def goto_unit3(self):
        self.quit()
        self.unit3 = unit3.QuizGen()
        self.unit3.root.mainloop()

    def goto_unit4(self):
        self.quit()
        self.back_home = home.Homepage()
        self.win.mainloop()

    def goto_unit6(self):
        self.quit()
        self.unit6 = unit6.ckStat()
        self.unit6.win.mainloop()


if __name__ == "__main__":
    gui = GUI()
    gui.win.mainloop()
