from tkinter import *
from tkinter import ttk
import sqlite3




#Loading and displaying all MC questions in Treeview
def display():
    conn = sqlite3.connect("system.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM MC_QUESTION")
    rows = cur.fetchall()
    for row in rows:
        print(row)
        tree.insert("", END, values=row)
    conn.close()
    print(choiceDiff)
    print(choiceCategory)

    


#Loading and displaying all TF questions in Treeview
def displayTF():
    conn = sqlite3.connect("system.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM TF_QUESTION")
    rows = cur.fetchall()
    for row in rows:
        print(row)
        tree.insert("", END, values=row)
    conn.close()
    print(choiceDiff)
    print(choiceCategory)




choiceCategory = ""
#Event for MC category
def boxCategoryValue(event):
    global boxcatvalue
    boxcatvalue = boxCategory.get()
    boxcatvalue = str(boxcatvalue)
    print(boxcatvalue)
    print(type(boxcatvalue))


choiceDiff = ""
#Event for MC difficulty
def boxDifficultyValue(event):
    global choiceDiff
    choiceDiff = boxDifficulty.get()
    choiceDiff = str(choiceDiff)
    print(choiceDiff)
    print(type(choiceDiff))





choiceCategoryTF = ""
#Event for MC category
def boxCategoryValueTF(event):
    global boxcatvalueTF
    boxcatvalueTF = boxCategoryTF.get()
    boxcatvalueTF = str(boxcatvalueTF)
    print(boxcatvalueTF)
    print(type(boxcatvalueTF))


choiceDiffTF = ""
#Event for MC difficulty
def boxDifficultyValueTF(event):
    global choiceDiffTF
    choiceDiffTF = boxDifficultyTF.get()
    choiceDiffTF = str(choiceDiffTF)
    print(choiceDiffTF)
    print(type(choiceDiffTF))






def createMCQuiz():
    qID = []
    conn = sqlite3.connect("system.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS MC_QUIZ ("
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
    conn.commit()

    print("Quiz table Created")


    conn = sqlite3.connect("system.db")

    cur.execute("SELECT pid FROM MC_QUESTION pid WHERE difficulty = ? AND category = ? ORDER BY RANDOM() LIMIT 5", (''.join(boxDifficulty.get()), ''.join(boxCategory.get())))
    item = cur.fetchall()
    print("List of ID length is: ", len(item))
    for row in item:
        print(row)
        qID.append(row)
        
        

    
    print(qID[1][0])
    print(type(qID[1][0]))
    print("Selection")

    

    cur.execute("INSERT INTO MC_QUIZ (Category, Difficulty, q1Id, q2Id, q3Id, q4Id, q5Id) VALUES (?, ?, ?, ?, ?, ?, ?)", (choiceCategory, choiceDiff, qID[0][0], qID[1][0], qID[2][0], qID[3][0], qID[4][0]))
    #cur.execute("INSERT INTO MC_QUIZ (Category, Difficulty, q1Id, q2Id, q3Id, q4Id, q5Id) VALUES (?, ?, ?, ?, ?, ?, ?)", (''.join(boxDifficulty.get()), ''.join(boxCategory.get()), qID[0][0], qID[1][0], qID[2][0], qID[3][0], qID[4][0]))
    conn.commit()
    conn.close()
    print("Insertion done")
    

    

#Categories for MC QUESTION combobox
categories = []

def showCategories():
    conn = sqlite3.connect("system.db")
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT Category FROM MC_QUESTION ORDER BY Category ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
        categories.append(row)
    conn.close()


showCategories()


#Difficulties for MC QUESTION combobox
difficulties = []

def showDifficulties():
    conn = sqlite3.connect("system.db")
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT Difficulty FROM MC_QUESTION")
    rows = cur.fetchall()
    for row in rows:
        print(row)
        difficulties.append(row)
    conn.close()

    
showDifficulties()





#Categories for TF QUESTION combobox
categoriesTF = []

def showCategoriesTF():
    conn = sqlite3.connect("system.db")
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT Category FROM TF_QUESTION ORDER BY Category ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
        categoriesTF.append(row)
    conn.close()


showCategoriesTF()


#Difficulties for TF QUESTION combobox
difficultiesTF = []

def showDifficultiesTF():
    conn = sqlite3.connect("system.db")
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT Difficulty FROM TF_QUESTION")
    rows = cur.fetchall()
    for row in rows:
        print(row)
        difficultiesTF.append(row)
    conn.close()

    
showDifficultiesTF()






# intializing the window
root = Tk()
root.title("Quiz Manager")
# configuring size of the window

#Create Tab Control
tabs = ttk.Notebook(root)
#Tab1
tab1 = ttk.Frame(tabs)
tabs.add(tab1, text="MC Question Viewer")

#Tab2
tab2 = ttk.Frame(tabs)
tabs.add(tab2, text="MC Quiz Creator")
tabs.pack(expand=1, fill="both")

#Tab3
tab3 = ttk.Frame(tabs)
tabs.add(tab3, text="TF Question Viewer")
tabs.pack(expand=1, fill="both")


#Tab4
tab4 = ttk.Frame(tabs)
tabs.add(tab4, text="TF Quiz Creator")
tabs.pack(expand=1, fill="both")

#Tab Name Labels
tab1Title = ttk.Label(tab1, text="MC Question Viewer")
tab1Title.pack()
tab1Title.config(font=("Ubuntu", 40))


tab2Title = ttk.Label(tab2, text="Multi Choice Quiz Creator")
tab2Title.pack()
tab2Title.config(font=("Ubuntu", 40))


tab3Title = ttk.Label(tab3, text="True/False Question Viewer")
tab3Title.pack()
tab3Title.config(font=("Ubuntu", 40))


tab4Title = ttk.Label(tab4, text="True/False Quiz Creator")
tab4Title.pack()
tab4Title.config(font=("Ubuntu", 40))



#Tree for MC QUESTION
tree = ttk.Treeview(tab1, column=("column", "colunn1", "colunn2", "colunn3", "colunn4", "colunn5", "colunn6", "colunn7"), show="headings")
tree.heading("#0", text="NUMBER")
tree.heading("#1", text="ID")
tree.heading("#2", text="Question")
tree.heading("#3", text="Category")
tree.heading("#4", text="Difficulty")
tree.heading("#5", text="Correct")
tree.heading("#6", text="Wrong Answer 1")
tree.heading("#7", text="Wrong Answer 2")
tree.heading("#8", text="Wrong Answer 3")
tree.pack()


#Tree for TF QUESTION
tree2 = ttk.Treeview(tab3, column=("column", "colunn1", "colunn2", "colunn3", "colunn4"), show="headings")
tree2.heading("#0", text="NUMBER")
tree2.heading("#1", text="ID")
tree2.heading("#2", text="Question")
tree2.heading("#3", text="Category")
tree2.heading("#4", text="Difficulty")
tree2.heading("#5", text="Correct")
tree2.pack()



#Buttons for MC QUESTION
bDispAllQ = Button(text="Display All MC Questions", command=display)
bDispAllQ.pack(side=BOTTOM)

bGenQuiz = Button(text="Create MC Quiz", command=createMCQuiz)
bGenQuiz.pack(side=BOTTOM)




#Buttons for TF QUESTION
bDispAllQTF = Button(text="Display All TF Questions", command=displayTF)
bDispAllQTF.pack(side=BOTTOM)

bGenQuiz = Button(text="Create TF Quiz", command=createMCQuiz)
bGenQuiz.pack(side=BOTTOM)




#Lables and comboboxes for MC QUESTION
lbCategory = Label(tab2,text="Choose Catgegory")
lbCategory.pack(ipady=50)


boxCategory = ttk.Combobox(tab2, values=categories, width=30, state="readonly")
boxCategory.pack()
boxCategory.current(0)
boxCategory.bind("<<ComboboxSelected>>", boxCategoryValue)





lbDifficulty = Label(tab2,text="Choose Difficulty")
lbDifficulty.pack(ipady=50)


boxDifficulty = ttk.Combobox(tab2, values=difficulties, width=30, state="readonly")
boxDifficulty.pack()
boxDifficulty.current(0)
boxDifficulty.bind("<<ComboboxSelected>>", boxDifficultyValue)















#Lables and comboboxes for TF QUESTION
lbCategoryTF = Label(tab4,text="Choose Catgegory")
lbCategoryTF.pack(ipady=50)


boxCategoryTF = ttk.Combobox(tab4, values=categoriesTF, width=30, state="readonly")
boxCategoryTF.pack()
boxCategoryTF.current(0)
boxCategoryTF.bind("<<ComboboxSelected>>", boxCategoryValueTF)





lbDifficultyTF = Label(tab4,text="Choose Difficulty")
lbDifficultyTF.pack(ipady=50)


boxDifficultyTF = ttk.Combobox(tab4, values=difficultiesTF, width=30, state="readonly")
boxDifficultyTF.pack()
boxDifficultyTF.current(0)
boxDifficultyTF.bind("<<ComboboxSelected>>", boxDifficultyValueTF)
















    


root.mainloop()
