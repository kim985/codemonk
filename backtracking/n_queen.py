import time


def n_queen_in_n_squared_time(board, n):

    if n == 0:
        return True  # All queens placed

    for i in range(len(board)):

        if 1 in board[i]:
            continue

        for j in range(len(board)):

            if board[i][j] == 1:
                continue

            if is_attacked(i, j, board):
                continue

            board[i][j] = 1

            if n_queen_in_n_squared_time(board, n - 1):
                return True
            board[i][j] = 0

    return False


def n_queen_in_linear_time(board, n):

    if n < 0:
        return True  # All queens placed

    for i in range(len(board)):

        if is_attacked(i, n, board):
            continue

        board[i][n] = 1

        if n_queen_in_linear_time(board, n - 1):
            return True
        board[i][n] = 0

    return False


def is_attacked(x, y, _board):

    if 1 in _board[x]:
        return True

    board_col = [i[y] for i in _board]

    if 1 in board_col:
        return True

    for p in range(len(_board)):
        q = (x + y) - p
        if q in range(len(_board)) and _board[p][q] == 1:
            return True
        q = -((x - y) - p)
        if q in range(len(_board)) and _board[p][q] == 1:
            return True

    return False


def display(_board):
    for row in _board:
        for el in row:
            print(el, end=" ")
        print()


def test_quad_time():
    n = int(input())

    t = time.time()
    board = [[0 for _ in range(n)] for _ in range(n)]

    print("YES") if n_queen_in_n_squared_time(board, n) else print("NO")

    display(board)
    print(time.time() - t)


def test_linear_time():
    n = int(input())

    t = time.time()
    board = [[0 for _ in range(n)] for _ in range(n)]

    print("YES") if n_queen_in_linear_time(board, n - 1) else print("NO")

    display(board)
    print(time.time() - t)


if __name__ == '__main__':
    test_quad_time()
    test_linear_time()
