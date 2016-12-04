#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
import math

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

class Sprite(pygame.sprite.Sprite):
    """ This is a sprite only used for collision detection. """
    def __init__(self,x,y,width,height):
        # Call the parent class (sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x,y,width,height)

class Block(pygame.sprite.Sprite):
    def __init__(self,x,y,filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

class Player(pygame.sprite.Sprite):
    change = 0
    def __init__(self,filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect()
        posX = (SCREEN_WIDTH /2) - (self.rect.width /2)
        posY = 420
        self.rect.topleft = (posX,posY)

    def reset_position(self):
        posX = (SCREEN_WIDTH /2) - (self.rect.width /2)
        posY = 420
        self.rect.topleft = (posX,posY)

    def update(self):
        if self.rect.left > 0 and self.change < 0:
            self.rect.x += self.change 
        elif self.rect.right < SCREEN_WIDTH and self.change > 0:
            self.rect.x += self.change 

    def move_right(self):
        self.change = 3

    def move_left(self):
        self.change = -3

    def stop(self):
        self.change = 0

    def draw(self,screen):
        # Draw the player onto the screen
        screen.blit(self.image,self.rect)


class Ball(pygame.sprite.Sprite):
    """ This is a sprite that will change direction depending on the side
    it hits another sprite. """
    def __init__(self,x,y,filename,angle=0):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        # Load the image
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect()
        posX = (SCREEN_WIDTH /2) - (self.rect.width /2)
        posY = 420
        self.rect.bottomleft = (posX,posY)
        # Set the direction angle
        self.angle = angle
        # Create two sprites which will be used only for collision detection
        self.sprite_x = Sprite(x,y+5,self.rect.width,self.rect.height-10)
        self.sprite_y = Sprite(x+5,y,self.rect.width-10,self.rect.height)
        
        # Load sound effects:
        self.bounce_sound = pygame.mixer.Sound("bounce.ogg")
        self.bounce_sound2 = pygame.mixer.Sound("bounce2.ogg")
        
    def reset_position(self):
        # Reset the position of the ball
        posX = (SCREEN_WIDTH /2) - (self.rect.width /2)
        posY = 420
        self.rect.bottomleft = (posX,posY)

    def update(self,block_group,player):
        # Move the ball
        self.move()
        # Check for collision
        self.collide(block_group,player)


    def move(self):
        # Check if the ball hit the boundaries of the screen
        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.angle = 180 - self.angle
        if self.rect.top <= 0:
            self.angle = 360 - self.angle
        # Increase the x and y coordinates depending on the angle direction
        self.rect.x += int(math.cos(math.radians(self.angle)) * 5)
        self.rect.y += int(math.sin(math.radians(self.angle)) * 5)
        # update the position of the sprites
        self.sprite_x.rect.center = self.rect.center
        self.sprite_y.rect.center = self.rect.center
        # Used when angle is greater or equal than 360 or less than 360
        if self.angle >= 360:
            self.angle -= 360
        elif self.angle < 0:
            self.angle += 360

        
    def collide(self,block_group,player):
        # Check for collision with sprites in block_group
        for sprite in pygame.sprite.spritecollide(self,block_group,True):
            # Check if the ball hit the sprite on the x axis
            if pygame.sprite.collide_rect(self.sprite_x,sprite):
                if self.sprite_x.rect.centerx < sprite.rect.centerx:
                    self.sprite_x.rect.right = sprite.rect.left
                else:
                    self.sprite_x.rect.left = sprite.rect.right
                self.rect.center = self.sprite_y.rect.center = self.sprite_x.rect.center
                self.angle = 180 - self.angle
            # Check if the ball hit the sprite on the y axis
            elif pygame.sprite.collide_rect(self.sprite_y,sprite):
                if self.sprite_y.rect.centery < sprite.rect.centery:
                    self.sprite_y.rect.bottom = sprite.rect.top
                else:
                    self.sprite_y.rect.top = sprite.rect.bottom
                self.rect.center = self.sprite_x.rect.center = self.sprite_y.rect.center
                self.angle = 360 - self.angle
            else:
                # Check if the ball hit the corner of the sprite
                if sprite.rect.centerx < self.rect.centerx:
                    if sprite.rect.centery < self.rect.centery:
                        self.angle = 45
                    else:
                        self.angle = 315
                else:
                    if sprite.rect.centery < self.rect.centery:
                        self.angle = 135
                    else:
                        self.angle = 225
            # Play sound effect
            self.bounce_sound.play()
            # Jump out of the loop
            break

        if pygame.sprite.collide_rect(self,player):
            # Check if the ball hit the player on the y axis
            if pygame.sprite.collide_rect(self.sprite_y,player):
                if self.sprite_y.rect.centery < player.rect.centery:
                    self.sprite_y.rect.bottom = player.rect.top
                else:
                    self.sprite_y.rect.top = player.rect.bottom
                self.rect.center = self.sprite_x.rect.center = self.sprite_y.rect.center
                self.angle = 360 - self.angle
            # Check if the ball hit the player on the x axis
            elif pygame.sprite.collide_rect(self.sprite_x,player):
                if self.sprite_x.rect.centerx < player.rect.centerx:
                    self.sprite_x.rect.right = player.rect.left
                else:
                    self.sprite_x.rect.left = player.rect.right
                self.rect.center = self.sprite_y.rect.center = self.sprite_x.rect.center
                self.angle = 180 - self.angle
            else:
                # Check if the ball hit the corner of the player
                if player.rect.centerx < self.rect.centerx:
                    if player.rect.centery < self.rect.centery:
                        self.angle = 45        
                    else:
                        self.angle = 315
                else:
                    if player.rect.centery < self.rect.centery:
                        self.angle = 135
                    else:
                        self.angle = 225
            
            # Play sound effect
            self.bounce_sound2.play()

    def draw(self,screen):
        # Draw the ball onto the screen
        screen.blit(self.image,self.rect)
