import pygame, math
from settings import *


def normalize(angle):
    angle = angle % (math.pi * 2)
    if angle <= 0:
        angle = (2 * math.pi) + angle
    return angle

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

class Ray:
    def __init__(self, angle, player, map):
        self.ray_angle = normalize(angle)
        self.player = player
        self.map = map

        self.is_facing_down = 0 < self.ray_angle < math.pi
        self.is_facing_up = not self.is_facing_down
        self.is_facing_right = self.ray_angle < 0.5 * math.pi or self.ray_angle > 1.5 * math.pi
        self.is_facing_left = not self.is_facing_right

        self.wall_hit_x = 0
        self.wall_hit_y = 0
        
        self.distance = 0

    def cast(self):
        found_horizontal_wall = False
        horizontal_hit_x = 0
        horizontal_hit_y = 0

        first_intersection_x = None
        first_intersection_y = None

        xa = 0
        ya = 0

        if self.is_facing_up:
            first_intersection_y = math.floor(self.player.y // TILE_SIZE) * TILE_SIZE - 1
            ya = -TILE_SIZE
        elif self.is_facing_down:
            first_intersection_y = math.floor(self.player.y // TILE_SIZE) * TILE_SIZE + TILE_SIZE
            ya = TILE_SIZE

        first_intersection_x = self.player.x + (first_intersection_y - self.player.y) / math.tan(self.ray_angle)

        next_horizontal_x = first_intersection_x
        next_horizontal_y = first_intersection_y

        xa = ya / math.tan(self.ray_angle)
        while (0 <= next_horizontal_x <= WINDOW_WIDTH) and (0 <= next_horizontal_y <= WINDOW_HEIGHT):
            if self.map.has_wall_at(next_horizontal_x, next_horizontal_y):
                found_horizontal_wall = True
                horizontal_hit_x = next_horizontal_x
                horizontal_hit_y = next_horizontal_y
                break
            else:
                next_horizontal_x += xa
                next_horizontal_y += ya

        # self.wall_hit_x = horizontal_hit_x
        # self.wall_hit_y = horizontal_hit_y

        found_vertical_wall = False
        vertical_hit_x = 0
        vertical_hit_y = 0
        
        if self.is_facing_right:
            first_intersection_x = ((self.player.x // TILE_SIZE) * TILE_SIZE) + TILE_SIZE
        else:
            first_intersection_x = ((self.player.x // TILE_SIZE) * TILE_SIZE) - 1
            
        first_intersection_y = self.player.y + (first_intersection_x - self.player.x) * math.tan(self.ray_angle)
        
        next_vertical_x = first_intersection_x
        next_vertical_y = first_intersection_y
        
        if self.is_facing_right:
            xa = TILE_SIZE
        else:
            xa = -TILE_SIZE
        ya  = xa * math.tan(self.ray_angle)
        while (0 <= next_vertical_x <= WINDOW_WIDTH and 0 <= next_vertical_y <= WINDOW_HEIGHT):
            if self.map.has_wall_at(next_vertical_x, next_vertical_y):
                found_vertical_wall = True
                vertical_hit_x = next_vertical_x
                vertical_hit_y = next_vertical_y
                break
            else:
                next_vertical_x += xa
                next_vertical_y += ya
                
        # DISTANCE CALCULATION
        horizontal_dist = 0
        vertical_dist = 0
        
        if found_horizontal_wall:
            horizontal_dist = distance(self.player.x, self.player.y, horizontal_hit_x, horizontal_hit_y)
        else:
            horizontal_dist = 9999
        if found_vertical_wall:
            vertical_dist = distance(self.player.x, self.player.y, vertical_hit_x, vertical_hit_y)
        else:
            vertical_dist = 9999
        
        if horizontal_dist < vertical_dist:
            self.wall_hit_x = horizontal_hit_x
            self.wall_hit_y = horizontal_hit_y
            self.distance = horizontal_dist
        else:
            self.wall_hit_x = vertical_hit_x
            self.wall_hit_y = vertical_hit_y
            self.distance = vertical_dist
        

    def render(self, screen):
        # pygame.draw.line(screen, "red", (self.player.x, self.player.y),
        #                  (
        #                      self.player.x + math.cos(self.ray_angle) * 50,
        #                      self.player.y + math.sin(self.ray_angle) * 50)
        #                  )
        pygame.draw.line(screen, "red", (self.player.x, self.player.y),
                         (self.wall_hit_x, self.wall_hit_y))
