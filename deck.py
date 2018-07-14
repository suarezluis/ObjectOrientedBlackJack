class deck:

    def __init__(self):
        self.maze = [] 
        for x in range(1,5):
            if x == 1:
                suit = "spades"
            if x == 2:
                suit = "hearts"
            if x == 3:
                suit = "clubs"
            if x == 4:
                suit = "diamonds"
                        
            self.maze = self.maze + [("ace",suit)]
            self.maze = self.maze + [("two",suit)]
            self.maze = self.maze + [("three",suit)]
            self.maze = self.maze + [("four",suit)]
            self.maze = self.maze + [("five",suit)]
            self.maze = self.maze + [("six",suit)]
            self.maze = self.maze + [("seven",suit)]
            self.maze = self.maze + [("eight",suit)]
            self.maze = self.maze + [("nine",suit)]
            self.maze = self.maze + [("ten",suit)]
            self.maze = self.maze + [("jack",suit)]
            self.maze = self.maze + [("queen",suit)]
            self.maze = self.maze + [("king",suit)]
            
    def Print(self):
        print(self.maze)

    def deal(self):
        import card
        mycard = self.maze.pop(0)
        name = mycard[0]
        suit = mycard[1]
        mycard = card.card(name, suit)
        return mycard

    def shuffle(self):
        import random
        random.shuffle(self.maze)
                
