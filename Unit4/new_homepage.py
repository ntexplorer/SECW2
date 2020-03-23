# NEW HOMEPAGE

import tkinter as tk
from tkinter import *

import login


class Homepage:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Homepage')
        self.root.geometry("600x400")
        self.init_window()

    # the following function sets out the GUI layout.

    def init_window(self):
        Label(self.root, text="Welcome to the Cardiff University Computer Science Quiz Homepage.").grid(row=0, padx=8,
                                                                                                        pady=20,
                                                                                                        sticky=W)
        self.quiz_page = Button(self.root, text="Start quiz as Pupil", command=self.choose_quiz)
        self.quiz_page.grid(row=1, padx=8, pady=8, sticky=W)
        self.login_btn = Button(self.root, text="Login as Admin", command=self.goto_login).grid(row=2, padx=8, pady=8,
                                                                                                sticky=W)

    def quit(self):
        self.root.destroy()

    def choose_quiz(self):
        self.quit()
        # self.????
        self.root.mainloop()

    def goto_login(self):
        self.quit()
        self.back_login = login.GUI()
        self.root.mainloop()


if __name__ == "__main__":
    app = Homepage()
    app.root.mainloop()
