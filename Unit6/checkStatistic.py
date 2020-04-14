import os
import time
import tkinter as tk
from tkinter import Listbox
from tkinter import Menu
from tkinter import ttk
from tkinter import messagebox as msg
from tkinter import Scrollbar
from tkinter import scrolledtext

# person = [
#     [[1, 0, 20], [2, 0, 20], [3, 0, 20], [4, 1, 15]],
#     [[1, 0, 10], [5, 1, 10], [6, 1, 12], [2, 1, 15]],
#     [[3, 1, 10], [2, 0, 10], [4, 0, 12], [6, 1, 15]]
# ]
# len(person) -> how many people
# len(person[0]) -> how many questions it has
# len(person[0][0]) -> the infos of 1st person's 1st question e.g. QuesID=1, isCorrect=0, time=20
# len(person[0][0][0]) -> the quesionID
# len(person[0][0][1]) -> whether the answer is correct


person1 = [
    {"id": 1, "isCorrect": 0},
    {"id": 2, "isCorrect": 1},
    {"id": 3, "isCorrect": 0},
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
personBig = [person1, person2]


class CheckStatistic:
    corListPpl = []  # this list store people's score.
    corListQid = []  # this list store accuracy of per question
    qIdList = []  # this is the list for all appeared question id
    EachQues_List = []  # this is the list to store all keys&values in EachQues_dict.
    qidQues = []  # the list for questions
    QuesWithID = []
    i = 0

    def __init__(self, human):
        self.personQuiz = human

        """
        the 'self.personQuiz = person2' below is just for test. 
        Please change it when have values input
        """
        # self.personQuiz = person2

        # Accuracy for single person.
        global corID_dict, allID_dict, accuForQuesID, QuizQues_dict
        countQues = 0
        corrQuesNum = 0

        # accuracy for person
        for x in self.personQuiz:  # show how many questions for the person
            CheckStatistic.qIdList.append(self.personQuiz[countQues].get("id"))  # append all Question id into qIdList

            # append all questions into EachQues_list.
            CheckStatistic.qidQues.append(self.personQuiz[countQues].get("q"))

            ansForQues = self.personQuiz[countQues].get("isCorrect")  # show if answer isCorrect
            if ansForQues is 1:  # check if answer is correct
                corrQuesNum += 1
                corrQuesID = self.personQuiz[countQues].get("id")  # if correct, add id to correctQuesID list
                CheckStatistic.corListQid.append(corrQuesID)
            else:
                pass

            # create dictionaries
            corID_dict = {}  # set dict storing correct ID
            allID_dict = {}  # set dict storing all ID

            for cQId in CheckStatistic.corListQid:  # show times of each correct question id
                corID_dict[cQId] = corID_dict.get(cQId, 0) + 1  # create new dict for correct Q's ID
            for aQid in CheckStatistic.qIdList:  # show times of all question ids
                allID_dict[aQid] = allID_dict.get(aQid, 0) + 1  # create new dict for all Q's ID

            countQues += 1  # control the counter

        # create new dict for saving accuracy of each questions {Q1: 50.00%, Q2: 25.00%, ... Qn: 100.00%}
        self.EachQues_dict = {}

        # accuracy for each question
        for allKeys in allID_dict.keys():  # scan values by keys
            if corID_dict.get(allKeys) is None:  # incorrect question's value would be None
                corID_dict[allKeys] = 0  # if None/int, TypeError. set None to 0
            else:
                accuByQid = corID_dict.get(allKeys) / allID_dict.get(allKeys)  # calculate accuracy
                percentAccu = "%.2f%%" % (accuByQid * 100)  # switch float type to percentage
                self.EachQues_dict["Q{}".format(allKeys)] = percentAccu  # set keys and values into dict
                # print("Qid{}: {:.2%}".format(allKeys, accuByQid))  # print out

        self.accuForPpl = corrQuesNum / countQues
        CheckStatistic.corListPpl.append(self.accuForPpl)  # append correct percentage of each person into list

        self.aveAccu = 0
        for ppl in range(len(CheckStatistic.corListPpl)):
            self.aveAccu = (self.aveAccu + self.accuForPpl) / len(
                CheckStatistic.corListPpl)  # calculate for average

        # create new dict for saving each qid's question dict
        QuizQues_dict = {}

        # store question with qid
        for keys in CheckStatistic.qidQues:
            QuizQues_dict[keys] = QuizQues_dict.get(keys, 0) + 1

        # create QuesWithID{Q1: "1?", Q2: "2?", ... Qn: "n?"}
        # CheckStatistic.getQidQues_dict(list(allID_dict.keys()), list(QuizQues_dict.keys()))
        # CheckStatistic.getQidQues_dict(list(allID_dict.keys(), list(QuizQues_dict.keys())))

        # print("accuracy for single person: {:.2%}.".format(self.accuForPpl))  # accuracy for single person
        # print("average accuracy for all people: {:.2%}.".format(self.aveAccu))  # average accuracy for all
        # people print("accuracy for each question: {}.".format(self.accuOfEachQues_dict))  # accuracy for each
        # question in dict

    # def checkAccu(self): pass # # Accuracy for single person. # global corID_dict, allID_dict, accuForQuesID #
    # countQues = 0 # corrQuesNum = 0 # # # accuracy for person # for x in self.personQuiz:  # show how many
    # questions for the person #     CheckStatistic.qIdList.append(self.personQuiz[countQues].get("id"))  # append
    # all Question id into qIdList # #     ansForQues = self.personQuiz[countQues].get("isCorrect")  # show if answer
    # isCorrect #     if ansForQues is 1:  # check if answer is correct #         corrQuesNum += 1 #
    # corrQuesID = self.personQuiz[countQues].get("id")  # if correct, add id to correctQuesID list #
    # CheckStatistic.corListQid.append(corrQuesID) # #     else: #         pass # #     # create dictionaries #
    # corID_dict = {}  # set dict storing correct ID #     allID_dict = {}  # set dict storing all ID # #     for
    # cQId in CheckStatistic.corListQid:  # show times of each correct question id #         corID_dict[cQId] =
    # corID_dict.get(cQId, 0) + 1  # create new dict for correct Q's ID #     for aQid in CheckStatistic.qIdList:  #
    # show times of all question ids #         allID_dict[aQid] = allID_dict.get(aQid, 0) + 1  # create new dict for
    # all Q's ID # #     countQues += 1  # control the counter # # # create new dict for saving accuracy of each
    # questions {Q1: 50.00%, Q2: 25.00%, ... Qn: 100.00%} # accuOfEachQues_dict = {} # # # accuracy for each question
    # for allKeys in allID_dict.keys():  # scan values by keys #     if corID_dict.get(allKeys) is None:  # incorrect
    # question's value would be None #         corID_dict[allKeys] = 0  # if None/int, TypeError. set None to 0 #
    # else: #         accuByQid = corID_dict.get(allKeys) / allID_dict.get(allKeys)  # calculate accuracy #
    # percentAccu = "%.2f%%" % (accuByQid * 100)  # switch float type to percentage #         accuOfEachQues_dict[
    # allKeys] = percentAccu  # set keys and values into dict #         print("Qid{}: {:.2%}".format(allKeys,
    # accuByQid))  # print out # # accuForPerson = corrQuesNum / countQues # CheckStatistic.corListPerson.append(
    # accuForPerson)  # append correct percentage of each person into list # # averageAccu = 0 # for ppl in range(
    # len(CheckStatistic.corListPerson)): #     averageAccu = (averageAccu + accuForPerson) / len(
    # CheckStatistic.corListPerson)  # calculate for average% # # print("accuracy for single person: {:.2%}.".format(
    # accuForPerson))  # accuracy for single person # print("average accuracy for all people: {:.2%}.".format(
    # averageAccu))  # average accuracy for all people # print("accuracy for each question: {}.".format(
    # accuOfEachQues_dict))  # accuracy for each question in dict # for ppl in range(len(self.person)):  # count
    # number of people #     print("******************\nPerson {}".format(ppl + 1)) #     for numOfQues in range(len(
    # self.person[0])):  # count number of qestions #         print("Hi, this is person{0}'s ({1}) question!".format(
    # ppl + 1, numOfQues + 1)) # # if person1[0][numOfQues][1] == 1: isCorrect += 1       # if correct, counter + 1
    # print("Nice, question{} is # correct.\n".format(numOfQues+1)) else: # print("Sorry, question{} isn't
    # correct.\n".format(numOfQues+1)) # pass correctNum = isCorrect CheckStatistic.scoreListforALL.append(
    # correctNum) print("person{}'s got {} # corrects.\naccuracy is: {:.2%}".format(ppl+1, correctNum,
    # correctNum/len(person1[0])))
    #
    #     # print("This is the score list for person: ", CheckStatistic.correctListforPerson)
    def getQidQues_dict(list1, list2):
        dic = dict(map(lambda x, y: [x, y], list1, list2))
        return dic

    def ckStatValues(self, select):  # feel free to use these data
        self.select = select
        if select == "aveAccu":
            return float(self.aveAccu)
        elif select == "QuesDict":
            return "{}".format(" ".join(CheckStatistic.EachQues_List))
        else:
            pass

        # accuForPpl = self.accuForPpl
        # aveAccu = self.aveAccu  #
        # accuEachQues = self.accuEachQues_dict

    def outputTXT(self):  # output data into .txt
        folderName = "CheckStatisticData"
        for keys, values in self.EachQues_dict.items():
            CheckStatistic.EachQues_List.append("\n{}: {}\n".format(keys, str(values)))

        text = ["The score for this person: {:.2%}\n\n".format(self.accuForPpl),
                # "The average score: {:.2%}\n\n".format(self.aveAccu),
                "The calculate for each questions: \n{}\n".format(" ".join(CheckStatistic.EachQues_List)),
                "{}".format(CheckStatistic.getQidQues_dict(list(allID_dict.keys()), list(QuizQues_dict.keys())))]

        if folderName not in os.listdir(os.getcwd()):  # if not in, then create folder and files
            os.mkdir("CheckStatisticData")  # create new dir to store output
            os.chdir("CheckStatisticData")  # change dir
            file = open("{}.txt".format(time.strftime("%Y%m%d %Hh%Mm%Ss", time.localtime())), mode="w")  # create file
            file.writelines(text)
            os.chdir("../")
            msg.showinfo("Congratulations", "File output complete. \n"
                                            "File name: {}".format(time.strftime("%Y%m%d %Hh%Mm%Ss", time.localtime())))

        else:  # if yes, create files
            os.chdir("CheckStatisticData")  # change dir
            file = open("{}.txt".format(time.strftime("%Y%m%d %Hh%Mm%Ss", time.localtime())), mode="w")
            file.writelines(text)
            os.chdir("../")
            msg.showinfo("Congratulations", "File output complete. \n"
                                            "File name: {}".format(time.strftime("%Y%m%d %Hh%Mm%Ss", time.localtime())))
        file.close()


def importData(pplList):
    pplList = personBig
    a = CheckStatistic.i
    if a < len(pplList):
        CheckStatistic(pplList[a])
        return importData(pplList[a + 1])
    else:
        pass


# personX = CheckStatistic(person2)
# personY = CheckStatistic(person1)
# personZ = CheckStatistic(person2)
# personZ.outputTXT()


def _quit():
    win = tk.Tk()
    win.quit()
    exit()


# class ckStatGUI(CheckStatistic):

# def __init__(self, human):
#     super().__init__(human)
#
#     # create new gui
#     self.win = tk.Tk()
#     self.win.title("CHECK STATISTIC - Quiz System by Team G")
#     self.win.resizable(False, False)
#
#     # set menus
#     menu_bar = Menu(self.win)
#     self.win.config(menu=menu_bar)
#     file_menu = Menu(menu_bar, tearoff=0)
#
#     # create File bar
#     menu_bar.add_cascade(label="File", menu=file_menu)
#     file_menu.add_command(label="Exit", command=_quit())
#
#     # set new Tab as Score
#     tabControl = ttk.Notebook(self.win)
#     tab1 = ttk.Frame(tabControl)
#     tabControl.add(tab1, text="Score")
#     tab2 = ttk.Frame(tabControl)
#     tabControl.add(tab2, text="Questions")
#     tabControl.pack(expand=1, fill="both")
#
#     # set new Tab as Score
#     averAccu_Frame = ttk.Labelframe(tab1, text="Score Display")
#     averAccu_Frame.grid(column=0, row=0, padx=20, pady=20)
#
#     # print text=""
#     """
#         the 'CheckStatistic(person2)' below is just for test,
#         please change it when values input.
#         """
#     ckstat = CheckStatistic(person2)
#
#     impDataBut = ttk.Button(averAccu_Frame, text="Import Data", command="importData")
#     impDataBut.grid(column=0, row=0, padx=10, pady=10)
#     ttk.Label(averAccu_Frame, text="Person's Score (%) : ").grid(column=0, row=1, padx=15, pady=10)
#     averageAccuracy = tk.StringVar()
#
#     ttk.Label(averAccu_Frame, width=15, textvariable=averageAccuracy, justify="center", relief="groove") \
#         .grid(column=1, row=1, padx=20, pady=10)
#
#     # create Exit button
#     exitBut = ttk.Button(averAccu_Frame, text="Exit", command=_quit)
#     exitBut.grid(column=0, row=2, padx=10, pady=20)
#
#     """
#         The 'CheckStatistic(person2)' is just for test.
#         Please change when values input.
#         """
#     outputButton = ttk.Button(averAccu_Frame, text="Output in txt", command=CheckStatistic(person2).outputTXT)
#     outputButton.grid(column=1, row=2, padx=15, pady=20)
#
#     # set new Tab for Question
#     quesFrame = ttk.LabelFrame(tab2, text="Question-Accuracy display")
#     quesFrame.grid(column=0, row=0, padx=20, pady=20)
#     ttk.Label(quesFrame, text="Correct rate for each Question : ", wraplength=110, justify="center") \
#         .grid(column=0, row=0, padx=15, pady=16)
#     lb = Listbox(self.win)
#     sl = Scrollbar(self.win)
#     sl.pack(side="right", fill="y")
#     for i in CheckStatistic.QuesWithID:
#         lb.insert("end", str(i))
#
#     lb.see(10)
#     lb.pack(side="left")
#     sl["command"] = lb.yview()


win = tk.Tk()
win.title("CHECK STATISTIC")
# win.geometry("440x300")
win.resizable(False, False)
#
#  Set Menus
menu_bar = Menu(win)
win.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)

# create File bar
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Exit", command=_quit)

# create Help me bar
help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About")

# set new Tab as Score
tabControl = ttk.Notebook(win)
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text="Score")
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text="Questions")
tabControl.pack(expand=1, fill="both")

# set new Tab as Score
averAccu_Frame = ttk.LabelFrame(tab1, text="Score display")
averAccu_Frame.grid(column=0, row=0, padx=20, pady=20)

# print text=""
"""
the 'CheckStatistic(person2)' below is just for test,
please change it when values input.
"""
ckSTAT = CheckStatistic(person2)

impDataButton = ttk.Button(averAccu_Frame, text="Import next \nanswer sheet", command="")
impDataButton.grid(column=0, row=0, padx=10, pady=10)

ttk.Label(averAccu_Frame, text="Person's Score (%) : ").grid(column=0, row=1, padx=15, pady=10)
averageAccuracy = tk.StringVar(value="{:.2%}".format(ckSTAT.ckStatValues("aveAccu")))

ttk.Label(averAccu_Frame, width=15, textvariable=averageAccuracy, justify="center", relief="groove") \
    .grid(column=1, row=1, padx=20, pady=10)

# create Exit button
exitButton = ttk.Button(averAccu_Frame, text="Exit", command=_quit)
exitButton.grid(column=0, row=2, padx=10, pady=20)

# def _outpScBox(self):
#     msg.showinfo("Congratulations", "File output complete. \n"
#                                     "File name: {}".format(time.strftime("%Y%m%d %Hh%Mm%Ss", time.localtime())))

"""
The 'CheckStatistic(person2)' is just for test.
Please change when values input.
"""
outputButton = ttk.Button(averAccu_Frame, text="Output in txt", command=CheckStatistic(person2).outputTXT)
outputButton.grid(column=1, row=2, padx=15, pady=20)

# set new Tab for Question
quesFrame = ttk.LabelFrame(tab2, text="Question-Accuracy display")
quesFrame.grid(column=0, row=0, padx=20, pady=20)
ttk.Label(quesFrame, text="Correct rate for each Question : ", wraplength=110, justify="center") \
    .grid(column=0, row=0, padx=15, pady=16)
# showQuesDict = tk.StringVar(value="{}".format(ckSTAT.ckStatValues("QuesDict")))
# ttk.Entry(quesFrame, width=50, textvariable=showQuesDict).grid(column=1, row=0, padx=10, pady=25)

# Using a scrolled Text control
scrol_w = 29
scorl_h = 3
quesDict = ckSTAT.ckStatValues("QuesDict")

dictOutput = scrolledtext.ScrolledText(quesFrame, width=scrol_w, height=scorl_h)
dictOutput.grid(column=1, row=0)
dictOutput.place(x=20, y=20)
dictOutput.insert("end", quesDict)
dictOutput.grid(column=1, row=0, padx=15, pady=25)
exitButton = ttk.Button(quesFrame, text="Exit", command=_quit)
exitButton.grid(column=0, row=1, padx=25, pady=25)
#
# # def click_me(self):
# #     action.configure(text="Hello ")  # "Hello" + name.get() -> read Entry's value
#
# # action = ttk.Button(checkStatFrame, text="Output txt file", command=click_me)
# # action.grid(column=0, row=4, padx=20, pady=20)
#
# # ttk.Label(win, text="Average Accuracy: ").grid(column=0, row=0)
#
# # action.configure(state="disabled")

win.mainloop()

"""
quizformat

person1 = [
            {QuesId: 1, isCorrect: 0},
            {QuesId: 2, isCorrect: 1},
            {QuesId: 3, isCorrect: 0},            
         ]

1: person accuracy V
2: question accuracy V
3: average score V
4: 输出的内容全放在另一个function里  V

按钮，输入框，
button参数command 链接到 function，function读取输出的数据并返回到label的框里
print的东西拿来label用来输出，
表格显示，scrollbar，widgets：tree，
做格式的调整，label里wraplines，
第五章：数据作为图表，柱状图：widget canvas，
ttk

输出，print用button
数据库/ 创建txt/ 
import os 
"""

"""
question what, display single accuracy

1: button: refresh, get data from Elliy; 
    E provide function
    
2: Change Entry to Label V

3: delete menu bar V
4: question topic V

"""
