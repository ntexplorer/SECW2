#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/11 22:41
# @Author : Tian ZHANG
# @Site : 
# @File : last_GUI_sample.py.py
# @Software: PyCharm
# @Version:

import tkinter as tk
from tkinter import ttk

import add_question as unit1


class GUI:
    def __init__(self):
        # Create instance
        self.win = tk.Tk()
        # Add a title
        self.win.title('Last GUI for testing GUI connection')
        self.label = ttk.Label(self.win, text='This is the last GUI!')
        self.label.grid(column=0, row=0, padx=10, pady=8)
        self.goto_next_btn = ttk.Button(self.win, text='goto next', command=self.goto_next)
        self.goto_next_btn.grid(column=0, row=1)

    def quit(self):
        self.win.destroy()

    def goto_next(self):
        self.quit()
        self.unit1 = unit1.GUI()
        self.win.mainloop()


if __name__ == "__main__":
    gui = GUI()
    gui.win.mainloop()
