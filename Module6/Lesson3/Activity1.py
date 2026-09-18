import pygame
import random
pygame.init()

background_color_change=pygame.USEREVENT+1
sprite_color_change=pygame.USEREVENT+2
blu=pygame.Color("blue")
wht=pygame.Color("white")
org=pygame.Color("orange")
red=pygame.Color("red")
ylo=pygame.Color("yellow")
grn=pygame.Color("green")
brn=pygame.Color("brown")

class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,height,width):
        super().__init__()
        self.image=pygame.Surface([width,height])
        self.image.fill(color)
        self.rect=self.image.get_rect()
        self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]   

    def update(self):
      

        self.rect.move_ip(self.velocity)


        boundary_hit = False


        if self.rect.left <= 0 or self.rect.right >= 500:

            self.velocity[0] = -1 * self.velocity[0]

            boundary_hit = True



        if self.rect.top <= 0 or self.rect.bottom >= 500:

            self.velocity[1] = -self.velocity[1]

            boundary_hit = True

        if boundary_hit:
              pygame.event.post(pygame.event.Event(sprite_color_change))
              pygame.event.post(pygame.event.Event(background_color_change))

    def colorchange(self):
        self.image.fill(random.choice([blu,wht,org,red]))

# clr=grn
def bgcolor():
    global clr 

    clr=random.choice([ylo,grn,brn])

all_sprites_list=pygame.sprite.Group()
sp1=Sprite(blu,20,30)
sp1.rect.x=random.randint(0,480)
sp1.rect.y=random.randint(0,470)

all_sprites_list.add(sp1)

screen=pygame.display.set_mode((500,500))
cap=pygame.display.set_caption("OOGA BOOGA RULE")

clr = org
screen.fill(clr)
done=False
clock=pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        elif event.type==sprite_color_change:
                    sp1.colorchange()
        elif event.type==background_color_change:
            bgcolor()
        

    all_sprites_list.update()

        
    screen.fill(clr)
    all_sprites_list.draw(screen)

    pygame.display.flip()
    clock.tick(60)



pygame.quit()