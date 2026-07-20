import sys
import random
import pygame
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code.Const import (
    C_WHITE, WIN_HEIGHT,
    EVENT_OBSTACLE, SPAWN_TIME,
    EVENT_TIMEOUT, TIMEOUT_STEP, TIMEOUT_LEVEL
)
from code.EntityMediator import EntityMediator
from code.GameOver import GameOver
from code.Player import Player
from code.EntityFactory import EntityFactory
from code.Background import Background


class Level:
    def __init__(self, window, name: str, fps: int = 80, player: Player = None):
        self.window = window
        self.name = name
        self.fps = fps
        self.background_list: list[Background] = EntityFactory.get_entity(f"{self.name}bg")

        if player:
            self.player = player
            self.player.rect.topleft = (50, self.player.ground_y - self.player.rect.height)
            self.player.is_jumping = False
            self.player.y_velocity = 0
            self.player.surf = self.player.animation_frames[self.player.current_frame]
        else:
            self.player: Player = EntityFactory.get_entity('playerwalk')

        self.entity_list = [self.player]
        self.timeout = TIMEOUT_LEVEL

        pygame.time.set_timer(EVENT_OBSTACLE, SPAWN_TIME)
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)

    def run(self):
        pygame.mixer_music.load(f'./asset/{self.name}.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()

        while True:
            clock.tick(self.fps)
            self.window.fill((0, 0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == EVENT_OBSTACLE:
                    obstacle_name = random.choice([
                        f"{self.name}obstacle0",
                        f"{self.name}obstacle1",
                        f"{self.name}obstacle2",
                        f"{self.name}obstacle3"
                    ])
                    self.entity_list.append(EntityFactory.get_entity(obstacle_name))

                else:
                    self.player.handle_event(event)

                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout <= 0:
                        return True

            for bg in self.background_list:
                bg.move()
                self.window.blit(bg.surf, bg.rect)

            self.player.move()
            self.window.blit(self.player.surf, self.player.rect)

            for entity in self.entity_list:
                if entity is not self.player:
                    entity.move()
                    self.window.blit(entity.surf, entity.rect)

            self.level_text(14, f'Health: {self.player.health} | Score: {self.player.score}', C_WHITE, (10, 25))

            EntityMediator.verify_collisions(self.entity_list)
            EntityMediator.verify_health(self.entity_list)

            if self.player.health <= 0:
                game_over = GameOver(self.window)
                game_over.run()
                return False

            pygame.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont("Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(text_surf, text_rect)
