import random

def placing_ship(gameboard, ship, whoisit):
    if ship.hv_orient is True:
        if ship.lr_ud_orient.upper() == "L":
            for i in range (1, ship.size + 1):
                #Real coordinates for the gameboard
                real_row_coordinate = 10 - ship.row_coordinate
                real_col_coordinate = ship.col_coordinate - i
                if ship.size == 2:
                    gameboard.board[real_row_coordinate][real_col_coordinate] = "B"
                elif ship.size > 2:
                    if gameboard.board[real_row_coordinate][real_col_coordinate] != 0:
                        #Undo previous placements
                        for u in range (1, i):
                            gameboard.board[10 - ship.row_coordinate][ship.col_coordinate - u] = 0
                        print("Ship overlapped with an existing one.")
                        print("Choose a different set of coordinates.")
                        if whoisit is True:
                            gameboard.print_board()
                        return gameboard, True
                    else:
                        if ship.size == 3:
                            gameboard.board[real_row_coordinate][real_col_coordinate] = "S"
                        elif ship.size == 4:
                            gameboard.board[real_row_coordinate][real_col_coordinate] = "D"
        elif ship.lr_ud_orient.upper() == "R":
            for i in range (1, ship.size + 1):
                #Real coordinates for the gameboard
                real_row_coordinate = 10 - ship.row_coordinate
                real_col_coordinate = (ship.col_coordinate - 2) + i
                if ship.size == 2:
                    gameboard.board[real_row_coordinate][real_col_coordinate] = "B"
                elif ship.size > 2:
                    if gameboard.board[real_row_coordinate][real_col_coordinate] != 0:
                        #Undo previous placements
                        for u in range (1, i):
                            gameboard.board[10 - ship.row_coordinate][(ship.col_coordinate - 2) + u] = 0
                        print("Ship overlapped with an existing one.")
                        print("Choose a different set of coordinates.")
                        if whoisit is True:
                            gameboard.print_board()
                        return gameboard, True
                    else:
                        if ship.size == 3:
                            gameboard.board[real_row_coordinate][real_col_coordinate] = "S"
                        elif ship.size == 4:
                            gameboard.board[real_row_coordinate][real_col_coordinate] = "D"
    else:
        if ship.lr_ud_orient.upper() == "U":
            for i in range (1, ship.size + 1):
                real_row_coordinate = 11 - ship.row_coordinate - i
                real_col_coordinate = ship.col_coordinate - 1
                if ship.size == 2:
                    gameboard.board[real_row_coordinate][real_col_coordinate] = "B"
                elif ship.size > 2:
                    if gameboard.board[real_row_coordinate][real_col_coordinate] != 0:
                        #Undo previous placements
                        for u in range (1, i):
                            gameboard.board[11 - ship.row_coordinate - u][ship.col_coordinate - 1] = 0
                        print("Ship overlapped with an existing one.")
                        print("Choose a different set of coordinates.")
                        if whoisit is True:
                            gameboard.print_board()
                        return gameboard, True
                    else:
                        if ship.size == 3:
                            gameboard.board[real_row_coordinate][real_col_coordinate] = "S"
                        elif ship.size == 4:
                            gameboard.board[real_row_coordinate][real_col_coordinate] = "D"
        elif ship.lr_ud_orient.upper() == "D":
            for i in range (0, ship.size):
                real_row_coordinate = 10 - ship.row_coordinate + i
                real_col_coordinate = ship.col_coordinate - 1
                if ship.size == 2:
                    gameboard.board[real_row_coordinate][real_col_coordinate] = "B"
                elif ship.size > 2:
                    if gameboard.board[real_row_coordinate][real_col_coordinate] != 0:
                        #Undo previous placements
                        for u in range (1, i):
                            gameboard.board[10 - ship.row_coordinate + u][ship.col_coordinate - 1] = 0
                        print("Ship overlapped with an existing one.")
                        print("Choose a different set of coordinates.")
                        if whoisit is True:
                            gameboard.print_board()
                        return gameboard, True
                    else:
                        if ship.size == 3:
                            gameboard.board[real_row_coordinate][real_col_coordinate] = "S"
                        elif ship.size == 4:
                            gameboard.board[real_row_coordinate][real_col_coordinate] = "D"
    if whoisit is True:
        print("Boat placed successfully.")
        gameboard.print_board()
    return gameboard, False

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

def user_ships(gameboard, ships):
    for i in range (3):
        redo = True
        while redo:
            print("Coordinates must be from 1 to 10.")
            while True:
                    col_input = input(f"Enter column or X coordinate to locate your {ships[i].name}: ").strip()
                    if col_input.isdigit():
                        col = int(col_input)
                        if 1 <= col <= 10:
                            break
                        else:
                            print("Invalid input. Please enter a number between 1 and 10.")
                    else:
                        print("Please enter a valid number")
            while True:
                    row_input = input(f"Enter row or Y coordinate to locate your {ships[i].name}: ").strip()
                    if row_input.isdigit():
                        row = int(row_input)
                        if 1 <= row <= 10:
                            break
                        else:
                            print("Invalid input. Please enter a number between 1 and 10.")
                    else:
                        print("Please enter a valid number")
            print("Orientation must be H for Horizontal or V for Vertical.")
            print("As well as L for Left or R for Right if Horizontal.")
            print("And U for Up or D for Down if Vertical.")
            while True:
                    orient_hv_input = input(f"Enter Horizontal (H) or Vertical (V) orientation of your {ships[i].name}: ").strip()
                    if orient_hv_input.upper() in {'H','V'}:
                        orient_hv = orient_hv_input.upper()
                        break
                    else:
                        print("Invalid orientation. Please enter H for Horizontal or V for Vertical.")
            if orient_hv == "H":
                orient_hv = True
                while True:
                    orient_lr_ud_input = input(f"Enter Left (L) or Right (R) orientation of your {ships[i].name}: ").strip()
                    if orient_lr_ud_input.upper() in {'L','R'}:
                        orient_lr_ud = orient_lr_ud_input.upper()
                        break
                    else:
                        print("Invalid orientation. Please enter L for Left or R for Right.")
            elif orient_hv.upper() == "V":
                orient_hv = False
                while True:
                    orient_lr_ud_input = input(f"Enter Up (U) or Down (D) orientation of your {ships[i].name}: ").strip()
                    if orient_lr_ud_input.upper() in {'U','D'}:
                        orient_lr_ud = orient_lr_ud_input.upper()
                        break
                    else:
                        print("Invalid orientation. Please enter U for Up or D for Down.")
            print("All inputs are valid.")
            ships[i].col_coordinate = col
            ships[i].row_coordinate = row
            ships[i].hv_orient = orient_hv
            ships[i].lr_ud_orient = orient_lr_ud
            is_place_check = val_placing(ships[i])
            whoisit = True
            if is_place_check is True:
                gameboard, redo = placing_ship(gameboard, ships[i], whoisit)
            else:
                print("Invalid placement. Please try again.")
    return gameboard

def console_ships(gameboard, ships):
    for i in range (0,3):
        redo = True
        while redo:
            while True:
                col = random.randint(1,10)
                row = random.randint(1,10)
                orient_hv = random.choice(['H','V'])
                if orient_hv == "H":
                    orient_hv = True
                    orient_lr_ud = random.choice(['L','R'])
                elif orient_hv == "V":
                    orient_hv = False
                    orient_lr_ud = random.choice(['U','D'])
                ships[i].col_coordinate = col
                ships[i].row_coordinate = row
                ships[i].hv_orient = orient_hv
                ships[i].lr_ud_orient = orient_lr_ud
                is_place_check = val_placing(ships[i])
                whoisit = False
                if is_place_check is True:
                    gameboard, redo = placing_ship(gameboard, ships[i], whoisit)
                    breakgit