import pygame
import pygame_gui
import sys
from .utils import Color, Board, DropDownWithCaption
from pygame_gui.elements import UIButton
from pygame_gui.elements.ui_selection_list import UISelectionList


class GUI:
    size = width, height = 800, 800
    elements = []

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        self.ui_manager = pygame_gui.UIManager(self.size)
        self.clock = pygame.time.Clock()
        self.build()
        
        self.board = Board(self.screen, 80, 40)

    def update(self, board_state, possible_moves):
        time_delta = self.clock.tick(60) / 1000.0
        self.process_events()
        self.ui_manager.update(time_delta)
        self.screen.fill(Color.BROWN.value)

        self.board.draw(board_state, possible_moves)
        self.pick_start_dropdown.draw()
        
        self.ui_manager.draw_ui(self.screen)
        pygame.display.update()

    def build(self):
        self.play_button = UIButton(
            relative_rect=pygame.Rect((350, 700), (100, 50)),
            text='GRAJ',
            manager=self.ui_manager
        )
        self.pick_start_dropdown = DropDownWithCaption(
            self.screen, self.ui_manager, 100, 700,
            options_list=['gracz', 'komputer'],
            starting_option='gracz',
            caption='Grę zaczyna'
        )

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == self.play_button:
                        print('Hello World!')
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(self.board.is_clicked(*pygame.mouse.get_pos()))

            self.ui_manager.process_events(event)