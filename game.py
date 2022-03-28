import pygame
import map_gen
import map_graphics
import map_solver
import constants
import button
import map_data
import sys


class Game:
    def __init__(self):
        pygame.init()
        self.window_width = constants.WIDTH
        self.window_height = constants.HEIGHT + constants.MARGIN_TOP
        self.amount_of_cells_x = constants.CELLS_X
        self.amount_of_cells_y = constants.CELLS_Y

        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        self.graphics = map_graphics.MapGraphics(self.window_width, self.window_height, self.amount_of_cells_x,
                                                 self.amount_of_cells_y, self.window)

        self.files_menu = map_data.FilesMenu(self.window)

        self.is_playing = True
        self.ready_to_solve = False

        self.button_width = 100
        self.button_height = 20
        dfs_button = button.Button(self.window, (
            constants.MARGIN_TOP / 4, constants.MARGIN_TOP / 4, self.button_width, self.button_height), "dfs",
                                   self.map_with_dfs)
        aldous_button = button.Button(self.window, (
            constants.MARGIN_TOP / 2 + self.button_width, constants.MARGIN_TOP / 4, self.button_width,
            self.button_height), "aldous", self.map_with_aldous)
        kruskal_button = button.Button(self.window, (
            (3 * constants.MARGIN_TOP) / 4 + 2 * self.button_width, constants.MARGIN_TOP / 4, self.button_width,
            self.button_height), "kruskal", self.map_with_kruskal)
        next_map_button = button.Button(self.window, (
            constants.WIDTH - (3 * constants.MARGIN_TOP) / 4, constants.MARGIN_TOP / 4, self.button_height,
            self.button_height), ">", self.load_next)
        prev_map_button = button.Button(self.window, (
            constants.WIDTH - (6 * constants.MARGIN_TOP) / 4, constants.MARGIN_TOP / 4,
            self.button_height, self.button_height), "<", self.load_next)
        save_button = button.Button(self.window, (
            constants.WIDTH - (7 * constants.MARGIN_TOP) / 4 - self.button_width, constants.MARGIN_TOP / 4,
            self.button_width, self.button_height), "save", self.save)
        solve_button = button.Button(self.window, (
            constants.WIDTH / 2 - self.button_width / 2, constants.MARGIN_TOP / 4, self.button_width,
            self.button_height),
                                     "solve", self.solve)
        self.buttons = [dfs_button,
                        aldous_button, kruskal_button, next_map_button,
                        prev_map_button, save_button, solve_button]

    def run(self):
        while self.is_playing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.click_buttons(event)
            pygame.display.flip()

    def map_with_dfs(self):
        self.graphics.cell = 0
        self.clear()
        dfs = map_gen.Generator(self.amount_of_cells_x, self.amount_of_cells_y)
        dfs.dfs()
        dfs.generate_map()
        self.graphics.gen_map(dfs.map, dfs.passes)
        self.ready_to_solve = True

    def map_with_aldous(self):
        self.graphics.cell = 0
        self.clear()
        dfs = map_gen.Generator(self.amount_of_cells_x, self.amount_of_cells_y)
        dfs.aldous_broder()
        dfs.generate_map()
        self.graphics.gen_map(dfs.map, dfs.passes)
        self.ready_to_solve = True

    def map_with_kruskal(self):
        self.graphics.cell = 0
        self.clear()
        dfs = map_gen.Generator(self.amount_of_cells_x, self.amount_of_cells_y)
        dfs.kruskal()
        dfs.generate_map()
        self.graphics.gen_map(dfs.map, dfs.passes)
        self.ready_to_solve = True

    def solve(self):
        if not self.ready_to_solve:
            return 0
        solve = map_solver.Solver(self.graphics.passes, self.amount_of_cells_x, self.amount_of_cells_y)
        pygame.display.flip()
        self.graphics.draw_path(solve.path)

    def clear(self):
        self.graphics.clear_display()

    def click_buttons(self, event):
        for but in self.buttons:
            but.click(event)

    def load_next(self):
        files = self.files_menu.read_next()
        self.load(files)

    def load_prev(self):
        files = self.files_menu.read_prev()
        self.load(files)

    def load(self, files):
        if files is not None:
            map, passes = files[0], files[1]
            self.clear()
            self.amount_of_cells_x = len(map[0]) // 3
            self.amount_of_cells_y = len(map) // 3
            self.graphics = map_graphics.MapGraphics(self.window_width, self.window_height, self.amount_of_cells_x,
                                                     self.amount_of_cells_y, self.window)
            self.graphics.gen_map(map, passes)
            solve = map_solver.Solver(self.graphics.passes, self.amount_of_cells_x, self.amount_of_cells_y)
            pygame.display.flip()
            self.graphics.draw_path(solve.path)

    def save(self):
        self.files_menu.save(self.graphics.field, self.graphics.passes)


game = Game()
game.run()
