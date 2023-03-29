import pygame

class Melee:
  def __init__(self, char, damage, stamina_use):
    self.char = char
    self.damage = damage
    self.stamina_use = stamina_use
    self.hitbox = None
    self.hitbox_rect = None
    self.hitbox_visible = False
  
  def draw(self, screen):
    
    if self.char.right:
      self.hitbox = (self.char.screen_x+40, self.char.screen_y+45, 54, 17)
      self.hitbox_rect = pygame.Rect(self.hitbox)
    elif self.char.left:
      self.hitbox = (self.char.screen_x-56, self.char.screen_y+45, 54, 17)
      self.hitbox_rect = pygame.Rect(self.hitbox)
    elif self.char.forward:
      self.hitbox = (self.char.screen_x+4, self.char.screen_y+67, 17, 54)
      self.hitbox_rect = pygame.Rect(self.hitbox)
    elif self.char.back:
      self.hitbox = (self.char.screen_x+34, self.char.screen_y-32, 17, 54)
      self.hitbox_rect = pygame.Rect(self.hitbox)
    else: #on spawn
      self.hitbox = (self.char.screen_x+4, self.char.screen_y+67, 17, 54)
      self.hitbox_rect = pygame.Rect(self.hitbox)

    if self.hitbox_visible:
      pygame.draw.rect(screen, (255,0,0), self.hitbox, 2)

  def hit(self):
    print('sword hit')