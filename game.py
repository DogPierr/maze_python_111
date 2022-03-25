import pygame
import dfs_gen
import graphics
import map_solver
import constants
import button
import sys


class Game:
    def __init__(self):
        pygame.init()
        self.window_width = constants.WIDTH
        self.window_height = constants.HEIGHT + constants.MARGIN_TOP
        self.amount_of_cells_x = constants.CELLS_X
        self.amount_of_cells_y = constants.CELLS_Y

        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        self.graphics = graphics.Graphics(self.window_width, self.window_height, self.amount_of_cells_x,
                                          self.amount_of_cells_y, self.window)

        self.gen_algo = 'dfs'
        self.is_playing = True
        self.is_stop = False

        self.buttons = [button.Button(self.window, (10, 10, 100, 20), "aboba", self.map_with_dfs)]

    def run(self):
        self.map_with_dfs()
        while self.is_playing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.click_buttons(event)
            pygame.display.flip()

    def map_with_dfs(self):
        self.clear()
        dfs = dfs_gen.DFSGenerator(self.amount_of_cells_x, self.amount_of_cells_y)
        self.graphics.gen_map(dfs.map, dfs.passes)
        solve = map_solver.Solver(self.graphics.passes, self.amount_of_cells_x, self.amount_of_cells_y)
        pygame.display.flip()
        self.graphics.draw_path(solve.path)

    def clear(self):
        self.graphics.clear_display()

    def click_buttons(self, event):
        for but in self.buttons:
            but.click(event)


game = Game()
game.run()
