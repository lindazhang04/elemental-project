#ELEMENTAL GAME - Linda Zhang & Victor Yu

import pygame, sys, time
from button import Button
from oldman import f_oldman1, m_oldman1, oldman10
from player import Fighter, Mage, Nimble
from enemy import Tree, Water, Skeleton, Dragon
from projectile import Projectile, Orb
from melee import Melee

pygame.init()

SCREEN = pygame.display.set_mode((600, 600))

GAME_LOGO = pygame.image.load('assets/menu/oldman.png')
pygame.display.set_icon(GAME_LOGO)
pygame.display.set_caption("Elemental")

def play_flowerfield(char_type, cur_health, cur_stamina, cur_mana):

  bgx, bgy = -300, 0
  bg = pygame.image.load("assets/backgrounds/endbg.PNG")

  if char_type == 'fighter':
    char = Fighter(300, 300, 40, 85, cur_health, cur_stamina, cur_mana)
    sword = Melee(char, 1, 2)
  elif char_type == 'mage':
    char = Mage(300, 300, 40, 85, cur_health, cur_stamina, cur_mana)
    orb = Orb(1, 1, 3)
    
  bullets = []
  shootLoop = 0 # lessens bullet spam

  k_z = False
  swingCount = 0
  
  while True:

    SCREEN.blit(bg, (bgx, bgy))
      
    clock = pygame.time.Clock()
    PLAY_MOUSE_POS = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()

    BACK_BUTTON_SURFACE = pygame.transform.scale(pygame.image.load("assets/buttons/back.png"), (100, 30))
    BACK_BUTTON = Button(BACK_BUTTON_SURFACE, 50, 15)

    if bgx < -250 and bgx > -300 and bgy == -410:

      press_x = pygame.transform.scale(pygame.image.load("assets/menu/press_x.PNG"), (125, 52))
      press_x_rect = press_x.get_rect(center=(char.screen_x+char.width/2, char.screen_y-80))
      SCREEN.blit(press_x, press_x_rect)

      if keys[pygame.K_x]:
        oldman10(SCREEN)
        playagain(SCREEN)

    if keys[pygame.K_p]:
      print(bgx,bgy)

    if keys[pygame.K_RIGHT]:
      char.right = True
      char.left = False
      char.forward = False
      char.back = False   
      char.standing = False

      if bgx > -600:
        bgx -= char.velocity
        char.game_x += char.velocity          

    elif keys[pygame.K_LEFT]:
      char.right = False
      char.left = True
      char.forward = False
      char.back = False
      char.standing = False

      if bgx < 0:
        bgx += char.velocity
        char.game_x -= char.velocity  

    elif keys[pygame.K_UP]:
      char.right = False
      char.left = False
      char.forward = False
      char.back = True
      char.standing = False

      if bgy < 0:
        bgy += char.velocity
        char.game_y -= char.velocity
        
    elif keys[pygame.K_DOWN]:
      char.right = False
      char.left = False
      char.forward = True
      char.back = False
      char.standing = False

      if bgy > -410:
        bgy -= char.velocity  
        char.game_y += char.velocity 
      
    else:
      char.standing = True
      char.walkCount = 0
    
    if char_type == 'fighter':
      if k_z and char.stamina > sword.stamina_use:
        if swingCount < 4:
          char.draw_dungeonsword_atk(SCREEN)
          swingCount += 1
        else:
          char.draw_dungeonsword(SCREEN)
      else:
        char.draw_dungeonsword(SCREEN)
      sword.draw(SCREEN) #hitbox

      if char.stamina < char.maxstamina:
        char.stamina += 1
        
    elif char_type == 'mage':

      if shootLoop > 0:
        shootLoop += 1
      if shootLoop > 3:
        shootLoop = 0
        
      if keys[pygame.K_z] and shootLoop == 0:
        if char.left:
          x_dir = -1
          y_dir = 0
        elif char.right:
          x_dir = 1
          y_dir = 0
        elif char.back:
          x_dir = 0
          y_dir = -1
        elif char.forward:
          x_dir = 0
          y_dir = 1
        else: #on character spawn
          x_dir = 0
          y_dir = 1
    
        if len(bullets) < orb.max_onscreen and char.mana > orb.mana_cost:
          bullets.append(Projectile(char.screen_x + char.width // 2, char.screen_y + char.height // 2, 6, (0,0,0), 'orb4.png', x_dir, y_dir))

        if char.mana >= orb.mana_cost:
          char.mana -= orb.mana_cost

        shootLoop = 1

      for bullet in bullets:
        
        #check if bullet is within game window
        if bullet.x < 600 and bullet.x > 0 and bullet.y < 600 and bullet.y > 0:
          bullet.x += bullet.x_vel
          bullet.y += bullet.y_vel
        else:
          bullets.pop(bullets.index(bullet))

        bullet.draw(SCREEN)

      char.draw_dungeonwand(SCREEN)

      if char.mana < char.maxmana:
        char.mana += 1
      
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.KEYDOWN:
        
        if event.key == pygame.K_z:
          k_z = True
          swingCount = 0

          if char_type == 'fighter':
            if char.stamina >= sword.stamina_use:
              char.stamina -= sword.stamina_use
                
      if event.type == pygame.MOUSEBUTTONDOWN:
        if BACK_BUTTON.checkForInput(PLAY_MOUSE_POS):
          char_select()

    BACK_BUTTON.update(SCREEN)
    pygame.display.update()
    clock.tick(24)  #fps

def play_dungeon(char_type, cur_health, cur_stamina, cur_mana):

  bgx, bgy = -300, 0
  bg = pygame.image.load("assets/backgrounds/dungeonbg.PNG")

  if char_type == 'fighter':
    char = Fighter(300, 300, 40, 85, cur_health, cur_stamina, cur_mana)
    sword = Melee(char, 10, 15)
  elif char_type == 'mage':
    char = Mage(300, 300, 40, 85, cur_health, cur_stamina, cur_mana)
    orb = Orb(3, 20, 5)
    
  enemy = Dragon(0, 0, 95, 70, 20, 200, 5, 5)
  bullets = []
  shootLoop = 0 # lessens bullet spam

  k_z = False
  swingCount = 0
  
  while True:

    SCREEN.blit(bg, (bgx, bgy))
    
    if bgy == -560 and not enemy.visible:
      play_flowerfield(char_type, char.health, char.stamina, char.mana)
      
    clock = pygame.time.Clock()
    PLAY_MOUSE_POS = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()

    BACK_BUTTON_SURFACE = pygame.transform.scale(pygame.image.load("assets/buttons/back.png"), (100, 30))
    BACK_BUTTON = Button(BACK_BUTTON_SURFACE, 50, 15)

    if keys[pygame.K_p]:
      print(bgx,bgy)

    if char.visible: #if the player is alive

      if keys[pygame.K_RIGHT]:
        char.right = True
        char.left = False
        char.forward = False
        char.back = False   
        char.standing = False

        if bgx > -600:
          bgx -= char.velocity
          char.game_x += char.velocity          

      elif keys[pygame.K_LEFT]:
        char.right = False
        char.left = True
        char.forward = False
        char.back = False
        char.standing = False

        if bgx < 0:
          bgx += char.velocity
          char.game_x -= char.velocity  

      elif keys[pygame.K_UP]:
        char.right = False
        char.left = False
        char.forward = False
        char.back = True
        char.standing = False

        if bgy < 0:
          bgy += char.velocity
          char.game_y -= char.velocity
          
      elif keys[pygame.K_DOWN]:
        char.right = False
        char.left = False
        char.forward = True
        char.back = False
        char.standing = False

        if bgy > -560:
          bgy -= char.velocity  
          char.game_y += char.velocity 
        
      else:
        char.standing = True
        char.walkCount = 0

      enemy.draw(SCREEN, bgx, bgy, char)
      
      if char_type == 'fighter':
        if k_z and char.stamina > sword.stamina_use:
          if swingCount < 4:
            char.draw_dungeonsword_atk(SCREEN)
            if enemy.visible and sword.hitbox_rect.colliderect(enemy.hitbox_rect) and swingCount == 0:
              enemy.hit(sword.damage)
            swingCount += 1
          else:
            char.draw_dungeonsword(SCREEN)
        else:
          char.draw_dungeonsword(SCREEN)
        sword.draw(SCREEN) #hitbox

        if char.stamina < char.maxstamina:
          char.stamina += 1
          
      elif char_type == 'mage':

        if shootLoop > 0:
          shootLoop += 1
        if shootLoop > 3:
          shootLoop = 0
          
        if keys[pygame.K_z] and shootLoop == 0:
          if char.left:
            x_dir = -1
            y_dir = 0
          elif char.right:
            x_dir = 1
            y_dir = 0
          elif char.back:
            x_dir = 0
            y_dir = -1
          elif char.forward:
            x_dir = 0
            y_dir = 1
          else: #on character spawn
            x_dir = 0
            y_dir = 1
      
          if len(bullets) < orb.max_onscreen and char.mana > orb.mana_cost:
            bullets.append(Projectile(char.screen_x + char.width // 2, char.screen_y + char.height // 2, 6, (0,0,0), 'orb4.png', x_dir, y_dir))
  
          if char.mana >= orb.mana_cost:
            char.mana -= orb.mana_cost

          shootLoop = 1

        for bullet in bullets:

          if bullet.rect != None:
            if bullet.rect.colliderect(enemy.hitbox_rect):
              if enemy.visible:
                enemy.hit(orb.damage)
                bullets.pop(bullets.index(bullet))
          
          #check if bullet is within game window
          if bullet.x < 600 and bullet.x > 0 and bullet.y < 600 and bullet.y > 0:
            bullet.x += bullet.x_vel
            bullet.y += bullet.y_vel
          else:
            bullets.pop(bullets.index(bullet))

          bullet.draw(SCREEN)

        char.draw_dungeonwand(SCREEN)

        if char.mana < char.maxmana:
          char.mana += 1

      if enemy.visible:
        if char.hitbox_rect.colliderect(enemy.hitbox_rect):
          char.collision(enemy.attackdmg)
          enemy.collision()
        else:
          enemy.colliding = False

    else: #game over
      lose(SCREEN)
      
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.KEYDOWN:
        
        if event.key == pygame.K_z:
          k_z = True
          swingCount = 0

          if char_type == 'fighter':
            if char.stamina >= sword.stamina_use:
              char.stamina -= sword.stamina_use
                
      if event.type == pygame.MOUSEBUTTONDOWN:
        if BACK_BUTTON.checkForInput(PLAY_MOUSE_POS):
          char_select()

    BACK_BUTTON.update(SCREEN)
    pygame.display.update()
    clock.tick(24)  #fps

def play_fire(char_type, cur_health, cur_stamina, cur_mana):

  bgx, bgy = -300, 0
  bg = pygame.image.load("assets/backgrounds/firebg.PNG")

  if char_type == 'fighter':
    char = Fighter(300, 300, 40, 85, cur_health, cur_stamina, cur_mana)
    sword = Melee(char, 5, 15)
  elif char_type == 'mage':
    char = Mage(300, 300, 40, 85, cur_health, cur_stamina, cur_mana)
    orb = Orb(5, 20, 5)
    
  enemy = Skeleton(0, 0, 40, 85, 15, 100, 3, 3)
  bullets = []
  shootLoop = 0 # lessens bullet spam

  k_z = False
  swingCount = 0
  
  while True:

    SCREEN.blit(bg, (bgx, bgy))
    
    if bgy == -560 and not enemy.visible:
      play_dungeon(char_type, char.health, char.stamina, char.mana)
      
    clock = pygame.time.Clock()
    PLAY_MOUSE_POS = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()

    BACK_BUTTON_SURFACE = pygame.transform.scale(pygame.image.load("assets/buttons/back.png"), (100, 30))
    BACK_BUTTON = Button(BACK_BUTTON_SURFACE, 50, 15)

    if keys[pygame.K_p]:
      print(bgx,bgy)

    if char.visible: #if the player is alive

      if keys[pygame.K_RIGHT]:
        char.right = True
        char.left = False
        char.forward = False
        char.back = False   
        char.standing = False

        if bgx > -600:
          bgx -= char.velocity
          char.game_x += char.velocity          

      elif keys[pygame.K_LEFT]:
        char.right = False
        char.left = True
        char.forward = False
        char.back = False
        char.standing = False

        if bgx < 0:
          bgx += char.velocity
          char.game_x -= char.velocity  

      elif keys[pygame.K_UP]:
        char.right = False
        char.left = False
        char.forward = False
        char.back = True
        char.standing = False

        if bgy < 0:
          bgy += char.velocity
          char.game_y -= char.velocity
          
      elif keys[pygame.K_DOWN]:
        char.right = False
        char.left = False
        char.forward = True
        char.back = False
        char.standing = False

        if bgy > -560:
          bgy -= char.velocity  
          char.game_y += char.velocity 
        
      else:
        char.standing = True
        char.walkCount = 0

      enemy.draw(SCREEN, bgx, bgy, char)
      
      if char_type == 'fighter':
        if k_z and char.stamina > sword.stamina_use:
          if swingCount < 4:
            char.draw_firesword_atk(SCREEN)
            if enemy.visible and sword.hitbox_rect.colliderect(enemy.hitbox_rect) and swingCount == 0:
              enemy.hit(sword.damage)
            swingCount += 1
          else:
            char.draw_firesword(SCREEN)
        else:
          char.draw_firesword(SCREEN)
        sword.draw(SCREEN) #hitbox

        if char.stamina < char.maxstamina:
          char.stamina += 1
          
      elif char_type == 'mage':

        if shootLoop > 0:
          shootLoop += 1
        if shootLoop > 3:
          shootLoop = 0
          
        if keys[pygame.K_z] and shootLoop == 0:
          if char.left:
            x_dir = -1
            y_dir = 0
          elif char.right:
            x_dir = 1
            y_dir = 0
          elif char.back:
            x_dir = 0
            y_dir = -1
          elif char.forward:
            x_dir = 0
            y_dir = 1
          else: #on character spawn
            x_dir = 0
            y_dir = 1
      
          if len(bullets) < orb.max_onscreen and char.mana > orb.mana_cost:
            bullets.append(Projectile(char.screen_x + char.width // 2, char.screen_y + char.height // 2, 6, (0,0,0), 'orb3.png', x_dir, y_dir))
  
          if char.mana >= orb.mana_cost:
            char.mana -= orb.mana_cost

          shootLoop = 1

        for bullet in bullets:

          if bullet.rect != None:
            if bullet.rect.colliderect(enemy.hitbox_rect):
              if enemy.visible:
                enemy.hit(orb.damage)
                bullets.pop(bullets.index(bullet))
          
          #check if bullet is within game window
          if bullet.x < 600 and bullet.x > 0 and bullet.y < 600 and bullet.y > 0:
            bullet.x += bullet.x_vel
            bullet.y += bullet.y_vel
          else:
            bullets.pop(bullets.index(bullet))

          bullet.draw(SCREEN)

        char.draw_firewand(SCREEN)

        if char.mana < char.maxmana:
          char.mana += 1

      if enemy.visible:
        if char.hitbox_rect.colliderect(enemy.hitbox_rect):
          char.collision(enemy.attackdmg)
          enemy.collision()
        else:
          enemy.colliding = False

    else: #game over
      lose(SCREEN)
      
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.KEYDOWN:
        
        if event.key == pygame.K_z:
          k_z = True
          swingCount = 0

          if char_type == 'fighter':
            if char.stamina >= sword.stamina_use:
              char.stamina -= sword.stamina_use
                
      if event.type == pygame.MOUSEBUTTONDOWN:
        if BACK_BUTTON.checkForInput(PLAY_MOUSE_POS):
          char_select()

    BACK_BUTTON.update(SCREEN)
    pygame.display.update()
    clock.tick(24)  #fps

def play_water(char_type, cur_health, cur_stamina, cur_mana):

  bgx, bgy = -300, 0
  bg = pygame.image.load("assets/backgrounds/waterbg.PNG")

  if char_type == 'fighter':
    char = Fighter(300, 300, 40, 85, cur_health, cur_stamina, cur_mana)
    sword = Melee(char, 3, 15)
  elif char_type == 'mage':
    char = Mage(300, 300, 40, 85, cur_health, cur_stamina, cur_mana)
    orb = Orb(3, 25, 3)
    
  enemy = Water(0, 0, 130, 50, 10, 50, 6, 4)
  bullets = []
  shootLoop = 0 # lessens bullet spam

  k_z = False
  swingCount = 0
  
  while True:

    SCREEN.blit(bg, (bgx, bgy))
    
    if bgy < -485 and not enemy.visible:
      play_fire(char_type, char.health, char.stamina, char.mana)
      
    clock = pygame.time.Clock()
    PLAY_MOUSE_POS = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()

    BACK_BUTTON_SURFACE = pygame.transform.scale(pygame.image.load("assets/buttons/back.png"), (100, 30))
    BACK_BUTTON = Button(BACK_BUTTON_SURFACE, 50, 15)

    if keys[pygame.K_p]:
      print(bgx,bgy)

    if char.visible: #if the player is alive

      if keys[pygame.K_RIGHT]:
        char.right = True
        char.left = False
        char.forward = False
        char.back = False   
        char.standing = False

        if bgx > -600:
          bgx -= char.velocity
          char.game_x += char.velocity          

      elif keys[pygame.K_LEFT]:
        char.right = False
        char.left = True
        char.forward = False
        char.back = False
        char.standing = False

        if bgx < 0:
          bgx += char.velocity
          char.game_x -= char.velocity  

      elif keys[pygame.K_UP]:
        char.right = False
        char.left = False
        char.forward = False
        char.back = True
        char.standing = False

        if bgy < 0:
          bgy += char.velocity
          char.game_y -= char.velocity
          
      elif keys[pygame.K_DOWN]:
        char.right = False
        char.left = False
        char.forward = True
        char.back = False
        char.standing = False

        if bgy > -560:
          bgy -= char.velocity  
          char.game_y += char.velocity 
        
      else:
        char.standing = True
        char.walkCount = 0

      enemy.draw(SCREEN, bgx, bgy, char)
      
      if char_type == 'fighter':
        if k_z and char.stamina > sword.stamina_use:
          if swingCount < 4:
            char.draw_watersword_atk(SCREEN)
            if enemy.visible and sword.hitbox_rect.colliderect(enemy.hitbox_rect) and swingCount == 0:
              enemy.hit(sword.damage)
            swingCount += 1
          else:
            char.draw_watersword(SCREEN)
        else:
          char.draw_watersword(SCREEN)
        sword.draw(SCREEN) #hitbox

        if char.stamina < char.maxstamina:
          char.stamina += 1
          
      elif char_type == 'mage':

        if shootLoop > 0:
          shootLoop += 1
        if shootLoop > 3:
          shootLoop = 0
          
        if keys[pygame.K_z] and shootLoop == 0:
          if char.left:
            x_dir = -1
            y_dir = 0
          elif char.right:
            x_dir = 1
            y_dir = 0
          elif char.back:
            x_dir = 0
            y_dir = -1
          elif char.forward:
            x_dir = 0
            y_dir = 1
          else: #on character spawn
            x_dir = 0
            y_dir = 1
      
          if len(bullets) < orb.max_onscreen and char.mana > orb.mana_cost:
            bullets.append(Projectile(char.screen_x + char.width // 2, char.screen_y + char.height // 2, 6, (0,0,0), 'orb2.png', x_dir, y_dir))
  
          if char.mana >= orb.mana_cost:
            char.mana -= orb.mana_cost

          shootLoop = 1

        for bullet in bullets:

          if bullet.rect != None:
            if bullet.rect.colliderect(enemy.hitbox_rect):
              if enemy.visible:
                enemy.hit(orb.damage)
                bullets.pop(bullets.index(bullet))
          
          #check if bullet is within game window
          if bullet.x < 600 and bullet.x > 0 and bullet.y < 600 and bullet.y > 0:
            bullet.x += bullet.x_vel
            bullet.y += bullet.y_vel
          else:
            bullets.pop(bullets.index(bullet))

          bullet.draw(SCREEN)

        char.draw_waterwand(SCREEN)

        if char.mana < char.maxmana:
          char.mana += 1

      if enemy.visible:
        if char.hitbox_rect.colliderect(enemy.hitbox_rect):
          char.collision(enemy.attackdmg)
          enemy.collision()
        else:
          enemy.colliding = False

    else: #game over
      lose(SCREEN)
      
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.KEYDOWN:
        
        if event.key == pygame.K_z:
          k_z = True
          swingCount = 0

          if char_type == 'fighter':
            if char.stamina >= sword.stamina_use:
              char.stamina -= sword.stamina_use
                
      if event.type == pygame.MOUSEBUTTONDOWN:
        if BACK_BUTTON.checkForInput(PLAY_MOUSE_POS):
          char_select()

    BACK_BUTTON.update(SCREEN)
    pygame.display.update()
    clock.tick(24)  #fps

def play_forest(char_type, cur_health, cur_stamina, cur_mana):

  bgx, bgy = -300, 0
  bg = pygame.image.load("assets/backgrounds/forestbg.PNG")

  if char_type == 'fighter':
    char = Fighter(300, 300, 40, 85, cur_health, cur_stamina, cur_mana)
    sword = Melee(char, 1, 20)
  elif char_type == 'mage':
    char = Mage(300, 300, 40, 85, cur_health, cur_stamina, cur_mana)
    orb = Orb(1, 33, 3)
    
  enemy = Tree(0, 0, 61, 89, 5, 20, 2, 2)
  bullets = []
  shootLoop = 0 # lessens bullet spam

  k_z = False
  swingCount = 0
  
  while True:

    SCREEN.blit(bg, (bgx, bgy))
    
    if bgy == -560 and not enemy.visible:
      play_water(char_type, char.health, char.stamina, char.mana)
      
    clock = pygame.time.Clock()
    PLAY_MOUSE_POS = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()

    BACK_BUTTON_SURFACE = pygame.transform.scale(pygame.image.load("assets/buttons/back.png"), (100, 30))
    BACK_BUTTON = Button(BACK_BUTTON_SURFACE, 50, 15)

    if keys[pygame.K_p]:
      print(bgx,bgy)

    if char.visible: #if the player is alive

      if keys[pygame.K_RIGHT]:
        char.right = True
        char.left = False
        char.forward = False
        char.back = False   
        char.standing = False

        if bgx > -600:
          bgx -= char.velocity
          char.game_x += char.velocity          

      elif keys[pygame.K_LEFT]:
        char.right = False
        char.left = True
        char.forward = False
        char.back = False
        char.standing = False

        if bgx < 0:
          bgx += char.velocity
          char.game_x -= char.velocity  

      elif keys[pygame.K_UP]:
        char.right = False
        char.left = False
        char.forward = False
        char.back = True
        char.standing = False

        if bgy < 0:
          bgy += char.velocity
          char.game_y -= char.velocity
          
      elif keys[pygame.K_DOWN]:
        char.right = False
        char.left = False
        char.forward = True
        char.back = False
        char.standing = False

        if bgy > -560:
          bgy -= char.velocity  
          char.game_y += char.velocity 
        
      else:
        char.standing = True
        char.walkCount = 0

      enemy.draw(SCREEN, bgx, bgy, char)
      
      if char_type == 'fighter':
        if k_z and char.stamina > sword.stamina_use:
          if swingCount < 4:
            char.draw_forestsword_atk(SCREEN)
            if enemy.visible and sword.hitbox_rect.colliderect(enemy.hitbox_rect) and swingCount == 0:
              enemy.hit(sword.damage)
            swingCount += 1
          else:
            char.draw_forestsword(SCREEN)
        else:
          char.draw_forestsword(SCREEN)
        sword.draw(SCREEN) #hitbox

        if char.stamina < char.maxstamina:
          char.stamina += 1
          
      elif char_type == 'mage':

        if shootLoop > 0:
          shootLoop += 1
        if shootLoop > 3:
          shootLoop = 0
          
        if keys[pygame.K_z] and shootLoop == 0:
          if char.left:
            x_dir = -1
            y_dir = 0
          elif char.right:
            x_dir = 1
            y_dir = 0
          elif char.back:
            x_dir = 0
            y_dir = -1
          elif char.forward:
            x_dir = 0
            y_dir = 1
          else: #on character spawn
            x_dir = 0
            y_dir = 1
      
          if len(bullets) < orb.max_onscreen and char.mana > orb.mana_cost:
            bullets.append(Projectile(char.screen_x + char.width // 2, char.screen_y + char.height // 2, 6, (0,0,0), 'orb1.png', x_dir, y_dir))
  
          if char.mana >= orb.mana_cost:
            char.mana -= orb.mana_cost

          shootLoop = 1

        for bullet in bullets:

          if bullet.rect != None:
            if bullet.rect.colliderect(enemy.hitbox_rect):
              if enemy.visible:
                enemy.hit(orb.damage)
                bullets.pop(bullets.index(bullet))
          
          #check if bullet is within game window
          if bullet.x < 600 and bullet.x > 0 and bullet.y < 600 and bullet.y > 0:
            bullet.x += bullet.x_vel
            bullet.y += bullet.y_vel
          else:
            bullets.pop(bullets.index(bullet))

          bullet.draw(SCREEN)

        char.draw_forestwand(SCREEN)

        if char.mana < char.maxmana:
          char.mana += 1

      if enemy.visible:
        if char.hitbox_rect.colliderect(enemy.hitbox_rect):
          char.collision(enemy.attackdmg)
          enemy.collision()
        else:
          enemy.colliding = False

    else: #game over
      lose(SCREEN)
      
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.KEYDOWN:
        
        if event.key == pygame.K_z:
          k_z = True
          swingCount = 0

          if char_type == 'fighter':
            if char.stamina >= sword.stamina_use:
              char.stamina -= sword.stamina_use
                
      if event.type == pygame.MOUSEBUTTONDOWN:
        if BACK_BUTTON.checkForInput(PLAY_MOUSE_POS):
          char_select()

    BACK_BUTTON.update(SCREEN)
    pygame.display.update()
    clock.tick(24)  #fps

def play_village(char_type):

  bgx, bgy = -600, -440
  bg = pygame.image.load("assets/backgrounds/villagebg.PNG")

  if char_type == 'fighter':
    char = Fighter(300, 300, 40, 85, 100, 100, 100)
    sword = Melee(char, 1, 20)
  elif char_type == 'mage':
    char = Mage(300, 300, 40, 85, 100, 100, 100)
    orb = Orb(1, 33, 3)

  k_z = False
  done_tutorial = False

  swingCount = 0
  bullets = []
  shootLoop = 0 # lessens bullet spam
  
  while True:

    SCREEN.blit(bg, (bgx, bgy))
    
    if bgy == -560 and done_tutorial:
      play_forest(char_type, char.health, char.stamina, char.mana)
      
    clock = pygame.time.Clock()
    PLAY_MOUSE_POS = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()

    BACK_BUTTON_SURFACE = pygame.transform.scale(pygame.image.load("assets/buttons/back.png"), (100, 30))
    BACK_BUTTON = Button(BACK_BUTTON_SURFACE, 50, 15)

    if bgx <= -160 and bgx >= -270 and bgy >= -60:
      
      press_x = pygame.transform.scale(pygame.image.load("assets/menu/press_x.PNG"), (125, 52))
      press_x_rect = press_x.get_rect(center=(char.screen_x+char.width/2, char.screen_y-80))
      SCREEN.blit(press_x, press_x_rect)
      
      if keys[pygame.K_x]:       
        if char_type == 'fighter':
          f_oldman1(SCREEN)
          done_tutorial = True
          
        elif char_type == 'mage':
          m_oldman1(SCREEN)
          done_tutorial = True

    if keys[pygame.K_p]:
      print(bgx,bgy)

    if keys[pygame.K_RIGHT]:
      char.right = True
      char.left = False
      char.forward = False
      char.back = False   
      char.standing = False

      if bgx > -600:
        bgx -= char.velocity
        char.game_x += char.velocity          

    elif keys[pygame.K_LEFT]:
      char.right = False
      char.left = True
      char.forward = False
      char.back = False
      char.standing = False

      if bgx < 0:
        bgx += char.velocity
        char.game_x -= char.velocity  

    elif keys[pygame.K_UP]:
      char.right = False
      char.left = False
      char.forward = False
      char.back = True
      char.standing = False

      if bgy < 0:
        bgy += char.velocity
        char.game_y -= char.velocity
        
    elif keys[pygame.K_DOWN]:
      char.right = False
      char.left = False
      char.forward = True
      char.back = False
      char.standing = False

      if bgy > -560:
        bgy -= char.velocity  
        char.game_y += char.velocity 
      
    else:
      char.standing = True
      char.walkCount = 0
    
    if char_type == 'fighter':
      if done_tutorial:
        if k_z and char.stamina > sword.stamina_use:
          if swingCount < 4:
            char.draw_forestsword_atk(SCREEN)
            swingCount += 1
          else:
            char.draw_forestsword(SCREEN)
        else:
          char.draw_forestsword(SCREEN)
        sword.draw(SCREEN) #hitbox
      else:
        char.draw(SCREEN)

      if char.stamina < char.maxstamina:
        char.stamina += 1
        
    elif char_type == 'mage':

      if done_tutorial:
        if shootLoop > 0:
          shootLoop += 1
        if shootLoop > 3:
          shootLoop = 0
          
        if keys[pygame.K_z] and shootLoop == 0:
          if char.left:
            x_dir = -1
            y_dir = 0
          elif char.right:
            x_dir = 1
            y_dir = 0
          elif char.back:
            x_dir = 0
            y_dir = -1
          elif char.forward:
            x_dir = 0
            y_dir = 1
          else: #on character spawn
            x_dir = 0
            y_dir = 1
      
          if len(bullets) < orb.max_onscreen and char.mana > orb.mana_cost:
            bullets.append(Projectile(char.screen_x + char.width // 2, char.screen_y + char.height // 2, 6, (0,0,0), 'orb1.png', x_dir, y_dir))

          if char.mana >= orb.mana_cost:
            char.mana -= orb.mana_cost

          shootLoop = 1

        for bullet in bullets:
          
          #check if bullet is within game window
          if bullet.x < 600 and bullet.x > 0 and bullet.y < 600 and bullet.y > 0:
            bullet.x += bullet.x_vel
            bullet.y += bullet.y_vel
          else:
            bullets.pop(bullets.index(bullet))

          bullet.draw(SCREEN)

        char.draw_forestwand(SCREEN)

        if char.mana < char.maxmana:
          char.mana += 1
      else:
        char.draw(SCREEN)
      
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.KEYDOWN:
        
        if event.key == pygame.K_z:
          k_z = True
          swingCount = 0

          if char_type == 'fighter' and done_tutorial:
            if char.stamina >= sword.stamina_use:
              char.stamina -= sword.stamina_use
                
      if event.type == pygame.MOUSEBUTTONDOWN:
        if BACK_BUTTON.checkForInput(PLAY_MOUSE_POS):
          char_select()

    BACK_BUTTON.update(SCREEN)
    pygame.display.update()
    clock.tick(24)  #fps

def char_select(): #character select
  while True:
    
    SCREEN.blit(pygame.image.load("assets/menu/menuBG.png"),(0,0))

    SELECT_MOUSE_POS = pygame.mouse.get_pos()

    SELECT_TEXT = pygame.image.load("assets/menu/selectcharacter.png")
    SELECT_RECT = SELECT_TEXT.get_rect(center=(300,200))

    BACK_BUTTON_SURFACE = pygame.transform.scale(pygame.image.load("assets/buttons/back.png"), (100, 30))
    BACK_BUTTON = Button(BACK_BUTTON_SURFACE, 50, 15)

    FIGHTER_BUTTON_SURFACE = pygame.transform.scale(pygame.image.load("assets/buttons/select_fighter.png"), (200, 150))
    FIGHTER_BUTTON = Button(FIGHTER_BUTTON_SURFACE, 175, 350)

    MAGE_BUTTON_SURFACE = pygame.transform.scale(pygame.image.load("assets/buttons/select_mage.png"), (200, 150))
    MAGE_BUTTON = Button(MAGE_BUTTON_SURFACE, 425, 350)
    
    SCREEN.blit(SELECT_TEXT, SELECT_RECT)

    for button in [BACK_BUTTON, FIGHTER_BUTTON, MAGE_BUTTON]:
      button.update(SCREEN)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if BACK_BUTTON.checkForInput(SELECT_MOUSE_POS):
          main_menu()
        if FIGHTER_BUTTON.checkForInput(SELECT_MOUSE_POS):
          play_village('fighter')   
        if MAGE_BUTTON.checkForInput(SELECT_MOUSE_POS):
          play_village('mage')

    pygame.display.update()

def main_menu():
  while True:

    SCREEN.blit(pygame.image.load("assets/menu/menuBG.png"),(0,0))

    MENU_MOUSE_POS = pygame.mouse.get_pos()

    MENU_TEXT = pygame.image.load("assets/menu/elemental.png")
    MENU_RECT = MENU_TEXT.get_rect(center=(300,175))

    PLAY_BUTTON_SURFACE = pygame.transform.scale(pygame.image.load("assets/buttons/play.png"), (150, 50))
    PLAY_BUTTON = Button(PLAY_BUTTON_SURFACE, 200, 400)

    EXIT_BUTTON_SURFACE = pygame.transform.scale(pygame.image.load("assets/buttons/exit.png"), (150, 50))
    EXIT_BUTTON = Button(EXIT_BUTTON_SURFACE, 400, 400)

    SCREEN.blit(MENU_TEXT, MENU_RECT)

    for button in [PLAY_BUTTON, EXIT_BUTTON]:
      button.update(SCREEN)
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
          char_select()
        if EXIT_BUTTON.checkForInput(MENU_MOUSE_POS):
          pygame.quit()
          sys.exit()
          
    pygame.display.update()

def playagain(SCREEN):
  while True: 
    MOUSE_POS = pygame.mouse.get_pos()
    
    playagain = pygame.transform.scale(pygame.image.load("assets/oldman/playagain.PNG"), (600, 600))

    SCREEN.blit(playagain, (0,0))

    PLAY_BUTTON_SURFACE = pygame.transform.scale(pygame.image.load("assets/buttons/play.png"), (150, 50))
    PLAY_BUTTON = Button(PLAY_BUTTON_SURFACE, 200, 375)

    EXIT_BUTTON_SURFACE = pygame.transform.scale(pygame.image.load("assets/buttons/exit.png"), (150, 50))
    EXIT_BUTTON = Button(EXIT_BUTTON_SURFACE, 400, 375)

    BACK_BUTTON_SURFACE = pygame.transform.scale(pygame.image.load("assets/buttons/back.png"), (100, 30))
    BACK_BUTTON = Button(BACK_BUTTON_SURFACE, 50, 15)

    for button in [PLAY_BUTTON, EXIT_BUTTON, BACK_BUTTON]:
      button.update(SCREEN)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if BACK_BUTTON.checkForInput(MOUSE_POS):
          return
        if PLAY_BUTTON.checkForInput(MOUSE_POS):
          main_menu()
        if EXIT_BUTTON.checkForInput(MOUSE_POS):
          pygame.quit()
          sys.exit()
          
    pygame.display.update()

def lose(SCREEN):
  while True: 
    MOUSE_POS = pygame.mouse.get_pos()
    
    game_over = pygame.transform.scale(pygame.image.load("assets/menu/gameover.png"), (600, 600))

    SCREEN.blit(game_over, (0,0))

    PLAY_BUTTON_SURFACE = pygame.transform.scale(pygame.image.load("assets/buttons/play.png"), (100, 34))
    PLAY_BUTTON = Button(PLAY_BUTTON_SURFACE, 210, 450)

    EXIT_BUTTON_SURFACE = pygame.transform.scale(pygame.image.load("assets/buttons/exit.png"), (100, 34))
    EXIT_BUTTON = Button(EXIT_BUTTON_SURFACE, 390, 450)

    for button in [PLAY_BUTTON, EXIT_BUTTON]:
      button.update(SCREEN)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if PLAY_BUTTON.checkForInput(MOUSE_POS):
          main_menu()
        if EXIT_BUTTON.checkForInput(MOUSE_POS):
          pygame.quit()
          sys.exit()
          
    pygame.display.update()

main_menu()