import pygame

class Projectile(object): #visual orb
  def __init__(self, x, y, radius, color, imagename, x_dir, y_dir):
    self.x = x
    self.y = y
    self.radius = radius
    self.color = color
    self.image = pygame.transform.scale(pygame.image.load(f'assets/p_mage/orbs/{imagename}'), (25, 25))
    self.rect = None
    self.x_dir = x_dir
    self.x_vel = 15 * x_dir
    self.y_dir = y_dir
    self.y_vel = 15 * y_dir

  def draw(self, screen):
    self.rect = self.image.get_rect(center=(self.x, self.y))
    screen.blit(self.image, self.rect)

class Orb(): #orb in code
  def __init__(self, damage, mana_cost, max_onscreen):
    self.damage = damage
    self.mana_cost = mana_cost
    self.max_onscreen = max_onscreen