#!/usr/bin/python
import sys
import re

# eg:
# $ python driver.py bfs 0,8,7,6,5,4,3,2,1

# get arguments from command line
firstArgument = sys.argv[1]
secondArgument = sys.argv[2]
#print firstArgument
#print secondArgument

# count the numbers in 2nd arg
#numbers = sum(c.isdigit() for c in secondArgument)
#print numbers

# get square root of numbers
#dimension = int(numbers**(.5))
#print dimension


# Tiles Class 
# Description:
# - One tile of the board
# Attribute: 
# - available moving space
#   up, dow, left, right
class Tiles:

	# No = position in the table
    No = 0

    def __init__(self, previous_state):

        # 1. Get details to math	
        # take the input to the list
        self.numList = re.findall(r'\d+', previous_state)
        # get amount of numbers
        self.count = len(self.numList)
        # get squere root of amount of numbers
        self.dimension = int(self.count**(.5))
		# get the zero position
        self.zeropos = 0
        while '0' != self.numList[self.zeropos]:
            self.zeropos = self.zeropos + 1
        print "Zero position: ",self.zeropos
        print "Dimension: ",self.dimension		
        print "Amount of numbers: ",self.count
		
		# 2. Calculate the attributes of Tile
		# default 0 everything -> 0=not able, 1=able 
        self.Up = 1
        self.Down = 1
        self.Left = 1
        self.Right = 1
		# if on the left side, left shift is not available
        self.x = self.count - self.dimension
        while self.x >= 0:
            print "self.x: ",self.x
            if self.x == self.zeropos:
                self.Right = 0
            self.x = self.x - self.dimension
        print "Left available: ",self.Right
		# if on the right side, right shift is not available
        self.x = self.count - 1
        while self.x >= 0:
            print "self.x: ",self.x
            if self.x == self.zeropos:
                self.Left = 0
            self.x = self.x - self.dimension
        print "Right available: ",self.Left
		# if on the top side, Up shift is not available
        self.x = self.dimension - 1
        while self.x >= 0:
            print "self.x: ",self.x
            if self.x == self.zeropos:
                self.Down = 0
            self.x = self.x - 1
        print "Up available: ",self.Down
        
		# if on the bot side, Down shift is not available
        self.x = self.count - 1
        while self.x >= (self.count - self.dimension):
            print "self.x: ",self.x
            if self.x == self.zeropos:
                self.Up = 0
            self.x = self.x - 1
        print "Down available: ",self.Up
		
        Tiles.No = Tiles.No + 1

    def printNo(self):
        print Tiles.No
    
    def printFirst(self):
        print self.numList[0]

stTil = Tiles('0,1,2,3,4,5,6,7,8')
#stTil.printNo()
#stTil.printFirst()
		
 




