import pygame
import random
pygame.init()
screen=pygame.display.set_mode((500,500))
movspeed=10
font=pygame.font.SysFont("Times New Roman",30)
background=pygame.transform.scale(pygame.image.load("grass_template2.jpg").convert(),(500,500))
class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,height,width):
        super().__init__()
        self.image=pygame.Surface([width,height])
        self.image.fill(color)
        pygame.draw.rect(self.image,color,pygame.Rect(0,0,width,height))
        self.rect=self.image.get_rect()

    def move(self,x_new,y_new):
        self.rect.x=max(min(self.rect.x+x_new,480),0)
        self.rect.y=max(min(self.rect.y+y_new,470),0)

sp1=Sprite(pygame.Color('blue'),20,30)
sp1.rect.x=random.randint(0,480)
sp1.rect.y=random.randint(0,470)
sp2=Sprite(pygame.Color('black'),20,30)
sp2.rect.x=random.randint(0,480)
sp2.rect.y=random.randint(0,470)
p=pygame.sprite.Group()
p.add(sp1)
p.add(sp2)
running,won=True,False
clock=pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

        if not won:
            keys=pygame.key.get_pressed()
            x_new=(keys[pygame.K_RIGHT]-keys[pygame.K_LEFT])*movspeed
            y_new=(keys[pygame.K_DOWN]-keys[pygame.K_UP])*movspeed
            sp1.move(x_new,y_new)
            if sp1.rect.colliderect(sp2.rect):
                p.remove(sp2)
                won=True

        screen.blit(background,(0,0))
        p.draw(screen)
        if won == True:
            ww=font.render("YOU WIN!",True,pygame.Color("black"))
            screen.blit(ww,(250,250))
        pygame.display.flip()
        clock.tick(60)
pygame.quit()