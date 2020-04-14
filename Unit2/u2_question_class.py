
# Question Classes

# Multiple Choice Queston Class

class questionMCClass:
    def __init__(self, qID=0, category="", difficulty="", type="Multiple Choice", question="",
                 correct="", wrong1="", wrong2="", wrong3=""):

        self.qID = qID
        self.category = category
        self.difficulty = difficulty
        self.type = type
        self.question = question
        self.correct = correct
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

# True/ False Question Class

class questionTFClass:
    def __init__(self, qID=0, category="", difficulty="", type="True/ False", question="",
                 answer=0):

        self.qID = qID
        self.category = category
        self.difficulty = difficulty
        self.type = type
        self.question = question
        self.answer = answer
