#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/23 19:32
# @Author : Elaine
# @Site :
# @File : new_homepage.py
# @Software: PyCharm
# @Version: 1.1

import tkinter as tk
from tkinter import *
from tkinter import ttk

import choose_quiz as choose
import login


class Homepage:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Welcome - Quiz System by Team G')
        self.root.geometry("600x400")
        self.init_window()

    # the following function sets out the GUI layout.

    def init_window(self):
        self.welcome_text = ttk.Label(self.root,
                                      text="Welcome to the Cardiff University Computer Science Quiz Homepage.")
        self.welcome_text.grid(row=0, column=0, padx=10, pady=8, columnspan=2, sticky="W")
        self.canvas = Canvas(width=300, height=300, bg='grey')
        self.canvas.grid(column=0, row=1, columnspan=2, sticky="N")
        self.logo = PhotoImage(file='logo.gif')
        self.canvas.create_image(0, 0, image=self.logo, anchor=NW)
        self.quiz_page = ttk.Button(self.root, text="Start quiz as Pupil", width=30, command=self.choose_quiz)
        self.quiz_page.grid(column=0, row=2, padx=8, pady=5, sticky="W")
        self.login_btn = ttk.Button(self.root, text="Login as Admin", width=30, command=self.goto_login)
        self.login_btn.grid(column=1, row=2, padx=8, pady=5, sticky="W")

    def quit(self):
        self.root.destroy()

    def choose_quiz(self):
        self.quit()
        self.choose = choose.Window()
        self.root.mainloop()

    def goto_login(self):
        self.quit()
        self.back_login = login.GUI()
        self.root.mainloop()


if __name__ == "__main__":
    app = Homepage()
    app.root.mainloop()
