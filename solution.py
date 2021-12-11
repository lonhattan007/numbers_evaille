from sys import argv
from card import Card
from deck import Deck
from algorithm import sum_of_n


def import_card(string: str) -> Card:
    """Importing a card from a data string"""

    return Card(string.split(', '))


def import_deck(filename: str) -> Deck:
    """Importing a deck from an input file"""

    deck = Deck()
    
    try:
        with open(filename, "r") as open_file_obj:
            for line in open_file_obj:
                deck.sorted_append(import_card(line))

        open_file_obj.close()
    except:
        print("Problem opening file!")

    return deck


def solve(deck: Deck, goal: int):
    """Solve the problem"""
    
    """Check for exceptions"""
    if deck.is_empty():
        raise Exception("Deck is empty")
    
    if len(deck.rank_lst) < 5:
        raise Exception("Not enough ranks")  

    if goal < deck.min_num() or goal > deck.max_num():
        raise Exception("Goal number is out of deck range")

    # TODO

    """Select all the candidates: differs from the goal number in rank and smaller than goal - 5"""
    goal_rank = deck.rank_of(goal)

    
    def check_valid_combo(lst) -> bool:
        """Check if a combination is valid"""
        
        rank_lst = [deck.rank_of(n) for n in lst]

        if len(rank_lst) != len(set(rank_lst)):
            return False        
        # Uncomment these 2 lines below if you want the goal number's rank not included in the combination"""
        # elif goal_rank in rank_lst:
            # return False
        else:
            return True

    
    solution_lst = sum_of_n(goal, 4, 1)
    solution_lst = [n for n in solution_lst if check_valid_combo(n)]

    return solution_lst


def main():
    deck = import_deck(argv[1])

    goal = int(input("Goal: "))

    solutions = solve(deck, goal)

    """Print result"""
    try:
        open_file_obj = open(argv[2], 'w')

        msg = "Desired card number: " + str(goal) + "; Rank: " + str(deck.rank_of(goal)) + "\n"
        open_file_obj.write(msg)

        if len(solutions) == 0:
            msg = "No solutions were found\n"
            print(msg, end="")
            open_file_obj.write(msg)
        else:
            if len(solutions) == 1:
                msg = "Found 1 solution\n"
            else:
                msg = "Found " + str(len(solutions)) + " solutions\n"

            open_file_obj.write(msg)
            open_file_obj.write("________________\n")

            no = 1
            for sol in solutions:
                msg = "Solution " + str(no) + "\n"
                open_file_obj.write(msg)

                i = 1
                for card_number in sol:
                    if i != len(sol):
                        msg = "Card " + str(card_number) + " - Rank " + str(deck.rank_of(card_number)) + "; "
                    else:
                        msg = "Card " + str(card_number) + " - Rank " + str(deck.rank_of(card_number)) + "\n"

                    open_file_obj.write(msg)
                    i+=1

                open_file_obj.write("________________\n")                        
                no += 1

        open_file_obj.close()

        print("All the solutions are in the", argv[2], "file")
    except:
        print("Problem opening and writing file!")

if __name__ == "__main__":
    """Input: (1) list of cards, sorted in ascending order of card number
              (2) the desired total number"""
    """Output: list of solutions"""
    
    main()

    
    
