#!/usr/bin/env python
# -*- coding: utf-8 -*-
#	< > \n

import pygame
from player import *
import random
from levels import *

# Define some colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
LIME = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
CYAN = (0,255,255)
MAGENTA = (255,0,255)
SILVER = (192,192,192)
GRAY = (128,128,128)
MAROON = (128,0,0)
OLIVE = (128,128,0)
GREEN = (0,128,0)
PURPLE = (128,0,128)
TEAL = (0,128,128)
NAVY = (0,0,128)

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

class Game(object):
    def __init__(self):
        self.font = pygame.font.Font("y.n.w.u.a.y.ttf",25)
        self.font_color = BLACK
        self.about_screen = False
        self.game_over = True
        self.round_screen = True
        self.you_won_message = False
        self.game_over_message = False
        self.menu = Menu(("start","about","exit"),ttf_font="y.n.w.u.a.y.ttf",font_size=40)
    
        # Define levels
        self.levels = (level_1(),level_2(),level_3(),level_4(),level_5(),level_6(),level_7(),
                       level_8(),level_9())
        self.level_number = 0
        self.current_level = self.levels[self.level_number]
        
        # Create the ball and the player
        angle = random.choice((210,215,220,225,230,235,240,300,305,310,315,320,325,330))
        ball_filename = random.choice(("ball-1.png","ball-2.png","ball-3.png","ball-4.png"))
        self.ball = Ball(320,400,ball_filename,angle)
        self.player = Player("player.png")
        
    def process_events(self):
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                return True
            self.menu.event_handler(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if self.game_over and not self.about_screen:
                        if self.menu.state == 0:
                            self.__init__()
                            self.game_over = False
                        elif self.menu.state == 1:
                            self.about_screen = True
                        elif self.menu.state == 2:
                            # User clicked exit
                            return True

                elif event.key == pygame.K_RIGHT:
                    self.player.move_right()

                elif event.key == pygame.K_LEFT:
                    self.player.move_left()
                
                elif event.key == pygame.K_ESCAPE:
                    self.game_over = True
                    self.about_screen = False
                    
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.player.stop()

                elif event.key == pygame.K_LEFT:
                    self.player.stop()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                print self.ball.rect.topleft
                    
        return False

    def run_logic(self):
        if not self.game_over:
            # Check if we have to go to the next level
            if len(self.current_level) < 1:
                self.round_screen = True
                if self.level_number < len(self.levels) -1:
                    self.level_number += 1
                    self.current_level = self.levels[self.level_number]
                    self.ball.reset_position()
                    self.player.reset_position()
                else:
                    self.game_over = True
                    self.you_won_message = True
            else:
                # Check if the ball is out of the screen
                if self.ball.rect.y > SCREEN_HEIGHT:
                    self.game_over = True
                    self.game_over_message = True
                # Run the logic of the game
                self.ball.update(self.current_level,self.player)
                self.player.update()

    def display_frame(self,screen):
        # First, clear the screen to white. Don't put other drawing commands
        screen.fill(TEAL)
        # --- Drawing code should go here
        if self.game_over:
            if self.about_screen:
                self.display_message(screen,"This game was written by:","Eduardo Grando")
            elif self.you_won_message:
                self.display_message(screen,"Congratulations!","You Won!")
                self.you_won_message = False
                pygame.display.flip()
                pygame.time.wait(1500)
            elif self.game_over_message:
                self.game_over_message = False
                self.display_message(screen,"GAME OVER")
                pygame.display.flip()
                pygame.time.wait(1000)
            else:
                self.menu.display_frame(screen)
        else:
            if self.round_screen:
                self.display_message(screen,"Round " + str(self.level_number +1))
                self.round_screen = False
                pygame.display.flip()
                pygame.time.wait(1000)
            else:
                self.current_level.draw(screen)
                self.ball.draw(screen)
                self.player.draw(screen)
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
        
    def display_message(self,screen,*args):
        for index, message in enumerate(args):
            label = self.font.render(message,True,self.font_color)
            # Get the width and height of the label
            width = label.get_width()
            height = label.get_height()
            
            posX = (SCREEN_WIDTH /2) - (width /2)
            # t_h: total height of text block
            t_h = len(args) * height
            posY = (SCREEN_HEIGHT /2) - (t_h /2) + (index * height)
            
            screen.blit(label,(posX,posY))


class Menu(object):
    state = 0
    def __init__(self,items,font_color=(0,0,0),select_color=(255,0,0),ttf_font=None,font_size=25):
        self.font_color = font_color
        self.select_color = select_color
        self.items = items
        self.font = pygame.font.Font(ttf_font,font_size)
        
    def display_frame(self,screen):
        for index, item in enumerate(self.items):
            if self.state == index:
                label = self.font.render(item,True,self.select_color)
            else:
                label = self.font.render(item,True,self.font_color)
            
            width = label.get_width()
            height = label.get_height()
            
            posX = (SCREEN_WIDTH /2) - (width /2)
            # t_h: total height of text block
            t_h = len(self.items) * height
            posY = (SCREEN_HEIGHT /2) - (t_h /2) + (index * height)
            
            screen.blit(label,(posX,posY))
        
    def event_handler(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if self.state > 0:
                    self.state -= 1
            elif event.key == pygame.K_DOWN:
                if self.state < len(self.items) -1:
                    self.state += 1
