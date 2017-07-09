def solveNQueens(n):
    """
    :type n: int
    :rtype: List[List[str]]
    """

    solutions = []

    def subSolveNQueens(row, curr_solution):
        if row == n:
            solutions.append(curr_solution)
        else:
            for i in range(n):
                flag = True
                for j in range(row):
                    if curr_solution[j] == i or curr_solution[j] == i - (row - j) or curr_solution[j] == i + (row - j):
                        flag = False
                        break
                if flag:
                    new_solution = []
                    for k in curr_solution:
                        new_solution.append(k)
                    new_solution.append(i)
                    subSolveNQueens(row+1, new_solution)

    subSolveNQueens(0, [])

    strsolutions = []
    for solution in solutions:
        strsolution = []
        for i in range(n):
            strs = ''
            for j in range(n):
                if j != solution[i]:
                    strs += '.'
                else:
                    strs += 'Q'
            strsolution.append(strs)
        strsolutions.append(strsolution)

    return strsolutions



if __name__ == '__main__':

    solutions = solveNQueens(4)

    for s in solutions:
        print s

    print len(solutions)