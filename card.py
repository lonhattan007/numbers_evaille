class Card():
    """A card has a number and a rank"""
    
    def __init__(self, number, rank):
        self.number = number
        self.rank = rank

    
    def __init__(self, info: list):
        self.number = int(info[0])
        self.rank = int(info[-1])


    def print(self):
        print("Number:", self.number)
        print("Rank:", self.rank)