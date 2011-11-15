#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sitecustomize

#to read and write binary
import struct

#module that has global variables
import gv
#module that has global functions
import gf

class Field:

    def __init__(self,city_file_name):

        #in the beginning, save file has map name
        #it also has event with map file may be in another file?
        #it also needs what map chip to use in that file
        #script file with events?
        #format: person_num event_num
        #        width height event_num

        self.map_width = 0
        self.map_height = 0

        self.map_chip = "town06_a.bmp"
        

        try:
            file = "Image/Map/" + city_file_name
            fp = open(file, "rb")
        except IOError, (errno, msg):
            pass
        else:
            fp.seek(0)

            #reads fmf header portion
            map_identifier = struct.unpack("i", fp.read(struct.calcsize("i")))[0]
            map_size = struct.unpack("i", fp.read(struct.calcsize("i")))[0]
            map_width = struct.unpack("i", fp.read(struct.calcsize("i")))[0]
            map_height = struct.unpack("i", fp.read(struct.calcsize("i")))[0]
            chip_width = struct.unpack("c", fp.read(struct.calcsize("c")))[0]
            chip_height = struct.unpack("c", fp.read(struct.calcsize("c")))[0]
            layer_count = struct.unpack("c", fp.read(struct.calcsize("c")))[0]
            bit_count = struct.unpack("c", fp.read(struct.calcsize("c")))[0]

##【レイヤーデータ】
##FMFヘッダの直後からマップパーツの値が mapWidth * mapHeight 個、ベタに並んでいます。
##
##bitCountが8の場合、1パーツ8ビット(1byte)
##bitCountが16の場合、1パーツが16ビット(2byte)
##
##１レイヤーのデータサイズは以下のようになる。
##layerSize = mapWidth * mapHeight * (bitCount / 8);
##また、
##fileSize = headerSize(20bytes) + layerSize * layerCount;
##となる。

            fp.close()
      
        pass
    def update(self):
        
        pass
    def render(self, party, screen):

        for chara in party:
            chara.render(screen)
        
        

        try:
            file = "Image/MapChip/" + self.map_chip
            fp = open(file, "r")
        except IOError, (errno, msg):
            pass
        else:


            fp.close()

        
        pass
    def event_handler(self, event, arcanum_saga):
        pass

    #can access each element by image_list[x+y*count_x]
    def load_map_chip(self, map_chip_name, size_x, size_y, count_x, count_y):

        image = pygame.image.load(map_chip_name).convert()

        image_list = []

        for x in count_x:
            for y in count_y:
                surface = pygame.Surface((size_x, size_y))

                surface.blit(image, (0,0), (x*size_x, y*size_y, x*(size_x+1), y*(size_y+1)))

                #needs invisible color in the script file also
                #surface.set_colorkey(surface.get_at((invisible1_x,invisible1_y)), RLEACCEL)

                surface.convert()
    
                image_list.append(surface)

        return image_list
