import pygame
from random import randrange
from maze_generator import *


class Food:
    def __init__(self):
        self.img = pygame.image.load('./img/food.png').convert_alpha()
        self.img = pygame.transform.scale(self.img, (TILE - 10, TILE - 10))
        self.rect = self.img.get_rect()
        self.set_pos()

    def set_pos(self):
        self.rect.topleft = randrange(cols) * TILE + 5, randrange(rows) * TILE + 5

    def draw(self):
        game_surface.blit(self.img, self.rect)

class Key_Icon:
    def __init__(self):
        self.img = pygame.image.load('./img/key.png').convert_alpha()
        self.img = pygame.transform.scale(self.img, (TILE - 10, TILE - 10))
        self.rect = self.img.get_rect()
        self.set_pos()

    def set_pos(self):
        self.rect.topleft = randrange(cols) * TILE + 5, randrange(rows) * TILE + 5

    def draw(self):
        game_surface.blit(self.img, self.rect)


def is_collide(x, y):
    tmp_rect = player_rect.move(x, y)
    if tmp_rect.collidelist(walls_collide_list) == -1:
        return False
    return True

def update_collision_list():
    global walls_collide_list
    walls_collide_list = sum([cell.get_rects() for cell in maze], [])

def eat_food():
    for food in food_list:
        if player_rect.collidepoint(food.rect.center):
            food.set_pos()
            return True
    return False

def collect_key():
    global has_key
    for key_icon in key_pos:
        if player_rect.collidepoint(key_icon.rect.center):
            key_pos.remove(key_icon)
            has_key = True
            exit_cell = maze[-1]
            exit_open(exit_cell)
            return True
    return False

def restart_game():
    global time, score, FPS, maze, has_key, key_pos
        time, FPS = 60, 60
    if score == None:
        score = 0
    high_score = get_record()
    set_record(high_score, score)
    has_key = False
    maze = generate_maze()
    update_collision_list()
    player_rect.center = TILE // 2, TILE // 2
    [food.set_pos() for food in food_list]
    key_pos = [Key_Icon() for i in range(1)]
    key_pos[0].set_pos()
    


def check_exit():
    global score, exit_reached  # Declare exit_reached as a global variable

    exit_cell = maze[-1]  
    exit_center = exit_cell.x * TILE + TILE // 2, exit_cell.y * TILE + TILE // 2
    player_center = player_rect.center
    distance = ((exit_center[0] - player_center[0]) ** 2 + (exit_center[1] - player_center[1]) ** 2) ** 0.5
    allowed_distance = TILE // 16

    if distance < allowed_distance and has_key:
         exit_reached = True
         score += 1
         restart_game()

def is_game_over():
    global time, score, record, FPS, last_restart_time  # Declare last_restart_time as global
    if time < 0:
        current_time = pygame.time.get_ticks()
        if current_time - last_restart_time > 1000:
            last_restart_time = current_time
            restart_game()
            player_rect.center = TILE // 2, TILE // 2
            [food.set_pos() for food in food_list]
            [Key_Icon.set_pos() for Key_Icon in key_pos]
            set_record(record, score)
            record = get_record()
            time, score, FPS = 60, 0, 60
            return True  # Indicates that the game is over
    return False  # Indicates that the game is not over

def get_record():
    try:
        with open('record.txt', 'r') as f:
            return f.readline()
    except FileNotFoundError:
        with open('record.txt', 'w') as f:
            f.write('0')
            return 0


def set_record(record, score):
    rec = max(int(record), score)
    with open('record.txt', 'w') as f:
        f.write(str(rec))

has_key = False

FPS = 60
pygame.init()
game_surface = pygame.Surface(RES)
surface = pygame.display.set_mode((WIDTH + 300, HEIGHT))
clock = pygame.time.Clock()

# images
bg_game = pygame.image.load('./img/bg_1.jpg').convert()
bg = pygame.image.load('./img/bg_main.jpg').convert()

# get maze
maze = generate_maze()
update_collision_list()

# player settings
player_speed = 5
player_img = pygame.image.load('./img/0.png').convert_alpha() # convert_alpha to remove background
player_img = pygame.transform.scale(player_img, (TILE - 2 * maze[0].thickness, TILE - 2 * maze[0].thickness))
player_rect = player_img.get_rect()
player_rect.center = TILE // 2, TILE // 2
directions = {'left': (-player_speed, 0), 'right': (player_speed, 0), 'up': (0, -player_speed), 'down': (0, player_speed)}
keys = {'left': pygame.K_LEFT, 'right': pygame.K_RIGHT, 'up': pygame.K_UP, 'down': pygame.K_DOWN}
direction = (0, 0)

# food settings
food_list = [Food() for i in range(3)]

# key settings
key_pos = [Key_Icon() for i in range(1)]

# collision list
walls_collide_list = sum([cell.get_rects() for cell in maze], [])

# timer, score, record
pygame.time.set_timer(pygame.USEREVENT, 1000)
time = 60
score = 0
record = get_record()

# fonts
font = pygame.font.SysFont('Impact', 150)
text_font = pygame.font.SysFont('Impact', 80)

last_restart_time = 0
exit_reached = False

while True:
    surface.blit(bg, (WIDTH, 0))
    surface.blit(game_surface, (0, 0))
    game_surface.blit(bg_game, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.USEREVENT:
            time -= 1

    # controls and movement
    pressed_key = pygame.key.get_pressed()
    for key, key_value in keys.items():
        if pressed_key[key_value] and not is_collide(*directions[key]):
            direction = directions[key]

    if not is_collide(*direction):  # Move the player only if it doesn't collide with walls
        player_rect.move_ip(direction)

    # Check if the game is over before calling check_exit()
    if is_game_over():
        restart_game()
    

    # draw maze
    [cell.draw(game_surface) for cell in maze]

    # gameplay
    if eat_food():
        FPS += 10
        score += 1
    
    # gameplay
    if collect_key():
        has_key = True
    

    # draw player
    game_surface.blit(player_img, player_rect)

    # draw food
    [food.draw() for food in food_list]

    # draw key
    [Key_Icon.draw() for Key_Icon in key_pos]

    # Open exit if the player has the key
    if has_key and not exit_reached and is_game_over():
        restart_game()
        exit_reached = False 



    check_exit()

    # draw stats
    surface.blit(text_font.render('Time', True, pygame.Color('cyan')), (WIDTH + 70, 30))
    surface.blit(font.render(f'{time}', True, pygame.Color('cyan')), (WIDTH + 70, 130))
    surface.blit(text_font.render('Score:', True, pygame.Color('forestgreen')), (WIDTH + 50, 350))
    surface.blit(font.render(f'{score}', True, pygame.Color('forestgreen')), (WIDTH + 70, 430))
    surface.blit(text_font.render('Best:', True, pygame.Color('magenta')), (WIDTH + 30, 620))
    surface.blit(font.render(f'{record}', True, pygame.Color('magenta')), (WIDTH + 70, 700))

    pygame.display.flip()
    clock.tick(FPS)
