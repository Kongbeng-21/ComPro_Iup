from typing import List, Tuple

def ask_board_size() -> int:
    while True:
        raw = input("Enter board size n for n x n board (3-10): ").strip()
        if not raw.isdigit():
            print("Invalid input. Please enter a number.")
            continue
        n = int(raw)
        if 3 <= n <= 10:
            return n
        print("Size out of range. Please enter a number between 3 and 10.")


def ask_player_symbol(prompt: str, taken: str = "") -> str:
    while True:
        sym = input(prompt).strip()
        if len(sym) != 1 or not sym.isalpha():
            print("Invalid symbol. Please enter a single letter (A-Z or a-z).")
            continue
        if taken and sym == taken:
            print(f"Symbol already taken by Player 1. Please choose another.")
            continue
        return sym



def create_board(n: int) -> List[List[str]]:
    cells = [str(i) for i in range(1, n * n + 1)]
    return [cells[i * n:(i + 1) * n] for i in range(n)]


def display_board(board: List[List[str]]) -> None:
    n = len(board)
    width = len(str(n * n))  
    hbar = "+" + "+".join(("-" * (width + 2)) for _ in range(n)) + "+"
    for r in range(n):
        print(hbar)
        row = "| " + " | ".join(f"{board[r][c]:>{width}}" for c in range(n)) + " |"
        print(row)
    print(hbar)


def pos_to_rc(pos: int, n: int) -> Tuple[int, int]:
    pos -= 1
    return pos // n, pos % n


def is_free(board: List[List[str]], r: int, c: int) -> bool:
    return board[r][c].isdigit()


def ask_move(n: int, board: List[List[str]], player_sym: str) -> Tuple[int, int]:
    limit = n * n
    while True:
        raw = input(f"Player '{player_sym}', enter your move position (1-{limit}): ").strip()
        try:
            pos = int(raw)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if not (1 <= pos <= limit):
            print("Position out of range. Please try again.")
            continue
        r, c = pos_to_rc(pos, n)
        if not is_free(board, r, c):
            print("Cell already occupied. Choose another.")
            continue
        return r, c


def place(board: List[List[str]], r: int, c: int, sym: str) -> None:
    board[r][c] = sym


def check_winner(board: List[List[str]], sym: str) -> bool:
    n = len(board)
    for i in range(n):
        if all(board[i][j] == sym for j in range(n)):
            return True
        if all(board[j][i] == sym for j in range(n)):
            return True
    if all(board[i][i] == sym for i in range(n)):
        return True
    if all(board[i][n - 1 - i] == sym for i in range(n)):
        return True
    return False


def board_full(board: List[List[str]]) -> bool:
    return all(not board[r][c].isdigit() for r in range(len(board)) for c in range(len(board)))


def main() -> None:
    n = ask_board_size()
    p1 = ask_player_symbol("Enter Player 1's symbol (a single letter): ")
    p2 = ask_player_symbol(
        f"Enter Player 2's symbol (a single letter, different from '{p1}'): ",
        taken=p1,
    )
    board = create_board(n)

    turn = 0  
    while True:
        display_board(board)
        current = p1 if turn == 0 else p2
        r, c = ask_move(n, board, current)
        place(board, r, c, current)

        if check_winner(board, current):
            display_board(board)
            print(f"Player '{current}' wins!")
            break
        if board_full(board):
            display_board(board)
            print("It's a draw!")
            break

        turn ^= 1


if __name__ == "__main__":
    main()

