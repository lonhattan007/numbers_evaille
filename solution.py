from sys import argv
from card import Card
from deck import Deck


def import_card(string: str) -> Card:
    return Card(string.split(', '))


def import_deck(filename: str) -> Deck:
    deck = Deck()
    
    with open(filename, "r") as open_file_obj:
        for line in open_file_obj:
            deck.sorted_append(import_card(line))

    return deck


def solve(deck: Deck, goal: int):
    # """Solve the problem in Dynamic Programming style"""
    
    # """Check for exceptions"""
    # if deck.is_empty():
    #     raise Exception("Deck is empty")
    
    # if len(deck.ranks) < 5:
    #     raise Exception("Not enough ranks")  

    # if goal < deck.min_num() or goal > deck.max_num():
    #     raise Exception("Goal number is out of deck range")

    # """Step 1: List all possible combos"""
    # """Might check for different ranks as well"""
    # solutions = []

    # # TODO
    # candidate_lst = deck.ranks
    # goal_rank = deck.rank_of(goal)

    # for rank_ind in range (0, len(candidate_lst)):
    #     if rank_ind[0].rank != goal_rank:
    #         pass  
    #     else:
    #         candidate_lst.pop(rank_ind)
    #         break

    
    
    # """Step 2: Check if their ranks are not the same"""
    # """Might be deleted later"""
    # if len(solutions) != 0:
    #     unqualified = []

    #     for sol in solutions:            
    #         if sol[0].rank != sol[1].rank and sol[1].rank != sol[2].rank and sol[2].rank != sol[3].rank and sol[3].rank != sol[1].rank:
    #             pass
    #         else:
    #             unqualified.append(sol)

    #     for sol in unqualified:
    #         solutions.remove(sol)

    return [] # solutions


def main():
    deck = import_deck(argv[1])
    deck.print()

    goal = int(input("Goal: "))

    print("Rank of number", goal, "is:", deck.rank_of(goal))
    print("Min number in the deck is:", deck.min_num())
    print("Max number in the deck is:", deck.max_num())

    solutions = solve(deck, goal)

    """Print result"""
    if len(solutions) == 0:
        print("No solutions were found")
    else:
        no = 1
        for sol in solutions:
            print("Solution", no)
            
            for card in sol:
                card.print()

            print("_____________")            
            
            no += 1


if __name__ == "__main__":
    """Input: (1) list of cards, sorted in ascending order of card number
              (2) the desired total number"""
    """Output: list of solutions"""
    
    main()
    
    
