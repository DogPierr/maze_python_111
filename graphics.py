import map_gen
from tkinter import *


class Graphics:
    def __init__(self):
        self.width = 1000
        self.height = 1000
        self.x_cells = 50
        self.y_cells = 50
        self.cell_width = self.height / (3 * self.y_cells)
        self.cell_height = self.width / (3 * self.x_cells)
        self.cells = [
            [(i * self.cell_width, j * self.cell_height, (i + 1) * self.cell_width, (j + 1) * self.cell_height) for i in
             range(3 * self.x_cells)] for j in
            range(3 * self.y_cells)]
        self.field = []
        self.window = Tk()
        self.window.geometry('1000x1000')
        self.canvas = Canvas(bg="white", width=self.width, height=self.height)
        self.passes = {}
        self.walls = {}

    def DFSmap(self):
        dfs = map_gen.DFSGenerator(self.x_cells, self.y_cells)
        self.field = dfs.map
        self.passes = dfs.passes
        self.walls = dfs.walls
        for y in range(3 * self.y_cells):
            # print(y, ")")
            for x in range(3 * self.x_cells):
                x0 = self.cells[y][x][0]
                y0 = self.cells[y][x][1]
                x1 = self.cells[y][x][2]
                y1 = self.cells[y][x][3]
                if self.field[y][x  ] == 1:
                    self.canvas.create_rectangle(x0, y0, x1, y1, fill="#1f1")
                # print()

        # for line in self.field:
        #     for var in line:
        #         print(var, end="")
        #     print()
        self.canvas.pack(fill=BOTH, expand=1)

    def MainLoop(self):
        self.DFSmap()
        self.window.mainloop()


game = Graphics()
game.MainLoop()
