import pygame
import pygame_gui
import sys
from .utils import Color, Board, DropDownWithCaption, Timer, TextBoxWithCaption
from .utils import draw_arrow
from pygame_gui.elements import UIButton
from typing import List
from app.game_state import GameState, Player, Property

""" Class handling app's GUI behaviour """
class GUI:
    def __init__(self, game_state: GameState):
        self.game_state = game_state
        pygame.init()
        self.size  = 800, 800
        self.screen = pygame.display.set_mode(self.size)
        self.ui_manager = pygame_gui.UIManager(self.size) # handles some of the GUI elements (buttons, dropdowns, ...)
        self.clock = pygame.time.Clock() # this is needed for UIManager
        pygame.time.set_timer(pygame.USEREVENT+1, 1000) # schedule a custom timer event
        self.__build() # build GUI

    """ Updates GUI state """
    def update(self):
        time_delta = self.clock.tick(60) / 1000.0
        self.screen.fill(Color.BROWN.value)
        self.__process_events()
        self.ui_manager.update(time_delta)
        self.player1_dropdown.set_caption("GRACZ1: " + str(self.game_state.get_points(Player.Player1)))
        self.player2_dropdown.set_caption("GRACZ2: " + str(self.game_state.get_points(Player.Player2)))

    """ Draw GUI elements """
    def draw(self):
        self.board.draw(self.game_state.get_board_state(), self.game_state.get_valid_moves())
        self.player1_dropdown.draw()
        self.player1_textbox.draw()
        self.player2_dropdown.draw()
        self.player2_textbox.draw()
        self.game_timer.draw()
        # draw an arrow pointing to player's name if it is their turn
        if self.game_state.get_turn() == Player.Player1:
            draw_arrow(self.screen, 340, 720, -10, 5)
        else:
            draw_arrow(self.screen, 460, 720, 10, 5)
        self.ui_manager.draw_ui(self.screen)
        pygame.display.update()

    """ Builds GUI elements """
    def __build(self):
        self.board = Board(self.screen, 80, 40)
        self.play_button = UIButton(
            relative_rect=pygame.Rect((350, 700), (100, 50)),
            text='START',
            manager=self.ui_manager
        )
        self.player1_dropdown = DropDownWithCaption(
            self.screen, self.ui_manager, 80, 700,
            options_list=['człowiek', 'komputer'],
            starting_option='człowiek',
            caption_text='Gracz1: 0'
        )
        self.player1_textbox = TextBoxWithCaption(self.screen, self.ui_manager, 220, 700, "d")
        self.player2_dropdown = DropDownWithCaption(
            self.screen, self.ui_manager, 580, 700,
            options_list=['człowiek', 'komputer'],
            starting_option='człowiek',
            caption_text='Gracz2: 0'
        )
        self.player2_textbox = TextBoxWithCaption(self.screen, self.ui_manager, 720, 700, "d")
        self.game_timer = Timer(self.screen, self.ui_manager, 370, 10)

    """ Processes GUI events (button and tile clicks) """
    def __process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == self.play_button:
                        self.__update_game_properties()
                        self.game_state.restart()
                        self.game_timer.reset()
                        self.game_timer.start()

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.game_state.add_move(self.board.is_clicked(*pygame.mouse.get_pos()))

            # timer event
            if event.type == pygame.USEREVENT+1:
                self.game_timer.tick()

            self.ui_manager.process_events(event)

    def __update_game_properties(self):
        player1_depth = 0
        player2_depth = 0
        try:
            player1_depth = int(self.player1_textbox.get_text())
            player2_depth = int(self.player2_textbox.get_text())
        except:
            pass
        self.game_state.set_player_property(Player.Player1, Property.DEPTH, player1_depth)
        self.game_state.set_player_property(Player.Player2, Property.DEPTH, player2_depth)
