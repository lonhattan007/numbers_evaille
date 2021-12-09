from card import Card

class Deck():
    """A set of cards categorized by their ranks"""

    def __init__(self):
        self.rank_lst = []


    def sorted_append(self, card: Card):
        index = 0
        flag = False
        
        if len(self.rank_lst) == 0:        
            pass
        else:
            for rank in self.rank_lst:
                if rank[0].rank == card.rank:
                    rank.append(card)
                    flag = True
                    break
                elif rank[0].rank < card.rank:
                    index += 1
                else:
                    break
        
        if flag != True:
            self.rank_lst.insert(index, [card])


    def is_empty(self):
        return len(self.rank_lst) == 0    


    def print(self):
        if self.is_empty():
            print("Empty deck")
        else:
            for rank in self.rank_lst:
                print("Rank", rank[0].rank)

                for card in rank:
                    print("Number:", card.number)
                
                print("_____________")

    
    def rank_of(self, number):
        if self.is_empty():
            return -1

        result = 0
        
        for rank in self.rank_lst:
            for card in rank:
                if card.number == number:
                    result = card.rank

        return result 


    def min_num(self):
        if self.is_empty():
            return -1

        min_lst = [rank[0].number for rank in self.rank_lst]
        rank_of_min_num = min_lst.index(min(min_lst))

        return self.rank_lst[rank_of_min_num][0].number        
        
    
    def max_num(self):
        if self.is_empty():
            return -1

        max_lst = [rank[-1].number for rank in self.rank_lst]
        rank_of_max_num = max_lst.index(max(max_lst))

        return self.rank_lst[rank_of_max_num][-1].number        
