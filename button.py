import pygame

#button class
class Button():
	def __init__(self, x, y, image, scale, action=None, origin=-1):
		width = image.get_width()
		height = image.get_height()
		self.baseImage = image
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False
		self.action = action
		self.origin = origin
		self.scale = scale

	def draw(self, surface):
		action = False
		#get mouse position
		pos = pygame.mouse.get_pos()

		if self.rect.collidepoint(pos):
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN:	
					self.clicked = True
					action = True
					if(self.action != None):
						self.action()
						break
						
			
			
		#draw button on screen
		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action
	
	def setAction(self, action):
		self.action = action

	def setImage(self, image, scale):
		self.image = pygame.transform.scale(image, (int(image.get_width() * scale), int(image.get_height() * scale)))

	def setLocation(self, x, y):
		self.rect.topleft = (x, y)

	def setOrigin(self, origin):
		self.origin = origin

	def getImage(self):
		return self.image
	
	def getLocation(self):
		return self.rect.topleft
	
	def getOrigin(self):
		return self.origin
	
	def getScale(self):
		return self.scale
	
	def getAction(self):
		return self.action
	
	def duplicate(self):
		return Button(self.rect.topleft[0], self.rect.topleft[1], self.baseImage, self.scale, self.action, self.origin)