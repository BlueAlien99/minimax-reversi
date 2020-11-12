import enum
import pygame
from typing import List
import pygame.freetype
from pygame_gui.elements.ui_drop_down_menu import UIDropDownMenu


class Color(enum.Enum):
    NO_COLOR = -1
    BLACK = "#212121"
    WHITE = "#f5f5f5"
    GREEN = "#388e3c"
    ORANGE = "#ffc107"
    BROWN = "#795548"

""" Different states of the board tile
        UNCHECKED -- tile is unchecked (GREEN)
        BLACK -- checked black
        WHITE -- checked white """
class State(enum.Enum):
    UNCHECKED = 0
    BLACK = 1
    WHITE = 2

""" Represents tiled game board """
class Board():
    """ Represenst single board tile """
    class Tile:
        """
        big_rect is always black it is used to display border around tiles
        if tile is in POSSIBLE_CHECK state:
            * normal_rect is orange
            * small rect is green
        else:
            * normal_rect is green
            * small_rect is not displayed
        """
        def __init__(self, screen, x: int, y: int):
            self.screen = screen
            self.x = x
            self.y = y
            self.big_rect = pygame.Rect(
                self.x - Board.tile_size,
                self.y - Board.tile_size,
                2 * Board.tile_size,
                2 * Board.tile_size
            )
            self.normal_rect = pygame.Rect(
                self.x - Board.tile_size + Board.tile_b_size,
                self.y - Board.tile_size + Board.tile_b_size,
                2 * Board.tile_size - 2 * Board.tile_b_size,
                2 * Board.tile_size - 2 * Board.tile_b_size
            )
            self.small_rect = pygame.Rect(
                self.x - Board.tile_size + Board.tile_b_size2,
                self.y - Board.tile_size + Board.tile_b_size2,
                2 * Board.tile_size - 2 * Board.tile_b_size2,
                2 * Board.tile_size - 2 * Board.tile_b_size2
            )

        """ Draws a tile """
        def draw(self, state: State, is_possible_check: bool):
            pygame.draw.rect(self.screen, Color.BLACK.value, self.big_rect)

            if is_possible_check:
                pygame.draw.rect(self.screen, Color.ORANGE.value, self.normal_rect)
                pygame.draw.rect(self.screen, Color.GREEN.value, self.small_rect)
            else:
                pygame.draw.rect(self.screen, Color.GREEN.value, self.normal_rect)

            if (state == State.BLACK):
                pygame.draw.circle(self.screen, Color.BLACK.value, (self.x, self.y),
                                   Board.tile_size - Board.tile_padding)
            elif (state == State.WHITE):
                pygame.draw.circle(self.screen, Color.WHITE.value, (self.x, self.y),
                                   Board.tile_size - Board.tile_padding)

        """ Returns True if tile was clicked """
        def is_clicked(self, x, y):
            return self.big_rect.collidepoint((x, y))

    tile_size = 40
    tile_padding = 10
    # outer tile border size
    tile_b_size = 2
    # border size of the orange indicator displayed when there is possible move on the tile
    tile_b_size2 = 6
    rows = 8
    cols = 8

    """ Creates tiled board of size 8x8 """
    def __init__(self, screen, board_x = 0, board_y = 0):
        self.tiles = [
            [
                Board.Tile(screen, board_x + (2 * c + 1) * self.tile_size, board_y + (2 * r + 1) * self.tile_size)
                for c in range(self.cols)
            ]
            for r in range(self.rows)
        ]

    def draw(self, board_state, valid_moves):
        y = 0
        for row in self.tiles:
            x = 0
            for tile in row:
                tile.draw(State(board_state[x][y]), valid_moves[x][y] < 0)
                x += 1
            y += 1

    """ Checks if any tile was clicked
            If a tile was clicked returns its coordinates
            Returns (-1, -1) otherwise """
    def is_clicked(self, mouse_x, mouse_y) -> (int, int):
        y = 0
        for row in self.tiles:
            x = 0
            for tile in row:
                if tile.is_clicked(mouse_x, mouse_y):
                    return x, y
                x += 1
            y += 1
        return -1, -1


""" Helper class aggregating dropdown list with caption """
class DropDownWithCaption:
    def __init__(self, screen, ui_manager, x: int, y: int, options_list: List[str], starting_option: str, caption: str):
        font = pygame.freetype.SysFont('Comic Sans MS', 24)
        self.x = x
        self.y = y
        self.screen = screen
        self.text_surface, rect = font.render(caption, (0, 0, 0))
        self.dropdown = UIDropDownMenu(options_list=options_list,
                                       starting_option=starting_option,
                                       relative_rect=pygame.Rect((x, y + 24), (140, 40)),
                                       manager=ui_manager)

    def draw(self):
        self.screen.blit(self.text_surface, (self.x, self.y))

""" Timer helper class """
class Timer:
    def __init__(self, screen):
        pass
