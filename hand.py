class hand:

    def __init__(self):
        self.cards = []

    def hit(self, deck):
        newcard = deck.deal()
        self.cards.append(newcard)
        return newcard

    def value(self):
        import handvalue
        return handvalue.handvalue(self.cards)
    
    def Print(self):
        for i in self.cards:
            print(i)

    def bust(self):
        if self.value() > 21:
            return True
        return False

    def blackjack(self):
        if len(self.cards) == 2 and self.value() == 21:
            return True
        return False

    def have21(self):
        if self.value() == 21:
            return True
        return False
            
        
        
            
