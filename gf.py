#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sitecustomize

import sys


#######################################
# This file defines functions that is
# used in the game program. Mainly used
# to simplify the code and reusing of
# similar codes
#######################################

#######################################
# The function to move the menu item.
# The object should have self.menu variable
# and the event would increment/decrement
# that variable with arrow key.
#@param obj is the object that has menu item
#@param event is the event on the game
#@return null
#######################################

def traverse_menu( obj, event ):
    if event.type == KEYDOWN and event.key == K_UP:
        obj.menu -= 1
        if obj.menu < 0:
            obj.menu = obj.MENUMAX

    if event.type == KEYDOWN and event.key == K_DOWN:
        obj.menu += 1
        if obj.menu > obj.MENUMAX:
            obj.menu = 0

#######################################
# The function that selects some of the
# key and check if it is pressed
#@param event is the event on the game
#@return bool - true if selecting key is pressed
#######################################

def selecting_key_pressed (event):
    return (event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_z or event.key == K_RETURN))

def gamequit_key_pressed (event):
    return (event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE))
 
#######################################
# The function that is called when the
# program is going to be closed.
#@return null
#######################################

def end_game():
    pygame.quit()
    sys.exit()
    
