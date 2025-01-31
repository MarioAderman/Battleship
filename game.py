import random

#See who goes first by tossing a coin
def tossing_coin():
    coin = ['HEADS', 'TAILS']
    while True:
        user = input('By typping in... Choose HEADS or TAILS: ').strip().upper()
        if user in coin:
            break
        else:
            print('Invalid input. Please try again.')
    tossed = random.choice(coin)
    if user == tossed:
        print(f'You chose {user} and the coin got {tossed}. You go first!')
        return True
    else: 
        print(f'You chose {user} and the coin got {tossed}. The console goes first!')
        return False

def hit(row_hit, col_hit, gameboard, whoisit):
    if gameboard.board[ord(row_hit) - 65][col_hit - 1] == '0':
        if whoisit is True:
            print("You missed!")
        else:
            print("Console missed!")
        # Mark the miss on the board
        gameboard.board[ord(row_hit) - 65][col_hit - 1] = 'X'
    elif gameboard.board[ord(row_hit) - 65][col_hit - 1] == 'B':
        if whoisit is True:    
            print("You hit a boat!")
        else:
            print("Console hit a boat!")
        # Mark the hit on the board
        gameboard.board[ord(row_hit) - 65][col_hit - 1] = 'H'
        for i in range(10):
            for j in range(10):
                if gameboard.board[i][j] == 'B':
                    gameboard.board[i][j] = 'H'
    elif gameboard.board[ord(row_hit) - 65][col_hit - 1] == 'S':
        if whoisit is True:
            print("You hit a submarine!")
        else:
            print("Console hit a submarine!")
        gameboard.board[ord(row_hit) - 65][col_hit - 1] = 'H'
        for i in range(10):
            for j in range(10):
                if gameboard.board[i][j] == 'S':
                    gameboard.board[i][j] = 'H'
    elif gameboard.board[ord(row_hit) - 65][col_hit - 1] == 'D':
        if whoisit is True:    
            print("You hit a destroyer!")
        else:
            print("Console hit a destroyer!")
        gameboard.board[ord(row_hit) - 65][col_hit - 1] = 'H'
        for i in range(10):
            for j in range(10):
                if gameboard.board[i][j] == 'D':
                    gameboard.board[i][j] = 'H'
    return gameboard
    
def user_hit(console_gameboard):
    print("It's your turn!")
    whoisit = True
    while True:
        print("Coordinates must be from 1 to 10.")
        col_input = input(f"Enter column or X coordinate to strike: ").strip()
        if col_input.isdigit():
            col_hit = int(col_input)
            if 1 <= col_hit <= 10:
                break
            else:
                print("Invalid input. Please enter a number between 1 and 10.")
        else:
            print("Please enter a valid number")
    print("Coordinates must be from A to J.")
    while True:
        row_input = input(f"Enter row or Y coordinate to strike: ").strip().upper()
        if len(row_input) == 1 and row_input >= 'A' and row_input <= 'J':
            row_hit = row_input
            break
        else:
            print("Please enter a valid letter between A and J.")
    console_gameboard = hit(row_hit, col_hit, console_gameboard, whoisit)
    return console_gameboard

def console_hit(user_gameboard):
    print("It's the console's turn!")
    whoisit = False
    row_hit = chr(random.randint(65, 74))
    col_hit = random.randint(1, 10)
    user_gameboard = hit(row_hit, col_hit, user_gameboard, whoisit)
    print("Console hit!")
    return user_gameboard

def check_if_game_over(gameboard):
    did_win = True
    for i in range (10):
        for j in range (10):
            if gameboard.board[i][j] == 'B' or gameboard.board[i][j] == 'S' or gameboard.board[i][j] == 'D':
                did_win = False
                break
    if did_win is False:
        return False
    else:
        return True
      
def start_game(user_gameboard, console_gameboard):
    print('Let\'s see who goes first!...')
    start_player = tossing_coin()
    while True:
        # User's turn
        if start_player is True:
            console_gameboard = user_hit(console_gameboard)
            start_player = False
            did_user_win = check_if_game_over(console_gameboard)
            if did_user_win == True:
                print("Game over!")
                print('Congratulations! You won!')
                break
        # Console's turn
        else:
            user_gameboard = console_hit(user_gameboard)
            user_gameboard.print_board()
            start_player = True
            did_console_win = check_if_game_over(user_gameboard)
            if did_console_win == True:
                print("Game over!")
                print('The console won! Better luck next time!')
                break