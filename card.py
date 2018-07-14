class card:

    def __init__(self, name, suit):
        self.name = name
        self.suit = suit

    def getname(self):
        return self.name

    def getsuit(self):
        return self.suit

    def loval(self):
        key = {\
               'ace':1,\
               'two':2,\
               'three':3,\
               'four':4,\
               'five':5,\
               'six':6,\
               'seven':7,\
               'eight':8,\
               'nine':9,\
               'ten':10,\
               'jack':10,\
               'queen':10,\
               'king':10\
               }
        return key[self.name]

    def hival(self):
        if self.name == "ace":
            return 11
        return self.loval()

    def __str__(self):
        return self.name + " of " + self.suit
        
    def isace(self):
        if self.name == "ace":
            return True
        return False
