#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from player import Block

blocks = ("block-1.png","block-2.png","block-3.png","block-4.png","block-5.png",
              "block-6.png","block-7.png","block-8.png")

def level_1():
    group = pygame.sprite.Group()

    array = ((0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
             (2, 2, 2, 2, 2, 2, 2, 2, 2, 2),
             (3, 3, 3, 3, 3, 3, 3, 3, 3, 3),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0))

    for y,row in enumerate(array):
        for x,item in enumerate(row):
            if item > 0:
                group.add(Block(x *64,y *32,blocks[item -1]))
                
    return group

def level_2():
    group = pygame.sprite.Group()

    array = ((0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (1, 1, 0, 0, 0, 0, 0, 0, 0, 0),
             (2, 2, 2, 2, 0, 0, 0, 0, 0, 0),
             (3, 3, 3, 3, 3, 3, 0, 0, 0, 0),
             (4, 4, 4, 4, 4, 4, 4, 4, 0, 0),
             (5, 5, 5, 5, 5, 5, 5, 5, 5, 5),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0))

    for y,row in enumerate(array):
        for x,item in enumerate(row):
            if item > 0:
                group.add(Block(x *64,y *32,blocks[item -1]))

    return group

def level_3():
    group = pygame.sprite.Group()

    array = ((0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (2, 2, 2, 2, 2, 2, 2, 2, 2, 2),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (4, 4, 4, 4, 4, 4, 4, 4, 4, 4),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (6, 6, 6, 6, 6, 6, 6, 6, 6, 6),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (8, 8, 8, 8, 8, 8, 8, 8, 8, 8),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0))

    for y,row in enumerate(array):
        for x,item in enumerate(row):
            if item > 0:
                group.add(Block(x *64,y *32,blocks[item -1]))

    return group

def level_4():
    group = pygame.sprite.Group()

    array = ((0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 1, 1, 1, 0, 0, 1, 1, 1, 0),
             (0, 2, 2, 2, 0, 0, 2, 2, 2, 0),
             (0, 3, 3, 3, 0, 0, 3, 3, 3, 0),
             (0, 4, 4, 4, 0, 0, 4, 4, 4, 0),
             (0, 5, 5, 5, 0, 0, 5, 5, 5, 0),
             (0, 6, 6, 6, 0, 0, 6, 6, 6, 0),
             (0, 7, 7, 7, 0, 0, 7, 7, 7, 0),
             (0, 8, 8, 8, 0, 0, 8, 8, 8, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0))

    for y,row in enumerate(array):
        for x,item in enumerate(row):
            if item > 0:
                group.add(Block(x *64,y *32,blocks[item -1]))

    return group

def level_5():
    group = pygame.sprite.Group()

    array = ((0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 1, 0, 1, 0, 0, 1, 0, 1, 0),
             (0, 2, 2, 2, 2, 2, 2, 2, 2, 0),
             (0, 3, 0, 3, 0, 0, 3, 0, 3, 0),
             (0, 4, 0, 4, 0, 0, 4, 0, 4, 0),
             (0, 5, 0, 5, 0, 0, 5, 0, 5, 0),
             (0, 6, 6, 6, 6, 6, 6, 6, 6, 0),
             (0, 7, 0, 7, 0, 0, 7, 0, 7, 0),
             (0, 8, 0, 8, 0, 0, 8, 0, 8, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0))

    for y,row in enumerate(array):
        for x,item in enumerate(row):
            if item > 0:
                group.add(Block(x *64,y *32,blocks[item -1]))

    return group


def level_6():
    group = pygame.sprite.Group()

    array = ((0, 0, 0, 0, 8, 8, 0, 0, 0, 0),
             (0, 0, 0, 1, 1, 1, 1, 0, 0, 0),
             (0, 0, 2, 2, 2, 2, 2, 2, 0, 0),
             (0, 3, 3, 3, 3, 3, 3, 3, 3, 0),
             (0, 4, 4, 4, 4, 4, 4, 4, 4, 0),
             (0, 5, 5, 5, 5, 5, 5, 5, 5, 0),
             (0, 0, 6, 6, 6, 6, 6, 6, 0, 0),
             (0, 0, 0, 7, 7, 7, 7, 0, 0, 0),
             (0, 0, 0, 0, 8, 8, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0))

    for y,row in enumerate(array):
        for x,item in enumerate(row):
            if item > 0:
                group.add(Block(x *64,y *32,blocks[item -1]))

    return group


def level_7():
    group = pygame.sprite.Group()

    array = ((0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 1, 0, 0, 0, 0, 0, 0, 2, 0),
             (0, 1, 1, 0, 0, 0, 0, 2, 2, 0),
             (0, 0, 0, 0, 3, 3, 0, 0, 0, 0),
             (0, 0, 0, 4, 4, 4, 4, 0, 0, 0),
             (0, 0, 0, 0, 5, 5, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 6, 0, 0, 0, 0, 0, 0, 7, 0),
             (0, 6, 6, 0, 0, 0, 0, 7, 7, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0))

    for y,row in enumerate(array):
        for x,item in enumerate(row):
            if item > 0:
                group.add(Block(x *64,y *32,blocks[item -1]))

    return group

def level_8():
    group = pygame.sprite.Group()

    array = ((0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 1, 1, 1, 0, 0, 2, 2, 2, 0),
             (0, 1, 1, 1, 0, 0, 2, 2, 2, 0),
             (0, 1, 1, 1, 0, 0, 2, 2, 2, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 0, 5, 5, 5, 5, 5, 5, 0, 0),
             (0, 0, 6, 6, 6, 6, 6, 6, 0, 0),
             (0, 0, 7, 7, 7, 7, 7, 7, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 0, 8, 8, 8, 8, 8, 8, 0, 0))

    for y,row in enumerate(array):
        for x,item in enumerate(row):
            if item > 0:
                group.add(Block(x *64,y *32,blocks[item -1]))

    return group

def level_9():
    group = pygame.sprite.Group()

    array = ((0, 2, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 2, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 2, 0, 0, 0, 1, 0, 0, 0, 0),
             (0, 2, 0, 0, 4, 4, 4, 0, 0, 0),
             (0, 2, 0, 5, 5, 5, 5, 5, 0, 0),
             (0, 2, 0, 0, 6, 6, 6, 0, 0, 0),
             (0, 2, 0, 0, 0, 7, 0, 0, 0, 0),
             (0, 2, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 2, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 3, 3, 3, 3, 3, 3, 3, 3, 3))

    for y,row in enumerate(array):
        for x,item in enumerate(row):
            if item > 0:
                group.add(Block(x *64,y *32,blocks[item -1]))

    return group
