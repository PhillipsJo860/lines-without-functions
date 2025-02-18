# Pygame game template

import pygame, sys, config

def init_game():
    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))
    pygame.display.set_caption(config.TITLE)
    return screen

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True

def main():
    screen = init_game()
    clock = pygame.time.Clock()
    running = True
    while running:
        running = handle_events()
        screen.fill(config.COLOR_WHITE)
        

        start_coordinate1 = (50, 15)
        start_coordinate2 = (800, 450)
        start_coordinate3 = (340, 100)
        start_coordinate4 = (205, 313)
        start_coordinate5 = (234,545)
        start_coordinate6 = (500, 600)

        end_coordinate1 = (623, 300)
        end_coordinate2 = (613, 300)
        end_coordinate3 = (123, 300)
        end_coordinate4 = (665, 300)
        end_coordinate5 = (432, 300)
        end_coordinate6 = (500, 300)
        line_thickness = (5)

        pygame.draw.line(screen, config.COLOR_RED, start_coordinate1, end_coordinate1, line_thickness)
        pygame.draw.line(screen, config.COLOR_BLACK, start_coordinate2, end_coordinate2, line_thickness)
        pygame.draw.line(screen, config.COLOR_GREEN, start_coordinate3, end_coordinate3, line_thickness)
        pygame.draw.line(screen, config.COLOR_BLUE, start_coordinate4, end_coordinate4, line_thickness)
        pygame.draw.line(screen, config.COLOR_CYAN, start_coordinate5, end_coordinate5, line_thickness)
        pygame.draw.line(screen, config.COLOR_SANDYBROWN, start_coordinate6, end_coordinate6, line_thickness)

        pygame.display.flip()
        clock.tick(config.FPS)
    
    pygame.quit()
    sys.exit()



if __name__ == '__main__':
    main()