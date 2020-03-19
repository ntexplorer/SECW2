#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/12 23:52
# @Author : Tian ZHANG
# @Site : 
# @File : login.py
# @Software: PyCharm
# @Version: 1.2

import tkinter as tk
from tkinter import messagebox as msg
from tkinter import ttk

import backstage_index as bkm
import homepage as home


class GUI:
    def __init__(self):
        # Create instance
        self.win = tk.Tk()
        # Add a title
        self.win.title('Login - Quiz System by Team G')
        self.login_lf = ttk.LabelFrame(self.win, text='Login')
        self.login_lf.grid(column=0, row=0, padx=10, pady=8)
        self.username_label = ttk.Label(self.login_lf, text='Username:')
        self.username_label.grid(column=0, row=0, padx=8, pady=5, sticky="W")
        self.username = tk.StringVar()
        self.entry_username = ttk.Entry(self.login_lf, textvariable=self.username)
        self.entry_username.grid(row=0, column=1, columnspan=2, sticky="W")
        self.entry_username.focus()
        self.password_label = ttk.Label(self.login_lf, text='Password:')
        self.password_label.grid(row=1, column=0, padx=8, pady=5, sticky="W")
        self.password = tk.StringVar()
        self.entry_password = ttk.Entry(self.login_lf, textvariable=self.password)
        self.entry_password["show"] = '*'
        self.entry_password.grid(row=1, column=1, columnspan=2, sticky="W")
        self.login_btn = ttk.Button(self.login_lf, text='Login', command=self.login)
        self.login_btn.grid(row=2, column=0, padx=8, pady=5, sticky="N")
        self.clear_btn = ttk.Button(self.login_lf, text='Clear', command=self.clear)
        self.clear_btn.grid(row=2, column=1, padx=8, pady=5, sticky="N")
        self.back_btn = ttk.Button(self.login_lf, text='Back', command=self.back)
        self.back_btn.grid(row=2, column=2, padx=8, pady=5, sticky="N")

    def login(self):
        self.username_entered = self.entry_username.get()
        self.password_entered = self.entry_password.get()

        if self.username_entered == "admin" and self.password_entered == "teamgrocks":
            msg.showinfo("Success", "Welcome to the backstage system!")
            self.goto_next()
        else:
            msg.showerror("Failed to login", "Invalid username or password, please try again.")

    def clear(self):
        self.entry_username.delete(0, 'end')
        self.entry_password.delete(0, 'end')

    def quit(self):
        self.win.destroy()

    def goto_next(self):
        self.quit()
        self.backstage_index = bkm.GUI()
        self.win.mainloop()

    def back(self):
        self.quit()
        self.back_home = home.Window()
        self.win.mainloop()


if __name__ == "__main__":
    gui = GUI()
    gui.win.mainloop()
