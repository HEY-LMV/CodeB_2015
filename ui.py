import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((1199, 857), 0, 32)
background = pygame.image.load("background.jpg").convert()

aapl = pygame.image.load("aapl.png").convert_alpha()
atvi = pygame.image.load("atvi.png").convert_alpha()
ea = pygame.image.load("ea.png").convert_alpha()
fb = pygame.image.load("fb.png").convert_alpha()
goog = pygame.image.load("goog.png").convert_alpha()
msft = pygame.image.load("msft.png").convert_alpha()
sbux = pygame.image.load("sbux.png").convert_alpha()
sny = pygame.image.load("sny.png").convert_alpha()
tsla = pygame.image.load("tsla.png").convert_alpha()
twtr = pygame.image.load("twtr.png").convert_alpha()

aapl2 = pygame.transform.scale(aapl, (90, 100))
atvi2 = pygame.transform.scale(atvi, (90, 100))
ea2 = pygame.transform.scale(ea, (90, 100))
fb2 = pygame.transform.scale(fb, (90, 100))
goog2 = pygame.transform.scale(goog, (90, 100))
msft2 = pygame.transform.scale(msft, (90, 100))
sbux2 = pygame.transform.scale(sbux, (90, 100))
sny2 = pygame.transform.scale(sny, (90, 100))
tsla2 = pygame.transform.scale(tsla, (90, 100))
twtr2 = pygame.transform.scale(twtr, (90, 100))

# image = pygame.transform.scale(image, (100, 100))
# w, h = image.get_size()
# print(w)


while True:
	screen.blit(background, (0,0))

	# screen.blit(aapl2, (350, 403))
	screen.blit(aapl2, (225, 303))
	screen.blit(atvi2, (386.6, 303))
	screen.blit(ea2, (549, 303))
	screen.blit(fb2, (711.4, 303))
	screen.blit(goog2, (873.8, 303))
	screen.blit(msft2, (225, 406))
	screen.blit(sbux2, (386.6, 406))
	screen.blit(sny2, (549, 406))
	screen.blit(tsla2, (711.4, 406))
	screen.blit(twtr2, (873.8, 406))
	# h += 4
	# w += 4
	# image = pygame.transform.scale(image, (int(w), int(h)))
	pygame.display.update()
	pygame.time.delay(5000)
	# if (h > 300):
	pygame.quit()