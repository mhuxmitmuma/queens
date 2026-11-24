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

def is_touching(queen1, queen2):
    r1, c1 = queen1
    r2, c2 = queen2
    return abs(r1-r2) <= 1 and abs(c1-c2) <= 1

def neighbor_conflicts(queens):
    conflicts = []
    for i in range(len(queens)):
        for j in range(i+1, len(queens)):
            if is_touching(queens[i], queens[j]):
                conflicts.append([queens[i], queens[j]])

    return conflicts

def add_exes(board, queen):
    for r in range(board.size):
        for c in range(board.size):
            blocked = r == queen[0] or c == queen[1] or is_touching(queen, (r, c))
            if blocked and board.marks[r][c] == Mark.EMPTY:
                board.marks[r][c] = Mark.EX

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
