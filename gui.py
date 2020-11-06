import pygame
import pygame_gui
import sys


class GUI:
    size = width, height = 800, 600

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        self.manager = pygame_gui.UIManager(self.size)
        self.clock = pygame.time.Clock()
        self.build()

    def update(self):
        time_delta = self.clock.tick(60) / 1000.0
        self.process_events()
        self.manager.update(time_delta)
        self.screen.fill((0, 0, 0))
        self.manager.draw_ui(self.screen)
        pygame.display.update()

    def build(self):
        self.hello_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((350, 275), (100, 50)),
            text='Say Hello',
            manager=self.manager
        )

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == self.hello_button:
                        print('Hello World!')

            self.manager.process_events(event)

    
