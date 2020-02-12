import time


def long_n_queen(board, n):  # Running time: O((n+1)!)
    """
    Running Time:
        for arbitrary number N,
            O(n)    = (i-for loop) * (j-for loop) * n_queen_in_n_squared_time(N-1)
                    = (N+1) * (N) * [N * (N-1) * n_queen_in_n_squared_time(N-2)]
                    ...
                    = (N+1) * (N) * [N * (N-1) * [...[ 3 * 2 *  n_queen_in_n_squared_time(1)]]]]     # N=2
                    = (N+1) * (N) * [N * (N-1) * [...[ 3 * 2 *  [2 * 1 * n_queen_in_n_squared_time(0)]]]]]
                    = (N+1) * (N) * [N * (N-1) * [...[ 3 * 2 *  [2 * 1 * 1]]]]]
                    = (N+1) * (N^2)!
                    = (N+1)!N!


    Parameters:
        board: grid of N X N to place queens in, where N is the input size of the grid
        n: no. of queens remaining to place

    Returns:
         true or false depending on if solution is possible.
    """

    if n == 0:
        return True  # All queens placed

    for i in range(len(board)):  # Calc running time: N+1

        if 1 in board[i]:  # Calc running time: 1
            continue

        for j in range(len(board)):  # Calc running time: N (from i loop) * (N+1) (from j loop)

            if board[i][j] == 1:  # Calc running time: 1
                continue

            if is_attacked(i, j, board):  # Calc running time: O(N) - see is_attacked function
                continue

            board[i][j] = 1  # Calc running time: k

            if long_n_queen(board, n - 1):  # Calc running time: substitute n = n-1
                return True
            board[i][j] = 0

    return False


def short_n_queen(board, n):
    """
    Running Time:
        for arbitrary number N,
            O(n)    = (i-for loop) * n_queen_in_n_squared_time(N-1)
                    = (N+1) * [N * n_queen_in_n_squared_time(N-2)]
                    ...
                    = (N+1) * [N * (N-1) * [...[ 3 * [ 2 *  n_queen_in_n_squared_time(1)]]]]     # N=2
                    = (N+1) * [N * (N-1) * [...[ 3 * [ 2 *  [1 * n_queen_in_n_squared_time(0)]]]]]
                    = (N+1) * [N * (N-1) * [...[ 3 * [ 2 *  [1 * 1]]]]]
                    = (N+1)!
                    ~ N!


    Parameters:
        board: grid of N X N to place queens in, where N is the input size of the grid
        n: no. of queens remaining to place

    Returns:
         true or false depending on if solution is possible.
    """
    if n < 0:
        return True  # All queens placed

    for i in range(len(board)):

        if is_attacked(i, n, board):
            continue

        board[i][n] = 1

        if short_n_queen(board, n - 1):
            return True
        board[i][n] = 0

    return False


def shorter_n_queen(_, __):
    pass


def is_attacked(x, y, _board):
    """ Check if square(x, y) is attacked """
    if 1 in _board[x]:  # Calc running time: k
        return True

    board_col = [i[y] for i in _board]  # Calc running time: N

    if 1 in board_col:  # Calc running time: 1
        return True

    for p in range(len(_board)):  # Calc running time: N+1
        q = (x + y) - p
        if q in range(len(_board)) and _board[p][q] == 1:
            return True
        q = -((x - y) - p)
        if q in range(len(_board)) and _board[p][q] == 1:
            return True

    return False


def display(_board):
    """ Display board """
    for row in _board:
        for el in row:
            print(el, end=" ")
        print()


def test_n_queen(n_queen_func):
    """ Utility to test the algorithms """
    n = int(input())

    t = time.time()
    board = [[0 for _ in range(n)] for _ in range(n)]

    print("YES") if n_queen_func(board, n) else print("NO")

    display(board)
    print(time.time() - t)


if __name__ == '__main__':
    test_n_queen(long_n_queen)
    test_n_queen(short_n_queen)
    test_n_queen(shorter_n_queen)
