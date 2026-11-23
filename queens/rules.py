from queens.board import Mark


def queen_positions(board):
    positions = []
    for r in range(board.size):
        for c in range(board.size):
            if board.marks[r][c] == Mark.QUEEN:
                positions.append((r, c))
    return positions

def group_conflicts(queens, key):
    groups = {}
    for queen in queens:
        k = key(queen)
        if k not in groups:
            groups[k] = []
        groups[k].append(queen)

    conflicts = []
    for group in groups.values():
        if len(group) > 1:
            conflicts.append(group)

    return conflicts

def neighbor_conflicts(queens):
    conflicts = []
    for i in range(len(queens)):
        for j in range(i+1, len(queens)):
            r1, c1 = queens[i]
            r2, c2 = queens[j]
            if abs(r1-r2) <= 1 and abs(c1-c2) <= 1:
                conflicts.append([queens[i], queens[j]])

    return conflicts

def find_conflicts(board):
    queens = queen_positions(board)
    conflicts = {
        "row": group_conflicts(queens, lambda q: q[0]),
        "column": group_conflicts(queens, lambda q: q[1]),
        "region": group_conflicts(queens, lambda q: board.regions[q[0]][q[1]]),
        "neighbor": neighbor_conflicts(queens)
    }
    return conflicts

def is_solved(board):
    queen_count = len(queen_positions(board))
    has_conflicts = any(find_conflicts(board).values())
    return queen_count == board.size and not has_conflicts
    