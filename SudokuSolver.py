class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        self.board = board
        self.val = self.initVals()
        self.Solver()

    def initVals(self):

        a = '123456789'

        tmp, val = {}, {}
        for i in range(9):
            for j in range(9):
                curr = self.board[i][j]
                if curr != '.':
                    tmp[('r', i)] = tmp.get(('r', i), []) + [curr]
                    tmp[('c', j)] = tmp.get(('c', j), []) + [curr]
                    tmp[(i / 3, j / 3)] = tmp.get((i / 3, j / 3), []) + [curr]
                else:
                    val[(i, j)] = []

        for (i, j) in val.keys():
            inval = tmp.get(('r', i), []) + tmp.get(('c', j), []) + tmp.get((i / 3, j / 3), [])
            val[(i, j)] = [s for s in a if s not in inval]

        return val

    def Solver(self):

        if len(self.val) == 0:
            return True

        start_key = min(self.val.keys(), key=lambda k : len(self.val[k]))
        start_num = self.val[start_key]

        for n in start_num:
            update = {start_key: self.val[start_key]}
            if self.ValidOne(n, start_key, update):
                if self.Solver():
                    return True
            self.undo(start_key, update)
        return False

    def ValidOne(self, n, start_key, update):
        self.board[start_key[0]][start_key[1]] = n
        del self.val[start_key]
        i, j = start_key
        for ind in self.val.keys():
            if n in self.val[ind] and (ind[0] == i or ind[1] == j or (ind[0] / 3, ind[1] / 3) == (i / 3, j / 3)):
                update[ind] = n
                self.val[ind].remove(n)
                if len(self.val[ind]) == 0:
                    return False
        return True

    def undo(self, kee, update):
        self.board[kee[0]][kee[1]] = "."
        for k in update:
            if k not in self.val:
                self.val[k] = update[k]
            else:
                self.val[k].append(update[k])
        return None

