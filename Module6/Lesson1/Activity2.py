import pygame
pygame.init()
x=pygame.display.set_mode((500,500))
pygame.display.set_caption("Add Penguin")
background=pygame.transform.scale(pygame.image.load("grass_template2.jpg").convert(),(500,500))
penguin=pygame.transform.scale(pygame.image.load("image.png").convert(),(100,100))
center=penguin.get_rect(center=(250,250))
xyz=pygame.font.Font(None,20).render('Hello Penguin',True,pygame.Color('black'))
center1=xyz.get_rect(center=(100,100))
done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        x.blit(background,(0,0))
        x.blit(penguin,center)
        x.blit(xyz,center1)
        pygame.display.flip()
