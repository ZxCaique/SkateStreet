import sys
from datetime import datetime

import pygame
from pygame import Surface, Rect, KEYDOWN, K_RETURN, K_BACKSPACE, K_ESCAPE
from pygame.font import Font

from code.Const import C_YELLOW, SCORE_POS, C_WHITE, C_PURPLE, C_BLACK
from code.DBProxy import DBProxy


def get_formatted_date():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%d/%m/%y")
    return f"{current_time} - {current_date}"


class Score:
    def __init__(self, window: Surface = None, current_score: int = 0, show_time: int = 4000):
        self.window = window
        self.score = current_score
        self.high_scores = []
        self.show_time = show_time
        if self.window is not None:
            self.surf = pygame.image.load('./asset/score.png').convert_alpha()
            self.rect = self.surf.get_rect(left=0, top=0)

    def save(self, new_score: int = None):
        if new_score is not None:
            self.score = new_score
        self.high_scores.append(self.score)
        pygame.mixer_music.load('./asset/win.mp3')
        pygame.mixer_music.play(-1)
        win_surf = pygame.image.load('./asset/win.png').convert_alpha()
        win_rect = win_surf.get_rect(left=0, top=0)
        db_proxy = DBProxy('DBScore')
        name = ''
        while True:
            self.window.blit(source=win_surf, dest=win_rect)
            self.score_text(48, 'YOU WIN!!', C_YELLOW, SCORE_POS['Title'])
            text = 'Enter Player name (4 characters):'
            self.score_text(20, text, C_WHITE, SCORE_POS['EnterName'])
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN and len(name) == 4:
                        db_proxy.save({'name': name, 'score': new_score, 'date': get_formatted_date()})
                        self.show()
                        return
                    elif event.key == K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) < 4:
                            name += event.unicode
            self.score_text(20, name, C_WHITE, SCORE_POS['Name'])
            pygame.display.flip()

    def show(self):
        pygame.mixer_music.load('./asset/score.mp3')
        pygame.mixer_music.play(-1)
        self.window.blit(source=self.surf, dest=self.rect)
        self.score_text(48, 'TOP 10 SCORE', C_PURPLE, SCORE_POS['Title'])
        self.score_text(20, 'NAME     SCORE           DATE      ', C_PURPLE, SCORE_POS['Label'])
        db_proxy = DBProxy('DBScore')
        list_score = db_proxy.retrieve_top10()
        db_proxy.close()
        for player_score in list_score:
            id_, name, score, date = player_score
            self.score_text(20, f'{name}     {score:05d}     {date}', C_BLACK,
                            SCORE_POS[list_score.index(player_score)])

        start_time = pygame.time.get_ticks()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.mixer_music.stop()
                        return

            now = pygame.time.get_ticks()
            if now - start_time >= self.show_time:
                pygame.mixer_music.stop()
                return

            pygame.display.flip()

    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
