class Button():
  def __init__(self, image, x_pos, y_pos):
    self.image = image
    self.x_pos = x_pos
    self.y_pos = y_pos
    self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

  def update(self, screen):
    screen.blit(self.image, self.rect)

  def update_oldman(self, screen, bgx, bgy):
    relative_bgx = self.x_pos + bgx
    relative_bgy = self.y_pos + bgy

    screen.blit(self.image, (relative_bgx, relative_bgy))

  def checkForInput(self, mouse_pos):
    if mouse_pos[0] in range(self.rect.left, self.rect.right) and mouse_pos[1] in range(self.rect.top, self.rect.bottom):
      return True
    else:
      return False