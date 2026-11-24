import tkinter as tk
from queens.board import Board, Mark
from queens.generator import generate_regions
from queens.rules import add_exes, find_conflicts, is_solved

CELL = 100
COLORS = ["#BBA3E2", "#FFC992", "#96BEFF", "#B3DFA0", "#DFDFDF",
          "#62EFBF", "#E6F388", "#B9B29E", "#DFA0BF", "#A3D2D8"]

class QueensApp:
    def __init__(self, root, board):
        self.set_board(board)

        pixels = board.size * CELL
        self.canvas = tk.Canvas(root, width=pixels, height=pixels)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.on_click)
        self.canvas.bind("<Button-3>", self.on_right_click)
        self.status = tk.Label(root, text="", font=("Arial", 20))
        self.status.pack()

        buttons = tk.Frame(root)
        buttons.pack(pady=10)
        self.clear_button = tk.Button(buttons, text="Clear board", font=("Arial", 14), command=self.on_clear)
        self.clear_button.pack(side="left", padx=5)
        self.new_button = tk.Button(buttons, text="New puzzle", font=("Arial", 14), command=self.on_new)
        self.new_button.pack(side="left", padx=5)
        self.auto_ex = tk.BooleanVar(root, value=False)
        self.auto_button = tk.Checkbutton(buttons, text="Auto X", font=("Arial", 14), variable=self.auto_ex)
        self.auto_button.pack(side="left", padx=5)
        self.draw()

    def set_board(self, board):
        self.board = board

        labels = set()
        for row in board.regions:
            for label in row:
                labels.add(label)

        self.region_colors = {}
        for i, label in enumerate(sorted(labels)):
            self.region_colors[label] = COLORS[i % len(COLORS)]

    def draw(self):
        self.canvas.delete("all")

        conflict_cells = set()
        for groups in find_conflicts(self.board).values():
            for group in groups:
                for cell in group:
                    conflict_cells.add(cell)

        for r in range(self.board.size):
            for c in range(self.board.size):
                x1 = c * CELL
                y1 = r * CELL
                x2 = x1 + CELL
                y2 = y1 + CELL

                color = self.region_colors[self.board.regions[r][c]]
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")

                center_x = x1 + CELL / 2
                center_y = y1 + CELL / 2
                mark = self.board.marks[r][c]
                if mark == Mark.QUEEN:
                    queen_color = "red" if (r, c) in conflict_cells else "black"
                    self.canvas.create_text(center_x, center_y, text="♛", font=("Arial", CELL // 2), fill=queen_color)
                elif mark == Mark.EX:
                    self.canvas.create_text(center_x, center_y, text="X", font=("Arial", CELL // 3))

        if is_solved(self.board):
            self.status.config(text="Solved!")
        else:
            self.status.config(text="")

    def on_click(self, event):
        self.change_cell(event, self.cycle_cell)

    def on_right_click(self, event):
        self.change_cell(event, self.board.clear_cell)

    def cycle_cell(self, r, c):
        self.board.cycle(r, c)
        if self.auto_ex.get() and self.board.marks[r][c] == Mark.QUEEN:
            add_exes(self.board, (r, c))

    def change_cell(self, event, change):
        r = event.y // CELL
        c = event.x // CELL
        if r < self.board.size and c < self.board.size:
            change(r, c)
            self.draw()

    def on_clear(self):
        self.board.clear()
        self.draw()

    def on_new(self):
        regions = generate_regions(self.board.size)
        self.set_board(Board(regions))
        self.draw()
