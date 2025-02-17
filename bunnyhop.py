import pygame
import os

pygame.init()
pygame.display.set_caption('ИГРА')


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    image = image.convert_alpha()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image


pygame.init()


bunny_width = 60
bunny_height = 80
bunny_x = 400
bunny_y = 180
anim = 1
clock = pygame.time.Clock()


def run_game():
    running = True
    image = load_image("holebackround.jpg")
    while running:
        for event in pygame.event.get():
            screen.fill((0, 0, 0))
            screen.blit(image, (0, 0))
            pygame.mouse.set_visible(True)
            pygame.display.flip()
            pygame.draw.rect(screen, (0, 0, 0), (bunny_x, bunny_y, bunny_width, bunny_height))
            pygame.display.update()
            clock.tick(60)
            if event.type == pygame.QUIT:
                running = False
    while pygame.event.wait().type != pygame.QUIT:
        pass


run_game()


class Button:
    def __init__(self, width, height, inactive_color, active_color):
        self.width = width
        self.height = height
        self.inactive_color = inactive_color
        self.active_color = active_color

    def draw_button(self, x, y, text, action=None):
        mouse = pygame.mouse.get_pos()
        if x < mouse[0] < x + self.width:
            if y < mouse[1] < y + self.height:
                pygame.draw.rect(screen, (216, 142, 179), (x, y, self.width, self.height))
        else:
            pygame.draw.rect(screen, (239, 154, 196), (x, y, self.width, self.height))


pygame.quit()