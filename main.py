import pygame
import time
from graphics.node import Node, BLACK, GRAY
from algorithm.functions import algorithm, get_start, get_end

WIDTH = 600
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A Star Algorithm")
pygame.init()


def make_grid(rows):
    width = WIDTH / rows
    grid = []
    for index in range(rows * rows):
        tem_node = Node(index % rows, index // rows, width)
        grid.append(tem_node)
    for node in grid:
        if node.col == rows - 1 or node.col == 0:
            node.switch()
        if node.row == rows - 1 or node.row == 0:
            node.switch()
    return grid


def draw_grid(win, rows):
    width = WIDTH / rows
    for index in range(rows):
        pygame.draw.line(win, GRAY, (0, index * width), (WIDTH, index * width))
        pygame.draw.line(win, GRAY, (index * width, 0), (index * width, WIDTH))


def draw(win, grid, rows):
    win.fill(BLACK)

    for spot in grid:
        spot.draw(win)

    draw_grid(win, rows)
    pygame.display.update()


def main(win, rows):
    width = WIDTH / rows
    grid = make_grid(rows)

    run = True
    started = False
    drag = False
    changed = []

    got_start = False

    while run:
        draw(win, grid, rows)

        if started:
            if not got_start:
                start = get_start(grid)
                grid[grid.index(start)].make_open()
                end = get_end(grid)
                got_start = True

            if algorithm(grid, start, end, rows):
                started = False
            # time.sleep(0.1)
            continue

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


            if (pygame.mouse.get_pressed()[0]
                    and event.type == pygame.MOUSEBUTTONDOWN):

                drag = True
                mouse_x, mouse_y = pygame.mouse.get_pos()
                index = int((mouse_x // width) + (mouse_y // width) * rows)
                grid[index].switch()
                changed.append(index)

            if event.type == pygame.MOUSEMOTION and drag:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                index = int((mouse_x // width) + (mouse_y // width) * rows)
                if index not in changed:
                    grid[index].switch()
                    changed.append(index)

            if event.type == pygame.MOUSEBUTTONUP:
                drag = False
                changed = []

            if pygame.mouse.get_pressed()[1]:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                index = int((mouse_x // width) + (mouse_y // width) * rows)
                grid[index].make_start()

            if pygame.mouse.get_pressed()[2]:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                index = int((mouse_x // width) + (mouse_y // width) * rows)
                grid[index].make_end()

            if (event.type == pygame.KEYDOWN
                and event.key == pygame.K_RETURN):
                started = True


if __name__ == '__main__':
    main(WIN, 20)
