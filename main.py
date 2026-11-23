from queens.board import Board, Mark

regions = [
    [1,2,1,1,1],
    [1,2,1,3,1],
    [1,1,1,3,1],
    [1,4,4,4,1],
    [1,1,1,4,5]]
solution = [(0, 1), (1, 3), (2, 0), (3, 2), (4, 4)]

board = Board(regions)
print(len(board.marks), len(board.marks[0]))   # expect: 5 5

for r, c in solution:
    board.marks[r][c] = Mark.QUEEN

print(board)