#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sitecustomize
import sys

#module of game states
import title

import character


#module that has global variables
import gv
#module that has global functions
import gf

class arcanum_saga:

    def __init__(self):

        #initialize pygame
        pygame.init()

        #creates window of SCREEN_RECTANGLE
        self.screen = pygame.display.set_mode(gv.SCREEN_RECTANGLE.size)

        #stores characters in party
        self.party = []

        self.party.append(character.Character("girl14/$Actor14.png"))


        #initialize game state
        self.title = title.Title()
        self.character_make = None
        self.field = None

        #set the title of the program (on left-top bar)
        pygame.display.set_caption("Arcanum SaGa")

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
        elif self.game_state == gv.CHARACTER_MAKE:
            self.character_make.update()
        elif self.game_state == gv.FIELD:
            self.party[0].update()
            self.field.update()
 
        pass

    def render(self):

        #fill background with black
        #if no previous rendering is needed
        self.screen.fill(gv.COLOR_BLACK)

        if self.game_state == gv.TITLE:
            self.title.render(self.screen)
        elif self.game_state == gv.CHARACTER_MAKE:
            self.character_make.render(self.screen)
        elif self.game_state == gv.FIELD:
            self.field.render(self.party,self.screen)

    def check_event(self):

        #traverse all events from user
        for event in pygame.event.get():

            #event to end program
            if gf.gamequit_key_pressed(event):
                gf.end_game()

            #add all other event handler here:
            #add self for changing states
            if self.game_state == gv.TITLE:
                self.title.event_handler(event, self)
            elif self.game_state == gv.CHARACTER_MAKE:
                self.character_make.event_handler(event, self)
            elif self.game_state == gv.FIELD:
                self.field.event_handler(event, self)




if __name__== "__main__":
    arcanum_saga()
            
