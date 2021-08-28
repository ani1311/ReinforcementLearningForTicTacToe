

"""
    This class contains the Game board functionality.
    Variables:
        board: 2D n by n array.
            0 - Empty
            1 - Player 1
            2 - Player 2
"""


class GameBoard:
    def __init__(self,n=3):
        self.n = n
        self.board = [[0 for _ in range(n)] for _ in range(n)]

    def __repr__(self):
        stringOfBoard = ""

        for i in self.board:
            for j in i:
                stringOfBoard = stringOfBoard + str(j) + " "
            stringOfBoard = stringOfBoard + "\n"

        return stringOfBoard

    def gameComplete(self):
        draw = True

        for i in range(self.n):
            f1 = True
            f2 = True

            pos1 = self.board[i][0]
            pos2 = self.board[0][i]

            if pos1 == 0:
                f1 = False

            if pos2 == 0:
                f2 = False

            for j in range(self.n):
                if self.board[i][j] == 0:
                    draw = False

                if self.board[i][j] != pos1:
                    f1 = False
                if self.board[j][i] != pos2:
                    f1 = False 
                if not f1 and not f2:
                    break

            if f1:
                return pos1;
            if f2:
                return pos2;

        if draw:
            return 0;

        f1 = True
        f2 = True
        pos1 = self.board[0][0]
        pos2 = self.board[self.n-1][0]

        if pos1 == 0:
            f1 = False

        if pos2 == 0:
            f2 = False

        for i in range(self.n):
            if self.board[i][i] != pos1:
                f1 = False
            if self.board[self.n-1-i][i] != pos2:
                f2 = False
            if not f1 and not f2:
                break

        if f1 :
            return pos1

        if f2 :
            return pos2

        return -1 

    def getInputForNN(self):
        ip = []

        for i in self.board:
            ip = ip + i

        return ip




