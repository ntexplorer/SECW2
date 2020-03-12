import os, random, sqlite3, string, time


class Quiz:

    def __init__(self, quizId, quizType, questionList, quizTime, score):

        self.quizID = quizID
        self.quizType = quizType
        self.questionList = questionList
        self.quizTime = quizTime
        self.score = score

    """def checkQuiz():

    def addQuestion():

    def delQuestion():

    def modifyQuestion():"""






class Timer:

    def countdown(t):

        while t:

            mins, secs = divmod(t, 60)
            timeformat = '{:2d}:{:02d}'.format(mins, secs)
            print(timeformat, end='r')
            time.sleep(1)
            t -= 1




quiz1 = Quiz(0, "MCQ", 60)

quiz2 = Quiz(1, "TF", 60)
