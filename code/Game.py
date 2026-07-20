# Game.py
import sys
import pygame
from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION, TIMEOUT_SCORE
from code.Level import Level
from code.Menu import Menu
from code.Player import Player
from code.EntityFactory import EntityFactory
from code.Score import Score
from code.GameOver import GameOver


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
        self.current_score = 0

    def run(self):
        while True:
            score_display = Score(self.window, show_time=TIMEOUT_SCORE)
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]:
                player: Player = EntityFactory.get_entity('playerwalk')
                player.score = self.current_score

                level1 = Level(self.window, "level1", fps=80, player=player)
                if level1.run():
                    self.current_score = player.score

                    level2 = Level(self.window, "level2", fps=100, player=player)
                    if level2.run():
                        self.current_score = player.score
                        score_display.save(self.current_score)
                        score_display.show()
                    else:
                        self.current_score = 0
                        GameOver(self.window).run()
                        continue
                else:
                    self.current_score = 0
                    GameOver(self.window).run()
                    continue

            elif menu_return == MENU_OPTION[1]:
                score_display.show()

            elif menu_return == MENU_OPTION[2]:
                pygame.quit()
                sys.exit()
