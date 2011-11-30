#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sitecustomize

import os
import math
import field

#module that has global variables
import gv
#module that has global functions
import gf

class Character:

    def __init__(self, image_name):

        self.field_image = self.split_field_image(self.load_image(image_name))#, -1))

        self.x = 0
        self.y = 0

        self.direction = gv.DIRECTION_DOWN
        self.moving = False

        self.image_frame = 0

        #############################################
        # 基礎能力
        #############################################

        #HP,MP,Stamina
        self.max_hp = 0
        self.max_mp = 0
        self.max_st = 0

        self.hp = 0
        self.mp = 0
        self.st = 0

        #Gauge

        #力
        self.power = 0
        #素早さ
        self.agility = 0
        #運
        self.luck = 0
        #魔力
        self.magic = 0
        #回避
        self.avoid = 0
        #体力
        self.strength = 0
        #知力
        self.intelligence = 0

        #動く早さ
        self.walk_speed = 6
        #the speed that map loads without showing black = 12?

        self.run_speed = 4

        #############################################
        # 武器
        #############################################


        #剣
        self.sword = 0
        #盾
        self.shield = 0
        #大剣
        self.large_sword = 0
        #短剣
        self.dagger = 0
        #槍
        self.spear = 0
        #鈍器
        self.blunt = 0
        #斧
        self.ax = 0
        #弓
        self.bow = 0
        #素手
        self.bare_hand = 0
        #杖
        self.wand = 0
        #銃
        self.gun = 0

        
        #############################################
        # 職業
        #############################################

        #冒険者
        self.adventurer = 0
        #戦士
        self.fighter = 0
        #魔術師
        self.maigcian = 0
        #盗賊
        self.thief = 0
        #弓術家
        self.archer = 0
        #商人
        self.merchant = 0
        #農人
        self.farmer = 0

    def update(self, map_object):

        #need function to move other party member?

        if map_object != None:

            pressed_keys = pygame.key.get_pressed()
            self.moving = True

            if pressed_keys[K_RIGHT] and pressed_keys[K_DOWN]:
                self.direction = gv.DIRECTION_DOWN
                next_x = self.x+(self.walk_speed / math.sqrt(2))
                next_y = self.y+(self.walk_speed / math.sqrt(2))            
            elif pressed_keys[K_RIGHT] and pressed_keys[K_UP]:
                self.direction = gv.DIRECTION_UP
                next_x = self.x+(self.walk_speed / math.sqrt(2))
                next_y = self.y-(self.walk_speed / math.sqrt(2))
            elif pressed_keys[K_LEFT] and pressed_keys[K_DOWN]:
                self.direction = gv.DIRECTION_DOWN
                next_x = self.x-(self.walk_speed / math.sqrt(2))
                next_y = self.y+(self.walk_speed / math.sqrt(2))
            elif pressed_keys[K_LEFT] and pressed_keys[K_UP]:
                self.direction = gv.DIRECTION_UP
                next_x = self.x-(self.walk_speed / math.sqrt(2))
                next_y = self.y-(self.walk_speed / math.sqrt(2))

                
            elif pressed_keys[K_DOWN]:
                self.direction = gv.DIRECTION_DOWN
                next_x = self.x
                next_y = self.y+self.walk_speed             
            elif pressed_keys[K_RIGHT]:
                self.direction = gv.DIRECTION_RIGHT
                next_x = self.x+self.walk_speed
                next_y = self.y
            elif pressed_keys[K_UP]:
                self.direction = gv.DIRECTION_UP
                next_x = self.x
                next_y = self.y-self.walk_speed
            elif pressed_keys[K_LEFT]:
                self.direction = gv.DIRECTION_LEFT
                next_x = self.x-self.walk_speed
                next_y = self.y
            else:
                self.moving = False

            if self.moving:
                #find the field the character is going to be in.
                field_num = None

                #also adjust the x,y to the field
                if next_x < 0 and next_y < 0:
                    next_x += gv.MAPSIZE
                    next_y += gv.MAPSIZE
                    field_num  = 0
                elif next_x < 0 and next_y >= gv.MAPSIZE:
                    next_x += gv.MAPSIZE
                    next_y -= gv.MAPSIZE                    
                    field_num  = 6
                elif next_x >= gv.MAPSIZE and next_y < 0:
                    next_x -= gv.MAPSIZE
                    next_y += gv.MAPSIZE
                    field_num  = 2
                elif next_x >= gv.MAPSIZE and next_y >= gv.MAPSIZE:
                    next_x -= gv.MAPSIZE
                    next_y -= gv.MAPSIZE
                    field_num  = 8
                elif next_x < 0:
                    next_x += gv.MAPSIZE
                    field_num  = 3
                elif next_x >= gv.MAPSIZE:
                    next_x -= gv.MAPSIZE
                    field_num  = 5
                elif next_y < 0:
                    next_y += gv.MAPSIZE
                    field_num  = 1
                elif next_y >= gv.MAPSIZE:
                    next_y -= gv.MAPSIZE
                    field_num  = 7
                else:
                    field_num  = 4

                current_field = None
                
                for field_map in map_object.other_map:
                    if field_num  == field_map.field_number:
                        current_field  = field_map

                if not isinstance(current_field, field.Field):
                    return

                #check if the field is movable
                if current_field.is_movable(next_x, next_y, self.direction):
                    #self.x = next_x
                    #self.y = next_y

                    if pressed_keys[K_RIGHT] and pressed_keys[K_DOWN]:
                        self.x = self.x+(self.walk_speed / math.sqrt(2))
                        self.y = self.y+(self.walk_speed / math.sqrt(2))            
                    elif pressed_keys[K_RIGHT] and pressed_keys[K_UP]:
                        self.x = self.x+(self.walk_speed / math.sqrt(2))
                        self.y = self.y-(self.walk_speed / math.sqrt(2))
                    elif pressed_keys[K_LEFT] and pressed_keys[K_DOWN]:
                        self.x = self.x-(self.walk_speed / math.sqrt(2))
                        self.y = self.y+(self.walk_speed / math.sqrt(2))
                    elif pressed_keys[K_LEFT] and pressed_keys[K_UP]:
                        self.x = self.x-(self.walk_speed / math.sqrt(2))
                        self.y = self.y-(self.walk_speed / math.sqrt(2))  
                    elif pressed_keys[K_DOWN]:
                        self.x = self.x
                        self.y = self.y+self.walk_speed             
                    elif pressed_keys[K_RIGHT]:
                        self.x = self.x+self.walk_speed
                        self.y = self.y
                    elif pressed_keys[K_UP]:
                        self.x = self.x
                        self.y = self.y-self.walk_speed
                    elif pressed_keys[K_LEFT]:
                        self.x = self.x-self.walk_speed
                        self.y = self.y
                else:
                    pass
                    #self.x = (int)(next_x/current_field.chip_width)*current_field.chip_width
                    #self.y = (int)(next_y/current_field.chip_height)*current_field.chip_height
                


                

            self.image_frame = self.image_frame + 1

            
    def render(self, screen):
        if (self.moving == False):
            screen.blit(self.field_image[self.direction*3], (gv.SCREEN_WIDTH/2-gv.IMAGE_SIZE/2,gv.SCREEN_HEIGHT/2-gv.IMAGE_SIZE))
        else:
            screen.blit(self.field_image[self.image_frame/(20-self.walk_speed)%3+self.direction*3], (gv.SCREEN_WIDTH/2-gv.IMAGE_SIZE/2,gv.SCREEN_HEIGHT/2-gv.IMAGE_SIZE))
        

    def load_image(self,image_name, color_key = None):
        image_path = os.path.join("Image", "Character", image_name)

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

    def split_field_image(self, image):
        
        image_list = []

        for j in range(0,4):
            for i in  range(0,3):
                surface = pygame.Surface((gv.IMAGE_SIZE, gv.IMAGE_SIZE))
                surface.blit(image, (0,0), (i*gv.IMAGE_SIZE,j*gv.IMAGE_SIZE,gv.IMAGE_SIZE, gv.IMAGE_SIZE))

                surface.set_colorkey(surface.get_at((0,0)), RLEACCEL)

                surface.convert()
                image_list.append(surface)
        return image_list


