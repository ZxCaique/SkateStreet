import time
import pygame
from .Entity import Entity
from .Const import ENTITY_SPEED, ENTITY_DAMAGE, ENTITY_HEALTH, ENTITY_SCORE, WIN_WIDTH

class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.animation_frames = [pygame.image.load(f'./asset/playerwalk{i}.png').convert_alpha() for i in range(6)]
        self.current_frame = 0
        self.last_frame_time = time.time()
        self.frame_duration = 0.1
        self.surf = self.animation_frames[self.current_frame]
        self.rect = self.surf.get_rect(topleft=position)
        self.ground_y = self.rect.bottom
        self.speed = ENTITY_SPEED.get('playerwalk0', 2)
        self.jump_speed = ENTITY_SPEED.get('jump_speed', 15)
        self.gravity = ENTITY_SPEED.get('gravity', 1)
        self.y_velocity = 0
        self.is_jumping = False
        self.jump_surf = pygame.image.load('./asset/playerjump.png').convert_alpha()
        self.damage_surf = pygame.image.load('./asset/playerdamage.png').convert_alpha()
        self.last_hit_time = 0
        self.invulnerability_time = 1.0
        self.health = ENTITY_HEALTH.get(name, 4)
        self.score = ENTITY_SCORE.get(name, 0)
        self.can_score = False

    def can_take_damage(self):
        return (time.time() - self.last_hit_time) >= self.invulnerability_time

    def take_damage(self, source_name: str):
        if self.can_take_damage():
            damage_amount = ENTITY_DAMAGE.get(source_name, 1)
            self.health -= damage_amount
            self.last_hit_time = time.time()
            self.surf = self.damage_surf

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not self.is_jumping and self.rect.top > 0:
                self.is_jumping = True
                self.y_velocity = -self.jump_speed
                self.surf = self.jump_surf
                self.can_score = True

    def move(self):
        keys = pygame.key.get_pressed()
        if not self.is_jumping:
            if keys[pygame.K_LEFT] and self.rect.left > 0:
                self.rect.x -= self.speed
            if keys[pygame.K_RIGHT] and self.rect.right < WIN_WIDTH:
                self.rect.x += self.speed

        if self.is_jumping:
            self.rect.y += self.y_velocity
            self.y_velocity += self.gravity
            self.rect.x += self.speed
            if self.rect.right > WIN_WIDTH:
                self.rect.right = WIN_WIDTH
            if self.rect.bottom >= self.ground_y:
                self.rect.bottom = self.ground_y
                self.is_jumping = False
                self.y_velocity = 0
                self.surf = self.animation_frames[self.current_frame]

        if not self.is_jumping and self.can_take_damage():
            current_time = time.time()
            if current_time - self.last_frame_time >= self.frame_duration:
                self.current_frame = (self.current_frame + 1) % len(self.animation_frames)
                self.last_frame_time = current_time
                self.surf = self.animation_frames[self.current_frame]
