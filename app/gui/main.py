import pygame
import pygame_gui
import sys
from .utils import Color, Board, DropDownWithCaption
from pygame_gui.elements import UIButton
from typing import List
from app.game_state import GameState

""" Class handling app's GUI behaviour """
class GUI:
    def __init__(self, game_state: GameState):
        self.game_state = game_state
        pygame.init()
        self.size  = 800, 800
        self.screen = pygame.display.set_mode(self.size)
        self.ui_manager = pygame_gui.UIManager(self.size) # handles some of the GUI elements (buttons, dropdowns, ...)
        self.clock = pygame.time.Clock() # this is needed for UIManager
        self.build() # build GUI

    """ Updates GUI state then draws its elements """
    def update(self):
        time_delta = self.clock.tick(60) / 1000.0
        self.screen.fill(Color.BROWN.value)

        self.process_events()
        self.ui_manager.update(time_delta)

        self.board.draw(self.game_state.get_board_state(), self.game_state.get_valid_moves())
        self.pick_start_dropdown.draw()

        self.ui_manager.draw_ui(self.screen)
        pygame.display.update()

    """ Builds GUI elements """
    def build(self):
        self.board = Board(self.screen, 80, 40)
        self.play_button = UIButton(
            relative_rect=pygame.Rect((350, 700), (100, 50)),
            text='START',
            manager=self.ui_manager
        )
        self.pick_start_dropdown = DropDownWithCaption(
            self.screen, self.ui_manager, 100, 700,
            options_list=['gracz', 'komputer'],
            starting_option='gracz',
            caption='Grę zaczyna'
        )

    """ Processes GUI events (button and tile clicks) """
    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == self.play_button:
                        self.game_state.started()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.game_state.add_move(self.board.is_clicked(*pygame.mouse.get_pos()))

            self.ui_manager.process_events(event)
