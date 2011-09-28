#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sitecustomize

#module that has global variables
import gv

class Title:

    #used on menu, each variable represents item on menu
    NEWGAME, LOADGAME, CONFIG, ENDGAME = 0, 1, 2, 3

    def __init__(self):

        #store the state of menu, initially set on new game
        self.menu = self.NEWGAME

        #creates font with different sizes
        self.title_font = pygame.font.Font("togoshi-mincho.ttf", gv.TEXT_SIZE_TITLE)
        self.menu_font = pygame.font.Font("togoshi-mincho.ttf", gv.TEXT_SIZE_NORMAL)
        self.copyright_font = pygame.font.Font("togoshi-mincho.ttf", gv.TEXT_SIZE_SMALL)

        #set the string of fonts            
        self.title_font = self.title_font.render("ARCANUM SAGA", True, gv.COLOR_BLACK)           
        self.newgame_font = self.menu_font.render("NEW GAME", True, gv.COLOR_BLACK)
        self.loadgame_font = self.menu_font.render("LOAD GAME", True, gv.COLOR_BLACK)
        self.config_font = self.menu_font.render("CONFIG", True, gv.COLOR_BLACK)
        self.endgame_font = self.menu_font.render("END GAME", True, gv.COLOR_BLACK)
        self.credit_font = self.copyright_font.render("Created by...?", True, gv.COLOR_BLACK)
        self.cursor = self.menu_font.render(u"⇒", True, gv.COLOR_BLACK)

        self.music = 0

    def update(self):
        pass

    def render(self, screen):
        #fill background with white
        screen.fill(gv.COLOR_WHITE)

        #draw title font
        screen.blit(self.title_font, ((gv.SCREEN_RECTANGLE.width-self.title_font.get_width())/2, (gv.SCREEN_RECTANGLE.height/6)+30))

        #draw menu font
        screen.blit(self.newgame_font, ((gv.SCREEN_RECTANGLE.width-self.newgame_font.get_width())/2, (gv.SCREEN_RECTANGLE.height/2)))
        screen.blit(self.loadgame_font, ((gv.SCREEN_RECTANGLE.width-self.loadgame_font.get_width())/2, (gv.SCREEN_RECTANGLE.height/2+30)))
        screen.blit(self.config_font, ((gv.SCREEN_RECTANGLE.width-self.config_font.get_width())/2, (gv.SCREEN_RECTANGLE.height/2+60)))
        screen.blit(self.endgame_font, ((gv.SCREEN_RECTANGLE.width-self.endgame_font.get_width())/2, (gv.SCREEN_RECTANGLE.height/2+90)))
        
        #draw credit
        screen.blit(self.credit_font, ((gv.SCREEN_RECTANGLE.width-self.credit_font.get_width())/2, (gv.SCREEN_RECTANGLE.height*5/6)))
        
