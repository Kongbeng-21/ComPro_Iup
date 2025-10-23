def ask_board_size():
    while True:
        size = input("Enter board size n for n x n board (3-10): ").strip()
        if size.isdigit():
            n = int(size)
            if 3 <= n <= 10:
                return n
        print("Invalid. Please enter a number between 3 and 10.")


def ask_symbol(prompt, taken=None):
    while True:
        sym = input(prompt).strip()
        if len(sym) == 1 and sym.isalpha() and (taken is None or sym != taken):
            return sym
        print("Invalid symbol. Enter ONE letter (A-Z) and not the same as the other player.")


def ask_move(board, n, symbol):
    limit = n * n
    while True:
        s = input(f"Player '{symbol}', enter your move (1-{limit}): ").strip()
        if s.isdigit():
            m = int(s)
            if 1 <= m <= limit:
                r, c = pos_to_rc(m, n)
                if is_free(board, r, c):
                    return r, c
                print("Cell already occupied. Try again.")
                continue
        print("Invalid move. Please try again.")


def create_board(n):
    nums = [str(i) for i in range(1, n * n + 1)]
    return [nums[i * n:(i + 1) * n] for i in range(n)]  # ← แก้สไลซ์


def display_board(board):
    n = len(board)
    w = len(str(n * n))
    sep = "+" + "+".join("-" * (w + 2) for _ in range(n)) + "+"
    for r in range(n):
        print(sep)
        row = "| " + " | ".join(f"{board[r][c]:>{w}}" for c in range(n)) + " |"
        print(row)
    print(sep)


def pos_to_rc(pos, n):
    pos -= 1
    return pos // n, pos % n


def is_free(board, r, c):
    return board[r][c].isdigit()


def is_board_full(board):
    for row in board:
        for cell in row:
            if cell.isdigit():
                return False
    return True


def check_for_winner(board, symbol):
    n = len(board)


    for r in range(n):
        ok = True
        for c in range(n):
            if board[r][c] != symbol:
                ok = False
                break
        if ok:
            return True

    for c in range(n):
        ok = True
        for r in range(n):
            if board[r][c] != symbol:
                ok = False
                break
        if ok:
            return True

    ok = True
    for i in range(n):
        if board[i][i] != symbol:
            ok = False
            break
    if ok:
        return True

    ok = True
    for i in range(n):
        if board[i][n - 1 - i] != symbol:
            ok = False
            break
    if ok:
        return True

    return False  # ← เดิมของคุณ return True ผิด


def main():
    n = ask_board_size()
    p1 = ask_symbol("Enter Player 1's symbol (a single letter): ")
    p2 = ask_symbol(f"Enter Player 2's symbol (a single letter, different from '{p1}'): ",
                    taken=p1)

    board = create_board(n)
    current = p1

    while True:
        display_board(board)
        r, c = ask_move(board, n, current)
        board[r][c] = current

        if check_for_winner(board, current):
            display_board(board)
            print(f"Player '{current}' wins!")
            break

        if is_board_full(board):
            display_board(board)
            print("It's a draw!")
            break

        current = p2 if current == p1 else p1


if __name__ == "__main__":
    main()
