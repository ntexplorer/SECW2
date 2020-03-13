#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/13 0:20
# @Author : Tian ZHANG
# @Site : 
# @File : backstage_index.py
# @Software: PyCharm
# @Version: 1.0

import tkinter as tk
from tkinter import ttk

import add_question as unit1


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

        self.goto_unit1_btn = ttk.Button(self.index_lf, text='Create Question', command=self.goto_unit1)
        self.goto_unit1_btn.grid(column=0, row=0, padx=10, pady=8, sticky="W")
        self.goto_unit2_btn = ttk.Button(self.index_lf, text='Manage Question', command=self.goto_unit2)
        self.goto_unit2_btn.grid(column=1, row=0, padx=10, pady=8, sticky="W")
        self.goto_unit3_btn = ttk.Button(self.index_lf, text='Manage Quiz', command=self.goto_unit3)
        self.goto_unit3_btn.grid(column=0, row=1, padx=10, pady=8, sticky="W")

    def quit(self):
        self.win.destroy()

    def goto_unit1(self):
        self.quit()
        self.unit1 = unit1.GUI()
        self.win.mainloop()

    def goto_unit2(self):
        pass

    def goto_unit3(self):
        pass


if __name__ == "__main__":
    gui = GUI()
    gui.win.mainloop()
