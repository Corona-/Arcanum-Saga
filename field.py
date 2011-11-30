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

import math

#module that has global variables
import gv
#module that has global functions
import gf

class MapSpriteLayer1(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self, self.containers)
        #image_path = os.path.join("Image", "MapChip", filename)
        self.image = image #pygame.image.load(image_path).convert_alpha()
        width = self.image.get_width()
        height = self.image.get_height()
        self.rect = Rect(x,y, width, height)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class MapSpriteLayerOther(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self, self.containers)
        #image_path = os.path.join("Image", "MapChip", filename)
        self.image = image #pygame.image.load(image_path).convert_alpha()
        width = self.image.get_width()
        height = self.image.get_height()
        self.rect = Rect(x,y, width, height)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Field:

    def __init__(self, file_name, field_number):

        #in the beginning, save file has map name
        #it also has event with map file may be in another file?
        #it also needs what map chip to use in that file
        #script file with events?
        #format: person_num event_num
        #        width height event_num

        self.map_width = 0
        self.map_height = 0
        self.chip_width = 0
        self.chip_height = 0
        self.layer_count = 0

        self.map_name = file_name

        self.field_number = field_number

        self.map_chip = self.get_mapchip()
        self.map_pass = None
        
        self.image = self.load_mapchip(self.map_chip)

        self.map_info = []


        #self.map_all = pygame.sprite.LayeredUpdates()
        self.map_sprite = pygame.sprite.LayeredUpdates()
        self.map_sprite_other = pygame.sprite.LayeredUpdates()
        MapSpriteLayer1.containers = self.map_sprite
        MapSpriteLayerOther.containers = self.map_sprite_other

        try:
            file = "Image/Map/" + file_name + ".fmf"
            fp = open(file, "rb")
        except IOError, (errno, msg):
            print msg
            pass
        else:
            fp.seek(0)

            #reads fmf header portion
            map_identifier = struct.unpack("i", fp.read(struct.calcsize("i")))[0]
            map_size = struct.unpack("i", fp.read(struct.calcsize("i")))[0]
            map_width = struct.unpack("i", fp.read(struct.calcsize("i")))[0]
            map_height = struct.unpack("i", fp.read(struct.calcsize("i")))[0]
            chip_width = struct.unpack("b", fp.read(struct.calcsize("b")))[0]
            chip_height = struct.unpack("b", fp.read(struct.calcsize("b")))[0]
            layer_count = struct.unpack("b", fp.read(struct.calcsize("b")))[0]
            bit_count = struct.unpack("b", fp.read(struct.calcsize("b")))[0]

            for layer in range(layer_count):
                one_layer = []

                for y in range(map_height):
                    for x in range(map_width):
                        map_data = struct.unpack("h", fp.read(struct.calcsize("h")))[0]

                        #need to change number from platinum to this game
                        if (map_data != 255):
                            #need to change 30 to mapchip's width
                            map_data = map_data%256+map_data/256*30

                            if self.map_pass[map_data] >= 0:
                                MapSpriteLayer1(self.image[map_data], x*chip_width, y*chip_height)
                            else:
                                MapSpriteLayerOther(self.image[map_data], x*chip_width, y*chip_height)

                                
                        
                        one_layer.append(map_data)
                                            
                self.map_info.append(one_layer)


            self.map_width = map_width
            self.map_height = map_height
            self.chip_width = chip_width
            self.chip_height = chip_height
            self.layer_count = layer_count

      
            fp.close()


        self.map_surface1 = pygame.Surface((self.map_width*self.chip_width, self.map_height*self.chip_height)).convert()
        self.map_sprite.draw(self.map_surface1)
        self.map_surface_other = pygame.Surface((self.map_width*self.chip_width, self.map_height*self.chip_height)).convert()
        self.map_sprite_other.draw(self.map_surface_other)
        transparent_color = self.map_surface_other.get_at((0,0))
        self.map_surface_other.set_colorkey(transparent_color)
        
        

    def update(self, party):
        #since map doesn't change, no need for update 
        #self.map_all.update()
        
        pass
    def render(self, party, screen):

        #self.map_all.draw(self.map_surface)

        if self.field_number == gv.TOPLEFT:
            x = party[0].x-gv.SCREEN_WIDTH/2+self.map_width*self.chip_width
            y = party[0].y-gv.SCREEN_HEIGHT/2+self.map_height*self.chip_height
        elif self.field_number == gv.TOPCENTER:
            x = party[0].x-gv.SCREEN_WIDTH/2
            y = party[0].y-gv.SCREEN_HEIGHT/2+self.map_height*self.chip_height
        elif self.field_number == gv.TOPRIGHT:
            x = party[0].x-gv.SCREEN_WIDTH/2-self.map_width*self.chip_width
            y = party[0].y-gv.SCREEN_HEIGHT/2+self.map_height*self.chip_height
        elif self.field_number == gv.MIDDLELEFT:
            x = party[0].x-gv.SCREEN_WIDTH/2+self.map_width*self.chip_width
            y = party[0].y-gv.SCREEN_HEIGHT/2
        elif self.field_number == gv.MIDDLECENTER:
            x = party[0].x-gv.SCREEN_WIDTH/2
            y = party[0].y-gv.SCREEN_HEIGHT/2
        elif self.field_number == gv.MIDDLERIGHT:
            x = party[0].x-gv.SCREEN_WIDTH/2-self.map_width*self.chip_width
            y = party[0].y-gv.SCREEN_HEIGHT/2
        elif self.field_number == gv.BELOWLEFT:
            x = party[0].x-gv.SCREEN_WIDTH/2+self.map_width*self.chip_width
            y = party[0].y-gv.SCREEN_HEIGHT/2-self.map_height*self.chip_height
        elif self.field_number == gv.BELOWCENTER:
            x = party[0].x-gv.SCREEN_WIDTH/2
            y = party[0].y-gv.SCREEN_HEIGHT/2-self.map_height*self.chip_height
        elif self.field_number == gv.BELOWRIGHT:
            x = party[0].x-gv.SCREEN_WIDTH/2-self.map_width*self.chip_width
            y = party[0].y-gv.SCREEN_HEIGHT/2-self.map_height*self.chip_height

        screen.blit(self.map_surface1, (0,0), ( x, y, gv.SCREEN_WIDTH, gv.SCREEN_HEIGHT))

        party[0].render(screen)

        screen.blit(self.map_surface_other, (0,0), ( x, y, gv.SCREEN_WIDTH, gv.SCREEN_HEIGHT))
        

        #draw character between layer
        #and if character is in front, display in front

        #need to make character as sprite too?

        #for main character use character but for other use party.render


    def event_handler(self, event, arcanum_saga):
        pass

    def load_image(self,image_name, color_key = None):
        image_path = os.path.join("Image", "MapChip", image_name)

        try:
            image = pygame.image.load(image_path)
        except pygame.error, message:
            print "failed to load the image:", image_path
            raise SystemExit, message
        image = image.convert()            

        if color_key is not None:
            if color_key == -1:
                color_key = image.get_at((0,0))
            image.set_colorkey(color_key, RLEACCEL)

        return image

    #can access each element by image_list[x+y*count_x]
    def load_mapchip(self, mapchip_name):

        image = self.load_image(mapchip_name + ".bmp")

        try:
            file = "Image/MapChip/" + mapchip_name + ".txt"
            fp = open(file, "r")
        except IOError, (errno, msg):
            print "failed to load the file:", mapchip_name
            raise SystemExit, message
        else:
            fp.seek(0)

            for line in fp:
                if (string.find(line, "size_x") != -1):
                    size_x = (int)(string.lstrip(line, "size_x:"))
                elif (string.find(line, "size_y") != -1):
                    size_y = (int)(string.lstrip(line, "size_y:"))
                elif (string.find(line, "count_x") != -1):
                    count_x = (int)(string.lstrip(line, "count_x:"))
                elif (string.find(line, "count_y") != -1):
                    count_y = (int)(string.lstrip(line, "count_y:"))
                elif (string.find(line, "color_key") != -1):
                    int_string_list = string.split(string.lstrip(line, "color_key:"))
                    color_key = []
                    for int_string in int_string_list:
                        color_key.append((int)(int_string))

                elif (string.find(line, "pass") != -1):
                    string_pass = string.split(string.lstrip(line, "pass:"), ",")
                    self.map_pass = []
                    for int_string in string_pass:
                        self.map_pass.append((int)(int_string))

            fp.close()

                                                    

        image_list = []

        color = Color("white")
        color.r = color_key[0]
        color.g = color_key[1]
        color.b = color_key[2]
        
        for y in range(count_y):
            for x in range(count_x):
                surface = pygame.Surface((size_x, size_y))

                surface.blit(image, (0,0), (x*size_x, y*size_y, size_x, size_y))

                #needs invisible color in the script file also
                surface.set_colorkey(color, RLEACCEL)

                surface.convert()
    
                image_list.append(surface)

        return image_list

    def get_mapchip(self):
        map_chip = ""
        try:
            file = "Image/Map/" + self.map_name + "_move.txt"
            fp = open(file, "r")
            
        except IOError, (errno, msg):
            pass
        else:
            fp.seek(0)

            for line in fp:
                if (string.find(line, "map_chip:") != -1):
                    strip_line = line[len("map_chip:"):]
                    map_chip = (string.rstrip(strip_line, "\n"))

            fp.close()

        return map_chip



    def change_field_number(self, offset):
        self.field_number += offset


    def is_movable(self, x, y, direction):


        movable = False

        if x < 0:
            x = 0
        elif x >= gv.MAPSIZE:
            x = gv.MAPSIZE-1
        if y < 0:
            y = 0
        elif y >= gv.MAPSIZE:
            y = gv.MAPSIZE-1

        i = 0
        for layer in self.map_info:
            mapchip_number = layer[(int)(x/self.chip_width)+self.map_width*(int)(y/self.chip_height)]
            movable_number = self.map_pass[mapchip_number]


            if movable_number == 0 or movable_number == -16:
                movable =  True
                                        #no chip is 255
            elif movable_number == 15 and mapchip_number != 255:
                movable = False
                
            elif bin((int)(math.fabs(movable_number)))[3] == "1" and direction == gv.DIRECTION_DOWN and mapchip_number != 255:
                movable = False
            elif (bin((int)(math.fabs(movable_number)))[2] == "1") and direction == gv.DIRECTION_LEFT and mapchip_number != 255:
                movable = False
            elif (bin((int)(math.fabs(movable_number)))[1] == "1") and direction == gv.DIRECTION_UP and mapchip_number != 255:
                movable = False
            elif (bin((int)(math.fabs(movable_number)))[0] == "1") and direction == gv.DIRECTION_RIGHT and mapchip_number != 255:
                movable = False
              
            i+=1

        return movable

      
