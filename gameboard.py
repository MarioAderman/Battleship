class Gameboard:
    def __init__(self):
        self.board = [[0 for _ in range(10)] for _ in range(10)]
    
    # Print the game board in a readable way for the user
    def print_board(self):
        numbers = "  1 2 3 4 5 6 7 8 9 10"
        letters = "ABCDEFGHIJ"
        row = ""
        print(numbers)
        for i in range(10):
            row_letter = letters[i]
            row = f"{row_letter} "
            for j in range(10):
                if j < 9:
                    row += str(self.board[i][j]) + " "
                else:
                    row += str(self.board[i][j])
            print(row)

