import bisect
import string
from abc import ABC, abstractmethod
from typing import Optional

from django.conf import settings


class AbstractGrid(ABC):
    enabled = False

    @abstractmethod
    def get_cell_for_point(self, x, y) -> Optional[str]:
        pass

    @abstractmethod
    def get_cells_for_bounds(self, bounds) -> Optional[str]:
        pass


class Grid(AbstractGrid):
    enabled = True

    def __init__(self, rows, cols):
        rows = tuple(float(y) for y in rows)
        cols = tuple(float(x) for x in cols)
        self.rows = tuple(sorted(rows))
        self.cols = tuple(sorted(cols))

        if self.rows == rows:
            self.invert_y = False
        elif self.rows == tuple(reversed(rows)):
            self.invert_y = True
        else:
            raise ValueError('row coordinates are not ordered')

        if self.cols == cols:
            self.invert_x = False
        elif self.cols == tuple(reversed(cols)):
            self.invert_x = True
        else:
            raise ValueError('column coordinates are not ordered')

    def get_cell_for_point(self, x, y):
        x = bisect.bisect(self.cols, x)
        if x <= 0 or x >= len(self.cols):
            return None

        y = bisect.bisect(self.rows, y)
        if y <= 0 or y >= len(self.rows):
            return None

        if self.invert_x:
            x = len(self.cols) - x
        if self.invert_y:
            y = len(self.rows) - y

        return '%s%d' % (string.ascii_uppercase[x-1], y)

    def get_cells_for_bounds(self, bounds):
        minx, miny, maxx, maxy = bounds

        if self.invert_x:
            minx, maxx = maxx, minx
        if self.invert_y:
            miny, maxy = maxy, miny

        min_cell = self.get_cell_for_point(minx, miny)
        max_cell = self.get_cell_for_point(maxx, maxy)

        if not min_cell or not max_cell:
            return None

        if min_cell == max_cell:
            return min_cell
        return '%s-%s' % (min_cell, max_cell)


class DummyGrid(AbstractGrid):
    def get_cell_for_point(self, x, y):
        return None

    def get_cells_for_bounds(self, bounds):
        return None


if settings.GRID_COLS and settings.GRID_ROWS:
    grid = Grid(settings.GRID_ROWS.split(','), settings.GRID_COLS.split(','))
else:
    grid = DummyGrid()
