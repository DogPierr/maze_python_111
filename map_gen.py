import random
import sys
from tkinter import *

sys.setrecursionlimit(12000)

class DFSGenerator:
    def __init__(self):
        self.width = 100
        self.height = 100
        self.map = [[0 for _ in range(self.width)] for _ in range(self.height)]
        self.drawable_map = [[0 for _ in range(self.width * 3)] for _ in range(self.height * 3)]
        self.edges = {}

    def DFS(self, coords):
        self.map[coords[0]][coords[1]] = 1
        available_neighbours = self.GetNeighbours(coords)

        while len(available_neighbours) > 0:
            direction = random.randint(0, len(available_neighbours) - 1)
            neighbour = available_neighbours[direction]
            if self.map[neighbour[0]][neighbour[1]] == 0:
                if not coords in self.edges.keys():
                    self.edges[coords] = []
                self.edges[coords].append(neighbour)
                self.DFS(neighbour)
            del available_neighbours[direction]

    def GetNeighbours(self, coords):
        neighbors = [(i, j) for i, j in zip([coords[0] - 1, coords[0] + 1, coords[0], coords[0]],
                                            [coords[1], coords[1], coords[1] + 1, coords[1] - 1])]
        i = 0
        while i < len(neighbors):
            coord = neighbors[i]
            if coord[0] < 0 or coord[0] >= self.height or coord[1] >= self.width or coord[1] < 0:
                del neighbors[i]
            else:
                i += 1

        return neighbors

    def GenerateMap(self):
        self.DFS((0, 0))


if __name__ == '__main__':
    map = DFSGenerator()
    map.GenerateMap()
    root = Tk()
    canvas = Canvas(bg="white", width=1000, height=1000)
    for v in map.edges.keys():
        for to in map.edges[v]:
            canvas.create_line(20 + v[0] * 20, 20 + v[1] * 20, 20 + to[0] * 20, 20 + to[1] * 20)

    canvas.pack(fill=BOTH, expand=1)
    root.mainloop()
