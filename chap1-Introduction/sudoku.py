class Sudoku(object):

    def __init__(self):
        self.digits = '123456789'
        self.rows = 'ABCDEFGHI'
        self.cols = self.digits
        self.squares = self.cross(self.rows, self.cols)
        self.unitlist = ([self.cross(self.rows, c) for c in self.cols] +
                         [self.cross(r, self.cols) for r in self.rows] +
                         [self.cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI')
                          for cs in ('123', '456', '789')])
        self.units = dict((s, [u for u in self.unitlist if s in u])
                          for s in self.squares)
        self.peers = dict((s, set(sum(self.units[s], [])) - set([s]))
                          for s in self.squares)

    def cross(self, A, B):
        """ Cross product of elements in A and B """
        return [a+b for a in A for b in B]
