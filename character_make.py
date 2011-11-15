#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sitecustomize

#module that has global variables
import gv
#module that has global functions
import gf

class Character_make:

    #character select
    #main weapon, sub weapon
    #job
    #god

    CATEGORY_SELECT, GENDER_SELECT, CHARACTER_SELECT, NAME_SELECT, JOB_SELECT, GOD_SELECT = 0,1,2,3,4,5
    
    def __init__(self):

        self.state = self.CATEGORY_SELECT

        self.gender = 0

        
        self.character_number = 0

        self.name = ""

        self.job = 0

        self.god = 0

        self.bonus = 0

    def update(self):
        if self.state == self.CATEGORY_SELECT:
            pass
        elif self.state == self.GENDER_SELECT:
            pass
        elif self.state == self.CHARACTER_SELECT:
            pass
        elif self.state == self.NAME_SELECT:
            pass
        elif self.state == self.JOB_SELECT:
            pass
        elif self.state == self.GOD_SELECT:
            pass
    def render(self,screen):

        if self.state == self.CATEGORY_SELECT:
            pass
        elif self.state == self.GENDER_SELECT:
            pass
        elif self.state == self.CHARACTER_SELECT:
            pass
        elif self.state == self.NAME_SELECT:
            pass
        elif self.state == self.JOB_SELECT:
            pass
        elif self.state == self.GOD_SELECT:
            pass
        pass

    def event_handler(self,event, arcanum_saga):
        
        if self.state == self.CATEGORY_SELECT:
            pass
        elif self.state == self.GENDER_SELECT:
            pass
        elif self.state == self.CHARACTER_SELECT:
            pass
        elif self.state == self.NAME_SELECT:
            pass
        elif self.state == self.JOB_SELECT:
            pass
        elif self.state == self.GOD_SELECT:
            pass
