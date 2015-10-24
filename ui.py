import pygame
from pygame.locals import *

class UI:
	def __init__(self):

		pygame.init()

		self.screen = pygame.display.set_mode((1199, 857), 0, 32)
		self.background = pygame.image.load("background.jpg").convert()

		self.aapl = pygame.image.load("aapl.png").convert_alpha()
		self.atvi = pygame.image.load("atvi.png").convert_alpha()
		self.ea = pygame.image.load("ea.png").convert_alpha()
		self.fb = pygame.image.load("fb.png").convert_alpha()
		self.goog = pygame.image.load("goog.png").convert_alpha()
		self.msft = pygame.image.load("msft.png").convert_alpha()
		self.sbux = pygame.image.load("sbux.png").convert_alpha()
		self.sny = pygame.image.load("sny.png").convert_alpha()
		self.tsla = pygame.image.load("tsla.png").convert_alpha()
		self.twtr = pygame.image.load("twtr.png").convert_alpha()

		self.aapl2 = pygame.transform.scale(self.aapl, (180, 200))
		self.atvi2 = pygame.transform.scale(self.atvi, (180, 200))
		self.ea2 = pygame.transform.scale(self.ea, (180, 200))
		self.fb2 = pygame.transform.scale(self.fb, (180, 200))
		self.goog2 = pygame.transform.scale(self.goog, (180, 200))
		self.msft2 = pygame.transform.scale(self.msft, (180, 200))
		self.sbux2 = pygame.transform.scale(self.sbux, (180, 200))
		self.sny2 = pygame.transform.scale(self.sny, (180, 200))
		self.tsla2 = pygame.transform.scale(self.tsla, (180, 200))
		self.twtr2 = pygame.transform.scale(self.twtr, (180, 200))

	# run()

	def get_net_worth(self, companies):
		self.companies = companies

	def run(self, _companies):
		self.screen.blit(self.background, (0,0))

		self.screen.blit(self.aapl2, (195, 203))
		self.screen.blit(self.atvi2, (356.6, 203))
		self.screen.blit(self.ea2, (519, 203))
		self.screen.blit(self.fb2, (681.4, 203))
		self.screen.blit(self.goog2, (843.8, 203))
		self.screen.blit(self.msft2, (195, 356))
		self.screen.blit(self.sbux2, (356.6, 356))
		self.screen.blit(self.sny2, (519, 356))
		self.screen.blit(self.tsla2, (681.4, 356))
		self.screen.blit(self.twtr2, (843.8, 356))

		self.aapl2 = pygame.transform.scale(self.aapl, (int((_companies[0])**2*180), int(_companies[0]**2*200)))
		self.atvi2 = pygame.transform.scale(self.atvi, (int(_companies[1]**2*180), int(_companies[1]**2*200)))
		self.ea2 = pygame.transform.scale(self.ea, (int(_companies[2]**2*180), int(_companies[2]**2*200)))
		self.fb2 = pygame.transform.scale(self.fb, (int(_companies[3]**2*180), int(_companies[3]**2*200)))
		self.goog2 = pygame.transform.scale(self.goog, (int(_companies[4]**2*180), int(_companies[4]**2*200)))
		self.msft2 = pygame.transform.scale(self.msft, (int(_companies[5]**2*180), int(_companies[5]**2*200)))
		self.sbux2 = pygame.transform.scale(self.sbux, (int(_companies[6]**2*180), int(_companies[6]**2*200)))
		self.sny2 = pygame.transform.scale(self.sny, (int(_companies[7]**2*180), int(_companies[7]**2*200)))
		self.tsla2 = pygame.transform.scale(self.tsla, (int(_companies[8]**2*180), int(_companies[8]**2*200)))
		self.twtr2 = pygame.transform.scale(self.twtr, (int(_companies[9]**2*180), int(_companies[9]**2*200)))

		# h += 4
		# w += 4
		# image = pygame.transform.scale(image, (int(w), int(h)))
		pygame.display.update()
		# pygame.time.delay(10000)
		# # if (h > 300):
		# pygame.quit()