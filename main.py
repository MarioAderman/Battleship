from gameboard import Gameboard
from ship import Ship
from utils import user_ships, console_ships
from txt_generation import save_boards_to_txt
from game import start_game

def main():
    
    ships = [
        Ship("Boat", 2, None, None, None, None),
        Ship("Submarine", 3, None, None, None, None),
        Ship("Destroyer", 4, None, None, None, None)
    ]
    
    # Initialize game boards
    user_gameboard = Gameboard()
    console_gameboard = Gameboard()
    
    # Place user's ships
    user_ships(user_gameboard, ships)
    
    # Place console's ships randomly
    console_ships(console_gameboard, ships)
    
    # Save boards to text files
    save_boards_to_txt(user_gameboard, console_gameboard)
    
    # Start the game
    start_game(user_gameboard, console_gameboard)
    
    print("Thank you for playing Battleship!")

if __name__ == '__main__':
    main()