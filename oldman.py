import pygame, sys, time
from button import Button

textarrow_surface = pygame.transform.scale(pygame.image.load("assets/buttons/textarrow.png"), (25, 40))
textarrow_button = Button(textarrow_surface, 545, 275)

textarrow_surface2 = pygame.transform.scale(pygame.image.load("assets/buttons/textarrow.png"), (25, 40))
textarrow_button2 = Button(textarrow_surface2, 530, 270)

BACK_BUTTON_SURFACE = pygame.transform.scale(pygame.image.load("assets/buttons/back.png"), (100, 30))
BACK_BUTTON = Button(BACK_BUTTON_SURFACE, 50, 15)

""""def playagain(SCREEN):

  display = True
  while display: 

    MOUSE_POS = pygame.mouse.get_pos()
    
    winscreen = pygame.transform.scale(pygame.image.load("assets/oldman/playagain.PNG"), (600, 600))

    SCREEN.blit(winscreen, (0,0))

    PLAY_BUTTON_SURFACE = pygame.transform.scale(pygame.image.load("assets/buttons/play.png"), (150, 50))
    PLAY_BUTTON = Button(PLAY_BUTTON_SURFACE, 200, 400)

    EXIT_BUTTON_SURFACE = pygame.transform.scale(pygame.image.load("assets/buttons/exit.png"), (150, 50))
    EXIT_BUTTON = Button(EXIT_BUTTON_SURFACE, 400, 400)

    for button in [PLAY_BUTTON, EXIT_BUTTON, textarrow_button2]:
      button.update(SCREEN)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if textarrow_button2.checkForInput(MOUSE_POS):
          display = False
        elif BACK_BUTTON.checkForInput(MOUSE_POS):
          return
        if PLAY_BUTTON.checkForInput(MOUSE_POS):
          pass
        if EXIT_BUTTON.checkForInput(MOUSE_POS):
          pygame.quit()
          sys.exit()
          
    pygame.display.update()"""
    
def winscreen(SCREEN):

  display = True
  while display: 

    MOUSE_POS = pygame.mouse.get_pos()
    
    winscreen = pygame.transform.scale(pygame.image.load("assets/oldman/winscreen.PNG"), (600, 600))

    SCREEN.blit(winscreen, (0,0))

    for button in [textarrow_button2]:
      button.update(SCREEN)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if textarrow_button2.checkForInput(MOUSE_POS):
          #playagain(SCREEN)
          display = False
        elif BACK_BUTTON.checkForInput(MOUSE_POS):
          return
          
    BACK_BUTTON.update(SCREEN)

    pygame.display.update()
    
def oldman12(SCREEN):

  display = True
  while display: 

    MOUSE_POS = pygame.mouse.get_pos()
    
    text12 = pygame.transform.scale(pygame.image.load("assets/oldman/oldmantext12.PNG"), (600, 600))

    SCREEN.blit(text12, (0,0))

    for button in [textarrow_button2]:
      button.update(SCREEN)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if textarrow_button2.checkForInput(MOUSE_POS):
          winscreen(SCREEN)
          display = False
        elif BACK_BUTTON.checkForInput(MOUSE_POS):
          return
          
    BACK_BUTTON.update(SCREEN)
    pygame.display.update()

def oldman11(SCREEN):

  display = True
  while display: 

    MOUSE_POS = pygame.mouse.get_pos()
    
    text11 = pygame.transform.scale(pygame.image.load("assets/oldman/oldmantext11.PNG"), (600, 600))

    SCREEN.blit(text11, (0,0))

    for button in [textarrow_button2]:
      button.update(SCREEN)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if textarrow_button2.checkForInput(MOUSE_POS):
          oldman12(SCREEN)
          display = False
        elif BACK_BUTTON.checkForInput(MOUSE_POS):
          return
          
    BACK_BUTTON.update(SCREEN)
    pygame.display.update()

def oldman10(SCREEN):

  display = True
  while display: 

    MOUSE_POS = pygame.mouse.get_pos()
    
    text10 = pygame.transform.scale(pygame.image.load("assets/oldman/oldmantext10.PNG"), (600, 600))

    SCREEN.blit(text10, (0,0))

    for button in [textarrow_button2]:
      button.update(SCREEN)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if textarrow_button2.checkForInput(MOUSE_POS): 
          oldman11(SCREEN)
          display = False
        elif BACK_BUTTON.checkForInput(MOUSE_POS):
          return
          
    BACK_BUTTON.update(SCREEN)
    pygame.display.update()
    
#tutorial
def oldman9(SCREEN):

  display = True
  while display: 

    MOUSE_POS = pygame.mouse.get_pos()
    
    text9 = pygame.transform.scale(pygame.image.load("assets/oldman/oldmantext9.PNG"), (600, 600))

    SCREEN.blit(text9, (0,0))

    for button in [textarrow_button]:
      button.update(SCREEN)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if textarrow_button.checkForInput(MOUSE_POS): 
          display = False
        elif BACK_BUTTON.checkForInput(MOUSE_POS):
          return
          
    BACK_BUTTON.update(SCREEN)
    pygame.display.update()

def m_oldman88(SCREEN):
  display = True
  while display: 

    MOUSE_POS = pygame.mouse.get_pos()
    
    text8 = pygame.transform.scale(pygame.image.load("assets/oldman/oldmantext8.8.PNG"), (600, 600))

    SCREEN.blit(text8, (0,0))

    for button in [textarrow_button]:
      button.update(SCREEN)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if textarrow_button.checkForInput(MOUSE_POS):
          oldman9(SCREEN)
          display = False
        elif BACK_BUTTON.checkForInput(MOUSE_POS):
          return

    BACK_BUTTON.update(SCREEN)
    pygame.display.update()

def m_oldman87(SCREEN):
  display = True
  while display: 

    MOUSE_POS = pygame.mouse.get_pos()
    
    text8 = pygame.transform.scale(pygame.image.load("assets/oldman/oldmantext8.7.PNG"), (600, 600))

    SCREEN.blit(text8, (0,0))

    for button in [textarrow_button]:
      button.update(SCREEN)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if textarrow_button.checkForInput(MOUSE_POS):
          m_oldman88(SCREEN)
          display = False
        elif BACK_BUTTON.checkForInput(MOUSE_POS):
          return

    BACK_BUTTON.update(SCREEN)
    pygame.display.update()

def m_oldman86(SCREEN):
  display = True
  while display: 

    MOUSE_POS = pygame.mouse.get_pos()
    
    text8 = pygame.transform.scale(pygame.image.load("assets/oldman/oldmantext8.6.PNG"), (600, 600))

    SCREEN.blit(text8, (0,0))

    for button in [textarrow_button]:
      button.update(SCREEN)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if textarrow_button.checkForInput(MOUSE_POS):
          m_oldman87(SCREEN)
          display = False
        elif BACK_BUTTON.checkForInput(MOUSE_POS):
          return

    BACK_BUTTON.update(SCREEN)
    pygame.display.update()

def f_oldman891(SCREEN):
  display = True
  while display: 

    MOUSE_POS = pygame.mouse.get_pos()
    
    text8 = pygame.transform.scale(pygame.image.load("assets/oldman/oldmantext8.91.PNG"), (600, 600))

    SCREEN.blit(text8, (0,0))

    for button in [textarrow_button]:
      button.update(SCREEN)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if textarrow_button.checkForInput(MOUSE_POS):
          oldman9(SCREEN)
          display = False
        elif BACK_BUTTON.checkForInput(MOUSE_POS):
          return

    BACK_BUTTON.update(SCREEN)
    pygame.display.update()

def f_oldman89(SCREEN):
  display = True
  while display: 

    MOUSE_POS = pygame.mouse.get_pos()
    
    text8 = pygame.transform.scale(pygame.image.load("assets/oldman/oldmantext8.9.PNG"), (600, 600))

    SCREEN.blit(text8, (0,0))

    for button in [textarrow_button]:
      button.update(SCREEN)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if textarrow_button.checkForInput(MOUSE_POS):
          f_oldman891(SCREEN)
          display = False
        elif BACK_BUTTON.checkForInput(MOUSE_POS):
          return

    BACK_BUTTON.update(SCREEN)
    pygame.display.update()

def f_oldman85(SCREEN):
  display = True
  while display: 

    MOUSE_POS = pygame.mouse.get_pos()
    
    text8 = pygame.transform.scale(pygame.image.load("assets/oldman/oldmantext8.5.PNG"), (600, 600))

    SCREEN.blit(text8, (0,0))

    for button in [textarrow_button]:
      button.update(SCREEN)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if textarrow_button.checkForInput(MOUSE_POS):
          f_oldman89(SCREEN)
          display = False
        elif BACK_BUTTON.checkForInput(MOUSE_POS):
          return

    BACK_BUTTON.update(SCREEN)
    pygame.display.update()

def f_oldman8(SCREEN):
  display = True
  while display: 

    MOUSE_POS = pygame.mouse.get_pos()
    
    text8 = pygame.transform.scale(pygame.image.load("assets/oldman/oldmantext8.PNG"), (600, 600))

    SCREEN.blit(text8, (0,0))

    for button in [textarrow_button]:
      button.update(SCREEN)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if textarrow_button.checkForInput(MOUSE_POS):
          f_oldman85(SCREEN)
          display = False
        elif BACK_BUTTON.checkForInput(MOUSE_POS):
          return

    BACK_BUTTON.update(SCREEN)
    pygame.display.update()

def f_oldman7(SCREEN):
  display = True
  while display: 

    MOUSE_POS = pygame.mouse.get_pos()
    
    text7 = pygame.transform.scale(pygame.image.load("assets/oldman/oldmantext7.PNG"), (600, 600))

    SCREEN.blit(text7, (0,0))

    for button in [textarrow_button]:
      button.update(SCREEN)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if textarrow_button.checkForInput(MOUSE_POS): 
          f_oldman8(SCREEN)
          display = False
        elif BACK_BUTTON.checkForInput(MOUSE_POS):
          return

    BACK_BUTTON.update(SCREEN)
    pygame.display.update()

def f_oldman6(SCREEN):
  display = True
  while display: 

    MOUSE_POS = pygame.mouse.get_pos()
    
    text6 = pygame.transform.scale(pygame.image.load("assets/oldman/oldmantext6.PNG"), (600, 600))

    SCREEN.blit(text6, (0,0))

    for button in [textarrow_button]:
      button.update(SCREEN)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if textarrow_button.checkForInput(MOUSE_POS): 
          f_oldman7(SCREEN)
          display = False
        elif BACK_BUTTON.checkForInput(MOUSE_POS):
          return

    BACK_BUTTON.update(SCREEN)
    pygame.display.update()

def f_oldman5(SCREEN):
  display = True
  while display: 

    MOUSE_POS = pygame.mouse.get_pos()
    
    text5 = pygame.transform.scale(pygame.image.load("assets/oldman/oldmantext5.PNG"), (600, 600))

    SCREEN.blit(text5, (0,0))

    for button in [textarrow_button]:
      button.update(SCREEN)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if textarrow_button.checkForInput(MOUSE_POS): 
          f_oldman6(SCREEN)
          display = False
        elif BACK_BUTTON.checkForInput(MOUSE_POS):
          return

    BACK_BUTTON.update(SCREEN)
    pygame.display.update()

def f_oldman4(SCREEN):
  display = True
  while display: 

    MOUSE_POS = pygame.mouse.get_pos()
    
    text4 = pygame.transform.scale(pygame.image.load("assets/oldman/oldmantext4.PNG"), (600, 600))

    SCREEN.blit(text4, (0,0))

    for button in [textarrow_button]:
      button.update(SCREEN)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if textarrow_button.checkForInput(MOUSE_POS): 
          f_oldman5(SCREEN)
          display = False
        elif BACK_BUTTON.checkForInput(MOUSE_POS):
          return

    BACK_BUTTON.update(SCREEN)
    pygame.display.update()

def f_oldman3(SCREEN):
  display = True
  while display: 

    MOUSE_POS = pygame.mouse.get_pos()
    
    text3 = pygame.transform.scale(pygame.image.load("assets/oldman/oldmantext3.PNG"), (600, 600))

    SCREEN.blit(text3, (0,0))

    for button in [textarrow_button]:
      button.update(SCREEN)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if textarrow_button.checkForInput(MOUSE_POS): 
          f_oldman4(SCREEN)
          display = False
        elif BACK_BUTTON.checkForInput(MOUSE_POS):
          return

    BACK_BUTTON.update(SCREEN)
    pygame.display.update()
  
def f_oldman2(SCREEN):
  display = True
  while display:

    MOUSE_POS = pygame.mouse.get_pos()
    
    text2 = pygame.transform.scale(pygame.image.load("assets/oldman/oldmantext2.PNG"), (600,600))

    SCREEN.blit(text2, (0,0))

    for button in [textarrow_button]:
      button.update(SCREEN)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if textarrow_button.checkForInput(MOUSE_POS): 
          f_oldman3(SCREEN)
          display = False
        elif BACK_BUTTON.checkForInput(MOUSE_POS):
          return

    BACK_BUTTON.update(SCREEN)
    pygame.display.update()
    
def f_oldman1(SCREEN):
  display = True
  while display:

    MOUSE_POS = pygame.mouse.get_pos()

    text1 = pygame.transform.scale(pygame.image.load("assets/oldman/oldmantext1.PNG"), (600,600))

    SCREEN.blit(text1, (0,0))
    
    for button in [textarrow_button]:
      button.update(SCREEN)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if textarrow_button.checkForInput(MOUSE_POS): 
          f_oldman2(SCREEN)
          display = False
        elif BACK_BUTTON.checkForInput(MOUSE_POS):
          return

    BACK_BUTTON.update(SCREEN)
    pygame.display.update()

def m_oldman8(SCREEN):
  display = True
  while display: 

    MOUSE_POS = pygame.mouse.get_pos()
    
    text8 = pygame.transform.scale(pygame.image.load("assets/oldman/oldmantext8.PNG"), (600, 600))

    SCREEN.blit(text8, (0,0))

    for button in [textarrow_button]:
      button.update(SCREEN)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if textarrow_button.checkForInput(MOUSE_POS):
          m_oldman86(SCREEN)
          display = False
        elif BACK_BUTTON.checkForInput(MOUSE_POS):
          return

    BACK_BUTTON.update(SCREEN)
    pygame.display.update()

def m_oldman7(SCREEN):
  display = True
  while display: 

    MOUSE_POS = pygame.mouse.get_pos()
    
    text7 = pygame.transform.scale(pygame.image.load("assets/oldman/oldmantext7.PNG"), (600, 600))

    SCREEN.blit(text7, (0,0))

    for button in [textarrow_button]:
      button.update(SCREEN)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if textarrow_button.checkForInput(MOUSE_POS): 
          m_oldman8(SCREEN)
          display = False
        elif BACK_BUTTON.checkForInput(MOUSE_POS):
          return

    BACK_BUTTON.update(SCREEN)
    pygame.display.update()

def m_oldman6(SCREEN):
  display = True
  while display: 

    MOUSE_POS = pygame.mouse.get_pos()
    
    text6 = pygame.transform.scale(pygame.image.load("assets/oldman/oldmantext6.PNG"), (600, 600))

    SCREEN.blit(text6, (0,0))

    for button in [textarrow_button]:
      button.update(SCREEN)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if textarrow_button.checkForInput(MOUSE_POS): 
          m_oldman7(SCREEN)
          display = False
        elif BACK_BUTTON.checkForInput(MOUSE_POS):
          return

    BACK_BUTTON.update(SCREEN)
    pygame.display.update()

def m_oldman5(SCREEN):
  display = True
  while display: 

    MOUSE_POS = pygame.mouse.get_pos()
    
    text5 = pygame.transform.scale(pygame.image.load("assets/oldman/oldmantext5.PNG"), (600, 600))

    SCREEN.blit(text5, (0,0))

    for button in [textarrow_button]:
      button.update(SCREEN)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if textarrow_button.checkForInput(MOUSE_POS): 
          m_oldman6(SCREEN)
          display = False
        elif BACK_BUTTON.checkForInput(MOUSE_POS):
          return

    BACK_BUTTON.update(SCREEN)
    pygame.display.update()

def m_oldman4(SCREEN):
  display = True
  while display: 

    MOUSE_POS = pygame.mouse.get_pos()
    
    text4 = pygame.transform.scale(pygame.image.load("assets/oldman/oldmantext4.PNG"), (600, 600))

    SCREEN.blit(text4, (0,0))

    for button in [textarrow_button]:
      button.update(SCREEN)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if textarrow_button.checkForInput(MOUSE_POS): 
          m_oldman5(SCREEN)
          display = False
        elif BACK_BUTTON.checkForInput(MOUSE_POS):
          return

    BACK_BUTTON.update(SCREEN)
    pygame.display.update()

def m_oldman3(SCREEN):
  display = True
  while display: 

    MOUSE_POS = pygame.mouse.get_pos()
    
    text3 = pygame.transform.scale(pygame.image.load("assets/oldman/oldmantext3.PNG"), (600, 600))

    SCREEN.blit(text3, (0,0))

    for button in [textarrow_button]:
      button.update(SCREEN)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if textarrow_button.checkForInput(MOUSE_POS): 
          m_oldman4(SCREEN)
          display = False
        elif BACK_BUTTON.checkForInput(MOUSE_POS):
          return

    BACK_BUTTON.update(SCREEN)
    pygame.display.update()
  
def m_oldman2(SCREEN):
  display = True
  while display:

    MOUSE_POS = pygame.mouse.get_pos()
    
    text2 = pygame.transform.scale(pygame.image.load("assets/oldman/oldmantext2.PNG"), (600,600))

    SCREEN.blit(text2, (0,0))

    for button in [textarrow_button]:
      button.update(SCREEN)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if textarrow_button.checkForInput(MOUSE_POS): 
          m_oldman3(SCREEN)
          display = False
        elif BACK_BUTTON.checkForInput(MOUSE_POS):
          return

    BACK_BUTTON.update(SCREEN)
    pygame.display.update()
    
def m_oldman1(SCREEN):
  display = True
  while display:

    MOUSE_POS = pygame.mouse.get_pos()

    text1 = pygame.transform.scale(pygame.image.load("assets/oldman/oldmantext1.PNG"), (600,600))

    SCREEN.blit(text1, (0,0))
    
    for button in [textarrow_button]:
      button.update(SCREEN)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if textarrow_button.checkForInput(MOUSE_POS): 
          m_oldman2(SCREEN)
          display = False
        elif BACK_BUTTON.checkForInput(MOUSE_POS):
          return

    BACK_BUTTON.update(SCREEN)
    pygame.display.update()