from code.Background import Background
from code.Obstacles import Obstacles
from code.Player import Player
from code.Const import WIN_WIDTH


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case 'level1bg':
                list_bg = []
                for i in range(6):
                    list_bg.append(Background(f'level1bg{i}', (0, 0)))
                    list_bg.append(Background(f'level1bg{i}', (WIN_WIDTH, 0)))
                return list_bg

            case 'level2bg':
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f'level2bg{i}', (0, 0)))
                    list_bg.append(Background(f'level2bg{i}', (WIN_WIDTH, 0)))
                return list_bg

            case 'playerwalk':
                return Player('playerwalk0', (0, 250))

            case 'level1obstacle0':
                return Obstacles('level1obstacle0', (WIN_WIDTH + 5, 250))
            case 'level1obstacle1':
                return Obstacles('level1obstacle1', (WIN_WIDTH + 5, 250))
            case 'level1obstacle2':
                return Obstacles('level1obstacle2', (WIN_WIDTH + 5, 250))
            case 'level1obstacle3':
                return Obstacles('level1obstacle3', (WIN_WIDTH + 5, 250))

            case 'level2obstacle0':
                return Obstacles('level2obstacle0', (WIN_WIDTH + 5, 250))
            case 'level2obstacle1':
                return Obstacles('level2obstacle1', (WIN_WIDTH + 5, 250))
            case 'level2obstacle2':
                return Obstacles('level2obstacle2', (WIN_WIDTH + 5, 250))
            case 'level2obstacle3':
                return Obstacles('level2obstacle3', (WIN_WIDTH + 5, 250))

        return None
