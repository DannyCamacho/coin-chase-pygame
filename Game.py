import pygame.font

from sprites import *
from config import *


class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.pathing = False

        self.font = pygame.font.Font('assets/general_font.ttf', 64)

        self.character_spritesheet = Spritesheet('img/character.png')
        self.enemy_spritesheet = Spritesheet('img/enemy.png')
        self.attack_spritesheet = Spritesheet('img/attack.png')
        self.terrain_spritesheet = Spritesheet('img/terrain.png')
        self.intro_background = pygame.image.load('img/introbackground.png')
        self.game_over_background = pygame.image.load('img/gameover.png')

    def draw_tilemap(self):
        for i, row in enumerate(tilemap):
            for j, col in enumerate(row):
                Ground(self, j, i)
                if col == "B":
                    Block(self, j, i)
                if col == "E":
                    Enemy(self, j, i)
                if col == "P":
                    self.player = Player(self, j, i)

    def new(self):  # a new game starts
        self.playing = True

        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()
        self.path = pygame.sprite.LayeredUpdates()

        self.draw_tilemap()

    def events(self):  # game loop events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.player.facing == 'up':
                        Attack(self, self.player.rect.x, self.player.rect.y - TILESIZE)
                    if self.player.facing == 'down':
                        Attack(self, self.player.rect.x, self.player.rect.y + TILESIZE)
                    if self.player.facing == 'left':
                        Attack(self, self.player.rect.x - TILESIZE, self.player.rect.y)
                    if self.player.facing == 'right':
                        Attack(self, self.player.rect.x + TILESIZE, self.player.rect.y)
                if event.key == pygame.K_p:
                    self.pathing = not self.pathing
                    for sprite in self.path:
                        sprite.kill()

    def update(self):  # game loop updates
        self.all_sprites.update()

    def draw(self):  # game loop draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()

    def main(self):  # game loop
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def game_over(self):
        title = self.font.render('Game Over', True, WHITE)
        title_rect = title.get_rect(center=(WIN_WIDTH / 2, WIN_HEIGHT / 2))

        restart_button = Button(10, WIN_HEIGHT - 120, 120, 50, WHITE, BLACK, 'Restart', 32)
        quit_button = Button(10, WIN_HEIGHT - 60, 120, 50, WHITE, BLACK, 'Quit', 32)

        for sprite in self.all_sprites:
            sprite.kill()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if restart_button.is_pressed(mouse_pos, mouse_pressed):
                self.new()
                self.main()

            if quit_button.is_pressed(mouse_pos, mouse_pressed):
                self.running = False

            self.screen.blit(self.game_over_background, (0, 0))
            self.screen.blit(title, title_rect)
            self.screen.blit(restart_button.image, restart_button.rect)
            self.screen.blit(quit_button.image, quit_button.rect)
            self.clock.tick(FPS)
            pygame.display.update()

    def game_win(self):
        title = self.font.render('You Win!', True, WHITE)
        title_rect = title.get_rect(center=(WIN_WIDTH / 2, WIN_HEIGHT / 2))

        restart_button = Button(10, WIN_HEIGHT - 120, 120, 50, WHITE, BLACK, 'Restart', 32)
        quit_button = Button(10, WIN_HEIGHT - 60, 120, 50, WHITE, BLACK, 'Quit', 32)

        for sprite in self.all_sprites:
            sprite.kill()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if restart_button.is_pressed(mouse_pos, mouse_pressed):
                self.new()
                self.main()

            if quit_button.is_pressed(mouse_pos, mouse_pressed):
                self.running = False

            self.screen.blit(self.intro_background, (0, 0))
            self.screen.blit(title, title_rect)
            self.screen.blit(restart_button.image, restart_button.rect)
            self.screen.blit(quit_button.image, quit_button.rect)
            self.clock.tick(FPS)
            pygame.display.update()

    def intro_screen(self):
        intro = True

        title = self.font.render('A* Algo Demo', True, BLACK)
        title_rect = title.get_rect(center=(WIN_WIDTH / 2, WIN_HEIGHT / 2))

        play_button = Button(10, WIN_HEIGHT - 60, 120, 50, WHITE, BLACK, 'Play', 32)

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False
                    self.running = False

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if play_button.is_pressed(mouse_pos, mouse_pressed):
                intro = False

            self.screen.blit(self.intro_background, (0, 0))
            self.screen.blit(title, title_rect)
            self.screen.blit(play_button.image, play_button.rect)
            self.clock.tick(FPS)
            pygame.display.update()
