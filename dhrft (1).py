import sys
import sqlite3

import pygame
import os
from PIL import Image
import random


# pygame.time.set_timer(pygame.USEREVENT, 2000)
clock = pygame.time.Clock()
pygame.init()
w, h = 800, 600
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('ИГРА')
brown = (115, 64, 34)

pygame.mixer.music.load('backgroundmusic.mp3')
boom_sound = pygame.mixer.Sound('boomsound.mp3')


def draw_text(surf, size,  x, y, text):
    pygame.font.init()
    font = pygame.font.SysFont(None, size)
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


def new_size(image, w, h):
    im = Image.open('data\\' + image)
    new_size = (w, h)
    resized_image = im.resize(new_size)
    resized_image.save('data\\' + image)


def load_image(name, colorkey=None):
    fullname = os.path.join('../pythonMASHAPROJECT/data', name)
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


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.top = 20
        self.cell_size = 60
        self.left = 190

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for i in range(self.width):
            for j in range(self.height):
                pygame.draw.rect(screen, (0, 0, 0), (self.left + i * self.cell_size,
                                                           self.top + j * self.cell_size, self.cell_size,
                                                           self.cell_size), width=1)


class Bunny(pygame.sprite.Sprite):
    image = load_image('bunnymove1.jpg')
    image1 = load_image('bunnymove2.jpg')

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Bunny.image
        self.image1 = Bunny.image1
        self.image2 = Bunny.image
        self.top = 20
        self.cell_size = 60
        self.left = 190
        self.rect = self.image.get_rect()
        self.rect.x = self.left + (self.cell_size * 3)
        self.rect.y = self.top + (self.cell_size * 2)
        self.clock = 0

    def get_event(self):
        if self.clock % 2 == 0:
            self.image = self.image1
        else:
            self.image = self.image2
        self.clock += 1

    def update(self, side, speed=60):
        if self.rect.x >= self.left + (self.cell_size * 6):
            if side:
                print(1)
                self.rect = self.rect.move(-speed, 0)

        elif self.rect.x <= self.left:
            if not side:
                print(2)
                self.rect = self.rect.move(speed, 0)
        else:
            if side:
                print(1)
                self.rect = self.rect.move(-speed, 0)
            else:
                print(2)
                self.rect = self.rect.move(speed, 0)


class Hurdle(pygame.sprite.Sprite):
    image = load_image('chocolate.jpg')
    image1 = load_image('cupcake.png')
    image2 = load_image('donut.jpg')
    s = [image, image1, image2]

    def __init__(self, *group):
        super().__init__(*group)
        self.image = self.s[random.randint(0, 2)]
        self.top = 20
        self.cell_size = 60
        self.left = 190
        self.cage = random.randint(0, 6)
        self.rect = self.image.get_rect()
        self.k = 9
        if self.image == self.s[2]:
            bad = True

    def get_event(self):
        self.k -= 1
        self.rect.topleft = (
            (self.left + (self.cell_size * self.cage), self.top + (self.cell_size * self.k)))


new_size('chocolatebackround.jpg', 800, 600)
new_size('bunnymove1.jpg', 60, 60)
new_size('bunnymove2.jpg', 60, 60)
new_size('chocolate.jpg', 60, 60)
new_size('cupcake.png', 60, 60)
new_size('donut.jpg', 60, 60)
new_size('soundon.png', 50, 50)
new_size('soundoff.png', 50, 50)
left = False
right = False
all_sprites = pygame.sprite.Group()
all_sprites1 = pygame.sprite.Group()
chocolatebackround = load_image('chocolatebackround.jpg')
gamebackround = load_image("gamebackround.jpg")
vertical_borders = pygame.sprite.Group()

Bunny(all_sprites)
boardstart = False
speed = 3
k = 0
score = 0
running = True
enter = False
start = True
flag_login = False
startgame = False
playbutton = False
active_log = False
active_pas = False
user_text = ''
user_text1 = ''
text1 = ''
flag_play = False
flag_uniq = True
soundon = True
soundoff = False
idscore = 0
result = 0
s = 0
collide1 = False
stopgame = False
board = Board(7, 9)
imagesoundon = load_image("soundon.png")
imagesoundoff = load_image("soundoff.png")
imagesound = imagesoundon
while running:
    if start:
        boardstart = True
        if boardstart:
            board.render(screen)
        pygame.mixer.music.play(-1)
        screen.blit(chocolatebackround, (0, 0))
        draw_text(screen, 100, 400, 250, 'BUNNYHOP')
        pygame.draw.rect(screen, 'pink', (300, 400, 220, 120))
        draw_text(screen, 100, 410, 430, 'ВХОД')
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(12121)
                print(pygame.mouse.get_pressed())
                if pygame.mouse.get_pressed()[0]:
                    pos = pygame.mouse.get_pos()
                    print(pos)
                    if (pos[0] > 300 and pos[1] > 400) and (pos[0] < 520 and pos[1] < 520):
                        print(1)
                        start = False
                        flag_login = True
    elif flag_login:
        # print(2222)
        flag = False
        base_font = pygame.font.Font(None, 32)

        input_rect = pygame.Rect(150, 200, 140, 32)
        input_rect1 = pygame.Rect(150, 250, 140, 32)
        color_passive = pygame.Color('white')

        darkerwhite = (190, 195, 198)
        color_active = pygame.Color(darkerwhite)
        color = color_passive

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(12121212)
                if input_rect.collidepoint(event.pos):
                    print(1111)
                    active_log = True
                else:
                    print(0000)
                    active_log = False
                if input_rect1.collidepoint(event.pos):
                    active_pas = True
                else:
                    active_pas = False
                if pygame.mouse.get_pressed()[0]:
                    pos = pygame.mouse.get_pos()
                    print(pos)
                    if pygame.mouse.get_pressed()[0] and ((pos[0] > 50 and pos[1] > 490) and
                                                          (pos[0] < 100 and pos[1] < 540)) and soundon:
                        print(11111)
                        soundoff = True
                        soundon = False
                        pygame.mixer.music.stop()
                    elif pygame.mouse.get_pressed()[0] and (pos[0] > 50 and pos[1] > 490) and \
                            (pos[0] < 100 and pos[1] < 540) and soundoff:
                        soundon = True
                        soundoff = False
                        pygame.mixer.music.play()
                    elif (pos[0] > 330 and pos[1] > 220) and (pos[0] < 475 and pos[1] < 265) or flag_play:
                        flag_play = True
                        try:
                                print(1212)
                                con = sqlite3.connect('films_db (1).sqlite')
                                cur = con.cursor()
                                resultlog = cur.execute(
                                    """SELECT u.login FROM users AS u WHERE u.login='{}'""".format(
                                        user_text)).fetchall()
                                resultpas = cur.execute(
                                    """SELECT u.password FROM users AS u WHERE u.login='{}'""".format(
                                        user_text)).fetchall()
                                resultid = cur.execute(
                                    """SELECT u.id FROM users AS u WHERE u.login='{}'""".format(
                                        user_text)).fetchall()
                                resultscore = cur.execute(
                                    """SELECT s.score FROM score AS s WHERE s.id_user='{}'""".format(
                                        resultid)).fetchall()
                                print('resss', resultlog)
                                print('ressssss', resultpas)
                                flag = False
                                print(resultpas, user_text1)
                                if not resultpas:
                                    flag = True
                                elif resultpas[0][0] == user_text1:
                                    print(11111111222222222222222222)
                                    playbutton = True
                                    if 275 < pos[0] < 545 and 400 < pos[1] < 545:
                                        startgame = True
                                        print(11111111222222222222222222)
                                        flag_login = False
                                        playbutton = False
                                        break
                                if flag:
                                    try:
                                        print(resultlog)
                                        if len(user_text) <= 8:
                                            print(1111111)
                                            text1 = 'Минимум 8 символов'

                                        elif user_text.lower() == user_text or user_text.upper() \
                                                == user_text:
                                            text1 = 'Должны присутствовать как заглавные, так и строчные буквы'

                                        #elif resultlog == resultlog:
                                            #raise SyntaxError(self.login_error.setText("Этот логин уже занят"))

                                        else:

                                            if len(user_text1) <= 8:
                                                text1 = 'Минимум 8 символов'

                                            elif user_text1.lower() == user_text1 or \
                                                    user_text1.upper() == user_text1:
                                                text1 = ('Должны присутствовать как заглавные, '
                                                         'так и строчные буквы')

                                            elif not any([i in user_text1 for i in list('0123456789')]):
                                                text1 = 'Цифры должны присутствовать'

                                            else:
                                                try:
                                                    if flag_uniq:
                                                        flag_uniq = False
                                                        con = sqlite3.connect('films_db (1).sqlite')
                                                        cur = con.cursor()
                                                        sqlite_insert_verbs = f"""INSERT INTO users
                                                                                  (login, password)
                                                                                  VALUES
                                                                                  ('{user_text}', '{user_text1}');"""
                                                        resultlog = [[user_text]]
                                                        resultpas = [[user_text1]]
                                                        resultid = cur.execute(
                                                            """SELECT u.id FROM users AS u WHERE u.login='{}'""".format(
                                                                user_text1)).fetchall()
                                                        print(sqlite_insert_verbs)
                                                        cur.execute(sqlite_insert_verbs)
                                                        con.commit()
                                                        print("Запись успешно вставлена в таблицу users", cur.rowcount)
                                                        playbutton = True
                                                except sqlite3.Error as error:
                                                    print("3, Ошибка при работе с SQLite", error)
                                                con.close()
                                    except sqlite3.Error as error:
                                        print("2, Ошибка при работе с SQLite", error)
                        except sqlite3.Error as error:
                            print("1, Ошибка при работе с SQLite", error)
            if event.type == pygame.KEYDOWN:
                print(999999)
                if event.key == pygame.K_BACKSPACE:
                    if active_log:
                        user_text = user_text[:-1]
                    if active_pas:
                        user_text1 = user_text1[:-1]
                else:
                    if active_log:
                        print(user_text)
                        user_text += event.unicode
                    if active_pas:
                        user_text1 += event.unicode
        screen.fill('pink')

        if active_log:
            color_log = color_active
        else:
            color_log = color_passive
        if active_pas:
            color_pas = color_active
        else:
            color_pas = color_passive
        pygame.draw.rect(screen, brown, (330, 215, 150, 50))
        draw_text(screen, 50, 395, 220, 'Войти')
        pygame.draw.rect(screen, brown, (50, 490, 50, 50))


        if soundon:

            imagesound = imagesoundon

        if soundoff:
            print(25)
            imagesound = imagesoundoff

        pygame.draw.rect(screen, color_log, input_rect)
        pygame.draw.rect(screen, color_pas, input_rect1)
        if active_log:
            text_surface = base_font.render(user_text, True, (0, 0, 0))
        else:
            text_surface = base_font.render("Логин", True, (0, 0, 0))
        if active_pas:
            text_surface1 = base_font.render(user_text1, True, (0, 0, 0))
        else:
            text_surface1 = base_font.render("Пароль", True, (0, 0, 0))
        if playbutton:
            pygame.draw.rect(screen, brown, (275, 400, 270, 120))
            draw_text(screen, 100, 410, 430, 'ИГРАТЬ')
        screen.blit(imagesound, (50, 490))
        screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
        screen.blit(text_surface1, (input_rect1.x + 5, input_rect1.y + 5))
        text_surface1 = base_font.render(text1, True, (0, 0, 0))
        screen.blit(text_surface1, (input_rect.x + 120, input_rect.y + 120))
        input_rect.w = max(100, text_surface.get_width() + 10)
        input_rect1.w = max(100, text_surface1.get_width() + 10)
        pygame.display.flip()
        clock.tick(60)

    if startgame:
        stopgame = True
        k += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    print(30)
                    pos = pygame.mouse.get_pos()
                    if pygame.mouse.get_pressed()[0] and ((pos[0] > 0 and pos[1] > 0) and
                                                        (pos[0] < 70 and pos[1] < 70)) and startgame and stopgame:
                        print(24)
                        stopgame = False
                        collide1 = True
                        enter = False
                        print('collide', collide1)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and enter:
                    pygame.mixer.music.unpause()
                    enter = False
                    k = 1
                    speed = 3
                    score = 0
                    all_sprites = pygame.sprite.Group()
                    all_sprites1 = pygame.sprite.Group()
                    Bunny(all_sprites)
                if event.key == pygame.K_LEFT and not enter:
                    for bunny in all_sprites:
                        bunny.update(True)
                if event.key == pygame.K_RIGHT and not enter:
                    for bunny in all_sprites:
                        bunny.update(False)
        if not enter:
            screen.blit(gamebackround, (0, 0))
            Hurdle(all_sprites1)
            all_sprites.draw(screen)
            all_sprites1.draw(screen)
            if stopgame:
                pygame.draw.rect(screen, 'pink', (0, 0, 70, 70))
                draw_text(screen, 30, 20, 20, 'Выход')

            if boardstart:
                board.render(screen)
            pygame.display.flip()
            clock.tick(speed)
            if k % 100 == 0:
                speed += 0.5
            score += 10
            for bunny in all_sprites:
                bunny.get_event()
            for hurdle in all_sprites1:
                hurdle.get_event()
            collide = pygame.sprite.groupcollide(all_sprites, all_sprites1, False, False)
            print(9767676, collide)
            if collide or collide1:
                stopgame = False
                collide1 = False
                boardstart = False
                pygame.mixer.music.pause()
                pygame.mixer.Sound.play(boom_sound)
                try:
                    con = sqlite3.connect('films_db (1).sqlite')
                    cur = con.cursor()
                    if not resultscore:
                        sqlite_insert_verbs = f"""INSERT INTO score(id_user, score)  VALUES('{resultid[0][0]}', '{score}')"""
                        cur.execute(sqlite_insert_verbs)
                        con.commit()
                        resultscore = [[score]]
                    if score > resultscore[0][0]:
                        print(score)
                        print(resultscore)
                        sqlite_insert_verbs = f"""UPDATE score SET score='{score}' WHERE id_user = '{resultid[0][0]}'"""
                        print(sqlite_insert_verbs)
                        cur.execute(sqlite_insert_verbs)
                        con.commit()
                        print("Запись успешно вставлена в таблицу score", cur.rowcount)
                        resultscore[0][0] = score
                except sqlite3.Error as error:
                    print("Ошибка при работе с SQLite", error)
                enter = True
                print(11111111111111)
                screen.blit(gamebackround, (0, 0))
                draw_text(screen, 100, 400, 250, 'ВЫ ПРОИГРАЛИ')
                draw_text(screen, 40, 400, 350, 'ВАШ РЕЗУЛЬТАТ: ' + str(score))
                draw_text(screen, 40, 400, 390, 'ВАШ РЕКОРД: ' + str(resultscore[0][0]))
                draw_text(screen, 40, 400, 420, 'Нажмите space, чтобы продолжить')
                board.render(screen)
                pygame.display.flip()
