from queens.board import Board, Mark
from queens.rules import queen_positions, group_conflicts, neighbor_conflicts, find_conflicts, is_solved

regions = [
    [1,2,1,1,1],
    [1,2,1,3,1],
    [1,1,1,3,1],
    [1,4,4,4,1],
    [1,1,1,4,5]]
solution = [(0, 1), (1, 3), (2, 0), (3, 2), (4, 4)]

board = Board(regions)
# print(len(board.marks), len(board.marks[0]))   # expect: 5 5

for r, c in solution:
    board.marks[r][c] = Mark.QUEEN

# print(board)
print(queen_positions(board))

# print(group_conflicts([(0, 2), (1, 0)], lambda q: board.regions[q[0]][q[1]]))
# print(group_conflicts(queen_positions(board), lambda q: board.regions[q[0]][q[1]]))

# print(neighbor_conflicts([(2, 3), (3, 2)]))       # diagonal → [[(2, 3), (3, 2)]]
# print(neighbor_conflicts([(0, 1), (0, 3)]))       # 2 apart → []
# print(neighbor_conflicts(queen_positions(board))) # solution → []

bad = Board(regions)
for r, c in [(0, 3), (0, 1), (2, 3), (3, 2), (4, 4)]:
    bad.marks[r][c] = Mark.QUEEN

print(find_conflicts(bad))
print(is_solved(bad))      # False
print(is_solved(board))    # True, with your solution placed