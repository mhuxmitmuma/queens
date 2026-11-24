import random
from queens.regions import adjacent_cells, can_remove, grow_regions
from queens.rules import neighbor_conflicts
from queens.solver import find_solutions

MIN_SIZE = 4
MAX_REPAIRS = 40

def generate_regions(size):
    if size < MIN_SIZE:
        raise ValueError(f"size must be at least {MIN_SIZE}")

    while True:
        solution = random_solution(size)
        regions = grow_regions(solution)
        if repair(regions, solution):
            return regions

def random_solution(size):
    columns = list(range(size))
    while True:
        random.shuffle(columns)
        solution = list(enumerate(columns))
        if not neighbor_conflicts(solution):
            return solution

def repair(regions, solution):
    for attempt in range(MAX_REPAIRS):
        solutions = find_solutions(regions)
        if len(solutions) == 1:
            return True

        other = solutions[0]
        if other == solution:
            other = solutions[1]
        if not break_solution(regions, solution, other):
            return False

    return False

def break_solution(regions, solution, other):
    moves = []
    for r, c in other:
        if (r, c) not in solution and can_remove(regions, r, c):
            for r2, c2 in adjacent_cells(r, c, len(regions)):
                if regions[r2][c2] != regions[r][c]:
                    moves.append((r, c, regions[r2][c2]))

    if len(moves) == 0:
        return False

    r, c, label = random.choice(moves)
    regions[r][c] = label
    return True
