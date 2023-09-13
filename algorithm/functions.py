import random
import time


def get_start(grid):
    start = [node for node in grid if node.is_start()]
    if start:
        return start[0]


def get_end(grid):
    end = [node for node in grid if node.is_end()]
    if end:
        return end[0]


def algorithm(grid, start, end, rows):
    open_nodes = [node for node in grid if node.is_open()]
    choices = select_minimum_f_cost(open_nodes)
    choices = select_minimum_h_cost(choices)
    selected = random.choice(choices)
    grid[grid.index(selected)].make_closed()

    grid[grid.index(selected)].update_neibours(grid, rows, start, end)

    if selected == end:
        grid[grid.index(end)].make_end()
        draw_path(grid, start, end, rows)
        grid[grid.index(start)].make_start()

        return True
    return False


def select_minimum_f_cost(arr):
    minimum = 9999999
    for node in arr:
        if node.f_cost <= minimum:
            minimum = node.f_cost
    return [node for node in arr if node.f_cost == minimum]


def select_minimum_h_cost(arr):
    minimum = 9999999
    for node in arr:
        if node.h_cost <= minimum:
            minimum = node.h_cost
    return [node for node in arr if node.h_cost == minimum]


def select_minimum_g_cost(arr):
    minimum = 9999999
    for node in arr:
        if node.g_cost <= minimum:
            minimum = node.g_cost
    return [node for node in arr if node.g_cost == minimum]


def draw_path(grid, start, end, rows):
    if end == start:
        return True

    path_nodes = [node for node in end.closed_neibours(grid, rows)]
    try:
        path_node = select_minimum_g_cost(path_nodes)
        path_node = path_node[0]
        grid[grid.index(path_node)].make_path()
    except IndexError:
        return True
    return draw_path(grid, start, path_node, rows)
