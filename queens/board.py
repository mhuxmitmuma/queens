from enum import Enum

class Mark(Enum):
    EMPTY = 0
    QUEEN = 1
    EX = 2

class Board:
    def __init__(self, regions):
        self.regions = regions
        self.size = len(regions)
        self.marks = [[Mark.EMPTY for column in range(self.size)] for row in range(self.size)]

    def __str__(self):
        lines = []
        for r in range(self.size):
            chars = []
            for c in range(self.size):
                mark = self.marks[r][c]
                if mark == Mark.QUEEN:
                    chars.append("Q")
                elif mark == Mark.EX:
                    chars.append("x")
                else:
                    chars.append(str(self.regions[r][c]))
            lines.append(" ".join(chars))
        return "\n".join(lines)