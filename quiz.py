#!/usr/bin/env python
#-*- coding:utf-8 -*_
import random
import math
import os

confusing = [('cards','cars'),('hard','heard'),('bug','bag'),('fan','fun'),('hat','hut'),('hot','hat'),('hot','hut'),('wonder','wander'),('collect','correct'),('flea','free'),('glass','grass'),('river','liver'),('row','low'),('raw','law'),('father','further'),('first','fast'),('year','ear'),('rock','lock')]

length = len(confusing)
csound = "/System/Library/Sounds/Hero.aiff"
wsound = "/System/Library/Sounds/Funk.aiff"

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

while True:
    number = int(math.floor(random.random()*length))
    pair = confusing[number]
    idx = int(math.floor(random.random()*2))

    cmd = "say " + pair[idx]
    os.system(cmd)

    answer = raw_input("Did you hear "+ pair[0] + " or " + pair[1]+ "? >> ")
    if (answer==pair[idx]):
        print bcolors.OKGREEN + bcolors.BOLD + "you are right!" + bcolors.ENDC
        cmd = "afplay " + csound
        os.system(cmd)
    else:
        print bcolors.FAIL + bcolors.BOLD + "you are wrong." + bcolors.ENDC
        cmd = "afplay " + wsound
        os.system(cmd)
    
