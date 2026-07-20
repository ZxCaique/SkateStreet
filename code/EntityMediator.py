from code.Entity import Entity
from code.Obstacles import Obstacles
from code.Player import Player
from code.Const import ENTITY_SCORE, WIN_WIDTH


class EntityMediator:

    @staticmethod
    def _verify_collision_window(ent: Entity):
        if isinstance(ent, Obstacles) and ent.rect.right <= 0:
            ent.health = 0

    @staticmethod
    def _verify_collision_entity(ent1: Entity, ent2: Entity):
        for player, obstacle in [(ent1, ent2), (ent2, ent1)]:
            if isinstance(player, Player) and isinstance(obstacle, Obstacles):

                if not hasattr(obstacle, 'passed_by_player'):
                    obstacle.passed_by_player = False

                if not obstacle.passed_by_player and player.rect.bottom <= obstacle.rect.top + 5 and obstacle.rect.x < WIN_WIDTH:
                    player.score += ENTITY_SCORE.get(obstacle.name, 1)
                    obstacle.passed_by_player = True

                if player.rect.colliderect(obstacle.rect) and player.rect.bottom > obstacle.rect.top + 5:
                    player.take_damage(obstacle.name)

    @staticmethod
    def verify_collisions(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            ent1 = entity_list[i]
            EntityMediator._verify_collision_window(ent1)
            for j in range(i + 1, len(entity_list)):
                ent2 = entity_list[j]
                EntityMediator._verify_collision_entity(ent1, ent2)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list[:]:
            if ent.health <= 0:
                entity_list.remove(ent)
