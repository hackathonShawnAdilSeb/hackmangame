# import necessary modules
import pygame
import sys
import os 
import random
import time

# Ensure the working directory is the script's directory
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# Initialize all imported pygame modules
pygame.init()

# Define game variables
player_size = 100
bullet_size= 30
enemy_size = 40
player_speed = 3
width = 800
height = 600
score = 0 

#bullet

bullet_x = 0
bullet_y = 0 
bulletx_change = 10
bullety_change = 0
bullet_state = "ready"

# Initialize the font variable for the game
font = pygame.font.Font(None, 36)

# Initialize screen display with width and height 
screen = pygame.display.set_mode((width, height))

# Set the current screen caption
pygame.display.set_caption('GOATBUSTERS')

background=pygame.image.load('customgrass.png')

# Load the player image
bullet_image = pygame.image.load(os.path.join('bullet.png')).convert_alpha()
player_image = pygame.image.load(os.path.join('goat.png')).convert_alpha()
enemy_image = pygame.image.load(os.path.join('ghost.png')).convert_alpha()
# Scale the player image to the desired size
bullet_image = pygame.transform.scale(bullet_image, (bullet_size, bullet_size))
player_image = pygame.transform.scale(player_image, (player_size, player_size))
enemy_image = pygame.transform.scale(enemy_image, (enemy_size, enemy_size))
# Get the rectangle for the player image
player_rect = player_image.get_rect()

# import necessary modules
import pygame, sys
import sys
import os 
import random
import time

# Ensure the working directory is the script's directory
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# Initialize all imported pygame modules
pygame.init()

# Define game variables
player_size = 100
enemy_size = 40
player_speed = 3
width = 800
height = 600
score = 0 

# Initialize the font variable for the game
font = pygame.font.Font(None, 36)

# Initialize screen display with width and height 
screen = pygame.display.set_mode((width, height))


# Set the current screen caption
pygame.display.set_caption('GOATBUSTERS')

background=pygame.image.load('customgrass.png')

# Load the player image
player_image = pygame.image.load(os.path.join('goat.png')).convert_alpha()
enemy_image = pygame.image.load(os.path.join('ghost.png')).convert_alpha()
# Scale the player image to the desired size
player_image = pygame.transform.scale(player_image, (player_size, player_size))
enemy_image = pygame.transform.scale(enemy_image, (enemy_size, enemy_size))
# Get the rectangle for the player image
player_rect = player_image.get_rect()

#mud
mud_image = pygame.image.load(os.path.join('mud3.png')).convert_alpha()
mud_mask = pygame.mask.from_surface(mud_image)
mud_rect = mud_image.get_rect(topleft=(200, 300))

def create_player_mask(player_rect):
    player_surface = pygame.Surface((player_hitbox_size, player_hitbox_size), pygame.SRCALPHA)
    # Blit the player's image onto the surface
    player_surface.blit(player_image, (0, 0), player_rect)
    # Create and return the mask from the player's surface
    return pygame.mask.from_surface(player_surface)


def draw_text(text, font, color, surface, x, y):
    
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y))
    surface.blit(text_obj, text_rect)

def main_menu():
   
    button_color = (100, 200, 150)
    button_hover_color = (150, 255, 200)
    button_width = 400
    button_height = 80
    button_padding = 20
    
    
    menu_background = pygame.image.load('customgrass.png')

    title_font = pygame.font.Font(None, 50)
    button_font = pygame.font.Font(None, 50)
    
   
    start_button_rect = pygame.Rect(width // 2 - button_width // 2, height // 2 - 150, button_width, button_height)
    quit_button_rect = pygame.Rect(width // 2 - button_width // 2, height // 2 + button_padding, button_width, button_height)

    while True:
        
        screen.blit(menu_background, (0, 0))
        
        
        draw_text("WELCOME TO THE GOATBUSTERS GAME", title_font, (255, 255, 255), screen, width // 2, 100)

        
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

       
        if start_button_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, button_hover_color, start_button_rect)
            if mouse_click[0]:  
                return  
        else:
            pygame.draw.rect(screen, button_color, start_button_rect)

        
        if quit_button_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, button_hover_color, quit_button_rect)
            if mouse_click[0]:  
                pygame.quit()
                sys.exit()
        else:
            pygame.draw.rect(screen, button_color, quit_button_rect)

        
        draw_text("Start Game", button_font, (0, 0, 0), screen, width // 2, height // 2 - 110)
        draw_text("Quit", button_font, (0, 0, 0), screen, width // 2, height // 2 + 40)

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()

        
main_menu()


# Enemy Class to handle enemies ###
class Enemy:
    def __init__(self):
        
        # Randomly select enemy's starting edge (top, bottom, left, right)
        edge = random.choice(['top', 'bottom', 'left', 'right'])
        
        # Set initial enemy position based on the selected edge
        if edge == 'top':
            self.rect = pygame.Rect(random.randint(0, width - enemy_size), 0, enemy_size, enemy_size)
        elif edge == 'bottom':
            self.rect = pygame.Rect(random.randint(0, width - enemy_size), height - enemy_size, enemy_size, enemy_size)
        elif edge == 'left':
            self.rect = pygame.Rect(0, random.randint(0, height - enemy_size), enemy_size, enemy_size)
        else:  # right
            self.rect = pygame.Rect(width - enemy_size, random.randint(0, height - enemy_size), enemy_size, enemy_size)
        
        # Define the speed for the enemy
        self.speed = 2

    # Move the enemy towards the player
    def move_towards_player(self, player_rect):
        # Calculate the direction vector towards the player
        direction = pygame.Vector2(player_rect.center) - pygame.Vector2(self.rect.center)
        if direction.length() != 0:
            direction = direction.normalize()  # Normalize direction vector for consistent speed
        # Update the enemy's position to move towards the player
        self.rect.x += direction.x * self.speed
        self.rect.y += direction.y * self.speed
        self.rect.x = max(0, min(width - enemy_size, self.rect.x))
        self.rect.y = max(0, min(height - enemy_size, self.rect.y))

    def move_away_from_other_enemies(self, enemies):
        for other_enemy in enemies:
            if other_enemy != self:  # Check that we're not comparing the enemy with itself
                if self.rect.colliderect(other_enemy.rect):  # If there's a collision
                    # Move this enemy away from the other enemy
                    overlap_direction = pygame.Vector2(self.rect.center) - pygame.Vector2(other_enemy.rect.center)
                    if overlap_direction.length() != 0:
                        overlap_direction = overlap_direction.normalize()  # Normalize direction
                    self.rect.x += overlap_direction.x * self.speed
                    self.rect.y += overlap_direction.y * self.speed
                    

    # Draw the enemy on the screen
    def draw(self, screen):
        screen.blit(enemy_image, self.rect)  
    
        



# Create an object to help track time (FPS control)
clock = pygame.time.Clock()

# Flag to control the main game loop
running = True

# Instantiate an enemy object (can add more enemies as needed)
num_of_enemies = 5
spawncamp=[]
for i in range(num_of_enemies):
    spawncamp.append(Enemy())

hitbox_reduction = 75  # This will reduce 10 pixels from both width and height
player_hitbox_size = player_size - hitbox_reduction

def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bullet_image, (x,y))

# Function to update player movement based on WASD keys
def update_player_movement():
    global player_x
    global player_y
    # Get the state of all keyboard buttons
    keys = pygame.key.get_pressed()
    
    # Update player's x and y coordinates based on key presses
    if keys[pygame.K_a]:  # Move left (A)
        player_x -= player_speed
    if keys[pygame.K_d]:  # Move right (D)
        player_x += player_speed
    if keys[pygame.K_w]:  # Move up (W)
        player_y -= player_speed
    if keys[pygame.K_s]:  # Move down (S)
        player_y += player_speed
    
    # Ensure player's position stays within screen boundaries
    player_x = max(0, min(width - player_size, player_x))
    player_y = max(0, min(height - player_size, player_y))
    
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)

    player_hitbox = pygame.Rect(
        player_x + hitbox_reduction // 2,
        player_y + hitbox_reduction // 2,
        player_hitbox_size,
        player_hitbox_size
    )

    # Update and return the player's rectangle for further processing (like collision detection)
    return pygame.Rect(player_x, player_y, player_size, player_size), player_hitbox

# Function to reset the game state (score, enemy and player position)
def reset_game():
    global player_x, player_y, enemy, score
    player_x = width // 2  # Reset player position to the center of the screen
    player_y = height // 2
    spawncamp.clear()
    for i in range(num_of_enemies):
        spawncamp.append(Enemy())
   
    score = 0  # Reset score


# Function to display "You Died" message and a countdown to restart
def display_you_died_and_restart(screen):
    for i in range(3, 0, -1):  # Countdown from 5 to 1
        screen.fill((0, 0, 0))  # Clear the screen
        text = font.render(f'You Died! Restarting in {i}...', True, (255, 0, 0))
        screen.blit(text, (width // 2 - 150, height // 2))  # Display centered message
        pygame.display.flip()  # Update the screen
        time.sleep(1)  # Wait for 1 second
    reset_game()  # Reset the game after countdown


# Function to display the current score on the screen
def display_score(screen, score):
    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(score_text, (10, 10))  # Display score in the top-left corner
    
# Define player's initial position at the center of the screen
player_x = width // 2
player_y = height // 2
time_since_last_score_increase = 0  # Track time to increase score every second



### Main Game Loop ###
while running:
    keys = pygame.key.get_pressed()
    # Event handling
    for event in pygame.event.get():
        # Quit the game if the user closes the window
        if event.type == pygame.QUIT:
            running = False

    # Update player position based on movement input
    player_rect, player_hitbox = update_player_movement()

    player_mask = create_player_mask(player_hitbox)

    if keys[pygame.K_SPACE]:
        fire_bullet(bullet_x,player_y)
   
    # Move the enemy towards the player
    for i in range(num_of_enemies):
        spawncamp[i].move_towards_player(player_rect)
        spawncamp[i].move_away_from_other_enemies(spawncamp)
    #enemy.move_towards_player(player_rect)
    #enemy2.move_towards_player(player_rect)
    # Check for collision between player and enemy
    
    offset_x = player_hitbox.x - mud_rect.x  # Offset between player and mud in the x-axis
    offset_y = player_hitbox.y - mud_rect.y  # Offset between player and mud in the y-axis
    mud_collision = mud_mask.overlap(player_mask, (offset_x, offset_y))
    
        

    # Fill the background with black
    screen.fill((0, 0, 0))



    #set background
    screen.blit(background, (0,0))
    
    # Draw the player on the screen
    screen.blit(player_image, player_rect)

    screen.blit(mud_image, mud_rect)

    pygame.draw.rect(screen, (255, 0, 0), mud_rect, 2)  # Red box around the mud
    pygame.draw.rect(screen, (0, 0, 255), player_hitbox, 2)  # Blue box around the player

    # Draw the enemy on the screen
    for i in range(num_of_enemies):
        spawncamp[i].draw(screen)
    #enemy.draw(screen)
    #enemy2.draw(screen)

    collision1 = False
    for i in range(num_of_enemies):
        if player_hitbox.colliderect(spawncamp[i].rect):
            collision1 = True
            break
            
    # If no collision occurs, increase the score every second
    if not collision1:
        time_since_last_score_increase += clock.get_time()  # Track the time since last score increase
        if time_since_last_score_increase > 1000:  # 1000 ms = 1 second
            score += 1  # Increase the score by 1
            time_since_last_score_increase = 0  # Reset the timer

    mud_slowdown_duration = 2000  # Slowdown lasts for 2 seconds
    mud_collision_time = None  # Track when the player enters the mud

    # Inside the main game loop where you handle the mud collision:
    if mud_collision:
        if mud_collision_time is None:  # If the player just collided with the mud
            mud_collision_time = pygame.time.get_ticks()  # Record the current time
            player_speed = 1.5  # Slow down the player

    # Check if enough time has passed to restore the speed
    if mud_collision_time is not None:
        current_time = pygame.time.get_ticks()
        if current_time - mud_collision_time > mud_slowdown_duration:  # Check if 2 seconds have passed
            player_speed = 3  # Restore player speed
            mud_collision_time = None
    



    # If collision occurs, show "You Died" and restart after 5 seconds
    if collision1 or mud_collision:
        display_you_died_and_restart(screen)

    # Display the current score
    display_score(screen, score)

    if bullet_state is "fire":
        fire_bullet(bullet_x, player_y)
        bullet_x += bulletx_change
    # If a collision occurs, display a message on the screen
    '''
    if collision1:
        text = font.render('Collision Occurred!', True, (255, 255, 255))
        screen.blit(text, (10, 10))
    ''' 
    
    # Update the display
    pygame.display.flip()

    # Cap the frame rate to 60 frames per second
    clock.tick(60)

# Quit the game
pygame.quit()
sys.exit()
