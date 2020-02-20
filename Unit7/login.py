#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/2/20 0:42
# @Author : Tian ZHANG
# @Site : 
# @File : login.py
# @Software: PyCharm
# @Version: 1.0

from tkinter import *


def login(event):
    username = entry1.get()
    password = entry2.get()
    if username == 'admin' and password == 'admin':
        response['text'] = 'Login successful!'
    else:
        response['text'] = 'Invalid username or password.'
        entry1.delete(0, END)
        entry2.delete(0, END)


def clear(event):
    entry1.delete(0, END)
    entry2.delete(0, END)


root = Tk()
label1 = Label(root, text='Username: ')
label1.grid(row=0, column=0, sticky=W)
entry1 = Entry(root)
entry1.grid(row=0, column=1, stick=E)

label2 = Label(root, text='Password: ')
label2.grid(row=1, column=0, sticky=W)
entry2 = Entry(root)
entry2['show'] = '*'
entry2.grid(row=1, column=1, sticky=E)

loginButton = Button(root, text='Login')
loginButton.bind('<Button-1>', login)
loginButton.grid(row=2, column=0, sticky=N)

clearButton = Button(root, text='Clear')
clearButton.bind('<Button-1>', clear)
clearButton.grid(row=2, column=1, sticky=N)

response = Label(root, text='')
response.grid(row=3, column=0, columnspan=2, sticky=W)

root.mainloop()
# TODO: refactor this file using OOP
