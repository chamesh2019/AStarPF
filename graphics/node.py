import pygame
from math import sqrt

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)
GREEN = (0, 255, 0)
TURQUISE = (63, 224, 208)
PURPLE = (128, 0, 128)
GRAY = (128, 128, 128)
YELLOW = (255, 255, 0)


class Node:
    def __init__(self, row, col, width):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neibours = []
        self.width = width
        self.g_cost = 9999999
        self.h_cost = 9999999
        self.f_cost = 9999999
        self.font = pygame.font.SysFont("Arial", 10)
        # self.total_rows = total_rows

    def get_pos(self):
        return (self.row, self.col)

    def is_closed(self):
        return self.color == RED

    def is_open(self):
        return self.color == GREEN

    def is_barrier(self):
        return self.color == BLACK

    def is_start(self):
        return self.color == ORANGE

    def is_end(self):
        return self.color == TURQUISE

    def switch(self):
        self.color = BLACK if self.color == WHITE else WHITE

    def make_closed(self):
        self.color = RED

    def make_open(self):
        self.color = GREEN

    def make_start(self):
        self.color = ORANGE
        self.g_cost = 0
        self.h_cost = 9999
        self.f_cost = 9999

    def make_end(self):
        self.color = TURQUISE

    def make_path(self):
        self.color = PURPLE

    def draw(self, win):
        pygame.draw.rect(
            win, self.color, (self.x, self.y, self.width, self.width)
        )

    def update_neibours(self, grid, rows, start, end):
        index = grid.index(self)
        self.neibours = []
        try:
            if (not grid[index - 1].is_barrier()
                    and not grid[index - 1].is_closed()):
                self.neibours.append(grid[index - 1])
        except IndexError:
            pass

        try:
            if (not grid[index + 1].is_barrier()
                    and not grid[index + 1].is_closed()):
                self.neibours.append(grid[index + 1])
        except IndexError:
            pass

        try:
            if (not grid[index - rows].is_barrier()
                    and not grid[index - rows].is_closed()):
                self.neibours.append(grid[index - rows])
        except IndexError:
            pass

        try:
            if (not grid[index + rows].is_barrier()
                    and not grid[index + rows].is_closed()):
                self.neibours.append(grid[index + rows])
        except IndexError:
            pass

        # try:
        #     if (not grid[index + rows - 1].is_barrier()
        #             and not grid[index + rows - 1].is_closed()):
        #         self.neibours.append(grid[index + rows - 1])
        # except IndexError:
        #     pass

        # try:
        #     if (not grid[index + rows + 1].is_barrier()
        #             and not grid[index + rows + 1].is_closed()):
        #         self.neibours.append(grid[index + rows + 1])
        # except IndexError:
        #     pass

        # try:
        #     if (not grid[index - rows - 1].is_barrier()
        #             and not grid[index - rows - 1].is_closed()):
        #         self.neibours.append(grid[index - rows - 1])
        # except IndexError:
        #     pass

        # try:
        #     if (not grid[index - rows + 1].is_barrier()
        #             and not grid[index - rows + 1].is_closed()):
        #         self.neibours.append(grid[index - rows + 1])
        # except IndexError:
        #     pass

        for node in self.neibours:
            grid[grid.index(node)].make_open()
            grid[grid.index(node)].h_cost = calculate_distance(node, end)
            grid[grid.index(node)].g_cost = self.g_cost + 1
            grid[grid.index(node)].f_cost = (grid[grid.index(node)].g_cost
                                             + grid[grid.index(node)].h_cost)

    def closed_neibours(self, grid, rows):
        index = grid.index(self)
        closed_neibours = []
        try:
            if grid[index - 1].is_closed():
                closed_neibours.append(grid[index - 1])
        except IndexError:
            pass

        try:
            if grid[index + 1].is_closed():
                closed_neibours.append(grid[index + 1])
        except IndexError:
            pass

        try:
            if grid[index - rows].is_closed():
                closed_neibours.append(grid[index - rows])
        except IndexError:
            pass

        try:
            if grid[index + rows].is_closed():
                closed_neibours.append(grid[index + rows])
        except IndexError:
            pass

        # try:
        #     if grid[index + rows - 1].is_closed():
        #         closed_neibours.append(grid[index + rows - 1])
        # except IndexError:
        #     pass

        # try:
        #     if grid[index + rows + 1].is_closed():
        #         closed_neibours.append(grid[index + rows + 1])
        # except IndexError:
        #     pass

        # try:
        #     if grid[index - rows - 1].is_closed():
        #         closed_neibours.append(grid[index - rows - 1])
        # except IndexError:
        #     pass

        # try:
        #     if grid[index - rows + 1].is_closed():
        #         closed_neibours.append(grid[index - rows + 1])
        # except IndexError:
        #     pass
        return closed_neibours

    def __str__(self):
        return f"node {self.row, self.col, self.g_cost}"

    def __repr__(self):
        return f"node {self.row, self.col, self.g_cost}"

    def __lt__(self, other):
        return False


def calculate_distance(point1, point2):
    return abs(point2.row - point1.row) + abs(point2.col - point1.col)
