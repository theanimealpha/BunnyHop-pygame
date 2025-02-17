import sys
import pygame
import colorsys

def main():
    # 1. Считываем входные данные из stdin
    try:
        line = sys.stdin.read().strip()
        parts = line.split()
        if len(parts) != 2:
            raise ValueError
        W_str, Hue_str = parts
        W = int(W_str)
        Hue = int(Hue_str)
    except ValueError:
        print("Неправильный формат ввода")
        return

    # 2. Проверяем условия:
    #  - W кратно 4
    #  - W <= 100
    #  - 0 <= Hue <= 360
    if (W % 4 != 0) or (W > 100) or (Hue < 0) or (Hue > 360):
        print("Неправильный формат ввода")
        return

    # 3. Инициализируем Pygame и создаём окно 300x300
    pygame.init()
    screen = pygame.display.set_mode((300, 300))
    pygame.display.set_caption("Изометрический куб")

    # Задаём фон (например, белый)
    screen.fill((255, 255, 255))

    # 4. Функция для перевода HSV (0..1) в RGB (0..255)
    #   используем модуль colorsys, где Hue, Sat, Val находятся в диапазоне [0,1].
    def hsv_to_rgb255(h, s, v):
        # colorsys принимает Hue от 0 до 1 (а у нас Hue от 0 до 360)
        # поэтому делим Hue на 360
        r, g, b = colorsys.hsv_to_rgb(h / 360, s, v)
        return (int(r * 255), int(g * 255), int(b * 255))

    # 5. Получаем нужные три цвета (яркости 1.0, 0.75, 0.5, насыщенность 1.0)
    color_top    = hsv_to_rgb255(Hue, 1.0, 1.0)
    color_front  = hsv_to_rgb255(Hue, 1.0, 0.75)
    color_side   = hsv_to_rgb255(Hue, 1.0, 0.5)

    # 6. Вычисляем координаты вершин куба.
    #    Центр окна (150, 150). Пусть передняя грань — квадрат со стороной W,
    #    центрированный относительно (150,150).
    cx, cy = 150, 150
    half = W // 2

    # Передняя грань (A-B-D-C)
    #  A = нижняя-левая вершина
    #  B = нижняя-правая
    #  C = верхняя-левая
    #  D = верхняя-правая
    A = (cx - half, cy + half)
    B = (cx + half, cy + half)
    C = (cx - half, cy - half)
    D = (cx + half, cy - half)

    # Смещение дальних вершин по осям X, Y на +W/2
    shift_x = half
    shift_y = half

    # "Дальние" (верхние) вершины (A', B', C', D') = (A, B, C, D) + (shift_x, shift_y)
    A_ = (A[0] + shift_x, A[1] + shift_y)
    B_ = (B[0] + shift_x, B[1] + shift_y)
    C_ = (C[0] + shift_x, C[1] + shift_y)
    D_ = (D[0] + shift_x, D[1] + shift_y)

    top_face = [A_, B_, D_, C_]
    side_face  = [B, B_, D_, D]
    front_face = [A, B, D, C]

    # 8. Рисуем сначала верхнюю грань, потом боковую, потом переднюю
    pygame.draw.polygon(screen, color_top,   top_face)
    pygame.draw.polygon(screen, color_side,  side_face)
    pygame.draw.polygon(screen, color_front, front_face)

    # Обновляем отображение
    pygame.display.flip()

    # 9. Главный цикл приложения, чтобы окно не закрылось сразу
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()