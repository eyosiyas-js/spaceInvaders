import pygame
import random
import math
from pygame import mixer

# line 4 upto 13 is for creat a screen for the game
# intialize the pygame
pygame.init() # its a code in first to start making a game with pygame
# creating a screen for the game
screen=pygame.display.set_mode((800,600))
# background for screen
background=pygame.image.load("background.png")
#background sound for the game
mixer.music.load("background.wav")
mixer.music.play(-1)
#title and icon
pygame.display.set_caption("space Invaders")
# player image = space ship
playerImg=pygame.image.load("player.png") # it code to load what i wanted image to the player
playerX= 370 # the place where the machine stay
playerY=480 # the place where the machine stay
playerX_change= 0

# enemy image = space ship
enemyImg=[] # its a code to multiple the enemies
enemyX=[] # its a code to multiple the enemies
enemyY=[] # its a code to multiple the enemies
enemyX_change=[] # its a code to multiple the enemies
enemyY_change=[] # its a code to multiple the enemies
num_of_enemies=6
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("enemy.png")) # it code to multiple the image of the enemy
    enemyX.append(random.randint(0,735)) # it code to multiple the image of the enemy
    enemyY.append(random.randint(40,150)) # it code to multiple the image of the enemy
    enemyX_change.append(6) # it code to multiple the image of the enemy
    enemyY_change.append(40) # its the meter of the enemy that goes to down after it hit the bordere
    # to creat multiple enemy
 # bullet
bulletImg=pygame.image.load("bullet.png") # it code to load what i wanted image to the enemy
bulletX= 0 # its 0 blc we dont want the bullet to set in X accis
bulletY=480 #
bulletX_change=0 # its 0 blc we dont want the bullet to move in X accis
bulletY_change=15 # its the speed of the bullet
bullet_state="ready" # it means that the bullet is not on screen. the bullet will on screen only when we fire it
# score
score_value=0
font= pygame.font.Font("freesansbold.ttf",32)
# socre text
textX=10
textY=10
#game over text
over_font=pygame.font.Font("freesansbold.ttf",64)

def show_score(x,y):
    score=font.render("score" + str(score_value),True,(255,255,255))
    screen.blit(score, (x,y))  # it makes to draw the image in pygame
def game_over_text():
    over_text=over_font.render("GAME OVER!!",True,(0,255,0))
    screen.blit(over_text,(200,250))

def player(x,y): # its a code to define playerx and y to the computer
    screen.blit(playerImg,(playerX,playerY)) # it makes to draw the image in pygame
def enemy(x,y,i): # its a code to define playerx and y to the computer
    screen.blit(enemyImg[i],(x,y)) # it makes to draw the image in pygame
def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletImg,(x+16,y+10))
def iscollisions(playerX,playerY,bulletX,bulletY):
    distance=math.sqrt((math.pow(enemyX[i]-bulletX,2))+(math.pow(enemyY[i]-bulletY,2)))
    if distance < 27:
        return True
    else:
        return False

#game Loop
# it makes the game run alwayes without clothing very important
running = True # its a loop
while running: # its a loop
    # RGB
    # it means red,green,blue
    screen.fill((0, 0, 0))  # its RGB
    # background image
    screen.blit(background,(0,0)) # its am code to make the image in the screen
     # its a code to move the machine and it can be playerX,playerY,+,-
    for event in pygame.event.get(): # its event to change the true to false
        if event.type == pygame.QUIT: # its a event like above. and quit must be capital letters and if its a capital no ()
            running= False # its now false
         # keystroke
        if event.type == pygame.KEYDOWN: # its a code to press or keydown means press
           if event.key == pygame.K_LEFT: # its code to move  left or use left arrow to move left
              playerX_change = -3 # its a the spped of the player
           if event.key == pygame.K_RIGHT: # its code to move  right or use right arrow to move right
              playerX_change = 3 # its the spped of the player
           if event.key == pygame.K_SPACE:  # its code to fire  or use the space to fire
              if bullet_state is "ready": # its make the bullet never after follow after fire when we press space
                 bullet_Sound=pygame.mixer.Sound("laser.wav")
                 bullet_Sound.play()
                 bulletX=playerX # its a code that make the bullet to dont the follow the player after fire the bullet
                 fire_bullet(playerX,bulletY)         # its b/c we want the bullet out and fire from the playerX
        if event.type == pygame.KEYUP:   # its a code to realease or keyup means releasd
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
               playerX_change = 0.1

    # its a very important to make our game. if we dont write them the game will not be complete.

    playerX += playerX_change # it makes the playerX_change to move in the screen
    #border for player(sapceship)
    if playerX <= 0:
        playerX = 0
    if playerX > 736:
        playerX = 736

    for i in range(num_of_enemies):
        # game over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i]=6
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] > 736:
              enemyX_change[i]=-6
              enemyY[i] += enemyY_change[i]

      # colisions of bullet and enemy
        collision = iscollisions(enemyX[i], enemyY[i],bulletX, bulletY) # we write [i] to secify. b/c we wrote many X and Y to multiple the enemy
        if collision:
             expolosion_Sound = mixer.Sound("explosion.wav")
             expolosion_Sound.play()
             bulletY = 480 # we write [i] to secify. b/c we wrote many X and Y to multiple the enemy
             bullet_state="ready"  # its makes the enemyX_change to move on the screen
             score_value += 1
             enemyX[i] = random.randint(0,755) # we write [i] to secify. b/c we wrote many X and Y to multiple the enemy
             enemyY[i] = random.randint(40,150) # we write [i] to secify. b/c we wrote many X and Y to multiple the enemy

        enemy(enemyX[i],enemyY[i],i)  # its a code to make the player on the screenX, playerY)  # its a code to make the enemy on
        # bullet movement
    if bulletY <0:
        bulletY = 480
        bullet_state="ready"
    if bullet_state is "fire":
       fire_bullet(bulletX, bulletY) # its a code to fire the bullet or loop
       bulletY -= bulletY_change # its means the speed of sound increase = bulletY_change(10)

# to make the player on the screen
    player(playerX, playerY)  # its a code to make the player to move
    show_score(textX,textY)   # its a code to make the text show in screen
    pygame.display.update() # its a code must be added in avery game after loop
