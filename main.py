gameboard = [[0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0]]

class Shipset:
    def __init__(self, size, col_coordinate, row_coordinate, hv_orient, lr_ud_orient):
        self.size = size
        self.col_coordinate = col_coordinate
        self.row_coordinate = row_coordinate
        self.hv_orient = hv_orient
        self.lr_ud_orient = lr_ud_orient

def print_board(gameboard):
    row = ""
    for i in range (0,10):
        for j in range (0,10):
            if j < 9:
                row += str(gameboard[i][j]) + " "
            else:
                row += str(gameboard[i][j]) + "\n"
    print(row)

def placing_ship(gameboard, ship):
    if ship.hv_orient is True:
        if ship.lr_ud_orient.upper() == "L":
            for i in range (0, ship.size):
                if ship.size == 2:
                    gameboard[10 - ship.row_coordinate][ship.col_coordinate - (i - 1)] = "B"
                elif ship.size == 3:
                    gameboard[10 - ship.row_coordinate][ship.col_coordinate - (i - 1)] = "S"
                elif ship.size == 4:
                    gameboard[10 - ship.row_coordinate][ship.col_coordinate - (i - 1)] = "D"
        elif ship.lr_ud_orient.upper() == "R":
            for i in range (0, ship.size):
                if ship.size == 2:
                    gameboard[10 - ship.row_coordinate][ship.col_coordinate + (i - 1)] = "B"
                elif ship.size == 3:
                    gameboard[10 - ship.row_coordinate][ship.col_coordinate + (i - 1)] = "S"
                elif ship.size == 4:
                    gameboard[10 - ship.row_coordinate][ship.col_coordinate + (i - 1)] = "D"
    else:
        if ship.lr_ud_orient.upper() == "U":
            for i in range (0, ship.size):
                if ship.size == 2:
                    gameboard[10 - ship.row_coordinate - i][ship.col_coordinate - 1] = "B"
                elif ship.size == 3:
                    gameboard[10 - ship.row_coordinate - i][ship.col_coordinate - 1] = "S"
                elif ship.size == 4:
                    gameboard[10 - ship.row_coordinate - i][ship.col_coordinate - 1] = "D"
        elif ship.lr_ud_orient.upper() == "D":
            for i in range (0, ship.size):
                if ship.size == 2:
                    gameboard[10 - ship.row_coordinate + i][ship.col_coordinate - 1] = "B"
                elif ship.size == 3:
                    gameboard[10 - ship.row_coordinate + i][ship.col_coordinate - 1] = "S"
                elif ship.size == 4:
                    gameboard[10 - ship.row_coordinate + i][ship.col_coordinate - 1] = "D"
    return gameboard

def val_placing(ship):
    if ship.hv_orient is True:
        if ship.lr_ud_orient.upper() == "L":
            if (ship.col_coordinate - ship.size) < 0:
                return False
            else:
                return True
        elif ship.lr_ud_orient.upper() == "R":
            if (ship.col_coordinate + ship.size) > 11:
                return False
            else:
                return True
        else:
            return False
    else:
        if ship.lr_ud_orient.upper() == "U":
            if (ship.row_coordinate + ship.size) > 11:
                return False
            else:
                return True
        elif ship.lr_ud_orient.upper() == "D":
            if (ship.row_coordinate - ship.size) < 0:
                return False
            else:
                return True
        else:
            return False

for i in range (0,3):
    ships = ["Boat", "Submarine", "Destroyer"]
    #Boat addition
    col = int(input(f"Enter column or X coordinate to locate your {ships[i]}: "))
    row = int(input(f"Enter row or Y coordinate to locate your {ships[i]}: "))
    orient_hv = input(f"Enter Horizontal (H) or Vertical (V) orientation of your {ships[i]}: ")
    if orient_hv.upper() == "H":
        orient_hv = True
        orient_lr_ud = input(f"Enter Left (L) or Right (R) orientation of your {ships[i]}: ")
    elif orient_hv.upper() == "V":
        orient_hv = False
        orient_lr_ud = input(f"Enter Up (U) or Down (D) orientation of your {ships[i]}: ")
    else:
        print("Invalid orientation. Please enter H for Horizontal or V for Vertical.")
        
    ship = Shipset(2 + i, col, row, orient_hv, orient_lr_ud)
    is_place_check = val_placing(ship)
    if is_place_check is True:
        gameboard = placing_ship(gameboard, ship)
        print("Boat placed successfully.")
        print_board(gameboard)
    else:
        print("Invalid placement. Please try again.")
    #Extra comment    
    #Submarine addition
    
