def print_board():
    print(f"{loc11} | {loc12} | {loc13}")
    print("--+---+--")
    print(f"{loc21} | {loc22} | {loc23}")
    print("--+---+--")
    print(f"{loc31} | {loc32} | {loc33}")
    
def read_move():
    while True:
        print(f"player {current_player}")
        id1 = int(input("Enter first cell id (1-3): "))
        id2 = int(input("Enter second cell id (1-3): "))
        print(id1, id2)
        
        if (id1 in [1,2,3]) and (id2 in [1,2,3]):
            if curr_cell_value == ' ':
                set_cell_value(id1, id2, current_player)
                break
            else:
                print("Cell already taken please try again")
        else:
            print('Invalid move please tyr again')
            
def switch_player():
    if current_player == 'X':
        return ('O')
    else:
        return ('X')
    
def check_winner(curr_player):
    if loc11 == loc12 == loc13 == curr_player:
        return True
    elif loc21 == loc22 == loc23 == curr_plaer:
        return True
    elif loc31 == loc32 == loc33 == curr_player:
        return True
    elif loc11 == loc22 == loc33 == curr_player:
        return True
    elif loc13 == loc22 == loc31 == curr_player:
        return True
    elif loc11 == loc21 == loc21 == curr_player:
        return True
    elif loc12 == loc22 == loc32 == curr_player:
        return True
    elif loc13 == loc23 == loc33 == curr_player:
        return True
    else:
        return False
    
def is_full():
    if loc11 == ' ' or loc12 == ' ' or loc13 == ' ' or
        loc21 == ' ' or loc22 == ' ' or loc23 == ' ' or
        loc31 == ' ' or loc32 == ' ' or loc33 == ' ':
        return False
   else:
       return True
    
    
def tictactoe():
    current_player = 'x'
    while True:
        print_board()
        
        read_move(current_player)
        
        if check_winner():
            print_ board()
            print(f"Player {current_player} wins !")
            break
        elif is_full():
            print_board()
            print
        
        current_player = switch_player(current_player)
    

loc11, loc12, loc13 = '', '', ''
loc21, loc22, loc23 = '', '', ''
loc31, loc32, loc33 = '', '', ''
current_player = 'x'

print print_board()

read_move(current_player)
