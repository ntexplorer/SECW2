import os
import time
import tkinter as tk
from tkinter import Menu
from tkinter import ttk
from tkinter import messagebox as msg

person1 = [
    {"id": 2, "isCorrect": 0, "q": "2?"},
    {"id": 2, "isCorrect": 0, "q": "2?"},
    {"id": 2, "isCorrect": 0, "q": "2?"},
    {"id": 2, "isCorrect": 0, "q": "2?"},
    {"id": 2, "isCorrect": 0, "q": "2?"},
    {"id": 2, "isCorrect": 0, "q": "2?"},
    {"id": 3, "isCorrect": 0, "q": "3?"},
    {"id": 4, "isCorrect": 0, "q": "4?"},
    {"id": 4, "isCorrect": 0, "q": "4?"},
    {"id": 4, "isCorrect": 0, "q": "4?"},
    {"id": 4, "isCorrect": 0, "q": "4?"},
    {"id": 2, "isCorrect": 0, "q": "2?"},
    {"id": 5, "isCorrect": 0, "q": "5?"},
    {"id": 5, "isCorrect": 0, "q": "5?"},
    {"id": 5, "isCorrect": 0, "q": "5?"},
    {"id": 6, "isCorrect": 0, "q": "6?"},
    {"id": 6, "isCorrect": 0, "q": "6?"},
    {"id": 6, "isCorrect": 1, "q": "6?"},
    {"id": 6, "isCorrect": 0, "q": "6?"},
]
person2 = [
    {"id": 2, "isCorrect": 1, "q": "2?"},
    {"id": 2, "isCorrect": 0, "q": "2?"},
    {"id": 2, "isCorrect": 1, "q": "2?"},
    {"id": 2, "isCorrect": 0, "q": "2?"},
    {"id": 2, "isCorrect": 1, "q": "2?"},
    {"id": 2, "isCorrect": 0, "q": "2?"},
    {"id": 3, "isCorrect": 1, "q": "3?"},
    {"id": 4, "isCorrect": 0, "q": "4?"},
    {"id": 4, "isCorrect": 1, "q": "4?"},
    {"id": 4, "isCorrect": 0, "q": "4?"},
    {"id": 4, "isCorrect": 0, "q": "4?"},
    {"id": 2, "isCorrect": 1, "q": "2?"},
    {"id": 5, "isCorrect": 1, "q": "5?"},
    {"id": 5, "isCorrect": 1, "q": "5?"},
    {"id": 5, "isCorrect": 1, "q": "5?"},
    {"id": 6, "isCorrect": 0, "q": "6?"},
    {"id": 6, "isCorrect": 1, "q": "6?"},
    {"id": 6, "isCorrect": 1, "q": "6?"},
    {"id": 6, "isCorrect": 0, "q": "6?"},
]
personBig = [person2, person1]


class ckStat:
    corListPpl = []  # this list store people's score.
    corListQid = []  # this list store accuracy of per question
    qIdList = []  # this is the list for all appeared question id
    EachQues_List = []  # this is the list to store all keys&values in EachQues_dict.
    qIdQues = []  # the list for questions
    QuesWithID_List = []
    accuForPpl = 0
    quizID = 0
    i = 0

    def doCalculate(self, listPpl):

        personQuiz = listPpl

        # Accuracy for single person.
        global corID_dict, allID_dict, accuForQuesID, QuizQues_dict, accuForPpl

        countQues = 0
        corrQuesNum = 0
        # accuracy for person
        for x in personQuiz[ckStat.quizID]:  # show how many questions for the person
            ckStat.qIdList.append(
                personQuiz[ckStat.quizID][countQues].get("id"))  # append all Question id into qIdList

            # append all questions into EachQues_list.
            ckStat.qIdQues.append(personQuiz[ckStat.quizID][countQues].get("q"))

            ansForQues = personQuiz[ckStat.quizID][countQues].get("isCorrect")  # show if answer isCorrect
            if ansForQues is 1:  # check if answer is correct
                corrQuesNum += 1  # if correct, add id to correctQuesID list
                corrQuesID = personQuiz[ckStat.quizID][countQues].get("id")
                ckStat.corListQid.append(corrQuesID)
            else:
                pass

            # create dictionaries
            corID_dict = {}  # set dict storing correct ID
            allID_dict = {}  # set dict storing all ID

            for cQId in ckStat.corListQid:  # show times of each correct question id
                corID_dict[cQId] = corID_dict.get(cQId, 0) + 1  # create new dict for correct Q's ID
            for aQid in ckStat.qIdList:  # show times of all question ids
                allID_dict[aQid] = allID_dict.get(aQid, 0) + 1  # create new dict for all Q's ID

            countQues += 1  # control the counter

        # create new dict for saving accuracy of each questions {Q1: 50.00%, Q2: 25.00%, ... Qn: 100.00%}
        self.EachQues_dict = {}

        # accuracy for each question
        for allKeys in allID_dict.keys():  # scan values by keys
            if corID_dict.get(allKeys) is None:  # incorrect question's value would be None
                corID_dict[allKeys] = 0  # if None/int, TypeError. set None to 0
            else:
                accuByQid = corID_dict.get(allKeys, 0) / allID_dict.get(allKeys, 0)  # calculate accuracy
                percentAccu = "%.2f%%" % (accuByQid * 100)  # switch float type to percentage
                self.EachQues_dict["Q{}".format(allKeys)] = percentAccu  # set keys and values into dict
                # print("Qid{}: {:.2%}".format(allKeys, accuByQid))  # print out

        ckStat.accuForPpl = corrQuesNum / countQues
        ckStat.corListPpl.append(ckStat.accuForPpl)  # append correct percentage of each person into list

        self.aveAccu = 0
        for ppl in range(len(ckStat.corListPpl)):
            self.aveAccu = (self.aveAccu + ckStat.accuForPpl) / len(ckStat.corListPpl)  # calculate for average

        # create new dict for saving each qid's question dict
        QuizQues_dict = {}

        # store question with qid
        for keys in ckStat.qIdQues:
            QuizQues_dict[keys] = QuizQues_dict.get(keys, 0) + 1

        # combine QuestionID_dict with Questions_dict to a new Dict showing Q{}: {}
        newDic = dict(map(lambda x, y: [x, y], list(allID_dict.keys()), list(QuizQues_dict.keys())))
        for keys, values in self.EachQues_dict.items():
            ckStat.EachQues_List.append("\n{}: {}\n".format(keys, str(values)))
        for keys, values in newDic.items():
            ckStat.QuesWithID_List.append("\nQ{}: {}\n".format(keys, str(values)))

    def ckStatValues(self, select):  # feel free to use these data
        self.select = select
        if select == "aveAccu":
            return float(self.aveAccu)
        elif select == "QuesDict":
            return "{}".format(" ".join(ckStat.EachQues_List))
        else:
            pass

    def outputTXT(self):  # output data into .txt
        folderName = "ckStatData"

        text = ["The score for this person: {:.2%}\n\n".format(ckStat.accuForPpl),
                # "The average score: {:.2%}\n\n".format(self.aveAccu),
                "\nThe calculate for each questions: \n{}\n".format(" ".join(ckStat.EachQues_List)),
                "\nHere are the question lists. \n{}" \
                    .format(" ".join(ckStat.QuesWithID_List))]

        if folderName not in os.listdir(os.getcwd()):  # if not in, then create folder and files
            os.mkdir("ckStatData")  # create new dir to store output
            os.chdir("ckStatData")  # change dir
            file = open("{}.txt".format(time.strftime("%Y%m%d %Hh%Mm%Ss", time.localtime())), mode="w")  # create file
            file.writelines(text)
            os.chdir("../")
            msg.showinfo("Congratulations", "File output complete. \n"
                                            "File name: {}".format(time.strftime("%Y%m%d %Hh%Mm%Ss", time.localtime())))

        else:  # if yes, create files
            os.chdir("ckStatData")  # change dir
            file = open("{}.txt".format(time.strftime("%Y%m%d %Hh%Mm%Ss", time.localtime())), mode="w")
            file.writelines(text)
            os.chdir("../")
            msg.showinfo("Congratulations", "File output complete. \n"
                                            "File name: {}".format(time.strftime("%Y%m%d %Hh%Mm%Ss", time.localtime())))
        file.close()

    def quit(self):
        win = tk.Tk()
        win.quit()
        exit()

    def importScore(self):
        aveAccur.set("{:.2%}".format(ckStat.accuForPpl))

    def quesDisplay(self, event):
        self.item = list(tree.item(tree.selection()[0], "values"))
        QID_List = ckStat.QuesWithID_List
        for i in range(len(QID_List)):
            if self.item[0] in QID_List[i]:
                quesDisp.set("{}".format(QID_List[i]))

    def importFile(self):
        for i in range(100):
            progBar["value"] = i + 1
            averAccu_Frame.update()
            time.sleep(0.007)

        x = ckStat()
        if ckStat.quizID == 0:
            x.doCalculate(personBig)
            ckStat.quizID += 1
        else:
            x.doCalculate(personBig)
            ckStat.quizID += 1
        msg.showinfo("Congratulations", "File import complete. \n")

    def cleanTable(self):
        x = tree.get_children()
        for item in x:
            tree.delete(item)
        quesDisp.set("")

    def displayDetail(self):
        # display Question-Accuracy
        data = ckStat.EachQues_List
        for keys in range(len(data)):
            tree.insert("", keys, values=data[keys])

    # ================ Build GUI ==================
    def display(self):

        # create new gui
        win = tk.Tk()
        win.title("CHECK STATISTIC - Quiz System by Team G")
        win.resizable(False, False)

        # set menus
        menu_bar = Menu(win)
        win.config(menu=menu_bar)
        file_menu = Menu(menu_bar, tearoff=0)

        # create File bar
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Exit", command=quit)

        # ============== create new Tabs =================
        tabControl = ttk.Notebook(win, padding=2)
        tab1 = ttk.Frame(tabControl)
        tabControl.add(tab1, text="Score")
        tab2 = ttk.Frame(tabControl)
        tabControl.add(tab2, text="Questions")
        tabControl.pack(expand=1, fill="both")

        # ============== set first tab =============
        # set new Tab as Score
        global averAccu_Frame
        averAccu_Frame = ttk.Labelframe(tab1, text="Score Display")
        averAccu_Frame.grid(column=0, row=0, padx=20, pady=20)

        # create button: ImportFile
        impFile = ttk.Button(averAccu_Frame, text="Import File (First)", command=self.importFile)
        impFile.grid(column=0, row=0, padx=10, pady=10)
        # create button: importScore
        impScore = ttk.Button(averAccu_Frame, text="Show Score (Second)", command=self.importScore)
        impScore.grid(column=1, row=0, padx=55, pady=10)

        # set Person score part
        ttk.Label(averAccu_Frame, text="Person's Score (%) : ").grid(column=0, row=1, padx=15, pady=10, sticky="e")
        global aveAccur
        aveAccur = tk.StringVar()

        ttk.Label(averAccu_Frame, textvariable=aveAccur, width=20, borderwidth=2, anchor="center",
                  relief="groove") \
            .grid(column=1, row=1, padx=20, pady=10)

        # create Exit button
        exitBut = ttk.Button(averAccu_Frame, text="Exit", command=quit)
        exitBut.grid(column=0, row=2, padx=10, pady=20)

        output_ScoreBut = ttk.Button(averAccu_Frame, text="Output in txt", command=self.outputTXT)
        output_ScoreBut.grid(column=1, row=2, padx=15, pady=20)

        # ============= set progressbar ==============
        pBar_Frame = ttk.LabelFrame(tab1, text="Progressing...")
        pBar_Frame.grid(column=0, row=1, padx=20, pady=10)
        global progBar
        progBar = ttk.Progressbar(pBar_Frame, length=350, mode="determinate", orient=tk.HORIZONTAL)
        progBar.grid(column=0, row=0, padx=5, pady=10)

        # ============ set new Tab for display each question's details =============

        # add Question detail display part
        quesFrame = ttk.LabelFrame(tab2, text="Question-Accuracy display")
        quesFrame.grid(column=0, row=0, padx=20, pady=20)

        # create button: importDetail
        output_DetailBut = ttk.Button(quesFrame, text="Display Detail", command=self.displayDetail)
        output_DetailBut.grid(column=0, row=0, padx=10, pady=10)

        # create clean button
        clean_But = ttk.Button(quesFrame, text="Clean Table", command=self.cleanTable)
        clean_But.grid(column=1, row=0, padx=10, pady=10)

        ttk.Label(quesFrame, text="Correct percentage for each question : ", wraplength=120, justify="center") \
            .grid(column=0, row=1, padx=15, pady=15)

        # add treeview display scores
        global tree
        tree = ttk.Treeview(quesFrame, height=4, show="headings", columns=("Question ID", "Accuracy"))
        tree.column("Question ID", width=100, anchor="center")
        tree.column("Accuracy", width=100, anchor="center")
        tree.heading("Question ID", text="Question ID")
        tree.heading("Accuracy", text="Accuracy")
        tree.grid(column=1, row=1, padx=15, pady=5, sticky="NEWS")
        tree.bind("<ButtonRelease-1>", self.quesDisplay)

        # add tree Scrollbar
        tScrollbar = ttk.Scrollbar(quesFrame, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=tScrollbar.set)
        tScrollbar.grid(column=2, row=1, sticky="NS")

        sep = ttk.Separator(win, orient="horizontal")
        sep.pack(fill=tk.X)
        # =========== create new Frame for question display============
        dispFrame = ttk.LabelFrame(tab2, text="Question display")
        dispFrame.grid(column=0, row=1, padx=20, pady=10, sticky="w")

        ttk.Label(dispFrame, text="Question display : ").grid(column=0, row=0, padx=15, pady=10)

        global quesDisp
        quesDisp = tk.StringVar()
        ttk.Label(dispFrame, textvariable=quesDisp, width=30, borderwidth=2, anchor="center", justify="center",
                  relief="groove").grid(column=1, row=0, padx=15, pady=20)

        win.mainloop()


if __name__ == "__main__":
    personZ = ckStat()
    personZ.display()

