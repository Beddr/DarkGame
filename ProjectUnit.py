"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame
import random
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

class Enemy(pygame.sprite.Sprite):
    
    """ This class represents the block. """
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = pygame.image.load("EnemyReal.png").convert()
        self.image.set_colorkey(BLACK)
 
        self.rect = self.image.get_rect()
        self.rect.y = 330
        self.rect.x = 300

    
    
    
class Player(pygame.sprite.Sprite): 
    
    def __init__(self):
        
        super().__init__()
        
        self.image = pygame.image.load("Character.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.y = 350
        
    def update(self):
        
        if x_speed == 3 :
            
            self.rect.x = x   
            self.image = pygame.image.load("Character.png").convert()
            self.image.set_colorkey(BLACK)
                       
        elif x_speed == -3: 
            
            self.rect.x = x
            self.image = pygame.image.load("CharacterCopy.png").convert()
            self.image.set_colorkey(BLACK)
                        
                  
        
      

pygame.init()

# Set the width and height of the screen [width, height]
size = (800, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")

block_list = pygame.sprite.Group()
 
# This is a list of every sprite. All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#background image
background_image = pygame.image.load("Location.gif").convert()
#Making Enemies
for i in range(5):
    enemy = Enemy()
    
    enemy.rect.x += 



#Adding Player
MyPlayer = Player()
all_sprites_list.add(MyPlayer)

click_sound = pygame.mixer.Sound("laser5.ogg")
instructions = pygame.image.load("Loading.jpg").convert()

x=0
y=350
x_speed= 0
y_speed= 0
font = pygame.font.Font(None, 36)
 
display_instructions = True
instruction_page = 1
name = ""
 
# -------- Instruction Page Loop -----------
while not done and display_instructions:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.unicode.isalpha():
                name += event.unicode
            elif event.key == pygame.K_BACKSPACE:
                name = name[:-1]
            elif event.key == pygame.K_RETURN:
                instruction_page += 1  
                if instruction_page == 3:
                    display_instructions = False                
 
    # Set the screen background
    screen.blit(instructions, [-230,0])
 
    if instruction_page == 1:
        # Draw instructions, page 1
        # This could also load an image created in another program.
        # That could be both easier and more flexible.
 
        text = font.render("Instructions", True, WHITE)
        screen.blit(text, [10, 10])
       
        text = font.render("Enter your name: ", True, WHITE)
        screen.blit(text, [10, 40])    
       
        text = font.render(name, True, WHITE)
        screen.blit(text, [220, 40])        
 
        text = font.render("Hit enter to continue", True, WHITE)
        screen.blit(text, [10, 80])
       
        text = font.render("Page 1", True, WHITE)
        screen.blit(text, [10, 120])
 
    if instruction_page == 2:
        # Draw instructions, page 2
        text = font.render("Defeat the enemies", True, WHITE)
        screen.blit(text, [10, 10])    
 
        text = font.render("Hit enter to continue", True, WHITE)
        screen.blit(text, [10, 40])
 
        text = font.render("Page 2", True, WHITE)
        screen.blit(text, [10, 80])
 
    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
   
    score = 0

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
        
#        elif event.type == pygame.MOUSEBUTTONDOWN:
#            click_sound.play()
        elif event.type == pygame.KEYDOWN:
                # Figure out if it was an arrow key. If so
                # adjust speed.
            if event.key == pygame.K_LEFT:
                x_speed = -3
            elif event.key == pygame.K_RIGHT:
                x_speed = 3
            #elif event.key == pygame.K_UP:
                #y_speed = -3
            #elif event.key == pygame.K_DOWN:
                #y_speed = 3        
            
        elif event.type == pygame.KEYUP:
                    # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0          
                
    x = x+x_speed
    #y = y+y_speed
   
        
    
    # --- Game logic should go here
    
    all_sprites_list.update()
    
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
    screen.blit(background_image, [0, 0])
    all_sprites_list.update()

    
    #if x > 635:
        #x = 635
    #elif x < 50:
        #x = 50
    #elif y > 400:
        #y = 400
    #elif y < 15:
        #y = 15    
     
    # Copy image to screen:
    #if x_speed == 3 or x_speed == 0 :
        #screen.blit(player_image, [x, y])
    #elif x_speed == -3 or x_speed == 0:
        #screen.blit(player_image_left, [x,y])
 
    # --- Drawing code should go here
    all_sprites_list.draw(screen)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
