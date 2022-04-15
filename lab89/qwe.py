import pygame

pygame.init()
Width, Height = 800, 800
lastPos = (0, 0)
screen = pygame.display.set_mode((Width, Height))
prev, cur = None, None
drawing = False
start_pos = 0
end_pos = 0
game_over = True
FPS = 30
color = 'black'
clock = pygame.time.Clock()
screen.fill('white')
mode = 'pen'
pygame.display.set_caption('Paint')


def clear():
    screen.fill('white')


def circle(screen, color, start, end):
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    radius = abs(x1 - x2) / 2
    pygame.draw.circle(screen, color, (x, y), radius, 15)
    print(x1, x2, y1, y2)


def rect(screen, color, start, end):

    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]

    widthr = abs(x1 - x2)
    height = abs(y1 - y2)
    if x2 > x1 and y2 > y1:
        pygame.draw.rect(screen, color, (x1, y1, widthr, height), 3)
    if y2 > y1 and x1 > x2:
        pygame.draw.rect(screen, color, (x2, y1, widthr, height), 3)
    if x1 > x2 and y1 > y2:
        pygame.draw.rect(screen, color, (x2, y2, widthr, height), 3)
    if x2 > x1 and y1 > y2:
        pygame.draw.rect(screen, color, (x1, y2, widthr, height), 3)


def sq(screen, color, start, end):
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    mn = min(abs(x2 - x1), abs(y2 - y1))

    if x2 > x1 and y2 > y1:
        pygame.draw.rect(screen, color, (x1, y1, mn, mn))
    if y2 > y1 and x1 > x2:
        pygame.draw.rect(screen, color, (x2, y1, mn, mn))
    if x1 > x2 and y1 > y2:
        pygame.draw.rect(screen, color, (x2, y2, mn, mn))
    if x2 > x1 and y1 > y2:
        pygame.draw.rect(screen, color, (x1, y2, mn, mn))


def right_triangle(screen, color, start, end):
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]

    if x2 > x1 and y2 > y1:
        pygame.draw.polygon(screen, color, ((x1, y1), (x2, y2), (x1, y2)))
    if y2 > y1 and x1 > x2:
        pygame.draw.polygon(screen, color, ((x1, y1), (x2, y2), (x1, y2)))
    if x1 > x2 and y1 > y2:
        pygame.draw.polygon(screen, color, ((x1, y1), (x2, y2), (x2, y1)))
    if x2 > x1 and y1 > y2:
        pygame.draw.polygon(screen, color, ((x1, y1), (x2, y2), (x2, y1)))


def equilateral_triangle(screen, color, start, end):
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]

    width_b = abs(x2 - x1)
    height = (3 ** 0.5) * width_b / 2

    if y2 > y1:
        pygame.draw.polygon(screen, color, ((x1, y2), (x2, y2), ((x1 + x2) / 2, y2 - height)), 15)
    else:
        pygame.draw.polygon(screen, color, ((x1, y1), (x2, y1), ((x1 + x2) / 2, y1 - height)))


def rhombus(screen, color, start, end):
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    pygame.draw.lines(screen, pygame.Color(color), True,
                      (((x1 + x2) / 2, y1), (x1, (y1 + y2) / 2), ((x1 + x2) / 2, y2), (x2, (y1 + y2) / 2)), 15)


while game_over:
    mouse_movement = pygame.mouse.get_pos()

    print(mouse_movement)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = False
        if event.type == pygame.MOUSEBUTTONDOWN and mouse_movement[0] >= 725 and mouse_movement[1] <= 75 and \
                mouse_movement[0] <= 750 and mouse_movement[1] >= 45:
            mode = 'pen'
        if event.type == pygame.MOUSEBUTTONDOWN and mouse_movement[0] >= 400 and mouse_movement[1] <= 70 and \
                mouse_movement[0] <= 420 and mouse_movement[1] >= 50:
            clear()
        if event.type == pygame.MOUSEBUTTONDOWN and mouse_movement[0] >= 460 and mouse_movement[1] <= 70 and \
                mouse_movement[
                    0] <= 480 and mouse_movement[1] >= 50:
            color = 'white'
        if event.type == pygame.MOUSEBUTTONDOWN and mouse_movement[0] >= 520 and mouse_movement[1] <= 70 and \
                mouse_movement[
                    0] <= 540 and mouse_movement[1] >= 50:
            color = 'yellow'
        if event.type == pygame.MOUSEBUTTONDOWN and mouse_movement[0] >= 580 and mouse_movement[1] <= 70 and \
                mouse_movement[
                    0] <= 600 and mouse_movement[1] >= 50:
            color = 'green'
        if event.type == pygame.MOUSEBUTTONDOWN and mouse_movement[0] >= 640 and mouse_movement[1] <= 70 and \
                mouse_movement[
                    0] <= 660 and mouse_movement[1] >= 50:
            color = 'blue'
        if event.type == pygame.MOUSEBUTTONDOWN and mouse_movement[0] >= 700 and mouse_movement[1] <= 70 and \
                mouse_movement[
                    0] <= 720 and mouse_movement[1] >= 50:
            color = 'red'
        if event.type == pygame.MOUSEBUTTONDOWN and mouse_movement[0] >= 340 and mouse_movement[1] <= 70 and \
                mouse_movement[0] <= 360 and mouse_movement[1] >= 50:
            color = 'black'
        if event.type == pygame.MOUSEBUTTONDOWN and mouse_movement[0] >= 260 and mouse_movement[1] <= 70 and \
                mouse_movement[0] <= 300 and mouse_movement[1] >= 30:
            mode = 'circle'
        if event.type == pygame.MOUSEBUTTONDOWN and mouse_movement[0] >= 220 and mouse_movement[1] <= 70 and \
                mouse_movement[0] <= 240 and mouse_movement[1] >= 50:
            mode = 'sq'
        if event.type == pygame.MOUSEBUTTONDOWN and mouse_movement[0] >= 110 and mouse_movement[1] <= 70 and \
                mouse_movement[0] <= 140 and mouse_movement[1] >= 40:
            mode = 'right_triangle'
        if event.type == pygame.MOUSEBUTTONDOWN and mouse_movement[0] >= 65 and mouse_movement[1] <= 65 and \
                mouse_movement[0] <= 95 and mouse_movement[1] >= 40:
            mode = 'equilateral_triangle'
        if event.type == pygame.MOUSEBUTTONDOWN and mouse_movement[0] >= 30 and mouse_movement[1] <= 50 and \
                mouse_movement[0] <= 50 and mouse_movement[1] >= 45:
            mode = 'rect'
        if event.type == pygame.MOUSEBUTTONDOWN and mouse_movement[0] >= 160 and mouse_movement[1] <= 80 and \
               mouse_movement[0] <= 200 and mouse_movement[1] >= 40:
           mode = 'rhombus'
        if event.type == pygame.MOUSEBUTTONDOWN:#мышка была зажата
            drawing = True
            prev = mouse_movement
            start_pos = mouse_movement
        if event.type == pygame.MOUSEBUTTONUP:#мышка была отпущена
            drawing = False
            end_pos = mouse_movement# записываем конец нажатия мышки
            if mode == 'rect':
                rect(screen, color, start_pos, end_pos)
            elif mode == 'circle':
                circle(screen, color, start_pos, end_pos)
            elif mode == 'right_triangle':
                right_triangle(screen, color, start_pos, end_pos)
            elif mode == 'equilateral_triangle':
                equilateral_triangle(screen, color, start_pos, end_pos)
            elif mode == 'rhombus':
                rhombus(screen, color, start_pos, end_pos)
            elif mode == 'sq':
                 sq(screen, color,start_pos, end_pos)
        if event.type == pygame.MOUSEMOTION and drawing and mode == 'pen':
            cur = pygame.mouse.get_pos()
            if prev:
                pygame.draw.line(screen, color, prev, cur, 5)
                prev = cur

        pygame.draw.line(screen, 'beige', (750, 60), (725, 60), 30)
        pygame.draw.rect(screen, 'red', (700, 50, 20, 20))
        pygame.draw.rect(screen, 'blue', (640, 50, 20, 20))
        pygame.draw.rect(screen, 'green', (580, 50, 20, 20))
        pygame.draw.rect(screen, 'yellow', (520, 50, 20, 20))
        pygame.draw.rect(screen, 'alice blue', (460, 50, 20, 20))
        pygame.draw.rect(screen, 'lavender', (400, 50, 20, 20))
        pygame.draw.rect(screen, 'black', (340, 50, 20, 20))
        pygame.draw.circle(screen, 'beige', (280, 50), 20)  # circle
        pygame.draw.rect(screen, 'beige', (220, 50, 20, 20))  # sq
        pygame.draw.lines(screen, 'beige', True, ((180, 80), (160, 60), (180, 40), (200, 60)), 8)  # rhomb
        pygame.draw.polygon(screen, 'beige', ((110, 40), (110, 70), (140, 70)))# right_triangle
        pygame.draw.polygon(screen, 'beige', ((65, 50), (95, 65), (80, 40)))#equilateral_triangle
        pygame.draw.rect(screen, 'beige', (30, 45, 10, 20))#rect


    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()