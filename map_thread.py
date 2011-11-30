#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sitecustomize

#to read and write binary
import struct

import os
import string
import codecs

import field
import thread

#module that has global variables
import gv
#module that has global functions
import gf

import threading
import thread

import multiprocessing

class Map_load_thread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.map_object = None
        self.direction = 0

    def run ( self):
        if self.map_object != None:
            #self.map_object.add_new_map( self.direction)
            thread.start_new_thread(self.map_object.add_new_map, (self.direction,))
    def setUp(self, map_object, direction):
        self.map_object = map_object
        self.direction = direction


class Map_load_process(multiprocessing.Process):

    def __init__(self):
        multiprocessing.Process.__init__(self)
        self.map_object = None
        self.direction = 0

    def run ( self):
        if self.map_object != None:
            self.map_object.add_new_map(self.direction)
    def setUp(self, map_object, direction):
        self.map_object = map_object
        self.direction = direction

