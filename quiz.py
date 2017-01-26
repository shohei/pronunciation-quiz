import random
import math
import os

confusing = [('cards','cars'),('hard','heard'),('bug','bag'),('fan','fun'),('hat','hut'),('wonder','wander'),('collect','correct'),('flea','free'),('glass','grass'),('river','liver'),('row','low'),('raw','law'),('father','further'),('first','fast'),('year','ear'),('rock','lock')]

length = len(confusing)
csound = "/System/Library/Sounds/Hero.aiff"
wsound = "/System/Library/Sounds/Funk.aiff"

while True:
    number = int(math.floor(random.random()*length))
    pair = confusing[number]
    idx = int(math.floor(random.random()*2))

    cmd = "say " + pair[idx]
    os.system(cmd)

    answer = raw_input("Did you hear "+ pair[0] + " or " + pair[1]+ "? >> ")
    if (answer==pair[idx]):
        print "you are right!"
        cmd = "afplay " + csound
        os.system(cmd)
    else:
        print "you are wrong."
        cmd = "afplay " + wsound
        os.system(cmd)
    
