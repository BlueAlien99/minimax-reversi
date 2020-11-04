import sys
import pygame
import pygame_gui


pygame.init()
size = width, height = 800, 600
black = 0, 0, 0

screen = pygame.display.set_mode(size)

manager = pygame_gui.UIManager(size)

hello_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((350, 275), (100, 50)),
    text='Say Hello',
    manager=manager
)


clock = pygame.time.Clock()

while True:
    time_delta = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.USEREVENT:
             if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                 if event.ui_element == hello_button:
                     print('Hello World!')

        manager.process_events(event)

    manager.update(time_delta)

    screen.fill(black)

    manager.draw_ui(screen)
    pygame.display.update()