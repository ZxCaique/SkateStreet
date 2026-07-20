from .Entity import Entity
from .Const import ENTITY_SPEED

class Obstacles(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.speed = ENTITY_SPEED.get(name, 1)
        self.passed_by_player = False


    def move(self):
        self.rect.x -= self.speed
