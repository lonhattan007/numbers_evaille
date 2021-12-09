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
    
    """Check for exceptions"""
    if deck.is_empty():
        raise Exception("Deck is empty")
    
    if len(deck.ranks) < 5:
        raise Exception("Not enough ranks")  

    if goal < deck.min_num() or goal > deck.max_num():
        raise Exception("Goal number is out of deck range")

    # TODO
    

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
    
    
