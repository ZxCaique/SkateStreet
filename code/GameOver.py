import sys
import pygame
from pygame import Surface

from code.Const import WIN_WIDTH, WIN_HEIGHT, C_WHITE


class GameOver:
    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./asset/gameover.png').convert_alpha()
        self.rect = self.surf.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2))

    def run(self):
        pygame.mixer_music.load('./asset/gameover.mp3')
        pygame.mixer_music.play()

        font = pygame.font.SysFont("Lucida Sans Typewriter", 64)
        text_surf = font.render("GAME OVER", True, C_WHITE).convert_alpha()
        text_rect = text_surf.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2))

        start_time = pygame.time.get_ticks()
        while True:
            self.window.fill((0, 0, 0))
            self.window.blit(self.surf, self.rect)
            self.window.blit(text_surf, text_rect)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if pygame.time.get_ticks() - start_time >= 4000:
                return
