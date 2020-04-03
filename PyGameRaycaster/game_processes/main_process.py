import pygame

pygame.init()


def main_process(game):
    is_running = True
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            game.camera.handle_event(event)
        game.screen.fill(pygame.Color('black'))
        game.camera.update()
        game.all_sprites.draw(game.screen)
        pygame.display.flip()
        game.clock.tick(game.FPS)
