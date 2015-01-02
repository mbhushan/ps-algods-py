from sudoku import Sudoku


def testCross(sudoku):
    """ a set of unit tests for testing cross api in Sudoku class """
    assert len(sudoku.getSquares()) == 81
    assert len(sudoku.getUnitlist()) == 27
    units = sudoku.getUnits()
    assert all(len(units[s]) == 3 for s in sudoku.getSquares())
    peers = sudoku.getPeers()
    assert all(len(peers[s]) == 20 for s in sudoku.getPeers())
    print ("Units in B2: ")
    print (units['B2'])
    u1 = ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9']
    u2 = ['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2']
    u3 = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
    ub2 = [u2, u1, u3]
    print (ub2)
    for u in range(3):
        for e in range(9):
            if units['B2'][u][e] != ub2[u][e]:
                print ("E:", e)
    print ('ALL B2 Passed!')
    assert units['B2'] == ub2
    assert peers['C2'] == set(['A2', 'B2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2',
                               'C1', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9',
                               'A1', 'A3', 'B1', 'B3'])
    print ('All TESTS PASS!')


def main():
    sd = Sudoku()
    testCross(sd)

if __name__ == '__main__':
    main()
