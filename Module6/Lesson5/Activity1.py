import math
import random
import pygame

screenwidth=500
screenheight=500
#bullet_speed_x=0
bullet_speed_y=25
enemies_speed_y=20
enemies_speed_x=30
enemies_y_max=250
enemies_y_min=67
player_x=250
player_y=250
collisiondistance=15

pygame.init()
screen=pygame.display.set_mode((screenwidth,screenheight))
bg=pygame.image.load("background.png")
pygame.display.set_caption("Space Invader")
icon=pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

playerx=250
playery=250
player=pygame.image.load("player.png")
player_x_change=0


enemy_image=[]
enemy_x=[]
enemy_y=[]
enemy_x_change=[]
enemy_y_change=[]
total_enemies=7

for i in range(total_enemies):
    enemy=pygame.image.load("enemy.png")
    enemy_image.append(enemy)
    enemy_x.append(random.randint(0,480))#make width 20
    enemy_y.append(random.randint(67,250))
    enemy_x_change.append(enemies_speed_x)
    enemy_y_change.append(enemies_speed_y)


bulletimg=pygame.image.load("bullet.png")
bulletx=0
bullety=player_y
bullety_change=bullet_speed_y
bulletx_change=0
bullet_state="ready"

score_value=0
fonty=pygame.font.Font('freesansbold.ttf',32)
textx=10
texty=10
over_font=pygame.font.Font('freesansbold.ttf',64)


def show_score(x,y):
    score=fonty.render("Score :"+str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))


def game_over_text():
    font=over_font.render("Game Over!",True,pygame.Color("black"))
    screen.blit(font,(200,250))

def Player(x,y):
    screen.blit(player,(x,y))


def Enemy(x,y,i):
    screen.blit(enemy_image[i],(x,y))

    

def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletimg,(x+0,y+10))
def iscollision(enemyx,enemyy,bulletx,bullety):
    distance=math.sqrt((enemy_x-bulletx)**2+(enemy_y-bulletx)**2)
    return distance<collisiondistance

running=True
while running==True:
    screen.fill((0,0,0))
    screen.blit(bg,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                player_x_change=-5
            if event.key==pygame.K_RIGHT:
                player_x_change=5
            if event.key==pygame.K_SPACE and bullet_state=="ready":
                bulletx=playerx
                fire_bullet(bulletx,bullety)
        if event.key==pygame.K_UP and (event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT):
            player_x_change=0

playerx+=player_x_change
playerx=max(0,min(playerx,screenwidth-64))

for i in range(total_enemies):
    if enemy_y[i]>340:
        for j in range(total_enemies):
            enemy_y[j]=2000
        game_over_text()
        break
    enemy_x[i]+=enemy_x_change[i]
    if enemy_x[i]<=0or enemy_x[i]>=screenwidth-64:
        enemy_x_change[i]*=-1
        enemy_y[i]+=enemy_y_change[i]