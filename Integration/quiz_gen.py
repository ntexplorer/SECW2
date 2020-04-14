import sqlite3
import tkinter.messagebox
from tkinter import *
from tkinter import ttk

import backstage_index as bks


class QuizGen:

    def __init__(self, categories=[], difficulties=[], categoriesTF=[], difficultiesTF=[], currentMC=[], currentTF=[]):
        self.difficulties = difficulties
        self.categories = categories
        self.difficultiesTF = difficultiesTF
        self.categoriesTF = categoriesTF
        self.currentMC = currentMC
        self.currentTF = currentTF
        self.root = Tk()
        self.root.title("Quiz Manager")
        self.window_ui()
        self.showCategories()
        self.showDifficulties()
        self.showCategoriesTF()
        self.showDifficultiesTF()
        self.quizInUseTable()
        self.mcInUse()
        self.tfInUse()
        self.quizTreeCurrent()

    # Going back to main menu
    def goBack(self):
        self.root.destroy()
        self.bks = bks.GUI()
        self.root.mainloop()

    # Loading and displaying all MC questions in Treeview
    def display(self):
        self.conn = sqlite3.connect("system.db")
        self.cur = self.conn.cursor()
        self.cur.execute("SELECT * FROM MC_QUESTION")
        self.rows = self.cur.fetchall()
        self.tree.delete(*self.tree.get_children())
        for row in self.rows:
            print(row)
            self.tree.insert("", END, values=row)
        self.conn.close()

    # Loading and displaying all MC quizes in Treeview
    def quizDispMC(self):
        self.conn = sqlite3.connect("system.db")
        self.cur = self.conn.cursor()
        try:
            self.cur.execute("SELECT * FROM MC_QUIZ")
        except:
            tkinter.messagebox.showerror(title="Error", message="You have to create a Multiple Choice Quiz first.")
        self.rows = self.cur.fetchall()
        self.tree3.delete(*self.tree3.get_children())
        for row in self.rows:
            print(row)
            self.tree3.insert("", END, values=row)
        self.conn.close()

    # Loading and displaying all TF questions in Treeview
    def displayTF(self):
        self.conn = sqlite3.connect("system.db")
        self.cur = self.conn.cursor()
        self.cur.execute("SELECT * FROM TF_QUESTION")
        self.rows = self.cur.fetchall()
        self.tree2.delete(*self.tree2.get_children())
        for row in self.rows:
            print(row)
            self.tree2.insert("", END, values=row)
        self.conn.close()

    # Loading and displaying all TF questions in Treeview
    def quizDispTF(self):
        self.conn = sqlite3.connect("system.db")
        self.cur = self.conn.cursor()
        try:
            self.cur.execute("SELECT * FROM TF_QUIZ")
        except:
            tkinter.messagebox.showerror(title="Error", message="You have to create a True/False Quiz first.")
        self.rows = self.cur.fetchall()
        self.tree4.delete(*self.tree4.get_children())
        for row in self.rows:
            print(row)
            self.tree4.insert("", END, values=row)
        self.conn.close()


    # Loading and displaying all current quiz in Treeview
    def quizTreeCurrent(self):
        self.conn = sqlite3.connect("system.db")
        self.cur = self.conn.cursor()
        try:
            self.cur.execute("SELECT * FROM CURRENT_QUIZ")
        except:
            pass
        self.rows = self.cur.fetchall()
        self.tree5.delete(*self.tree5.get_children())
        for row in self.rows:
            print(row)
            self.tree5.insert("", END, values=row)
        self.conn.close()

    # Event for MC category
    def boxCategoryValue(self):
        self.boxcatvalue = self.boxCategory.get()
        self.boxcatvalue = str(self.boxcatvalue)
        print(self.boxcatvalue)
        print(type(self.boxcatvalue))

    # Event for MC difficulty
    def boxDifficultyValue(self):
        self.boxdiffvalue = self.boxDifficulty.get()
        self.boxdiffvalue = str(self.boxdiffvalue)
        print(self.boxdiffvalue)
        print(type(self.boxdiffvalue))

    # Event for TF category
    def boxCategoryValueTF(self):
        self.boxcatvalueTF = self.boxCategoryTF.get()
        self.boxcatvalueTF = str(self.boxcatvalueTF)
        print(self.boxcatvalueTF)
        print(type(self.boxcatvalueTF))

    # Event for TF difficulty
    def boxDifficultyValueTF(self):
        choiceDiffTF = self.boxDifficultyTF.get()
        choiceDiffTF = str(choiceDiffTF)
        print(choiceDiffTF)
        print(type(choiceDiffTF))

    # Categories for MC QUESTION combobox

    def showCategories(self):
        self.conn = sqlite3.connect("system.db")
        self.cur = self.conn.cursor()
        try:
            self.cur.execute("SELECT DISTINCT Category FROM MC_QUESTION ORDER BY Category ASC")
            self.rows = self.cur.fetchall()
            for row in self.rows:
                print(row)
                self.categories.append(row[0])
            self.conn.commit()
            self.conn.close()
        except sqlite3.OperationalError:
            self.conn.commit()
            self.conn.close()

        # Lables and comboboxes for MC QUESTION
        self.lbCategory = Label(self.tab2, text="Choose Catgegory")
        self.lbCategory.pack(ipady=50)

        self.boxCategory = ttk.Combobox(self.tab2, values=self.categories, width=30, state="readonly")
        self.boxCategory.pack()
        try:
            self.boxCategory.current(0)
        except tkinter.TclError:
            pass
        self.boxCategory.bind("<<ComboboxSelected>>", lambda y: self.boxCategoryValue())

    # Difficulties for MC QUESTION combobox

    def showDifficulties(self):
        self.conn = sqlite3.connect("system.db")
        self.cur = self.conn.cursor()
        try:
            self.cur.execute("SELECT DISTINCT Difficulty FROM MC_QUESTION")
            self.rows = self.cur.fetchall()
            for row in self.rows:
                print(row)
                self.difficulties.append(row[0])
            self.conn.commit()
            self.conn.close()
        except sqlite3.OperationalError:
            pass

        self.lbDifficulty = Label(self.tab2, text="Choose Difficulty")
        self.lbDifficulty.pack(ipady=50)

        self.boxDifficulty = ttk.Combobox(self.tab2, values=self.difficulties, width=30, state="readonly")
        self.boxDifficulty.pack()
        try:
            self.boxDifficulty.current(0)
        except tkinter.TclError:
            pass
        self.boxDifficulty.bind("<<ComboboxSelected>>", lambda x: self.boxDifficultyValue())

    # Categories for TF QUESTION combobox

    def showCategoriesTF(self):
        self.conn = sqlite3.connect("system.db")
        self.cur = self.conn.cursor()
        try:
            self.cur.execute("SELECT DISTINCT Category FROM TF_QUESTION ORDER BY Category ASC")
            self.rows = self.cur.fetchall()
            for row in self.rows:
                print(row)
                self.categoriesTF.append(row[0])
            self.conn.commit()
            self.conn.close()
        except sqlite3.OperationalError:
            pass

        self.lbCategoryTF = Label(self.tab4, text="Choose Catgegory")
        self.lbCategoryTF.pack(ipady=50)

        self.boxCategoryTF = ttk.Combobox(self.tab4, values=self.categoriesTF, width=30, state="readonly")
        self.boxCategoryTF.pack()
        try:
            self.boxCategoryTF.current(0)
        except tkinter.TclError:
            pass
        self.boxCategoryTF.bind("<<ComboboxSelected>>", lambda x: self.boxCategoryValueTF())

    # Table for Quiz in use
    def quizInUseTable(self):
        self.conn = sqlite3.connect("system.db")
        self.cur = self.conn.cursor()
        try:
            self.cur.execute("CREATE TABLE IF NOT EXISTS CURRENT_QUIZ ("
                             "PROFILE INTEGER PRIMARY KEY AUTOINCREMENT, "
                             "MCUSED INTEGER, "
                             "TFUSED INTEGER, "
                             "FOREIGN KEY (MCUSED) REFERENCES MC_QUIZ(QuizID), "
                             "FOREIGN KEY (TFUSED) REFERENCES TF_QUIZ(QuizID)) ")
            self.conn.commit()
            self.conn.close()
        except sqlite3.OperationalError:
            pass

        self.conn4 = sqlite3.connect("system.db")
        self.cur4 = self.conn4.cursor()
        self.cur4.execute("UPDATE CURRENT_QUIZ SET profile = 1")
        self.conn4.commit()
        self.conn4.close()

    # MC in use
    def mcInUse(self):
        self.conn = sqlite3.connect("system.db")
        self.cur = self.conn.cursor()
        try:

            self.cur.execute("SELECT QuizID FROM MC_QUIZ")
            self.rows = self.cur.fetchall()
            for row in self.rows:
                print(row)
                self.currentMC.append(row[0])
            self.conn.commit()
            self.conn.close()
        except sqlite3.OperationalError:
            pass

        self.lbselectMC = Label(self.tab7, text="Select Multiple Choice Quiz to use")
        self.lbselectMC.pack(ipady=50)

        self.boxSelectMC = ttk.Combobox(self.tab7, values=self.currentMC, width=30, state="readonly")
        self.boxSelectMC.pack()

    # TF in Use
    def tfInUse(self):
        self.conn = sqlite3.connect("system.db")
        self.cur = self.conn.cursor()
        try:
            self.cur.execute("SELECT QuizID FROM TF_QUIZ")
            self.rows = self.cur.fetchall()
            for row in self.rows:
                print(row)
                self.currentTF.append(row[0])
            self.conn.commit()
            self.conn.close()
        except sqlite3.OperationalError:
            pass

        self.lbselectTF = Label(self.tab7, text="Select True/False Quiz to use")
        self.lbselectTF.pack(ipady=50)

        self.boxSelectTF = ttk.Combobox(self.tab7, values=self.currentTF, width=30, state="readonly")
        self.boxSelectTF.pack()

    # For button use quiz
    def useQuiz(self):
        self.conn = sqlite3.connect("system.db")
        self.cur = self.conn.cursor()
        self.cur.execute("UPDATE CURRENT_QUIZ SET MCUSED = ?, TFUSED = ?",
                         (self.boxSelectMC.get(), self.boxSelectTF.get()))
        print("Use MC number ", self.boxSelectMC.get())
        self.conn.commit()
        self.conn.close()
        self.quizTreeCurrent()

    # Difficulties for TF QUESTION combobox

    def showDifficultiesTF(self):
        self.conn = sqlite3.connect("system.db")
        self.cur = self.conn.cursor()
        try:
            self.cur.execute("SELECT DISTINCT Difficulty FROM TF_QUESTION")
            self.rows = self.cur.fetchall()
            for row in self.rows:
                print(row)
                self.difficultiesTF.append(row[0])
            self.conn.commit()
            self.conn.close()
        except sqlite3.OperationalError:
            pass

        self.lbDifficultyTF = Label(self.tab4, text="Choose Difficulty")
        self.lbDifficultyTF.pack(ipady=50)

        self.boxDifficultyTF = ttk.Combobox(self.tab4, values=self.difficultiesTF, width=30, state="readonly")
        self.boxDifficultyTF.pack()
        try:
            self.boxDifficultyTF.current(0)
        except tkinter.TclError:
            pass
        self.boxDifficultyTF.bind("<<ComboboxSelected>>", lambda y: self.boxDifficultyValueTF)

    # Create MC Quiz table and add values
    def createMCQuiz(self):
        self.qID = []
        self.conn = sqlite3.connect("system.db")
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS MC_QUIZ ("
                         "QuizID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, "
                         "CATEGORY TEXT NOT NULL, "
                         "DIFFICULTY TEXT NOT NULL, "
                         "q1Id INTEGER, "
                         "q2Id INTEGER, "
                         "q3Id INTEGER, "
                         "q4Id INTEGER, "
                         "q5Id INTEGER, "
                         "FOREIGN KEY (q1Id) REFERENCES MC_QUESTION(pid), "
                         "FOREIGN KEY (q2Id) REFERENCES MC_QUESTION(pid), "
                         "FOREIGN KEY (q3Id) REFERENCES MC_QUESTION(pid), "
                         "FOREIGN KEY (q4Id) REFERENCES MC_QUESTION(pid), "
                         "FOREIGN KEY (q5Id) REFERENCES MC_QUESTION(pid))")
        self.conn.commit()

        print("Quiz table Created")

        self.conn = sqlite3.connect("system.db")

        self.cur.execute(
            "SELECT pid FROM MC_QUESTION pid WHERE difficulty = ? AND category = ? ORDER BY RANDOM() LIMIT 5",
            (''.join(self.boxDifficulty.get()), ''.join(self.boxCategory.get())))
        self.item = self.cur.fetchall()
        print("List of ID length is: ", len(self.item))
        if (len(self.item) < 5):
            tkinter.messagebox.showerror(title="Error",
                                         message="Sorry, less than 5 results were found according to selected category and difficulty")
            raise IndexError
        print(''.join(self.boxCategory.get()))
        for row in self.item:
            print(row)
            self.qID.append(row)

        print(self.qID[1][0])
        print(type(self.qID[1][0]))
        print("Selection")

        self.conn2 = sqlite3.connect("system.db")
        self.cur2 = self.conn2.cursor()
        self.cur2.execute(
            "INSERT INTO MC_QUIZ (Category, Difficulty, q1Id, q2Id, q3Id, q4Id, q5Id) VALUES (?, ?, ?, ?, ?, ?, ?)", (
            ''.join(self.boxCategory.get()), ''.join(self.boxDifficulty.get()), self.qID[0][0], self.qID[1][0],
            self.qID[2][0], self.qID[3][0], self.qID[4][0]))
        self.conn2.commit()
        self.conn2.close()
        print("Insertion done for MC")

    # Create TF Quiz table and add values
    def createTFQuiz(self):
        self.qID = []
        self.conn = sqlite3.connect("system.db")
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS TF_QUIZ ("
                         "QuizID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, "
                         "CATEGORY TEXT NOT NULL, "
                         "DIFFICULTY TEXT NOT NULL, "
                         "q1Id INTEGER, "
                         "q2Id INTEGER, "
                         "q3Id INTEGER, "
                         "q4Id INTEGER, "
                         "q5Id INTEGER, "
                         "FOREIGN KEY (q1Id) REFERENCES TF_QUESTION(pid), "
                         "FOREIGN KEY (q2Id) REFERENCES TF_QUESTION(pid), "
                         "FOREIGN KEY (q3Id) REFERENCES TF_QUESTION(pid), "
                         "FOREIGN KEY (q4Id) REFERENCES TF_QUESTION(pid), "
                         "FOREIGN KEY (q5Id) REFERENCES TF_QUESTION(pid))")
        self.conn.commit()

        print("Quiz TF table Created")

        self.conn = sqlite3.connect("system.db")

        self.cur.execute(
            "SELECT pid FROM TF_QUESTION pid WHERE difficulty = ? AND category = ? ORDER BY RANDOM() LIMIT 5",
            (''.join(self.boxDifficultyTF.get()), ''.join(self.boxCategoryTF.get())))
        self.item = self.cur.fetchall()
        print("List of ID length is: ", len(self.item))
        if len(self.item) < 5:
            tkinter.messagebox.showerror(title="Error",
                                         message="Sorry, less than 5 results were found according to selected category and difficulty.\nPlease, use file that has more questions.")
            raise IndexError
        for row in self.item:
            print(row)
            self.qID.append(row)

        print(self.qID[1][0])
        print(type(self.qID[1][0]))
        print("Selection TF")

        self.conn3 = sqlite3.connect("system.db")
        self.cur3 = self.conn3.cursor()
        self.cur3.execute(
            "INSERT INTO TF_QUIZ (Category, Difficulty, q1Id, q2Id, q3Id, q4Id, q5Id) VALUES (?, ?, ?, ?, ?, ?, ?)", (
                ''.join(self.boxCategoryTF.get()), ''.join(self.boxDifficultyTF.get()), self.qID[0][0], self.qID[1][0],
                self.qID[2][0], self.qID[3][0], self.qID[4][0]))
        self.conn3.commit()
        self.conn3.close()
        print("Insertion done for TF")

    # Creating UI elements
    def window_ui(self):

        # Create Tab Control
        self.tabs = ttk.Notebook(self.root)
        # Tab1
        self.tab1 = ttk.Frame(self.tabs)
        self.tabs.add(self.tab1, text="Multiple Choice Question Viewer")

        # Tab2
        self.tab2 = ttk.Frame(self.tabs)
        self.tabs.add(self.tab2, text="Multiple Choice Quiz Creator")
        self.tabs.pack(expand=1, fill="both")

        # Tab3
        self.tab3 = ttk.Frame(self.tabs)
        self.tabs.add(self.tab3, text="True/False Question Viewer")
        self.tabs.pack(expand=1, fill="both")

        # Tab4
        self.tab4 = ttk.Frame(self.tabs)
        self.tabs.add(self.tab4, text="True/False Quiz Creator")
        self.tabs.pack(expand=1, fill="both")

        # Tab5
        self.tab5 = ttk.Frame(self.tabs)
        self.tabs.add(self.tab5, text="Multiple Choice Quiz Viewer")
        self.tabs.pack(expand=1, fill="both")

        # Tab6
        self.tab6 = ttk.Frame(self.tabs)
        self.tabs.add(self.tab6, text="True/False Quiz Viewer")
        self.tabs.pack(expand=1, fill="both")

        # Tab7
        self.tab7 = ttk.Frame(self.tabs)
        self.tabs.add(self.tab7, text="Quizzes in use")
        self.tabs.pack(expand=1, fill="both")

        # Tab Name Labels
        self.tab1Title = ttk.Label(self.tab1, text="Multiple Choice Question Viewer")
        self.tab1Title.pack()
        self.tab1Title.config(font=("Ubuntu", 40))

        self.tab2Title = ttk.Label(self.tab2, text="Multiple Choice Quiz Creator")
        self.tab2Title.pack()
        self.tab2Title.config(font=("Ubuntu", 40))

        self.tab3Title = ttk.Label(self.tab3, text="True/False Question Viewer")
        self.tab3Title.pack()
        self.tab3Title.config(font=("Ubuntu", 40))

        self.tab4Title = ttk.Label(self.tab4, text="True/False Quiz Creator")
        self.tab4Title.pack()
        self.tab4Title.config(font=("Ubuntu", 40))

        self.tab5Title = ttk.Label(self.tab5, text="Multiple Choice Quiz Viewer")
        self.tab5Title.pack()
        self.tab5Title.config(font=("Ubuntu", 40))

        self.tab6Title = ttk.Label(self.tab6, text="True/False Quiz Viewer")
        self.tab6Title.pack()
        self.tab6Title.config(font=("Ubuntu", 40))

        self.tab6Title = ttk.Label(self.tab7, text="Quizzes in Use")
        self.tab6Title.pack()
        self.tab6Title.config(font=("Ubuntu", 40))

        # Tree for MC QUESTION
        self.tree = ttk.Treeview(self.tab1, column=(
            "column", "colunn1", "colunn2", "colunn3", "colunn4", "colunn5", "colunn6", "colunn7"), show="headings")
        self.tree.heading("#0", text="NUMBER")
        self.tree.heading("#1", text="ID")
        self.tree.heading("#2", text="Question")
        self.tree.heading("#3", text="Category")
        self.tree.heading("#4", text="Difficulty")
        self.tree.heading("#5", text="Correct")
        self.tree.heading("#6", text="Wrong Answer 1")
        self.tree.heading("#7", text="Wrong Answer 2")
        self.tree.heading("#8", text="Wrong Answer 3")
        self.tree.pack()

        # Tree for TF QUESTION
        self.tree2 = ttk.Treeview(self.tab3, column=("column", "colunn1", "colunn2", "colunn3", "colunn4"),
                                  show="headings")
        self.tree2.heading("#0", text="NUMBER")
        self.tree2.heading("#1", text="ID")
        self.tree2.heading("#2", text="Question")
        self.tree2.heading("#3", text="Category")
        self.tree2.heading("#4", text="Difficulty")
        self.tree2.heading("#5", text="Correct")
        self.tree2.pack()

        # Tree for MC Quiz Viewer
        self.tree3 = ttk.Treeview(self.tab5, column=(
        "column", "colunn1", "colunn2", "colunn3", "colunn4", "colunn5", "colunn6", "colunn7"), show="headings")
        self.tree3.heading("#0", text="NUMBER")
        self.tree3.heading("#1", text="QuizID")
        self.tree3.heading("#2", text="Category")
        self.tree3.heading("#3", text="Difficulty")
        self.tree3.heading("#4", text="Question 1")
        self.tree3.heading("#5", text="Question 2")
        self.tree3.heading("#6", text="Question 3")
        self.tree3.heading("#7", text="Question 4")
        self.tree3.heading("#8", text="Question 5")
        self.tree3.pack()

        # Tree for TF Quiz Viewer
        self.tree4 = ttk.Treeview(self.tab6, column=(
        "column", "colunn1", "colunn2", "colunn3", "colunn4", "colunn5", "colunn6", "colunn7"), show="headings")
        self.tree4.heading("#0", text="NUMBER")
        self.tree4.heading("#1", text="QuizID")
        self.tree4.heading("#2", text="Category")
        self.tree4.heading("#3", text="Difficulty")
        self.tree4.heading("#4", text="Question 1")
        self.tree4.heading("#5", text="Question 2")
        self.tree4.heading("#6", text="Question 3")
        self.tree4.heading("#7", text="Question 4")
        self.tree4.heading("#8", text="Question 5")
        self.tree4.pack()

        # Tree for quiz in use
        self.tree5 = ttk.Treeview(self.tab7, column=(
            "column", "colunn1", "profile"), show="headings")
        self.tree5.heading("#0", text="NUMBER")
        self.tree5.heading("#1", text="Profile")
        self.tree5.heading("#2", text="Multi Choice Quiz")
        self.tree5.heading("#3", text="True/False Quiz")
        self.tree5.pack()

        # Buttons for MC QUESTION
        self.bDispAllQ = Button(self.tab1, text="Display All Multiple Choice Questions", command=self.display)
        self.bDispAllQ.pack(side=BOTTOM, ipady=50, expand=1)

        self.bGenQuiz = Button(self.tab2, text="Create Multiple Choice Quiz", command=self.createMCQuiz)
        self.bGenQuiz.pack(side=BOTTOM, ipady=30, pady=20, expand=1)

        self.bDispAllQuizes = Button(self.tab5, text="Display All Multiple Choice Quizzes", command=self.quizDispMC)
        self.bDispAllQuizes.pack(side=BOTTOM, ipady=50, expand=1)

        # Buttons for TF QUESTION
        self.bDispAllQTF = Button(self.tab3, text="Display All True/False Questions", command=self.displayTF)
        self.bDispAllQTF.pack(side=BOTTOM, ipady=50, expand=1)

        self.bGenQuiz = Button(self.tab4, text="Create True/False Quiz", command=self.createTFQuiz)
        self.bGenQuiz.pack(side=BOTTOM, ipady=30, pady=20, expand=1)

        self.bDispAllQuizesTF = Button(self.tab6, text="Display All True/False Quizzes", command=self.quizDispTF)
        self.bDispAllQuizesTF.pack(side=BOTTOM, ipady=50, expand=1)

        #Button for quiz in use
        self.bUseQuiz = Button(self.tab7, text="Use those quizes", command=self.useQuiz)
        self.bUseQuiz.pack(side=BOTTOM, ipady=30, pady=15, expand=1)

        # Button for going back
        self.backButton = Button(self.root, text="Back to main menu", command=self.goBack)
        self.backButton.pack()



if __name__ == "__main__":
    application = QuizGen()
    application = mainloop()
