import enum
import pygame
from typing import List
from typing import NewType

class Color(enum.Enum):
    NO_COLOR = -1
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BG_GREEN = (0, 128, 0)

class Board:
    class Tile:
        def __init__(self, screen, x, y, color: Color = Color.NO_COLOR):
            self.screen = screen
            self.x = x
            self.y = y
            self.color = color
            self.rect = (
                self.x - Board.tile_size + Board.tile_border_size,
                self.y - Board.tile_size + Board.tile_border_size,
                2*Board.tile_size - 2*Board.tile_border_size,
                2*Board.tile_size - 2*Board.tile_border_size
            )
            self.border_rect = (
                self.x - Board.tile_size,
                self.y - Board.tile_size,
                2 * Board.tile_size,
                2 * Board.tile_size
            )

        def draw(self):
            if self.color != Color.NO_COLOR:
                pygame.draw.rect(self.screen, Color.BLACK.value, self.border_rect)
                pygame.draw.rect(self.screen, Color.BG_GREEN.value, self.rect)
                pygame.draw.circle(self.screen, self.color.value, (self.x, self.y), Board.tile_size - Board.tile_padding)

    tile_size = 40
    tile_padding = 5
    tile_border_size = 2
    rows = 8
    columns = 8

    def __init__(self, screen, board_x = 0, board_y = 0):
        self.tiles = [
            [
                Board.Tile(
                    screen,
                    board_x + (2*c + 1) * self.tile_size,
                    board_y + (2*r + 1) * self.tile_size,
                    Color.BLACK
                )
                for c in range(self.columns)
            ]
            for r in range (self.rows)
        ]

    def draw(self):
        for row in self.tiles:
            for tile in row:
                tile.draw()






