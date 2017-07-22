def exist(board, word):
    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
    """

    def subsearch(currloc, curridx, board, word, state):

        row, col = currloc[0], currloc[1]

        if board[row][col] == word[curridx]:
            if curridx + 1 == len(word):
                return True

            newstate = [[j for j in i] for i in state]
            newstate[row][col] = 1

            if row > 0 and state[row - 1][col] == 0:
                if subsearch((row - 1, col), curridx + 1, board, word, newstate):
                    return True
            if col > 0 and state[row][col - 1] == 0:
                if subsearch((row, col - 1), curridx + 1, board, word, newstate):
                    return True
            if row < m - 1 and state[row + 1][col] == 0:
                if subsearch((row + 1, col), curridx + 1, board, word, newstate):
                    return True
            if col < n - 1 and state[row][col + 1] == 0:
                if subsearch((row, col + 1), curridx + 1, board, word, newstate):
                    return True

            return False

    m = len(board)
    if m <= 0:
        return False
    n = len(board[0])
    if n <= 0:
        return False

    state = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if board[i][j] == word[0]:
                if subsearch((i, j), 0, board, word, state):
                    return True

    return False


if __name__ == '__main__':
    print exist([
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
], "ABCB")