import pygame

class Enemy():
  def __init__(self, screen_x, screen_y, width, height, attackdmg, health, x_vel, y_vel):
    self.screen_x = screen_x + 300
    self.screen_y = screen_y + 300
    self.game_x = width // 2 #center
    self.game_y = height // 2 #center
    self.width = width
    self.height = height
    self.walkCount = 0
    self.x_vel = x_vel
    self.y_vel = y_vel
    self.hitbox = None
    self.hitbox_rect = None
    self.hitbox_visible = False
    self.attackdmg = attackdmg
    self.health = health
    self.maxhealth = health
    self.visible = True #alive
    self.colliding = False
    
  def draw(self, screen, bgx, bgy, walkRight, walkLeft, walkForward, walkBack, char):

    if self.health <= 0:
      self.visible = False
      return

    self.move(char)
      
    relative_bgx = self.screen_x + bgx
    relative_bgy = self.screen_y + bgy

    if self.walkCount + 1 >= 9:
      self.walkCount = 0

    dx = abs(abs(char.game_x) - abs(self.game_x)) #distance from player in the x-axis
    dy = abs(abs(char.game_y) - abs(self.game_y)) #distance from player in the y-axis

    if self.x_vel > 0 and dx >= dy:
      screen.blit(walkRight[self.walkCount // 3], (relative_bgx, relative_bgy))
      self.walkCount += 1
    elif self.x_vel < 0 and dx >= dy:
      screen.blit(walkLeft[self.walkCount // 3], (relative_bgx, relative_bgy))
      self.walkCount += 1
    elif self.y_vel > 0 and dy >= dx:
      screen.blit(walkForward[self.walkCount // 3], (relative_bgx, relative_bgy))
      self.walkCount += 1
    elif self.y_vel < 0 and dy >= dx:
      screen.blit(walkBack[self.walkCount // 3], (relative_bgx, relative_bgy))
      self.walkCount += 1
       
    self.hitbox = (relative_bgx, relative_bgy, self.width, self.height)
    self.hitbox_rect = pygame.Rect(self.hitbox)
    hitbox_centerx = pygame.Rect(self.hitbox).centerx
    hitbox_top = pygame.Rect(self.hitbox).top
    if self.hitbox_visible:
      pygame.draw.rect(screen, (255,0,0), self.hitbox, 2)

    #red health bar
    bar_width = self.width
    bar_height = 10

    red_hbar = pygame.Rect(self.hitbox[0], self.hitbox[1], bar_width, bar_height)
    red_hbar.centerx = hitbox_centerx
    red_hbar.bottom = hitbox_top - 5
    pygame.draw.rect(screen, (255,0,0), red_hbar)

    #green health bar
    green_hbar = pygame.Rect(red_hbar.left, red_hbar.top, bar_width-((bar_width/self.maxhealth)*(self.maxhealth-self.health)), bar_height)
    pygame.draw.rect(screen, (0,255,0), green_hbar)

    #health text
    health_font = pygame.font.Font('assets/fonts/8-bit fortress.ttf', 24)
    health_text = health_font.render(str(self.health), True, (0,255,0))
    health_text_rect = health_text.get_rect(center=(red_hbar.centerx, red_hbar.centery - 20))
    screen.blit(health_text, health_text_rect)

  def move(self, char):
    
    """if self.x_vel > 0:
      if self.screen_x + self.x_vel < self.path[1]:
        self.screen_x += self.x_vel
      else:
        self.x_vel = self.x_vel * -1
        self.walkCount = 0
    else:
      if self.screen_x - self.x_vel > self.path[0]:
        self.screen_x += self.x_vel
      else:
        self.x_vel = self.x_vel * -1
        self.walkCount = 0"""

    if self.colliding: return

    if self.game_x >= char.game_x + self.x_vel and self.game_x <= char.game_x - self.x_vel:
      same_x = True
    else:
      same_x = False

    if self.game_y >= char.game_y + self.y_vel and self.game_y <= char.game_y - self.y_vel:
      same_y = True
    else:
      same_y = False

    if not same_x:
      if self.x_vel > 0:
        if self.game_x < char.game_x:
          self.game_x += self.x_vel
          self.screen_x += self.x_vel
        else:
          self.x_vel = self.x_vel * -1
          self.walkCount = 0
      else:
        if self.game_x > char.game_x:
          self.game_x += self.x_vel
          self.screen_x += self.x_vel
        else:
          self.x_vel = self.x_vel * -1
          self.walkCount = 0

    if not same_y:
      if self.y_vel > 0:
        if self.game_y < char.game_y:
          self.game_y += self.y_vel
          self.screen_y += self.y_vel
        else:
          self.y_vel = self.y_vel * -1
          self.walkCount = 0
      else:
        if self.game_y > char.game_y:
          self.game_y += self.y_vel
          self.screen_y += self.y_vel
        else:
          self.y_vel = self.y_vel * -1
          self.walkCount = 0

  def collision(self):
    self.colliding = True

  def hit(self, damage): #called when hit by weapon
    self.health -= damage

class Tree(Enemy):
  def draw(self, screen, bgx, bgy, char): #called in main.py
    walkRight = [
      pygame.image.load("assets/e_tree/treeright.png"),
      pygame.image.load("assets/e_tree/treeright2.png"),
      pygame.image.load("assets/e_tree/treeright3.png")
    ]
      
    walkLeft = [
      pygame.image.load("assets/e_tree/treeleft.png"),
      pygame.image.load("assets/e_tree/treeleft3.png"),
      pygame.image.load("assets/e_tree/treeleft2.png")
    ]

    walkForward = [
      pygame.image.load("assets/e_tree/treeforward.png"),
      pygame.image.load("assets/e_tree/treeforward2.png"),
      pygame.image.load("assets/e_tree/treeforward3.png")
    ]

    walkBack = [
      pygame.image.load("assets/e_tree/treeback.png"),
      pygame.image.load("assets/e_tree/treeback2.png"),
      pygame.image.load("assets/e_tree/treeback3.png")
    ]

    Enemy.draw(self, screen, bgx, bgy, walkRight, walkLeft, walkForward, walkBack, char)

class Water(Enemy):
  def draw(self, screen, bgx, bgy, char): 
    walkRight = [
      pygame.image.load("assets/e_water/waterright1.png"),
      pygame.image.load("assets/e_water/waterright2.png"),
      pygame.image.load("assets/e_water/waterright3.png")
    ]
      
    walkLeft = [
      pygame.image.load("assets/e_water/waterleft1.png"),
      pygame.image.load("assets/e_water/waterleft2.png"),
      pygame.image.load("assets/e_water/waterleft3.png")
    ]

    walkForward = [
      pygame.image.load("assets/e_water/waterforward1.png"),
      pygame.image.load("assets/e_water/waterforward2.png"),
      pygame.image.load("assets/e_water/waterforward3.png")
    ]

    walkBack = [
      pygame.image.load("assets/e_water/waterback1.png"),
      pygame.image.load("assets/e_water/waterback2.png"),
      pygame.image.load("assets/e_water/waterback3.png")
    ]

    Enemy.draw(self, screen, bgx, bgy, walkRight, walkLeft, walkForward, walkBack, char)

class Skeleton(Enemy):
  def draw(self, screen, bgx, bgy, char):
    walkRight = [
      pygame.image.load("assets/e_skeleton/skelright1.png"),
      pygame.image.load("assets/e_skeleton/skelright2.png"),
      pygame.image.load("assets/e_skeleton/skelright3.png")
    ]
      
    walkLeft = [
      pygame.image.load("assets/e_skeleton/skelleft1.png"),
      pygame.image.load("assets/e_skeleton/skelleft3.png"),
      pygame.image.load("assets/e_skeleton/skelleft2.png")
    ]

    walkForward =[
      pygame.image.load("assets/e_skeleton/skelforward1.png"),
      pygame.image.load("assets/e_skeleton/skelforward3.png"),
      pygame.image.load("assets/e_skeleton/skelforward2.png")
    ]

    walkBack =[
      pygame.image.load("assets/e_skeleton/skelback1.png"),
      pygame.image.load("assets/e_skeleton/skelback3.png"),
      pygame.image.load("assets/e_skeleton/skelback2.png")
    ]

    Enemy.draw(self, screen, bgx, bgy, walkRight, walkLeft, walkForward, walkBack, char)

class Dragon(Enemy):
  def draw(self, screen, bgx, bgy, char): 
    walkRight = [
      pygame.image.load("assets/e_dragon/dragonright1.png"),
      pygame.image.load("assets/e_dragon/dragonright2.png"),
      pygame.image.load("assets/e_dragon/dragonright3.png")
    ]
      
    walkLeft = [
      pygame.image.load("assets/e_dragon/dragonleft1.png"),
      pygame.image.load("assets/e_dragon/dragonleft2.png"),
      pygame.image.load("assets/e_dragon/dragonleft3.png")
    ]

    walkForward = [
      pygame.image.load("assets/e_dragon/dragonforward1.png"),
      pygame.image.load("assets/e_dragon/dragonforward2.png"),
      pygame.image.load("assets/e_dragon/dragonforward3.png")
    ]

    walkBack = [
      pygame.image.load("assets/e_dragon/dragonback1.png"),
      pygame.image.load("assets/e_dragon/dragonback2.png"),
      pygame.image.load("assets/e_dragon/dragonback3.png")
    ]

    Enemy.draw(self, screen, bgx, bgy, walkRight, walkLeft, walkForward, walkBack, char)