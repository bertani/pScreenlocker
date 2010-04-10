from pe import *
from random import randint

def update(screen):
	global cow, slangs
	screen.blit(cow,(50,250))
	fontimg = font__.render(slangs[randint(0,5)],1,(200,200,200))
        screen.blit(fontimg, (120-fontimg.get_width()/2,260))
	pygame.display.update(pygame.rect.Rect((50,120),(400,400)))#(50,250),(400,150)))
slangs=["asd","lol","n00b!","stfu!","wtf?","meh"]
cow=pygame.image.load(folder+res+"cow.bmp")
__timer=5
