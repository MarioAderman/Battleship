class Gameboard:
    def __init__(self):
        self.board = [[0 for _ in range(10)] for _ in range(10)]
    
    def print_board(self):
        row = ""
        for i in range(10):
            for j in range(10):
                if j < 9:
                    row += str(self.board[i][j]) + " "
                else:
                    row += str(self.board[i][j]) + "\n"
        print(row)

