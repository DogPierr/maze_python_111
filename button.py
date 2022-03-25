import pygame.draw


class Button:
    def __init__(self, window, coords, text, func=lambda: True):
        self.rect = pygame.Rect(coords)
        self.text = text
        self.func = func
        self.window = window
        self.draw_button()

    def draw_button(self):
        pygame.draw.rect(self.window, (255, 255, 255), self.rect, 0)
        pygame.display.flip()

    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    return self.func()
