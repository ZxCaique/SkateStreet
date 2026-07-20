import pygame

# Cores
C_ORANGE = (255, 128, 0)
C_YELLOW = (255, 255, 128)
C_WHITE = (255, 255, 255)
C_BLACK = (0, 0, 0)
C_PURPLE = (128, 0, 128)

# Eventos
EVENT_OBSTACLE = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2

# Dimensões da janela
WIN_WIDTH = 576
WIN_HEIGHT = 324

# Menu
MENU_OPTION = ('PLAY',
               'SCORE',
               'EXIT')

# Velocidades
PLAYER_SPEED = 1

ENTITY_SPEED = {
    # Level
    'level1bg0': 0, 'level1bg1': 1, 'level1bg2': 2,
    'level1bg3': 3, 'level1bg4': 4, 'level1bg5': 5, 'level1bg6': 6,
    'level2bg0': 0, 'level2bg1': 1, 'level2bg2': 2,
    'level2bg3': 3, 'level2bg4': 4, 'level2bg5': 5, 'level2bg6': 6,

    # Player
    'playerwalk0': PLAYER_SPEED,
    'jump_speed': 14,
    'gravity': 1,

    # Obstaculos
    'level1obstacle0': 3, 'level1obstacle1': 3, 'level1obstacle2': 3, 'level1obstacle3': 3,
    'level2obstacle0': 3, 'level2obstacle1': 3, 'level2obstacle2': 3, 'level2obstacle3': 3,
}

# Vida
PLAYER_HEALTH = 4
ENTITY_HEALTH = {
    # Level
    'level1bg0': 999, 'level1bg1': 999, 'level1bg2': 999,
    'level1bg3': 999, 'level1bg4': 999, 'level1bg5': 999, 'level1bg6': 999,
    'level2bg0': 999, 'level2bg1': 999, 'level2bg2': 999,
    'level2bg3': 999, 'level2bg4': 999, 'level2bg5': 999, 'level2bg6': 999,

    # player
    'playerwalk0': PLAYER_HEALTH, 'playerwalk1': PLAYER_HEALTH, 'playerwalk2': PLAYER_HEALTH,
    'playerwalk3': PLAYER_HEALTH, 'playerwalk4': PLAYER_HEALTH, 'playerwalk5': PLAYER_HEALTH,
    'playerjump': PLAYER_HEALTH, 'playerdamage': PLAYER_HEALTH,

    #Obstaculos
    'level1obstacle0': 1, 'level1obstacle1': 1, 'level1obstacle2': 1, 'level1obstacle3': 1,
    'level2obstacle0': 1, 'level2obstacle1': 1, 'level2obstacle2': 1, 'level2obstacle3': 1,
}

# Dano
PLAYER_DAMAGE = 0
ENTITY_DAMAGE = {
    # Level
    'level1bg0': 0, 'level1bg1': 0, 'level1bg2': 0,
    'level1bg3': 0, 'level1bg4': 0, 'level1bg5': 0, 'level1bg6': 0,
    'level2bg0': 0, 'level2bg1': 0, 'level2bg2': 0,
    'level2bg3': 0, 'level2bg4': 0, 'level2bg5': 0, 'level2bg6': 0,

    # Player
    'playerwalk0': PLAYER_DAMAGE, 'playerwalk1': PLAYER_DAMAGE, 'playerwalk2': PLAYER_DAMAGE,
    'playerwalk3': PLAYER_DAMAGE, 'playerwalk4': PLAYER_DAMAGE, 'playerwalk5': PLAYER_DAMAGE,
    'playerjump': PLAYER_DAMAGE, 'playerdamage': PLAYER_DAMAGE,

    #Obstaculos
    'level1obstacle0': 1, 'level1obstacle1': 1, 'level1obstacle2': 1, 'level1obstacle3': 1,
    'level2obstacle0': 1, 'level2obstacle1': 1, 'level2obstacle2': 1, 'level2obstacle3': 1,
}


# Tempo
SPAWN_TIME = 1300
TIMEOUT_STEP = 100
TIMEOUT_LEVEL = 60000
TIMEOUT_SCORE = 20000

# Score
PLAYER_SCORE = 0
ENTITY_SCORE = {
# Level
    'level1bg0': 0, 'level1bg1': 0, 'level1bg2': 0,
    'level1bg3': 0, 'level1bg4': 0, 'level1bg5': 0, 'level1bg6': 0,
    'level2bg0': 0, 'level2bg1': 0, 'level2bg2': 0,
    'level2bg3': 0, 'level2bg4': 0, 'level2bg5': 0, 'level2bg6': 0,

    # Player
    'playerwalk0': PLAYER_SCORE, 'playerwalk1': PLAYER_SCORE, 'playerwalk2': PLAYER_SCORE,
    'playerwalk3': PLAYER_SCORE, 'playerwalk4': PLAYER_SCORE, 'playerwalk5': PLAYER_SCORE,
    'playerjump': PLAYER_SCORE, 'playerdamage': PLAYER_SCORE,

    #Obstaculos
    'level1obstacle0': 1, 'level1obstacle1': 1, 'level1obstacle2': 1, 'level1obstacle3': 1,
    'level2obstacle0': 1, 'level2obstacle1': 1, 'level2obstacle2': 1, 'level2obstacle3': 1,
}

SCORE_POS = {
    'Title': (WIN_WIDTH / 2, 50),
    'EnterName': (WIN_WIDTH / 2, 80),
    'Label': (WIN_WIDTH / 2, 90),
    'Name': (WIN_WIDTH / 2, 110),
    0: (WIN_WIDTH / 2, 110), 1: (WIN_WIDTH / 2, 130), 2: (WIN_WIDTH / 2, 150),
    3: (WIN_WIDTH / 2, 170), 4: (WIN_WIDTH / 2, 190), 5: (WIN_WIDTH / 2, 210),
    6: (WIN_WIDTH / 2, 230), 7: (WIN_WIDTH / 2, 250), 8: (WIN_WIDTH / 2, 270),
    9: (WIN_WIDTH / 2, 290),
}
