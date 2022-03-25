import constants
import pygame
import button
import sys


class Graphics:
    def __init__(self, w, h, x_cells, y_cells, window):
        self.width = w
        self.height = h
        self.x_cells = x_cells
        self.y_cells = y_cells
        self.cell_width = self.width / (3 * self.y_cells)
        self.cell_height = self.cell_width

        self.cells = [
            [pygame.Rect(i * self.cell_width, constants.MARGIN_TOP + j * self.cell_height, self.cell_width,
                         self.cell_height) for i in
             range(3 * self.x_cells)] for j in
            range(3 * self.y_cells)]
        self.field = []
        self.passes = {}

        self.window = window

    def gen_map(self, map, passes):
        self.field = map
        self.passes = passes
        for y in range(3 * self.y_cells):
            for x in range(3 * self.x_cells):
                if self.field[y][x] == 1:
                    pygame.draw.rect(self.window, (0, 255, 0), self.cells[y][x], 0)

    def draw_cell(self, x, y):
        pygame.draw.rect(self.window, (255, 0, 0), self.cells[y][x], 0)
        # pygame.time.delay(1)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def draw_path(self, path):
        for cell in range(len(path) - 1):
            v = path[cell]
            to = path[cell + 1]
            if v[0] == to[0]:
                start = min(v[1], to[1])
                end = max(v[1], to[1])
                for i in range(1 + 3 * start, 1 + 3 * end + 1):
                    self.draw_cell(i, 1 + 3 * v[0])
            elif v[1] == to[1]:
                start = min(v[0], to[0])
                end = max(v[0], to[0])
                for i in range(1 + 3 * start, 1 + 3 * end + 1):
                    self.draw_cell(1 + 3 * v[1], i)

    def clear_display(self):
        pygame.draw.rect(self.window, (0, 0, 0),
                         pygame.Rect(0, constants.MARGIN_TOP, self.width, self.height - constants.MARGIN_TOP), 0)
        pygame.display.flip()
