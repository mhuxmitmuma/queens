from queens.rules import is_touching

def find_solutions(regions, limit=2):
    solutions = []
    place_queens(regions, [], solutions, limit)
    return solutions

def place_queens(regions, queens, solutions, limit):
    r = len(queens)
    if r == len(regions):
        solutions.append(queens)
        return

    for c in range(len(regions)):
        if len(solutions) < limit and can_place(regions, queens, r, c):
            place_queens(regions, queens + [(r, c)], solutions, limit)

def can_place(regions, queens, r, c):
    for r2, c2 in queens:
        if c == c2 or regions[r][c] == regions[r2][c2]:
            return False
    return len(queens) == 0 or not is_touching(queens[-1], (r, c))
