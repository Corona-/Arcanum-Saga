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

import title

import time
import multiprocessing

#module that has global variables
import gv
#module that has global functions
import gf

import map_thread

def add_new_map(self, direction, q):
    print "int"
    start = time.clock()
    if direction == gv.DIRECTION_LEFT:
        self.other_map.append(field.Field(self.northwest_map,0))
        self.other_map.append(field.Field(self.west_map,3))
        self.other_map.append(field.Field(self.southwest_map,6))
    elif direction == gv.DIRECTION_RIGHT:
        self.other_map.append(field.Field(self.northeast_map,2))
        self.other_map.append(field.Field(self.east_map,5))
        self.other_map.append(field.Field(self.southeast_map,8))
    elif direction == gv.DIRECTION_UP:
        self.other_map.append(field.Field(self.northwest_map,0))
        self.other_map.append(field.Field(self.north_map,1))
        self.other_map.append(field.Field(self.northeast_map,2))

    elif direction == gv.DIRECTION_DOWN:
        self.other_map.append(field.Field(self.southwest_map,6))
        self.other_map.append(field.Field(self.south_map,7))
        self.other_map.append(field.Field(self.southeast_map,8))
    end = time.clock()

    q.put(self.other_map)
    print end-start

class Map:
    def __init__(self, file_name):

        #as showing map, show map surrounds that map
        self.other_map = []

        self.map_name = file_name



        self.north_map=""
        self.south_map=""
        self.east_map=""
        self.west_map=""
        self.northwest_map=""
        self.northeast_map=""
        self.southwest_map=""
        self.southeast_map=""

        #self.other_map.append(field.Field(file_name))

        self.get_surrounding_fields()

        self.map_load_thread = None
        self.map_load_process = None

        self.q = multiprocessing.Queue()


    def update(self, party):

        #the thread updates the map and add up to 9 fields
        #otherwise, thread is not finished so not start another thread
        if (len(self.other_map) == 9):
        
            if party[0].x < 0:
                #now that update of map doesn't occur when moving map,
                #need to change the offset
                party[0].x += gv.MAPSIZE
                self.change_map(gv.DIRECTION_LEFT)
                
            elif party[0].x >= gv.MAPSIZE:
                party[0].x -= gv.MAPSIZE
                self.change_map(gv.DIRECTION_RIGHT)
                       
            elif party[0].y < 0:
                party[0].y += gv.MAPSIZE
                self.change_map(gv.DIRECTION_UP)
            elif party[0].y >= gv.MAPSIZE:
                party[0].y -= gv.MAPSIZE
                self.change_map(gv.DIRECTION_DOWN)

            #need to move this before 4 simple directions
            elif party[0].x < 0 and party[0].y < 0:
                party[0].x += gv.MAPSIZE
                party[0].y += gv.MAPSIZE

                self.change_map(gv.DIRECTION_TOPLEFT)
            
            elif party[0].x > gv.MAPSIZE and party[0].y < 0:
                party[0].x -= gv.MAPSIZE
                party[0].y += gv.MAPSIZE

                self.change_map(gv.DIRECTION_TOPRIGHT)

            elif party[0].x < 0 and party[0].y >= gv.MAPSIZE:
                party[0].x += gv.MAPSIZE
                party[0].y -= gv.MAPSIZE

                self.change_map(gv.DIRECTION_DOWNLEFT)

            elif party[0].x >= gv.MAPSIZE and party[0].y >= gv.MAPSIZE:
                party[0].x -= gv.MAPSIZE
                party[0].y -= gv.MAPSIZE

                self.change_map(gv.DIRECTION_DOWNRIGHT)

    def render(self, party, screen):

        screen.fill(gv.COLOR_BLACK)


        #print party[0].x
        #print party[0].y
        for field_map in self.other_map:
            field_map.render(party, screen)


        if self.map_load_process != None and self.map_load_process.is_alive():
            self.other_map = self.q.get()
            self.map_load_process.join()
            

##
##        for chara in party:
##            chara.render(screen)

##        if self.map_load_thread.isAlive():
##            self.map_load_thread.join()
##            self.map_load_thread = None
##  

    def event_handler(self, event, arcanum_saga):

        if event.type == KEYDOWN and event.key == K_x:

            arcanum_saga.map = None
            arcanum_saga.game_state = gv.TITLE
            arcanum_saga.title = title.Title()
        pass


    def get_surrounding_fields(self):
        try:
            file = "Image/Map/" + self.map_name + "_move.txt"
            #fp = codecs.open(file, "r", encoding="utf-8")
            fp = open(file, "r")
            
        except IOError, (errno, msg):
            pass
        else:
            fp.seek(0)

            for line in fp:
                if (string.find(line, "north_map:") != -1):
                    strip_line = line[len("north_map:"):]
                    self.north_map = (string.rstrip(strip_line, "\n"))
                elif (string.find(line, "south_map:") != -1):
                    strip_line = line[len("south_map:"):]
                    self.south_map = (string.rstrip(strip_line, "\n"))
                elif (string.find(line, "east_map:") != -1):
                    strip_line = line[len("east_map:"):]
                    self.east_map = (string.rstrip(strip_line, "\n"))
                elif (string.find(line, "west_map:") != -1):
                    strip_line = line[len("west_map:"):]
                    self.west_map = (string.rstrip(strip_line, "\n"))

##                #other buildings below
            fp.close()

        #get corner maps also
        self.get_surrounding_fields_corner(self.north_map, self.south_map)

        #store fields in order
        self.other_map.append(field.Field(self.northwest_map,0))
        self.other_map.append(field.Field(self.north_map,1))
        self.other_map.append(field.Field(self.northeast_map,2))
        self.other_map.append(field.Field(self.west_map,3))
        self.other_map.append(field.Field(self.map_name,4))
        self.other_map.append(field.Field(self.east_map,5))
        self.other_map.append(field.Field(self.southwest_map,6))
        self.other_map.append(field.Field(self.south_map,7))
        self.other_map.append(field.Field(self.southeast_map,8))


    def get_surrounding_fields_corner(self, north_map, south_map):


        try:
            file = "Image/Map/" + north_map + "_move.txt"
            fp = open(file, "r")
            
        except IOError, (errno, msg):
            pass
        else:
            fp.seek(0)

            for line in fp:
                if (string.find(line, "east_map:") != -1):
                    strip_line = line[len("east_map:"):]
                    left_top_map = (string.rstrip(strip_line, "\n"))
                elif (string.find(line, "west_map:") != -1):
                    strip_line = line[len("west_map:"):]
                    right_top_map = (string.rstrip(strip_line, "\n"))

            fp.close()
                    

        try:
            file = "Image/Map/" + south_map + "_move.txt"
            fp = open(file, "r")
            
        except IOError, (errno, msg):
            pass
        else:
            fp.seek(0)

            for line in fp:
                if (string.find(line, "east_map:") != -1):
                    strip_line = line[len("east_map:"):]
                    left_below_map = (string.rstrip(strip_line, "\n"))
                elif (string.find(line, "west_map:") != -1):
                    strip_line = line[len("west_map:"):]
                    right_below_map = (string.rstrip(strip_line, "\n"))

            fp.close()

        self.northwest_map = left_top_map
        self.northeast_map = right_top_map
        self.southwest_map = left_below_map
        self.southeast_map = right_below_map

    def change_map(self, direction):
        
        to_del = []
        
        if direction == gv.DIRECTION_LEFT:
            for field_map in self.other_map:
                #remove right map
                if field_map.field_number % 3 == 2:
                    to_del.insert(0,field_map)

            for field_map in to_del:
                self.other_map.remove(field_map)

            for field_map in self.other_map:
                field_map.change_field_number(1)

        elif direction == gv.DIRECTION_RIGHT:
            for field_map in self.other_map:
                #remove left map
                if field_map.field_number % 3 == 0:
                    to_del.insert(0,field_map)

            for field_map in to_del:
                self.other_map.remove(field_map)

            for field_map in self.other_map:
                #adjust the field_number
                field_map.change_field_number(-1)

       

        elif direction == gv.DIRECTION_UP:
            for field_map in self.other_map:
                #remove below 3 map
                if field_map.field_number > 5:
                    to_del.insert(0,field_map)

            for field_map in to_del:
                self.other_map.remove(field_map)

            for field_map in self.other_map:
                #adjust the field_number
                field_map.change_field_number(3)
                    
        elif direction == gv.DIRECTION_DOWN:
            for field_map in self.other_map:
                #remove top 3 maps
                if field_map.field_number < 3:
                    to_del.insert(0,field_map)

            for field_map in to_del:
                self.other_map.remove(field_map)


            for field_map in self.other_map:
                #adjust the field_number
                field_map.change_field_number(-3)
                
        #self.map_load_thread = None
        #self.map_load_thread = map_thread.Map_load_thread()
        #self.map_load_thread.setUp(self, direction)
        #self.map_load_thread.run()

        #self.map_load_process = map_thread.Map_load_process()
        #self.map_load_process.setUp(self,direction)
        #self.map_load_process.run()

        self.map_load_process = multiprocessing.Process(target=add_new_map, args=(self, direction, self.q))
        self.map_load_process.run()
            

    def add_new_map(self, direction):
        print "int"
        start = time.clock()
        if direction == gv.DIRECTION_LEFT:
            self.other_map.append(field.Field(self.northwest_map,0))
            self.other_map.append(field.Field(self.west_map,3))
            self.other_map.append(field.Field(self.southwest_map,6))
        elif direction == gv.DIRECTION_RIGHT:
            self.other_map.append(field.Field(self.northeast_map,2))
            self.other_map.append(field.Field(self.east_map,5))
            self.other_map.append(field.Field(self.southeast_map,8))
        elif direction == gv.DIRECTION_UP:
            self.other_map.append(field.Field(self.northwest_map,0))
            self.other_map.append(field.Field(self.north_map,1))
            self.other_map.append(field.Field(self.northeast_map,2))

        elif direction == gv.DIRECTION_DOWN:
            self.other_map.append(field.Field(self.southwest_map,6))
            self.other_map.append(field.Field(self.south_map,7))
            self.other_map.append(field.Field(self.southeast_map,8))
        end = time.clock()
        print end-start
