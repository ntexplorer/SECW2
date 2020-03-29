from tkinter import *
from tkinter import ttk
import sqlite3






class QuizGen:

    def __init__(self, categories = [], difficulties = [], categoriesTF = [], difficultiesTF = []):
        self.difficulties = difficulties
        self.categories = categories
        self.difficultiesTF = difficultiesTF
        self.categoriesTF = categoriesTF
        self.root = Tk()
        self.root.title("Quiz Manager")
        self.window_ui()
        self.showCategories()
        self.showDifficulties()
        self.showCategoriesTF()
        self.showDifficultiesTF()

    #Loading and displaying all MC questions in Treeview
    def display(self):
        self.conn = sqlite3.connect("system.db")
        self.cur = self.conn.cursor()
        self.cur.execute("SELECT * FROM MC_QUESTION")
        self.rows = self.cur.fetchall()
        for row in self.rows:
            print(row)
            self.tree.insert("", END, values=row)
        self.conn.close()




    #Loading and displaying all TF questions in Treeview
    def displayTF(self):
        self.conn = sqlite3.connect("system.db")
        self.cur = self.conn.cursor()
        self.cur.execute("SELECT * FROM TF_QUESTION")
        self.rows = self.cur.fetchall()
        for row in self.rows:
            print(row)
            self.tree2.insert("", END, values=row)
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



    #Event for TF category
    def boxCategoryValueTF(self):
        self.boxcatvalueTF = self.boxCategoryTF.get()
        self.boxcatvalueTF = str(self.boxcatvalueTF)
        print(self.boxcatvalueTF)
        print(type(self.boxcatvalueTF))



    #Event for TF difficulty
    def boxDifficultyValueTF(self):
        choiceDiffTF = self.boxDifficultyTF.get()
        choiceDiffTF = str(choiceDiffTF)
        print(choiceDiffTF)
        print(type(choiceDiffTF))




    #Categories for MC QUESTION combobox


    def showCategories(self):
        self.conn = sqlite3.connect("system.db")
        self.cur = self.conn.cursor()
        self.cur.execute("SELECT DISTINCT Category FROM MC_QUESTION ORDER BY Category ASC")
        self.rows = self.cur.fetchall()
        for row in self.rows:
            print(row)
            self.categories.append(row[0])
        self.conn.close()

        # Lables and comboboxes for MC QUESTION
        self.lbCategory = Label(self.tab2, text="Choose Catgegory")
        self.lbCategory.pack(ipady=50)

        self.boxCategory = ttk.Combobox(self.tab2, values=self.categories, width=30, state="readonly")
        self.boxCategory.pack()
        self.boxCategory.current(0)
        self.boxCategory.bind("<<ComboboxSelected>>", lambda y: self.boxCategoryValue())



    # Difficulties for MC QUESTION combobox

    def showDifficulties(self):
        self.conn = sqlite3.connect("system.db")
        self.cur = self.conn.cursor()
        self.cur.execute("SELECT DISTINCT Difficulty FROM MC_QUESTION")
        self.rows = self.cur.fetchall()
        for row in self.rows:
            print(row)
            self.difficulties.append(row[0])
        self.conn.close()

        self.lbDifficulty = Label(self.tab2, text="Choose Difficulty")
        self.lbDifficulty.pack(ipady=50)

        self.boxDifficulty = ttk.Combobox(self.tab2, values=self.difficulties, width=30, state="readonly")
        self.boxDifficulty.pack()
        self.boxDifficulty.current(0)
        self.boxDifficulty.bind("<<ComboboxSelected>>", lambda x: self.boxDifficultyValue())

    # Categories for TF QUESTION combobox

    def showCategoriesTF(self):
        self.conn = sqlite3.connect("system.db")
        self.cur = self.conn.cursor()
        self.cur.execute("SELECT DISTINCT Category FROM TF_QUESTION ORDER BY Category ASC")
        self.rows = self.cur.fetchall()
        for row in self.rows:
            print(row)
            self.categoriesTF.append(row[0])
        self.conn.close()

        self.lbCategoryTF = Label(self.tab4, text="Choose Catgegory")
        self.lbCategoryTF.pack(ipady=50)

        self.boxCategoryTF = ttk.Combobox(self.tab4, values=self.categoriesTF, width=30, state="readonly")
        self.boxCategoryTF.pack()
        self.boxCategoryTF.current(0)
        self.boxCategoryTF.bind("<<ComboboxSelected>>", lambda x: self.boxCategoryValueTF())

    # Difficulties for TF QUESTION combobox

    def showDifficultiesTF(self):
        self.conn = sqlite3.connect("system.db")
        self.cur = self.conn.cursor()
        self.cur.execute("SELECT DISTINCT Difficulty FROM TF_QUESTION")
        self.rows = self.cur.fetchall()
        for row in self.rows:
            print(row)
            self.difficultiesTF.append(row[0])
        self.conn.close()

        self.lbDifficultyTF = Label(self.tab4, text="Choose Difficulty")
        self.lbDifficultyTF.pack(ipady=50)

        self.boxDifficultyTF = ttk.Combobox(self.tab4, values=self.difficultiesTF, width=30, state="readonly")
        self.boxDifficultyTF.pack()
        self.boxDifficultyTF.current(0)
        self.boxDifficultyTF.bind("<<ComboboxSelected>>", lambda y: self.boxDifficultyValueTF)



    #Create MC Quiz table and add values
    def createMCQuiz(self):
        self.qID = []
        self.conn = sqlite3.connect("system.db")
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS MC_QUIZ ("
                "QuizID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, " 
                "CATEGORY TEXT NOT NULL, "
                "DIFFICULTY TEXT NOT NULL, "
                "q1Id TEXT, "
                "q2Id TEXT, "
                "q3Id TEXT, "
                "q4Id TEXT, "
                "q5Id TEXT, "
                "FOREIGN KEY (q1Id) REFERENCES MC_QUESTION(pid), "
                "FOREIGN KEY (q2Id) REFERENCES MC_QUESTION(pid), "
                "FOREIGN KEY (q3Id) REFERENCES MC_QUESTION(pid), "
                "FOREIGN KEY (q4Id) REFERENCES MC_QUESTION(pid), "
                "FOREIGN KEY (q5Id) REFERENCES MC_QUESTION(pid))")
        self.conn.commit()

        print("Quiz table Created")


        self.conn = sqlite3.connect("system.db")

        self.cur.execute("SELECT pid FROM MC_QUESTION pid WHERE difficulty = ? AND category = ? ORDER BY RANDOM() LIMIT 5", (''.join(self.boxDifficulty.get()), ''.join(self.boxCategory.get())))
        self.item = self.cur.fetchall()
        print("List of ID length is: ", len(self.item))
        print(''.join(self.boxCategory.get()))
        for row in self.item:
            print(row)
            self.qID.append(row)




        print(self.qID[1][0])
        print(type(self.qID[1][0]))
        print("Selection")



        self.cur.execute("INSERT INTO MC_QUIZ (Category, Difficulty, q1Id, q2Id, q3Id, q4Id, q5Id) VALUES (?, ?, ?, ?, ?, ?, ?)", (''.join(self.boxCategory.get()), ''.join(self.boxDifficulty.get()), self.qID[0][0], self.qID[1][0], self.qID[2][0], self.qID[3][0], self.qID[4][0]))
        self.conn.commit()
        self.conn.close()
        print("Insertion done for MC")





        #Create TF Quiz table and add values
    def createTFQuiz(self):
        self.qID = []
        self.conn = sqlite3.connect("system.db")
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS TF_QUIZ ("
                "QuizID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, " 
                "CATEGORY TEXT NOT NULL, "
                "DIFFICULTY TEXT NOT NULL, "
                "q1Id TEXT, "
                "q2Id TEXT, "
                "q3Id TEXT, "
                "q4Id TEXT, "
                "q5Id TEXT, "
                "FOREIGN KEY (q1Id) REFERENCES TF_QUESTION(pid), "
                "FOREIGN KEY (q2Id) REFERENCES TF_QUESTION(pid), "
                "FOREIGN KEY (q3Id) REFERENCES TF_QUESTION(pid), "
                "FOREIGN KEY (q4Id) REFERENCES TF_QUESTION(pid), "
                "FOREIGN KEY (q5Id) REFERENCES TF_QUESTION(pid))")
        self.conn.commit()

        print("Quiz TF table Created")


        self.conn = sqlite3.connect("system.db")

        self.cur.execute("SELECT pid FROM TF_QUESTION pid WHERE difficulty = ? AND category = ? ORDER BY RANDOM() LIMIT 5", (''.join(self.boxDifficultyTF.get()), ''.join(self.boxCategoryTF.get())))
        self.item = self.cur.fetchall()
        print("List of ID length is: ", len(self.item))
        for row in self.item:
            print(row)
            self.qID.append(row)




        print(self.qID[1][0])
        print(type(self.qID[1][0]))
        print("Selection TF")



        self.cur.execute("INSERT INTO TF_QUIZ (Category, Difficulty, q1Id, q2Id, q3Id, q4Id, q5Id) VALUES (?, ?, ?, ?, ?, ?, ?)", (''.join(self.boxCategoryTF.get()), ''.join(self.boxDifficultyTF.get()), self.qID[0][0], self.qID[1][0], self.qID[2][0], self.qID[3][0], self.qID[4][0]))
        self.conn.commit()
        self.conn.close()
        print("Insertion done for TF")




    #Creating UI elements
    def window_ui(self):

        #Create Tab Control
        self.tabs = ttk.Notebook(self.root)
        #Tab1
        self.tab1 = ttk.Frame(self.tabs)
        self.tabs.add(self.tab1, text="MC Question Viewer")

        #Tab2
        self.tab2 = ttk.Frame(self.tabs)
        self.tabs.add(self.tab2, text="MC Quiz Creator")
        self.tabs.pack(expand=1, fill="both")

        #Tab3
        self.tab3 = ttk.Frame(self.tabs)
        self.tabs.add(self.tab3, text="TF Question Viewer")
        self.tabs.pack(expand=1, fill="both")


        #Tab4
        self.tab4 = ttk.Frame(self.tabs)
        self.tabs.add(self.tab4, text="TF Quiz Creator")
        self.tabs.pack(expand=1, fill="both")

        #Tab Name Labels
        self.tab1Title = ttk.Label(self.tab1, text="MC Question Viewer")
        self.tab1Title.pack()
        self.tab1Title.config(font=("Ubuntu", 40))


        self.tab2Title = ttk.Label(self.tab2, text="Multi Choice Quiz Creator")
        self.tab2Title.pack()
        self.tab2Title.config(font=("Ubuntu", 40))


        self.tab3Title = ttk.Label(self.tab3, text="True/False Question Viewer")
        self.tab3Title.pack()
        self.tab3Title.config(font=("Ubuntu", 40))


        self.tab4Title = ttk.Label(self.tab4, text="True/False Quiz Creator")
        self.tab4Title.pack()
        self.tab4Title.config(font=("Ubuntu", 40))


        #Tree for MC QUESTION
        self.tree = ttk.Treeview(self.tab1, column=("column", "colunn1", "colunn2", "colunn3", "colunn4", "colunn5", "colunn6", "colunn7"), show="headings")
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



        #Tree for TF QUESTION
        self.tree2 = ttk.Treeview(self.tab3, column=("column", "colunn1", "colunn2", "colunn3", "colunn4"), show="headings")
        self.tree2.heading("#0", text="NUMBER")
        self.tree2.heading("#1", text="ID")
        self.tree2.heading("#2", text="Question")
        self.tree2.heading("#3", text="Category")
        self.tree2.heading("#4", text="Difficulty")
        self.tree2.heading("#5", text="Correct")
        self.tree2.pack()



        #Buttons for MC QUESTION
        self.bDispAllQ = Button(text="Display All MC Questions", command=self.display)
        self.bDispAllQ.pack(side=LEFT, ipady=50, expand=1)

        self.bGenQuiz = Button(text="Create MC Quiz", command=self.createMCQuiz)
        self.bGenQuiz.pack(side=LEFT, ipady=50, expand=1)



        #Buttons for TF QUESTION
        self.bDispAllQTF = Button(text="Display All TF Questions", command=self.displayTF)
        self.bDispAllQTF.pack(side=LEFT, ipady=50, expand=1)

        self.bGenQuiz = Button(text="Create TF Quiz", command=self.createTFQuiz)
        self.bGenQuiz.pack(side=LEFT, ipady=50, expand=1)















application = QuizGen()
application = mainloop()



































