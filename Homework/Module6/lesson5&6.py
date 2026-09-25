import math
import random
import pygame

screenwidth = 500
screenheight = 500
bullet_speed_y = 10  
enemies_speed_y = 20
enemies_speed_x = 3  
enemies_y_max = 250
enemies_y_min = 67
player_x = 250
player_y = 400  
collisiondistance = 25  

# Initialize Pygame and Mixer
pygame.init()
pygame.mixer.init() 

screen = pygame.display.set_mode((screenwidth, screenheight))

# Load Images
bg = pygame.image.load("background.png")
pygame.display.set_caption("Space Invader")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

playerx = 250
playery = 400
player = pygame.image.load("player.png")
player_x_change = 0

# ================= AUDIO SETUP =================
# Background Music
pygame.mixer.music.load("music.mp3") 
pygame.mixer.music.set_volume(0.3)  # Adjust volume from 0.0 to 1.0
pygame.mixer.music.play(-1)          # -1 makes the music loop forever


enemy_image = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
total_enemies = 7

for i in range(total_enemies):
    enemy = pygame.image.load("enemy.png")
    enemy_image.append(enemy)
    enemy_x.append(random.randint(0, screenwidth - 64))
    enemy_y.append(random.randint(enemies_y_min, enemies_y_max))
    enemy_x_change.append(enemies_speed_x)
    enemy_y_change.append(enemies_speed_y)

bulletimg = pygame.image.load("bullet.png")
bulletx = 0
bullety = playery  
bullety_change = bullet_speed_y
bullet_state = "ready"

score_value = 0
fonty = pygame.font.Font('freesansbold.ttf', 32)
textx = 10
texty = 10
over_font = pygame.font.Font('freesansbold.ttf', 64)


def show_score(x, y):
    score = fonty.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    font = over_font.render("Game Over!", True, (255, 0, 0))
    screen.blit(font, (100, 220))


def Player(x, y):
    screen.blit(player, (x, y))


def Enemy(x, y, i):
    screen.blit(enemy_image[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg, (x + 16, y + 10))  


def iscollision(enemyx, enemyy, bulletx, bullety):
    distance = math.sqrt((enemyx - bulletx) ** 2 + (enemyy - bullety) ** 2)
    return distance < collisiondistance


running = True
clock = pygame.time.Clock()  

while running:
    clock.tick(60)  
    screen.fill((0, 0, 0))
    screen.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -5
            if event.key == pygame.K_RIGHT:
                player_x_change = 5
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bulletx = playerx
                bullety = playery  
                fire_bullet(bulletx, bullety)
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

    playerx += player_x_change
    playerx = max(0, min(playerx, screenwidth - 64))

    for i in range(total_enemies):
        if enemy_y[i] > 340:
            for j in range(total_enemies):
                enemy_y[j] = 2000
            game_over_text()
            break

        enemy_x[i] += enemy_x_change[i]
        
        if enemy_x[i] <= 0:
            enemy_x_change[i] = enemies_speed_x
            enemy_y[i] += enemy_y_change[i]
        elif enemy_x[i] >= screenwidth - 64:
            enemy_x_change[i] = -enemies_speed_x
            enemy_y[i] += enemy_y_change[i]

        if bullet_state == "fire" and iscollision(enemy_x[i], enemy_y[i], bulletx, bullety):
            bullet_state = "ready"
            bullety = playery  
            score_value += 1
            enemy_x[i] = random.randint(0, screenwidth - 64)
            enemy_y[i] = random.randint(enemies_y_min, enemies_y_max)

        Enemy(enemy_x[i], enemy_y[i], i)

    if bullety <= 0:
        bullety = playery  
        bullet_state = "ready"
        
    if bullet_state == "fire":
        fire_bullet(bulletx, bullety)
        bullety -= bullety_change

    Player(playerx, playery)
    show_score(textx, texty)
    pygame.display.update()

pygame.quit()
