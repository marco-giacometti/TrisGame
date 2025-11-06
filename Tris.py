class OccupiedBoxError(Exception):
    pass

class Status:

    WIN_COMBOS = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]  # All the possible win combos

    def __init__(self):
        self.tab = [' ' for i in range(9)]

    def add_X(self, pos):
        if self.tab[pos] != ' ':
            raise OccupiedBoxError
        self.tab[pos] = 'X'

    def add_O(self, pos):
        if self.tab[pos] != ' ':
            raise OccupiedBoxError
        self.tab[pos] = 'O'
              
    def printBoard(self):
        s = ''
        for i in range(len(self.tab)):
            s = s + '|' + self.tab[i]
            if i == 2 or i ==5:
                s = s +'|\n-------\n'
            if i == 8:
                s = s + '|'
        return s

    def win(self):
        for a,b,c in self.WIN_COMBOS:
            if self.tab[a] != ' ' and self.tab[a]==self.tab[b]==self.tab[c]:
                return True
        return False
    
    def tie(self):
        return ' ' not in self.tab and not self.win()

    def __str__(self):
        return self.printBoard()