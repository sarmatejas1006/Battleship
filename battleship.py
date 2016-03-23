from random import randint

board = []

for x in range(0, 5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

# title
print "Clash of Clans Debacle: Arrhenians vs Zyrkonians\n"

# description
print "The Arrhenians, lead by the Pirate Captain John Badbeard are attacking! \
You, Captain Jack Parrot have to save your clan of Zyrkonians from the evil John Badbeard and his wicked Arrhenians.\n \
Your task is to find the enemy ship and sink it. Are you up for the task? \
Can you bomb their ship and save your clan of Zyrkonians from destruction?\n Enter the battle and let's see what happens!\n"

# rules
print "Rules: Welcome to the vast ocean. This ocean is divided into 25 sectors. \
Each sector of the ocean is marked by unique co-ordinates from (1, 1) to (5, 5).\n \
My battleship is present in one of these sectors. Can you bomb the correct sector? \nLet the battle begin!"

# start of challenge
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)
ans = ""
guess = 1  # counts no of guesses
while 1:
    ship_row = random_row(board)
    ship_col = random_col(board)
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))

    print "You guessed that the ship was present at sector (%d, %d) and in reality, \
    the ship was present at (%d, %d)\n" % (guess_row, guess_col, ship_row, ship_col)

    # Main Program
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sank the Arrhenians' battleship! You had to fire %d bombs to sink it" % guess
    elif board[guess_row][guess_col] == "X":
        print "You guessed that one already."
    else:
        if guess_row not in range(5) or guess_col not in range(5):
            print "Oops, that's not even in the ocean."
        else:
            print "You missed the Arrhenians' battleship!"
            guess += 1
    board[guess_row][guess_col] = "X"
    print "Sectors you have already bombed are marked with an X"
    print_board(board)
    flag = 0
    # response check and chance another guess
    while flag == 0:
        ans = raw_input("Would you like to bomb another sector? Select Yes/ No.\n").lower()
        if ans.lower() == "yes" and ans.lower() != "no":
            "You have another bomb loaded. Take aim and fire!!"
            break
        elif ans.lower() == "no":
            print "You let the Arrhenians take over. You've lost the battle but the war is not over yet. \
             Better luck next time. Thank you for playing."
            exit()
        else:
            print "I didn't get your response. Try again.\n"