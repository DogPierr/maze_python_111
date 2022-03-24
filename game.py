import pygame
import graphics
import map_gen
import map_solver
import sys


class Game:
    def __init__(self):
        pygame.init()
        self.window_width = 1000
        self.window_height = 1000
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        self.amount_of_cells_x = 50
        self.amount_of_cells_y = 50
        self.graphics = graphics.Graphics(self.window_width, self.window_height, self.amount_of_cells_x,
                                          self.amount_of_cells_y, self.window)
        self.is_playing = True
        self.is_stop = False

    def Run(self):
        self.graphics.DFSmap()
        solve = map_solver.Solver(self.graphics.passes, self.amount_of_cells_x, self.amount_of_cells_y)
        pygame.display.flip()
        self.graphics.DrawPath(solve.path)
        print(solve.path)
        print(self.graphics.passes)
        while self.is_playing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.flip()


game = Game()
game.Run()
