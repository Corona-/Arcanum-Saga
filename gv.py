#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sitecustomize

#######################################
# This file defines variables that is
# used in the game program. Mainly used
# to remove magic numbers and make the
# program easier to read.
#######################################

#######################################
# Variables for the characters
#######################################

IMAGE_SIZE = 32

DIRECTION_DOWN = 0
DIRECTION_LEFT = 1
DIRECTION_RIGHT = 2
DIRECTION_UP = 3



#######################################
# Variables for the game state
#######################################

TITLE = 0
CHARACTER_MAKE = 1
FIELD = 2

#######################################
# Variables for the character make
#######################################

MALE = 0
FEMALE = 1



#jobs
FIGHTER = 0
MAGICIAN = 1
PRIEST = 2
THIEF = 3
ARCHER = 4
MERCHANT = 5
FARMER = 6
NOVICE = 7
#hidden job
MONSTER = 8



#gods
ZEUS = 0
HERA = 1
ATHENA = 2
APOLLON = 3
APHRODITE = 4
ARES = 5
ARTEMIS = 6
DEMETER = 7
HEPHAISTOS = 8
HERMES = 9
POSEIDON = 10
HESTIA = 11
#hidden god
DEATH = 12


#######################################
# Variables for the skill and jobs
#######################################



#######################################
# Variables for the game screen
#######################################

SCREEN_RECTANGLE = Rect(0,0,640,480)

#######################################
# Variables for the color
#######################################

COLOR_BLACK = (0,0,0)
COLOR_WHITE = (255,255,255)


#######################################
# Variables for the text size of font
#######################################

TEXT_SIZE_TITLE = 60
TEXT_SIZE_NORMAL = 20
TEXT_SIZE_SMALL = 10

pygame.init()
TM_TITLE_FONT = pygame.font.Font("Font/togoshi-mincho.ttf", TEXT_SIZE_TITLE)
TM_NORMAL_FONT = pygame.font.Font("Font/togoshi-mincho.ttf", TEXT_SIZE_NORMAL)
TM_SMALL_FONT = pygame.font.Font("Font/togoshi-mincho.ttf", TEXT_SIZE_SMALL)
