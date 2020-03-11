#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/11 22:40
# @Author : Tian ZHANG
# @Site :
# @File : next_GUI_sample.py
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
        self.win.title('Next GUI for testing GUI connection')
        self.label = ttk.Label(self.win, text='This is the next GUI!')
        self.label.grid(column=0, row=0, padx=10, pady=8)
        self.goto_last_btn = ttk.Button(self.win, text='goto last', command=self.goto_last)
        self.goto_last_btn.grid(column=0, row=1)

    def quit(self):
        self.win.destroy()

    def goto_last(self):
        self.quit()
        self.unit1 = unit1.GUI()
        self.win.mainloop()


if __name__ == "__main__":
    gui = GUI()
    gui.win.mainloop()
