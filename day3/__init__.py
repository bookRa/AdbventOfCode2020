

from typing import List
import logging


def toboggan_1(horiz_speed:int, vert_speed:int, course:List[str]) -> int:
    x, y = 0, 0
    trees = 0
    minlen = len(course[0])
    while y < len(course):
        if course[y][x] == '#':
            logging.debug(course[y])
            logging.debug(f"encountered tree at pos[{y}][{x}]")
            trees +=1
        x = (x+horiz_speed) % minlen
        y += vert_speed
    return trees