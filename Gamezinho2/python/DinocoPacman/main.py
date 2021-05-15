from game import *


g = Game()


while g.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            g.ruuning = False

    g.curr_menu.display_menu()
    g.game_loop()
