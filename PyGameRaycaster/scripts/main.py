import pygame
from PyGameRaycaster.scripts.game import Game
from PyGameRaycaster.game_processes.main_process import main_process

pygame.init()


def main():
    game = Game()
    main_process(game)


if __name__ == '__main__':
    main()
