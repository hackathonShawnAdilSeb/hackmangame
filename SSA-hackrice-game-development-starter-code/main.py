# import necessary modules
import pygame
import sys
import os 
import random
import time
import math

# Ensure the working directory is the script's directory
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# Initialize all imported pygame modules
pygame.init()

# Define game variables
player_size = 100
bullet_size= 80
enemy_size = 40
player_speed = 8
width = 800
height = 600
score = 0 

#bullet

bullet_x = 0
bullet_y = 0 
bulletx_change = 10
bullety_change = 0
bullet_state = "ready"
bullet_dir = "neutral"

# Initialize the font variable for the game
font = pygame.font.Font(None, 36)

# Initialize screen display with width and height 
screen = pygame.display.set_mode((width, height))

# Set the current screen caption
pygame.display.set_caption('GOATBUSTERS')

background=pygame.image.load('customgrass.png')

# Load the player image
bullet_image = pygame.image.load(os.path.join('bullet.png')).convert_alpha()
bullet_image2 = pygame.image.load(os.path.join('boss_bullet.png')).convert_alpha()
player_image = pygame.image.load(os.path.join('goat.png')).convert_alpha()
enemy_image = pygame.image.load(os.path.join('ghost.png')).convert_alpha()
# Scale the player image to the desired size
bullet_image = pygame.transform.scale(bullet_image, (bullet_size, bullet_size))
bullet_image2 = pygame.transform.scale(bullet_image2, (bullet_size - 50, bullet_size - 50))
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
player_speed = 8
width = 800
height = 600
score = 0 
boss_bullets = []
boss_bullet_size = 5
boss_shoot_timer = 0
boss_shoot_interval = 60
boss_size = 100
level = 1
level_score_update = 5
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
boss_image = pygame.image.load(os.path.join('boss.png')).convert_alpha()
# Scale the player image to the desired size
player_image = pygame.transform.scale(player_image, (player_size, player_size))
enemy_image = pygame.transform.scale(enemy_image, (enemy_size, enemy_size))
boss_image = pygame.transform.scale(boss_image, (boss_size, boss_size))
player_rect = player_image.get_rect()


def spawn_mud_randomly(tree_rect):
    max_x = width - mud_size[0]  # Maximum x-coordinate (screen width - mud width)
    max_y = height - mud_size[1]  # Maximum y-coordinate (screen height - mud height)
    
    while True:  
        random_x = random.randint(0, max_x)
        random_y = random.randint(0, max_y)
        mud_rect = pygame.Rect(random_x, random_y, mud_size[0], mud_size[1])
        
        if not mud_rect.colliderect(tree_rect): 
            return mud_rect


def spawn_tree_randomly(mud_rect):
    max_x = width - tree_size[0]
    max_y = height - tree_size[1]

    while True: 
        random_x = random.randint(0, max_x)
        random_y = random.randint(0, max_y)
        tree_rect = pygame.Rect(random_x, random_y, tree_size[0], tree_size[1])
        
        if not tree_rect.colliderect(mud_rect):  
            return tree_rect
        
#mud
mud_size = (100, 100)  # Set new size for the mud (width, height)
mud_image = pygame.image.load(os.path.join('mud3.png')).convert_alpha()
mud_image = pygame.transform.scale(mud_image, mud_size)
mud_mask = pygame.mask.from_surface(mud_image)
mud_rect = spawn_mud_randomly(pygame.Rect(0, 0, 0, 0))

#tree
tree_size = (150, 150)
tree_image = pygame.image.load(os.path.join('tree.png')).convert_alpha()
tree_image = pygame.transform.scale(tree_image, tree_size)
tree_mask = pygame.mask.from_surface(tree_image)
tree_rect = spawn_tree_randomly(mud_rect)


def create_player_mask(player_image, player_size, player_x, player_y):

    player_surface = pygame.Surface((player_size, player_size), pygame.SRCALPHA)
    player_surface.blit(player_image, (0, 0))
    return pygame.mask.from_surface(player_surface)


def draw_text(text, font, color, surface, x, y):
    
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y))
    surface.blit(text_obj, text_rect)

player_x = width // 2
player_y = height // 2

def main_menu():
   
    button_color = (100, 200, 150)
    button_hover_color = (150, 255, 200)
    button_width = 400
    button_height = 80
    button_padding = 20
    
    
    menu_background = pygame.image.load('customgrass.png')

    title_font = pygame.font.SysFont("chalkboard", 50)
    button_font = pygame.font.SysFont("chalkboard", 50)
    
   
    start_button_rect = pygame.Rect(width // 2 - button_width // 2, height // 2 - 80, button_width, button_height)
    quit_button_rect = pygame.Rect(width // 2 - button_width // 2, height // 2 + button_padding, button_width, button_height)

    while True:
        
        screen.blit(menu_background, (0, 0))
        
        
        draw_text("WELCOME TO GOATBUSTERS", title_font, (255, 255, 255), screen, width // 2, 155)

        
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

        
        draw_text("Start Game", button_font, (0, 0, 0), screen, width // 2, height // 2 - 40)
        draw_text("Quit", button_font, (0, 0, 0), screen, width // 2, height // 2 + 60)

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()

        
main_menu()
#portal class
# Portal Class with Image
class Portal:
    def __init__(self, x, y, width, height, target_x, target_y):
        self.rect = pygame.Rect(x, y, width, height)  # Position and size of portal
        try:
            self.image = pygame.image.load('portal.png').convert_alpha()  # Load the portal image
            self.image = pygame.transform.scale(self.image, (width, height))  # Scale the image to the desired size
        except pygame.error as e:
            print(f"Error loading portal image: {e}")  # Debug print for loading issues
            self.image = pygame.Surface((width, height))  # Fallback to a placeholder surface
            self.image.fill((0, 0, 255))  # Blue color for fallback

        self.target_x = target_x  # Where the portal teleports the player (x-coordinate)
        self.target_y = target_y  # Where the portal teleports the player (y-coordinate)

    def draw(self, screen):
        screen.blit(self.image, self.rect)  # Draw the portal image on the screen

class Boss:
   def __init__(self):
       self.image = pygame.transform.scale(pygame.image.load(os.path.join('boss.png')).convert_alpha(), (enemy_size, enemy_size))
       self.rect = self.image.get_rect(center=(width // 2, height // 2))
       self.alive = True
       self.bullet_timer = 0
       self.bullet_interval = 6000  # 1 second
       self.bullets = []
       self.speed = 1
       self.health = 5  # Boss starts with 5 health points


   def take_damage(self):
        self.health -= 1
        if self.health <= 0:
            self.alive = False

   def move_towards_player(self, player_rect):
       if not self.alive:
           return
       # Calculate the direction vector towards the player
       direction = pygame.Vector2(player_rect.center) - pygame.Vector2(self.rect.center)
       if direction.length() != 0:
           direction = direction.normalize()  # Normalize direction vector for consistent speed
       # Update the enemy's position to move towards the player
       self.rect.x += direction.x * self.speed
       self.rect.y += direction.y * self.speed
       self.rect.x = max(0, min(width - boss_size, self.rect.x))
       self.rect.y = max(0, min(height - boss_size, self.rect.y))


   def move_away_from_other_enemies(self, enemies):
       if not self.alive:
           return
       for other_enemy in enemies:
           if other_enemy != self and other_enemy.alive:  # Check only against alive enemies
               if self.rect.colliderect(other_enemy.rect):  # If there's a collision
                   # Move this enemy away from the other enemy
                   overlap_direction = pygame.Vector2(self.rect.center) - pygame.Vector2(other_enemy.rect.center)
                   if overlap_direction.length() != 0:
                       overlap_direction = overlap_direction.normalize()  # Normalize direction
                   self.rect.x += overlap_direction.x * self.speed
                   self.rect.y += overlap_direction.y * self.speed
      


   def shoot_bullets(self):
       if self.alive:
           # Shoot bullets in a circular pattern
           for angle in range(0, 360, 45):  # Adjust angle step for more or fewer bullets
               bullet_speed = 5
               bullet_dx = bullet_speed * math.cos(math.radians(angle))
               bullet_dy = bullet_speed * math.sin(math.radians(angle))
               self.bullets.append(Bullet(self.rect.centerx, self.rect.centery, bullet_dx, bullet_dy))


   def update(self):
       # Update bullet positions
       for bullet in self.bullets:
           bullet.update()
           if bullet.is_off_screen():
               self.bullets.remove(bullet)


   def draw(self, screen):
       if self.alive:
           screen.blit(self.image, self.rect)
           for bullet in self.bullets:
               bullet.draw(screen)
              


class Bullet:
   def __init__(self, x, y, dx, dy):
       self.rect = pygame.Rect(x, y, bullet_size // 2, bullet_size // 2)  # Smaller size for bullets
       self.dx = dx
       self.dy = dy


   def update(self):
       self.rect.x += self.dx
       self.rect.y += self.dy


   def is_off_screen(self):
       return self.rect.x < 0 or self.rect.x > width or self.rect.y < 0 or self.rect.y > height


   def draw(self, screen):
       screen.blit(bullet_image2, self.rect)

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
        self.speed = 1
        self.alive = True

    # Move the enemy towards the player
    def move_towards_player(self, player_rect):
        if not self.alive:
            return
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
        if not self.alive:
            return
        for other_enemy in enemies:
            if other_enemy != self and other_enemy.alive:  # Check only against alive enemies
                if self.rect.colliderect(other_enemy.rect):  # If there's a collision
                    # Move this enemy away from the other enemy
                    overlap_direction = pygame.Vector2(self.rect.center) - pygame.Vector2(other_enemy.rect.center)
                    if overlap_direction.length() != 0:
                        overlap_direction = overlap_direction.normalize()  # Normalize direction
                    self.rect.x += overlap_direction.x * self.speed
                    self.rect.y += overlap_direction.y * self.speed
                    
    def draw(self, screen):
        if self.alive:  # Only draw if the enemy is alive
            screen.blit(enemy_image, self.rect)
    def kill(self):
        self.alive = False

# Create an object to help track time (FPS control)
clock = pygame.time.Clock()

# Flag to control the main game loop
running = True

# Instantiate an enemy object (can add more enemies as needed)
num_of_enemies = (level * 3)
spawncamp=[]
for i in range(num_of_enemies):
    spawncamp.append(Enemy())

hitbox_reduction = 75  # This will reduce 10 pixels from both width and height
player_hitbox_size = player_size - hitbox_reduction
player_hitbox = pygame.Rect(
    player_x + hitbox_reduction // 2,
    player_y + hitbox_reduction // 2,
    player_hitbox_size,
    player_hitbox_size
)

tree_hitbox_reduction_height = 60
tree_hitbox_reduction_width = 90
tree_hitbox_size = (tree_size[0] - tree_hitbox_reduction_width, tree_size[1] - tree_hitbox_reduction_height)
tree_hitbox = pygame.Rect(
    tree_rect.x + tree_hitbox_reduction_width // 2,  # Offset the hitbox to the center
    tree_rect.y + tree_hitbox_reduction_height // 2,  
    tree_hitbox_size[0], 
    tree_hitbox_size[1]
)

bullet_active = False

def fire_bullet(x, y):
    global bullet_active, bullet_x, bullet_y
    bullet_active = True
    bullet_x = x + player_size // 2 - bullet_size // 2
    bullet_y = y
    screen.blit(bullet_image, (bullet_x, bullet_y))

# Function to update player movement based on WASD keys
def update_player_movement():
    global player_x
    global player_y
    global player_image
    # Get the state of all keyboard buttons
    keys = pygame.key.get_pressed()

    original_x = player_x
    original_y = player_y
    
    # Update player's x and y coordinates based on key presses
    if keys[pygame.K_a]:  # Move left (A)
        player_x -= player_speed
        if not in_mud:
            player_image = pygame.transform.scale(
                    pygame.image.load(os.path.join('goat.png')).convert_alpha(),
                    (player_size, player_size)
                )
        else:
            player_image = pygame.transform.scale(
                pygame.image.load(os.path.join('mud_goat.png')).convert_alpha(),
                (player_size, player_size)
            )
    if keys[pygame.K_d]:  # Move right (D)
        player_x += player_speed
        if not in_mud:
            player_image = pygame.transform.scale(
                    pygame.image.load(os.path.join('goatR.png')).convert_alpha(),
                    (player_size, player_size)
                )
        else: 
            player_image = pygame.transform.scale(
                pygame.image.load(os.path.join('mud_goatR.png')).convert_alpha(),
                (player_size, player_size)
            )
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

    if player_hitbox.colliderect(tree_hitbox):
        # Reset player position if collision is detected
        player_x = original_x
        player_y = original_y
    


    # Update and return the player's rectangle for further processing (like collision detection)
    return pygame.Rect(player_x, player_y, player_size, player_size), player_hitbox




# Function to reset the game state (score, enemy and player position)
def reset_game():
    global player_x, player_y, score, enemy, mud_rect, mud_mask, tree_rect, tree_mask, tree_hitbox, boss

    player_x = width // 2 - player_size // 2
    player_y = height // 2 - player_size // 2

    num_of_enemies = level * 3
    spawncamp.clear()
    for i in range(num_of_enemies):
        spawncamp.append(Enemy())
   
    score = 0  # Reset score
    boss = Boss()


    mud_rect = spawn_mud_randomly(tree_rect)
    mud_mask = pygame.mask.from_surface(mud_image)
    tree_rect = spawn_tree_randomly(mud_rect)
    tree_mask = pygame.mask.from_surface(tree_image)

    # Update the player's hitbox after positioning
    player_hitbox = pygame.Rect(
        player_x + hitbox_reduction // 2,
        player_y + hitbox_reduction // 2,
        player_hitbox_size,
        player_hitbox_size
    )

    tree_hitbox = pygame.Rect(
        tree_rect.x + tree_hitbox_reduction_width // 2,  # Offset the hitbox to the center
        tree_rect.y + tree_hitbox_reduction_height // 2,  
        tree_hitbox_size[0], 
        tree_hitbox_size[1]
    )


# Function to display "You Died" message and a countdown to restart
def display_you_died_and_restart(screen):
    for i in range(3, 0, -1):  # Countdown from 5 to 1
        screen.fill((0, 0, 0))  # Clear the screen
        text = font.render(f'You Died! Restarting in {i}...', True, (255, 0, 0))
        screen.blit(text, (width // 2 - 150, height // 2))  # Display centered message
        pygame.display.flip()  # Update the screen
        time.sleep(1)  # Wait for 1 second
    reset_game()  # Reset the game after countdown

def winner(screen):
    screen.fill((255, 255, 255))
    text = font.render(f'CONGRATS YOU WON!', True, (0, 255, 255))
    screen.blit(text, (width // 2 - 150, height // 2))
    pygame.display.flip()
    



# Function to display the current score on the screen
def display_score(screen, score):
    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(score_text, (10, 10))  # Display score in the top-left corner

def display_level(screen, level):
    level_text = font.render(f'Level: {level}', True, (255, 255, 255))
    screen.blit(level_text, (10, 40))

# Define player's initial position at the center of the screen
player_x = width // 2
player_y = height // 2
time_since_last_score_increase = 0  # Track time to increase score every second


player_mask = create_player_mask(player_image, player_size, player_x, player_y)



# Function to display level-up announcement
def display_level_change(screen, level):
    screen.fill((0, 0, 0))
    reset_game()
    level_text = font.render(f'Level {level}', True, (255, 255, 0))  # Yellow color for level change announcement
    screen.blit(level_text, (width // 2 - 50, height // 2))
    pygame.display.flip()
    time.sleep(2)  # Pause for 2 seconds to display the level change

# Function to display the current score and level
def display_score_and_level(screen, score, level):
    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
    level_text = font.render(f'Level: {level}', True, (255, 255, 255))
    screen.blit(score_text, (10, 10))  # Display score in the top-left corner
    screen.blit(level_text, (10, 50))  # Display level below score

mud_rect = spawn_mud_randomly(pygame.Rect(0, 0, 0, 0)) 
tree_rect = spawn_tree_randomly(mud_rect)

tree_hitbox = pygame.Rect(
    tree_rect.x + tree_hitbox_reduction_width // 2,
    tree_rect.y + tree_hitbox_reduction_height // 2,
    tree_hitbox_size[0],
    tree_hitbox_size[1]
)
portals = []
portals.append(Portal(100, 150, 50, 50, 500, 400))  
portals.append(Portal(300, 450, 50, 50, 100, 100))  

boss = Boss()

### Main Game Loop ###
while running:

    keys = pygame.key.get_pressed()
    # Event handling
    for event in pygame.event.get():
        # Quit the game if the user closes the window
        if event.type == pygame.QUIT:
            running = False

    for bullet in boss.bullets:
       if bullet.rect.colliderect(player_hitbox):
           # Handle player getting hit by boss bullets
           display_you_died_and_restart(screen)

    # Update player position based on movement input
    player_rect, player_hitbox = update_player_movement()

    for portal in portals:
        portal.draw(screen)  # Draw each portal on the screen

    if (keys[pygame.K_RIGHT] or keys[pygame.K_LEFT]) and bullet_state == "ready":
        fire_bullet(player_x, player_y)
        bullet_dir = "right" if keys[pygame.K_RIGHT] else "left"

    for enemy in spawncamp:
        if enemy.alive and bullet_active:
            bullet_rect = pygame.Rect(bullet_x, bullet_y, bullet_size, bullet_size)
            if enemy.rect.colliderect(bullet_rect):
                enemy.kill()  # Mark the enemy as dead
                bullet_active = False  # Reset bullet state
                break  # Exit the loop after the bullet hits one ghost    

    for enemy in spawncamp:
        if enemy.alive:  # Only move if the enemy is alive
            enemy.move_towards_player(player_rect)
            enemy.move_away_from_other_enemies(spawncamp)


    # Check if all enemies are dead
    all_enemies_dead = all(not enemy.alive for enemy in spawncamp)
    boss_dead = not boss.alive

# If all enemies are dead, increase the level and reset the game
    if level < 5:
        if all_enemies_dead:
            level += 1
            reset_game()  # Reset the game state for the new level
            display_level_change(screen, level)

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


    for portal in portals:
        if player_rect.colliderect(portal.rect):  # If player collides with the portal
            player_x = portal.target_x  # Teleport player to the target position
            player_y = portal.target_y
            player_rect.topleft = (player_x, player_y)  # Update the player's rectangle position

    # Fill the background with black
    screen.fill((0, 0, 0))

    for enemy in spawncamp:
        enemy.draw(screen)

    #set background
    screen.blit(background, (0,0))
    
    if level >= 5:
        if not boss.alive:  # Check if the boss is dead
            boss = Boss()  # Create a new boss instance
            boss.alive = True  # Set boss as alive

        if boss.alive:
            boss.draw(screen)
            boss.move_towards_player(player_rect)
            boss.move_away_from_other_enemies(spawncamp)
            boss.bullet_timer += clock.get_time()
            if boss.bullet_timer > boss.bullet_interval:
                boss.shoot_bullets()
                boss.bullet_timer = 0
            boss.update()

            # Check if player's bullet hits the boss
            if bullet_active:
                bullet_rect = pygame.Rect(bullet_x, bullet_y, bullet_size, bullet_size)
                if boss.rect.colliderect(bullet_rect):
                    boss.take_damage()  # Call the take_damage method
                    bullet_active = False  # Reset bullet state

            # Check if the boss has been defeated
            if not boss.alive:
                level += 1  # Increase the level

                winner(screen)  # Reset game state
    for portal in portals:
        portal.draw(screen)
    # Draw stuff on the screen
    screen.blit(mud_image, mud_rect)
    screen.blit(player_image, player_rect)
    screen.blit(tree_image, tree_rect)

    
    # Draw the enemy on the screen
    for i in range(num_of_enemies):
        num_of_enemies = level * 3
        spawncamp[i].draw(screen)
    #enemy.draw(screen)
    #enemy2.draw(screen)

    collision1 = False
    for enemy in spawncamp:
        if score >= 1:
            if enemy.alive and player_hitbox.colliderect(enemy.rect):  # Only check collision with alive enemies
                collision1 = True
                break

            
    # If no collision occurs, increase the score every second
    if not collision1:
        time_since_last_score_increase += clock.get_time()  # Track the time since last score increase
        if time_since_last_score_increase > 1000:  # 1000 ms = 1 second
            score += 1  # Increase the score by 1
            time_since_last_score_increase = 0  # Reset the timer

    # Initialize variables
    mud_collision_time = None  # Track when the player enters the mud
    mud_slowdown_duration = 3000  # Slowdown lasts for 3 seconds (3000 milliseconds)
    in_mud = False

    # Inside the main game loop where you handle the mud collision:
    # Handle mud collision and slowdown
    if mud_collision:
        if not in_mud:  # Player just collided with the mud
            in_mud = True
            mud_collision_time = pygame.time.get_ticks()  # Track the time the player enters the mud
            player_speed = 1.5  # Slow down the player
            player_image = pygame.transform.scale(
                pygame.image.load(os.path.join('mud_goat.png')).convert_alpha(),
                (player_size, player_size)
            )
    else:
        in_mud = False
          # Player is not in mud anymore
  # Slow down the player

    # Check if enough time has passed to restore the speed
    # Check if enough time has passed to restore the player's speed
    if in_mud and mud_collision_time is not None:
        current_time = pygame.time.get_ticks()
        if current_time - mud_collision_time > mud_slowdown_duration:  # If 3 seconds passed
            player_speed = 3  # Restore the player's speed
            player_image = pygame.transform.scale(
                pygame.image.load(os.path.join('goat.png')).convert_alpha(),
                (player_size, player_size)
            )
            mud_collision_time = None 
    # If the player exits the mud, ensure the speed returns to normal
    if not in_mud and mud_collision_time is None:
        player_speed = 8  # Restore player speed immediately if out of mud
        player_image = pygame.transform.scale(
                pygame.image.load(os.path.join('goat.png')).convert_alpha(),
                (player_size, player_size)
            )
    # Reset the mud collision timer

    # If collision occurs, show "You Died" and restart after 5 seconds
    if collision1:
        display_you_died_and_restart(screen)

    # Display the current score
    display_score(screen, score)
    display_level(screen, level)

    if bullet_active:
        if bullet_dir == "right":
            bullet_x += bulletx_change
            if bullet_x > width:  # Off-screen check
                bullet_active = False
        elif bullet_dir == "left":
            bullet_x -= bulletx_change
            if bullet_x < 0:  # Off-screen check
                bullet_active = False

    if bullet_active:
        screen.blit(bullet_image, (bullet_x, bullet_y))

    if bullet_active:
        if bullet_rect.colliderect(tree_hitbox):
            bullet_active = False
    
       
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
