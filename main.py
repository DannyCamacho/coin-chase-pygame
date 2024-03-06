from Game import *


def main():
    game = Game()
    game.intro_screen()
    game.new()
    while game.running:
        game.main()
        game.game_over()
    pygame.quit()


if __name__ == "__main__":
    main()
