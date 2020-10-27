# initialize the board with size n
def init_board(n):
    board = []
    temp = []

    for i in range(n):
        for j in range(n):
            temp.append(0)
        board.append(temp[:])
        temp.clear()

    return board


# print the solution
def print_board(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(f'{board[i][j]} ', end='')
        print()


# check if a queen can be placed on board[row][col]
def is_safe(board, n, row, col):
    # check the row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # check the upper left diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i][j] == 1:
            return False

    # check the lower left diagonal
    for i, j in zip(range(row + 1, n, 1), range(col - 1, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


# function that solves the n-queen problem
def solve_nq(board, n, col):
    # base case, all queens are placed
    if col >= n:
        return True

    # check each row in col and try to place a queen
    for row in range(n):
        if is_safe(board, n, row, col):
            board[row][col] = 1

            # go to the next column
            if solve_nq(board, n, col + 1):
                return True

            # if the queen in board[row][col] doesn't lead to a solution,
            # we remove the queen and backtrack
            board[row][col] = 0

    return False


def main():
    n = int(input('Board size: '))
    board = init_board(n)

    if not solve_nq(board, n, 0):
        print('Solution does not exist')
        return False

    print_board(board)
    return True


if __name__ == '__main__':
    main()
