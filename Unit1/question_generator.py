import sqlite3
from random import sample, randint
from string import ascii_letters, digits


# ID Generator
def Question_gen():
    # generates a 6-character-string
    question = ''.join(sample(ascii_letters + digits + "@_#*-&", 10))
    return question


cate_ls = ["Computer Science", "Nature", "History", "Language", "Video Game", "Nature"]


def category():
    category = cate_ls[randint(0, 5)]  # generates random float from 0 to 100
    return category


diff_ls = ["Easy", "Medium", "Hard"]


def diff_gen():
    diffculty = diff_ls[randint(0, 2)]
    return diffculty


answer_ls = ("C1", "W1", "W2", "W3")


def task_gen():
    task_num = 100
    count = 0
    task_list = []
    while count < task_num:
        pid = count + 1
        # generates all the task and put them into a list
        task_list.append((Question_gen(), category(), diff_gen(), "C1", "W1", "W2", "W3"))
        count += 1
    return task_list


# Create database
conn = sqlite3.connect("system.db")
c = conn.cursor()
# create another column called PID in case same ID generated
c.execute('''CREATE TABLE IF NOT EXISTS MC_QUESTION (PID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
QUESTION TEXT NOT NULL, CATEGORY TEXT NOT NULL, DIFFICULTY TEXT NOT NULL, CORRECT TEXT NOT NULL,
WRONG1 TEXT NOT NULL, WRONG2 TEXT NOT NULL, WRONG3 TEXT NOT NULL)''')
task_list = task_gen()  # Generate data(the task list)
# Insert data(the task list) into the database
c.executemany("INSERT INTO MC_QUESTION (QUESTION, CATEGORY, DIFFICULTY, CORRECT, WRONG1,"
              "WRONG2, WRONG3) VALUES (?, ?, ?, ?, ?, ?, ?)", task_list)
conn.commit()
conn.close()
