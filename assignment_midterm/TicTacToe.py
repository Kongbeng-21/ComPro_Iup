loc11 = loc12 = loc13 = ' '
loc21 = loc22 = loc23 = ' '
loc31 = loc32 = loc33 = ' '

def print_board():
    print(f"{loc11}|{loc12}|{loc13}")
    print("-+-+-")
    print(f"{loc21}|{loc22}|{loc23}")
    print("-+-+-")
    print(f"{loc31}|{loc32}|{loc33}")

def get_cell_value(r, c):
    if   r==1 and c==1: return loc11
    elif r==1 and c==2: return loc12
    elif r==1 and c==3: return loc13
    elif r==2 and c==1: return loc21
    elif r==2 and c==2: return loc22
    elif r==2 and c==3: return loc23
    elif r==3 and c==1: return loc31
    elif r==3 and c==2: return loc32
    elif r==3 and c==3: return loc33

def set_cell_value(r, c, mark):
    global loc11, loc12, loc13, loc21, loc22, loc23, loc31, loc32, loc33
    if   r==1 and c==1: loc11 = mark
    elif r==1 and c==2: loc12 = mark
    elif r==1 and c==3: loc13 = mark
    elif r==2 and c==1: loc21 = mark
    elif r==2 and c==2: loc22 = mark
    elif r==2 and c==3: loc23 = mark
    elif r==3 and c==1: loc31 = mark
    elif r==3 and c==2: loc32 = mark
    elif r==3 and c==3: loc33 = mark

def read_move(player):
    while True:
        print(f"Player {player}")
        try:
            r = int(input("Enter first cell id (1-3): "))
            c = int(input("Enter second cell id (1-3): "))
        except ValueError:
            print("Please enter numbers 1-3."); continue
        if r in (1,2,3) and c in (1,2,3):
            if get_cell_value(r, c) == ' ':
                set_cell_value(r, c, player)
                break
            else:
                print("Cell already taken, please try again.")
        else:
            print("Invalid move, please try again.")

def switch_player(p):
    return 'O' if p == 'X' else 'X'

def check_winner(mark):
    lines = [
        (loc11, loc12, loc13),
        (loc21, loc22, loc23),
        (loc31, loc32, loc33),
        (loc11, loc21, loc31),
        (loc12, loc22, loc32),
        (loc13, loc23, loc33),
        (loc11, loc22, loc33),
        (loc13, loc22, loc31),
    ]
    return any(a == b == c == mark for a, b, c in lines)

def is_full():
    cells = (loc11, loc12, loc13, loc21, loc22, loc23, loc31, loc32, loc33)
    return all(ch in ('X', 'O') for ch in cells)

def tictactoe():
    player = 'X'
    while True:
        print_board()
        read_move(player)
        if check_winner(player):
            print_board()
            print(f"Player {player} wins!")
            break
        if is_full():
            print_board()
            print("Draw.")
            break
        player = switch_player(player)

if __name__ == "__main__":
    tictactoe()
