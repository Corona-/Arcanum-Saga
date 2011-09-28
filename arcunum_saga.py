#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sitecustomize
import sys

#module of game states
import title

#module that has global variables
import gv

class arcunum_saga:

    def __init__(self):

        #initialize pygame
        pygame.init()

        #creates window of SCREEN_RECTANGLE
        self.screen = pygame.display.set_mode(gv.SCREEN_RECTANGLE.size)

        #initialize game state
        self.title = title.Title()

        #set the title of the program (on left-top bar)
        pygame.display.set_caption("Arcunum SaGa")

        self.game_state = gv.TITLE

        self.main_loop()

    def main_loop(self):

        clock = pygame.time.Clock()

        while True:

            #wait until clock tick 60 or frame rate of 60
            clock.tick(60)

            #updates the objects of game
            self.update()

            #deciding what to draw on screen
            self.render()

            #Update the screen
            pygame.display.update()

            #check the event happened and change game state accordingly
            self.check_event()

    def update(self):

        if self.game_state == gv.TITLE:
            self.title.update()
        pass

    def render(self):

        #fill background with black
        #self.screen.fill(gv.COLOR_BLACK)

        if self.game_state == gv.TITLE:
            self.title.render(self.screen)

    def check_event(self):

        #traverse all events from user
        for event in pygame.event.get():

            #event to end program
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            #add all other event handler here:


if __name__== "__main__":
    arcunum_saga()
            
