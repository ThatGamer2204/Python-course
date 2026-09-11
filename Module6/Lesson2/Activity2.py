import pygame
pygame.init()
x=pygame.display.set_mode((400,500))
pygame.draw.circle(x,pygame.Color("Blue"),(250,250),75)
pygame.draw.circle(x,pygame.Color("Blue"),(350,150),75,5)
done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        pygame.display.flip()
