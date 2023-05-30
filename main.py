import pygame
from pygame.locals import *
from player import Player

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)


class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.player = Player(100, 100, 80, 80, self)

    def main(self):
        self.init_game()
        self.game_loop()


    def init_game(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.running = True


    def game_loop(self):
        while self.running:
            # Dodanie funkcji sprawdzającej, czy gracz kliknął przyciski
            self.get_input()
            self.update()
            self.check_if_close_game()
            self.draw()
        pygame.quit()



    def check_if_close_game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                break

    # Stworzenie nowej funkcji sprawdzającej, czy gracz wcisął cokolwiek na klawiaturze
    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[K_d]:
            self.player.move(0.5, 0)
        if keys[K_a]:
            self.player.move(-0.5, 0)
        if keys[K_w]:
            self.player.move(0, -0.5)
        if keys[K_s]:
            self.player.move(0, 0.5)

    def update(self):
        self.player.update()

    def draw(self):
        self.screen.fill(BLACK)
        self.player.draw()

        self.clock.tick(60)
        pygame.display.flip()


game = Game(1366, 768)
game.main()