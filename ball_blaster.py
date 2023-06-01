import math
import os
import pygame

class Wall(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((200, 20))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Ball(pygame.sprite.Sprite):
    def __init__(self, pos, vector):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(pos[0], pos[1], 50, 50)
        self.vector = vector
        self.time = 0
        self.gravity = 9.8

    def update(self):
        newpos = self.calcnewpos(self.rect,self.vector)
        self.rect = newpos

    def calcnewpos(self,rect,vector):
        (angle,z) = vector
        (dx,dy) = (z*math.cos(angle), z*math.sin(angle) + (self.time * self.gravity))
        return rect.move(dx,dy)

    def draw(self, screen):
        # Blit the ball onto the game screen
        pygame.draw.ellipse(screen, (255, 255, 255), self.rect)

def load_png(name):
    """ Load image and return image object"""
    fullname = os.path.join("data", name)
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except FileNotFoundError:
        print(f"Cannot load image: {fullname}")
        raise SystemExit
    return image, image.get_rect()

def main():
    # Initialize
    pygame.init()
    width, height = 1000, 1000  # Set your desired window dimensions
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Ball Blaster")

    # Sprite groups
    all_sprites = pygame.sprite.Group()
    walls = pygame.sprite.Group()

    # Create instances of the Ball and Wall classes
    ball = Ball((100, 100), [1, 1])
    wall = Wall((300, 400))

    # Add sprites to their respective groups
    all_sprites.add(ball)
    all_sprites.add(wall)
    walls.add(wall)
    
    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Add your game logic and update the game state here
        ball.update()

        screen.fill((0, 0, 0))  # Clear the screen with a solid color

        # Add your game rendering code here
        ball.draw(screen)

        pygame.display.flip()  # Update the display

    pygame.quit()  # Quit Pygame when the game loop ends

    # # Handle user input
    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_LEFT]:
    #     # Handle left arrow key press
    # elif keys[pygame.K_RIGHT]:
    #     # Handle right arrow key press

main()