def read_board_size():
    while True:
        raw = input('Enter board size n for n x n board (3-10): ')
        if not raw.isdigit():
            print('Invalid input. Please enter a number.')
            continue
        n = int(raw)
        if 3 <= n <= 10:
            return n
        print('Size must be between 3 and 10. Please try again.')