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
        self.velocity=[random.choice(-1,1),random.choice(-1,1)]

    def update(self):
        self.rect.move_ip(self.velocity)
        edgehit=False
        if self.rect.left<=0 or self.rect.right>=500:
            self.velocity*=(-1)
            edgehit=True
        if self.rect.top<=0 or self.rect.bottom>=500:
            self.velocity*=(-1)
            edgehit=True
        if edgehit==True:
            pygame.event.post(pygame.event.Event(background_color_change))
            pygame.event.post(pygame.event.Event(sprite_color_change))

    def colorchange(self):
        self.image.fill(random.choice([blu,wht,org,red]))

clr=0
def bgcolor():
    clr=random.choice([ylo,grn,brn])


pygame.display.set_mode((500,500))
done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        pygame.display.flip()
