import random

def adjacent_cells(r, c, size):
    cells = []
    for r2, c2 in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
        if 0 <= r2 < size and 0 <= c2 < size:
            cells.append((r2, c2))
    return cells

def grow_regions(solution):
    size = len(solution)
    regions = [[None for column in range(size)] for row in range(size)]
    for i in range(size):
        r, c = solution[i]
        regions[r][c] = i + 1

    empty_count = size * size - size
    while empty_count > 0:
        r = random.randrange(size)
        c = random.randrange(size)
        if regions[r][c] is None:
            labels = []
            for r2, c2 in adjacent_cells(r, c, size):
                if regions[r2][c2] is not None:
                    labels.append(regions[r2][c2])

            if len(labels) > 0:
                regions[r][c] = random.choice(labels)
                empty_count -= 1

    return regions

def can_remove(regions, r, c):
    size = len(regions)
    cells = []
    for r2 in range(size):
        for c2 in range(size):
            if regions[r2][c2] == regions[r][c] and (r2, c2) != (r, c):
                cells.append((r2, c2))

    if len(cells) == 0:
        return False

    reached = [cells[0]]
    for r2, c2 in reached:
        for cell in adjacent_cells(r2, c2, size):
            if cell in cells and cell not in reached:
                reached.append(cell)

    return len(reached) == len(cells)
