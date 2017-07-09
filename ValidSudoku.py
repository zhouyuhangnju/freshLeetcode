def isValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """

    seen = set()

    for i in range(9):
        for j in range(9):
            if board[i][j] != '.':
                curr = board[i][j]
                if (i, curr) in seen or (curr, j) in seen or (i / 3, j / 3, curr) in seen:
                    return False
                else:
                    seen.add((i, curr))
                    seen.add((curr, j))
                    seen.add((i / 3, j / 3, curr))

    return True


print isValidSudoku([".87654321","2........","3........","4........","5........","6........","7........","8........","9........"])