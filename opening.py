#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sitecustomize

#module that has global variables
import gv
#module that has global functions
import gf

class Opening:

    #time for the opening class
    TIME = 240

    def __init__(self):

        #store the current time
        self.time = 0

        self.menu_font = gv.TM_NORMAL_FONT

        #text for the opening
        #self.text

        #image on the background of the opening
        #self.background

        self.music = 0

    def update(self):
        pass

    def render(self, screen):

        #if self.time...

        pass
        
    def event_handler(self, event):

        #may skip opening by pressing a selecting key
        
        pass
