import pygame
#mage height = 80 width = 40

class Player: #base class
  def __init__(self, screen_x, screen_y, width, height, health, stamina, mana):
    self.screen_x = screen_x
    self.screen_y = screen_y
    self.game_x = 300 + width // 2
    self.game_y = 0 + height // 2
    self.width = width
    self.height = height
    self.velocity = 10 #how fast the player moves
    self.isjump = False
    self.left = False
    self.right = False
    self.forward = False
    self.back = False
    self.walkCount = 0
    self.jumpCount = 10
    self.standing = True
    self.health, self.maxhealth = health, 100
    self.stamina, self.maxstamina = stamina, 100
    self.mana, self.maxmana = mana, 100
    self.current_weapon = None
    self.hitbox = (self.screen_x, self.screen_y, self.width, self.height)
    self.hitbox_rect = pygame.Rect(self.hitbox)
    self.hitbox_visible = False
    self.visible = True #alive

    #cooldown for taking damage
    self.counter = 0
    self.timer = 15

  def draw_resourcebar(self, screen, relative_y, current, max, color, iconpath):

    x = 40
    y = 520 + relative_y
    width = 200
    height = 30

    bar = pygame.Rect(x, y, width-((width/max)*(max-current)), height)
    pygame.draw.rect(screen, color, bar)

    bar_outline = pygame.Rect(bar.x, bar.y, width, height)
    pygame.draw.rect(screen, (0,0,0), bar_outline, 4)

    icon = pygame.image.load(iconpath)
    icon_rect = icon.get_rect()
    icon_rect.right = bar_outline.left - 5
    icon_rect.centery = bar_outline.centery
    screen.blit(icon, icon_rect)

    font = pygame.font.Font('assets/fonts/8-bit fortress.ttf', 24)
    text = font.render(str(current), True, (0,0,0))

    text_rect = text.get_rect()
    text_rect.left = bar_outline.right+5
    text_rect.centery = bar_outline.centery
    screen.blit(text, text_rect)

  def draw(self, screen, walkRight, walkLeft, walkForward, walkBack, standingchar, char_type):

    if not self.visible:
      return

    if self.walkCount + 1 >= 9:
      self.walkCount = 0

    if self.right:
      screen.blit(walkRight[self.walkCount // 3], (self.screen_x, self.screen_y))
      self.walkCount += 1

    elif self.left:
      screen.blit(walkLeft[self.walkCount // 3], (self.screen_x, self.screen_y))
      self.walkCount += 1

    elif self.forward:
      screen.blit(walkForward[self.walkCount // 3], (self.screen_x, self.screen_y))
      self.walkCount += 1

    elif self.back:
      screen.blit(walkBack[self.walkCount // 3], (self.screen_x, self.screen_y))
      self.walkCount += 1

    else:
      screen.blit(standingchar, (self.screen_x, self.screen_y))

    self.hitbox = (self.screen_x, self.screen_y, self.width, self.height)
    self.hitbox_rect = pygame.Rect(self.hitbox)
    if self.hitbox_visible:
      pygame.draw.rect(screen, (255,0,0), self.hitbox, 2)

    self.draw_resourcebar(screen, 0, self.health, self.maxhealth, (235,54,54), 'assets/menu/heart.png')
    if char_type == 'fighter':
      self.draw_resourcebar(screen, 40, self.stamina, self.maxstamina, (255,193,7), 'assets/menu/lightning.png')
    elif char_type == 'mage':
      self.draw_resourcebar(screen, 40, self.mana, self.maxmana, (224,64,251), 'assets/menu/star.PNG')

  def draw_sword(self, screen, walkRight, walkLeft, walkForward, walkBack, standingchar):

    if not self.visible:
      return

    if self.walkCount + 1 >= 9:
      self.walkCount = 0

    if self.right:
      screen.blit(walkRight[self.walkCount // 3], (self.screen_x, self.screen_y))
      self.walkCount += 1

    elif self.left:
      screen.blit(walkLeft[self.walkCount // 3], (self.screen_x-50, self.screen_y))
      self.walkCount += 1

    elif self.forward:
      screen.blit(walkForward[self.walkCount // 3], (self.screen_x, self.screen_y))
      self.walkCount += 1

    elif self.back:
      screen.blit(walkBack[self.walkCount // 3], (self.screen_x, self.screen_y))
      self.walkCount += 1

    else:
      screen.blit(standingchar, (self.screen_x, self.screen_y))

    self.hitbox = (self.screen_x, self.screen_y, self.width, self.height)
    self.hitbox_rect = pygame.Rect(self.hitbox)
    if self.hitbox_visible:
      pygame.draw.rect(screen, (255,0,0), self.hitbox, 2)

    self.draw_resourcebar(screen, 0, self.health, self.maxhealth, (235,54,54), 'assets/menu/heart.png')
    self.draw_resourcebar(screen, 40, self.stamina, self.maxstamina, (255,193,7), 'assets/menu/lightning.png')

  def draw_attack(self, screen, swingRight, swingLeft, swingForward, swingBack):

    if not self.visible:
      return

    if self.right:
      screen.blit(swingRight, (self.screen_x, self.screen_y))
    elif self.left:
      screen.blit(swingLeft, (self.screen_x-55, self.screen_y))
    elif self.forward:
      screen.blit(swingForward, (self.screen_x, self.screen_y))
    elif self.back:
      screen.blit(swingBack, (self.screen_x, self.screen_y-30))

    self.hitbox = (self.screen_x, self.screen_y, self.width, self.height)
    self.hitbox_rect = pygame.Rect(self.hitbox)
    if self.hitbox_visible:
      pygame.draw.rect(screen, (255,0,0), self.hitbox, 2)

    self.draw_resourcebar(screen, 0, self.health, self.maxhealth, (235,54,54), 'assets/menu/heart.png')
    self.draw_resourcebar(screen, 40, self.stamina, self.maxstamina, (255,193,7), 'assets/menu/lightning.png')

  def draw_wand(self, screen, walkRight, walkLeft, walkForward, walkBack, standingchar):

    if not self.visible:
      return

    if self.walkCount + 1 >= 9:
      self.walkCount = 0

    if self.right:
      screen.blit(walkRight[self.walkCount // 3], (self.screen_x, self.screen_y))
      self.walkCount += 1

    elif self.left:
      screen.blit(walkLeft[self.walkCount // 3], (self.screen_x, self.screen_y))
      self.walkCount += 1

    elif self.forward:
      screen.blit(walkForward[self.walkCount // 3], (self.screen_x, self.screen_y))
      self.walkCount += 1

    elif self.back:
      screen.blit(walkBack[self.walkCount // 3], (self.screen_x, self.screen_y))
      self.walkCount += 1

    else:
      screen.blit(standingchar, (self.screen_x, self.screen_y))

    self.hitbox = (self.screen_x, self.screen_y, self.width, self.height)
    self.hitbox_rect = pygame.Rect(self.hitbox)
    if self.hitbox_visible:
      pygame.draw.rect(screen, (255,0,0), self.hitbox, 2)

    self.draw_resourcebar(screen, 0, self.health, self.maxhealth, (235,54,54), 'assets/menu/heart.png')
    self.draw_resourcebar(screen, 40, self.mana, self.maxmana, (224,64,251), 'assets/menu/star.PNG')

  def collision(self, damage):
    if self.health > 1:
      if self.counter > self.timer:
        self.health -= damage
        self.counter = 0
      else:
        self.counter += 1
    else:
      self.visible = False

class Fighter(Player):

  def draw(self, screen): #called in main.py
    walkRight = [
      pygame.image.load("assets/p_fighter/rightwalk1.png"),
      pygame.image.load("assets/p_fighter/rightwalk2.png"),
      pygame.image.load("assets/p_fighter/rightwalk3.png")
    ]
    
    walkLeft = [
      pygame.image.load("assets/p_fighter/leftwalk1.png"),
      pygame.image.load("assets/p_fighter/leftwalk2.png"),
      pygame.image.load("assets/p_fighter/leftwalk3.png")
    ]
    
    walkForward = [
      pygame.image.load("assets/p_fighter/forwardwalk1.png"),
      pygame.image.load("assets/p_fighter/forwardwalk2.png"),
      pygame.image.load("assets/p_fighter/forwardwalk3.png")
    ]
    
    walkBack = [
      pygame.image.load("assets/p_fighter/backwardwalk1.png"),
      pygame.image.load("assets/p_fighter/backwardwalk2.png"),
      pygame.image.load("assets/p_fighter/backwardwalk3.png")
    ]

    standingchar = pygame.image.load("assets/p_fighter/standing.png")

    Player.draw(self, screen, walkRight, walkLeft, walkForward, walkBack, standingchar, 'fighter')

  def draw_forestsword(self, screen):
    walkRight = [
      pygame.image.load("assets/p_fighter/sword1/walk/rightwalk1.png"),
      pygame.image.load("assets/p_fighter/sword1/walk/rightwalk2.png"),
      pygame.image.load("assets/p_fighter/sword1/walk/rightwalk3.png")
    ]
    
    walkLeft = [
      pygame.image.load("assets/p_fighter/sword1/walk/leftwalk1.png"),
      pygame.image.load("assets/p_fighter/sword1/walk/leftwalk2.png"),
      pygame.image.load("assets/p_fighter/sword1/walk/leftwalk3.png")
    ]
    
    walkForward = [
      pygame.image.load("assets/p_fighter/sword1/walk/forwardwalk1.png"),
      pygame.image.load("assets/p_fighter/sword1/walk/forwardwalk2.png"),
      pygame.image.load("assets/p_fighter/sword1/walk/forwardwalk3.png")
    ]
    
    walkBack = [
      pygame.image.load("assets/p_fighter/sword1/walk/backwalk1.png"),
      pygame.image.load("assets/p_fighter/sword1/walk/backwalk2.png"),
      pygame.image.load("assets/p_fighter/sword1/walk/backwalk3.png")
    ]

    standingchar = pygame.image.load("assets/p_fighter/sword1/walk/forwardwalk1.png")

    Player.draw_sword(self, screen, walkRight, walkLeft, walkForward, walkBack, standingchar)

  def draw_forestsword_atk(self, screen):
    swingRight = pygame.image.load("assets/p_fighter/sword1/attack/rightswing2.png")
    swingLeft = pygame.image.load("assets/p_fighter/sword1/attack/leftswing2.png")
    swingForward = pygame.image.load("assets/p_fighter/sword1/attack/forwardswing2.png")
    swingBack = pygame.image.load("assets/p_fighter/sword1/attack/backswing2.png")

    Player.draw_attack(self, screen, swingRight, swingLeft, swingForward, swingBack)

  def draw_watersword(self, screen):
    walkRight = [
      pygame.image.load("assets/p_fighter/sword2/walk/rightwalk1.png"),
      pygame.image.load("assets/p_fighter/sword2/walk/rightwalk2.png"),
      pygame.image.load("assets/p_fighter/sword2/walk/rightwalk3.png")
    ]
    
    walkLeft = [
      pygame.image.load("assets/p_fighter/sword2/walk/leftwalk1.png"),
      pygame.image.load("assets/p_fighter/sword2/walk/leftwalk2.png"),
      pygame.image.load("assets/p_fighter/sword2/walk/leftwalk3.png")
    ]
    
    walkForward = [
      pygame.image.load("assets/p_fighter/sword2/walk/forwardwalk1.png"),
      pygame.image.load("assets/p_fighter/sword2/walk/forwardwalk2.png"),
      pygame.image.load("assets/p_fighter/sword2/walk/forwardwalk3.png")
    ]
    
    walkBack = [
      pygame.image.load("assets/p_fighter/sword2/walk/backwalk1.png"),
      pygame.image.load("assets/p_fighter/sword2/walk/backwalk2.png"),
      pygame.image.load("assets/p_fighter/sword2/walk/backwalk3.png")
    ]

    standingchar = pygame.image.load("assets/p_fighter/sword2/walk/forwardwalk1.png")

    Player.draw_sword(self, screen, walkRight, walkLeft, walkForward, walkBack, standingchar)

  def draw_watersword_atk(self, screen):
    swingRight = pygame.image.load("assets/p_fighter/sword2/attack/rightswing2.png")
    swingLeft = pygame.image.load("assets/p_fighter/sword2/attack/leftswing2.png")
    swingForward = pygame.image.load("assets/p_fighter/sword2/attack/forwardswing2.png")
    swingBack = pygame.image.load("assets/p_fighter/sword2/attack/backswing2.png")

    Player.draw_attack(self, screen, swingRight, swingLeft, swingForward, swingBack)

  def draw_firesword(self, screen):
    walkRight = [
      pygame.image.load("assets/p_fighter/sword3/walk/rightwalk1.png"),
      pygame.image.load("assets/p_fighter/sword3/walk/rightwalk2.png"),
      pygame.image.load("assets/p_fighter/sword3/walk/rightwalk3.png")
    ]
    
    walkLeft = [
      pygame.image.load("assets/p_fighter/sword3/walk/leftwalk1.png"),
      pygame.image.load("assets/p_fighter/sword3/walk/leftwalk2.png"),
      pygame.image.load("assets/p_fighter/sword3/walk/leftwalk3.png")
    ]
    
    walkForward = [
      pygame.image.load("assets/p_fighter/sword3/walk/forwardwalk1.png"),
      pygame.image.load("assets/p_fighter/sword3/walk/forwardwalk2.png"),
      pygame.image.load("assets/p_fighter/sword3/walk/forwardwalk3.png")
    ]
    
    walkBack = [
      pygame.image.load("assets/p_fighter/sword3/walk/backwalk1.png"),
      pygame.image.load("assets/p_fighter/sword3/walk/backwalk2.png"),
      pygame.image.load("assets/p_fighter/sword3/walk/backwalk3.png")
    ]

    standingchar = pygame.image.load("assets/p_fighter/sword3/walk/forwardwalk1.png")

    Player.draw_sword(self, screen, walkRight, walkLeft, walkForward, walkBack, standingchar)

  def draw_firesword_atk(self, screen):
    swingRight = pygame.image.load("assets/p_fighter/sword3/attack/rightswing2.png")
    swingLeft = pygame.image.load("assets/p_fighter/sword3/attack/leftswing2.png")
    swingForward = pygame.image.load("assets/p_fighter/sword3/attack/forwardswing2.png")
    swingBack = pygame.image.load("assets/p_fighter/sword3/attack/backswing2.png")

    Player.draw_attack(self, screen, swingRight, swingLeft, swingForward, swingBack)

  def draw_dungeonsword(self, screen):
    walkRight = [
      pygame.image.load("assets/p_fighter/sword4/walk/rightwalk1.png"),
      pygame.image.load("assets/p_fighter/sword4/walk/rightwalk2.png"),
      pygame.image.load("assets/p_fighter/sword4/walk/rightwalk3.png")
    ]
    
    walkLeft = [
      pygame.image.load("assets/p_fighter/sword4/walk/leftwalk1.png"),
      pygame.image.load("assets/p_fighter/sword4/walk/leftwalk2.png"),
      pygame.image.load("assets/p_fighter/sword4/walk/leftwalk3.png")
    ]
    
    walkForward = [
      pygame.image.load("assets/p_fighter/sword4/walk/forwardwalk1.png"),
      pygame.image.load("assets/p_fighter/sword4/walk/forwardwalk2.png"),
      pygame.image.load("assets/p_fighter/sword4/walk/forwardwalk3.png")
    ]
    
    walkBack = [
      pygame.image.load("assets/p_fighter/sword4/walk/backwalk1.png"),
      pygame.image.load("assets/p_fighter/sword4/walk/backwalk2.png"),
      pygame.image.load("assets/p_fighter/sword4/walk/backwalk3.png")
    ]

    standingchar = pygame.image.load("assets/p_fighter/sword4/walk/forwardwalk1.png")

    Player.draw_sword(self, screen, walkRight, walkLeft, walkForward, walkBack, standingchar)

  def draw_dungeonsword_atk(self, screen):
    swingRight = pygame.image.load("assets/p_fighter/sword4/attack/rightswing2.png")
    swingLeft = pygame.image.load("assets/p_fighter/sword4/attack/leftswing2.png")
    swingForward = pygame.image.load("assets/p_fighter/sword4/attack/forwardswing2.png")
    swingBack = pygame.image.load("assets/p_fighter/sword4/attack/backswing2.png")

    Player.draw_attack(self, screen, swingRight, swingLeft, swingForward, swingBack)

class Mage(Player):

  def draw(self, screen): #called in main.py
    walkRight = [
      pygame.image.load("assets/p_mage/rightwalk1.png"),
      pygame.image.load("assets/p_mage/rightwalk2.png"),
      pygame.image.load("assets/p_mage/rightwalk3.png")
    ]
    
    walkLeft = [
      pygame.image.load("assets/p_mage/leftwalk1.png"),
      pygame.image.load("assets/p_mage/leftwalk2.png"),
      pygame.image.load("assets/p_mage/leftwalk3.png")
    ]
    
    walkForward = [
      pygame.image.load("assets/p_mage/forwardwalk1.png"),
      pygame.image.load("assets/p_mage/forwardwalk2.png"),
      pygame.image.load("assets/p_mage/forwardwalk3.png")
    ]
    
    walkBack = [
      pygame.image.load("assets/p_mage/backwalk1.png"),
      pygame.image.load("assets/p_mage/backwalk2.png"),
      pygame.image.load("assets/p_mage/backwalk3.png")
    ]

    standingchar = pygame.image.load("assets/p_mage/forwardwalk1.png")

    Player.draw(self, screen, walkRight, walkLeft, walkForward, walkBack, standingchar, 'mage')

  def draw_forestwand(self, screen):
    walkRight = [
      pygame.image.load("assets/p_mage/wand1/mageright1.png"),
      pygame.image.load("assets/p_mage/wand1/mageright2.png"),
      pygame.image.load("assets/p_mage/wand1/mageright3.png")
    ]
    
    walkLeft = [
      pygame.image.load("assets/p_mage/wand1/mageleft1.png"),
      pygame.image.load("assets/p_mage/wand1/mageleft2.png"),
      pygame.image.load("assets/p_mage/wand1/mageleft3.png")
    ]
    
    walkForward = [
      pygame.image.load("assets/p_mage/wand1/mageforward1.png"),
      pygame.image.load("assets/p_mage/wand1/mageforward2.png"),
      pygame.image.load("assets/p_mage/wand1/mageforward3.png")
    ]
    
    walkBack = [
      pygame.image.load("assets/p_mage/wand1/mageback1.png"),
      pygame.image.load("assets/p_mage/wand1/mageback2.png"),
      pygame.image.load("assets/p_mage/wand1/mageback3.png")
    ]

    standingchar = pygame.image.load("assets/p_mage/wand1/mageforward1.png")

    Player.draw_wand(self, screen, walkRight, walkLeft, walkForward, walkBack, standingchar)

  def draw_waterwand(self, screen):
    walkRight = [
      pygame.image.load("assets/p_mage/wand2/mageright1.png"),
      pygame.image.load("assets/p_mage/wand2/mageright2.png"),
      pygame.image.load("assets/p_mage/wand2/mageright3.png")
    ]
    
    walkLeft = [
      pygame.image.load("assets/p_mage/wand2/mageleft1.png"),
      pygame.image.load("assets/p_mage/wand2/mageleft2.png"),
      pygame.image.load("assets/p_mage/wand2/mageleft3.png")
    ]
    
    walkForward = [
      pygame.image.load("assets/p_mage/wand2/mageforward1.png"),
      pygame.image.load("assets/p_mage/wand2/mageforward2.png"),
      pygame.image.load("assets/p_mage/wand2/mageforward3.png")
    ]
    
    walkBack = [
      pygame.image.load("assets/p_mage/wand2/mageback1.png"),
      pygame.image.load("assets/p_mage/wand2/mageback2.png"),
      pygame.image.load("assets/p_mage/wand2/mageback3.png")
    ]

    standingchar = pygame.image.load("assets/p_mage/wand2/mageforward1.png")

    Player.draw_wand(self, screen, walkRight, walkLeft, walkForward, walkBack, standingchar)

  def draw_firewand(self, screen):
    walkRight = [
      pygame.image.load("assets/p_mage/wand3/mageright1.png"),
      pygame.image.load("assets/p_mage/wand3/mageright2.png"),
      pygame.image.load("assets/p_mage/wand3/mageright3.png")
    ]
    
    walkLeft = [
      pygame.image.load("assets/p_mage/wand3/mageleft1.png"),
      pygame.image.load("assets/p_mage/wand3/mageleft2.png"),
      pygame.image.load("assets/p_mage/wand3/mageleft3.png")
    ]
    
    walkForward = [
      pygame.image.load("assets/p_mage/wand3/mageforward1.png"),
      pygame.image.load("assets/p_mage/wand3/mageforward2.png"),
      pygame.image.load("assets/p_mage/wand3/mageforward3.png")
    ]
    
    walkBack = [
      pygame.image.load("assets/p_mage/wand3/mageback1.png"),
      pygame.image.load("assets/p_mage/wand3/mageback2.png"),
      pygame.image.load("assets/p_mage/wand3/mageback3.png")
    ]

    standingchar = pygame.image.load("assets/p_mage/wand3/mageforward1.png")

    Player.draw_wand(self, screen, walkRight, walkLeft, walkForward, walkBack, standingchar)

  def draw_dungeonwand(self, screen):
    walkRight = [
      pygame.image.load("assets/p_mage/wand4/mageright1.png"),
      pygame.image.load("assets/p_mage/wand4/mageright2.png"),
      pygame.image.load("assets/p_mage/wand4/mageright3.png")
    ]
    
    walkLeft = [
      pygame.image.load("assets/p_mage/wand4/mageleft1.png"),
      pygame.image.load("assets/p_mage/wand4/mageleft2.png"),
      pygame.image.load("assets/p_mage/wand4/mageleft3.png")
    ]
    
    walkForward = [
      pygame.image.load("assets/p_mage/wand4/mageforward1.png"),
      pygame.image.load("assets/p_mage/wand4/mageforward2.png"),
      pygame.image.load("assets/p_mage/wand4/mageforward3.png")
    ]
    
    walkBack = [
      pygame.image.load("assets/p_mage/wand4/mageback1.png"),
      pygame.image.load("assets/p_mage/wand4/mageback2.png"),
      pygame.image.load("assets/p_mage/wand4/mageback3.png")
    ]

    standingchar = pygame.image.load("assets/p_mage/wand4/mageforward1.png")

    Player.draw_wand(self, screen, walkRight, walkLeft, walkForward, walkBack, standingchar)

class Nimble(Player):

  def draw(self, screen): #called in main.py
    walkRight = [
      pygame.image.load("assets/p_nimble/nimbleright1.png"),
      pygame.image.load("assets/p_nimble/nimbleright2.png"),
      pygame.image.load("assets/p_nimble/nimbleright3.png")
    ]
    
    walkLeft = [
      pygame.image.load("assets/p_nimble/nimbleleft1.png"),
      pygame.image.load("assets/p_nimble/nimbleleft2.png"),
      pygame.image.load("assets/p_nimble/nimbleleft3.png")
    ]
    
    walkForward = [
      pygame.image.load("assets/p_nimble/nimbleforward1.png"),
      pygame.image.load("assets/p_nimble/nimbleforward2.png"),
      pygame.image.load("assets/p_nimble/nimbleforward3.png")
    ]
    
    walkBack = [
      pygame.image.load("assets/p_nimble/nimbleback1.png"),
      pygame.image.load("assets/p_nimble/nimbleback2.png"),
      pygame.image.load("assets/p_nimble/nimbleback3.png")
    ]

    standingchar = pygame.image.load("assets/p_nimble/nimblestanding.png")
    
    Player.draw(self, screen, walkRight, walkLeft, walkForward, walkBack, standingchar)