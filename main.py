from Game import *


def main():
    game = Game()
    game.intro_screen()
    while game.running:
        game.new()
        game.main()
    pygame.quit()


if __name__ == "__main__":
    main()
