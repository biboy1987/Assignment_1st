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

actualSate = '0,8,7,6,5,4,3,2,1'

# count the numbers in 2nd arg
numbers = sum(c.isdigit() for c in secondArgument)
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
		# take No to object No
        self.No = Tiles.No
        Tiles.No = Tiles.No + 1
		# get the input from the list
        self.numList = re.findall(r'\d+', previous_state)
        # get amount of numbers
        self.count = len(self.numList)
        # get squere root of amount of numbers
        self.dimension = int(self.count**(.5))
		# get the zero position
        self.zeropos = 0
        while '0' != self.numList[self.zeropos]:
            self.zeropos = self.zeropos + 1
        # get position related value from input
        self.value = int(self.numList[self.No])
        print "Self No: ",self.No
        print "Self Value: ",self.value		
        print "Amount of numbers: ",self.count
		
		# 3. Calculate the attributes of Tile
		# default 0 everything -> 0=not able, 1=able
		# if this tile's value is not 0
        self.Up = 0
        self.Down = 0
        self.Left = 0
        self.Right = 0
		# if this tile's value is 0
        if self.value == 0:		
            self.Up = 1
            self.Down = 1
            self.Left = 1
            self.Right = 1
		    # if on the left side, left shift is not available
            self.x = self.count - self.dimension
            while self.x >= 0:
                print "self.x: ",self.x
                if self.x == self.zeropos:
                    self.Left = 0
                self.x = self.x - self.dimension
            print "Left available: ",self.Left
		    # if on the right side, right shift is not available
            self.x = self.count - 1
            while self.x >= 0:
                print "self.x: ",self.x
                if self.x == self.zeropos:
                    self.Right = 0
                self.x = self.x - self.dimension
            print "Right available: ",self.Right
		    # if on the top side, Up shift is not available
            self.x = self.dimension - 1
            while self.x >= 0:
                print "self.x: ",self.x
                if self.x == self.zeropos:
                    self.Up = 0
                self.x = self.x - 1
            print "Up available: ",self.Up
        
		    # if on the bot side, Down shift is not available
            self.x = self.count - 1
            while self.x >= (self.count - self.dimension):
                print "self.x: ",self.x
                if self.x == self.zeropos:
                    self.Down = 0
                self.x = self.x - 1
            print "Down available: ",self.Down
	
    def __str__(self):
        string = " Position: {:d} \n Value: {:d} \n Up: {:d} \n Down: {:d} \n Left: {:d} \n Right: {:d} \n".format(self.No,int(self.value),self.Up,self.Down,self.Left,self.Right)
        return str(string)		
    
    def getNo(self):
        print self.No
        return self.No
    
    def getValue(self):
        print self.value
        return self.value
		
    def getUp(self):
        print self.Up
        return self.Up
		
    def getDown(self):
        print self.Down
        return self.Down
		
    def getRight(self):
        print self.Right
        return self.Right

    def getLeft(self):
        print self.Left
        return self.Left

#generate table
class Table():
    
    def __init__(self, actualState_s):
		# 0. Initialization of table
        self.dimesion_i = 3										# ToDo: calculate it!!!
        self.tableId_s = actualState_s							# set name to instance
        self.listofTiles_l = []									# declaration object list of tiles
        self.numList_l = re.findall(r'\d+', self.tableId_s)		# get the input from the list
        self.amountOfTiles_i = len(self.numList_l)				# get amount of numbers
        for x in range(0, self.amountOfTiles_i):   				# take Tales into the list
            self.listofTiles_l.append(Tiles(self.tableId_s))		
		# 1. Calculate amount of available steps
		# - get position of zero
        for x in range(0, self.amountOfTiles_i):
            if self.listofTiles_l[x].getValue() == 0:
                self.zeroPosition_i = self.listofTiles_l[x].getNo()	
        # - get zeropostion related available shifts
        self.amountOfavilableshifts_i = 0
        if self.listofTiles_l[self.zeroPosition_i].getDown() == 1:
            self.amountOfavilableshifts_i = self.amountOfavilableshifts_i + 1
        if self.listofTiles_l[self.zeroPosition_i].getUp() == 1:
            self.amountOfavilableshifts_i = self.amountOfavilableshifts_i + 1
        if self.listofTiles_l[self.zeroPosition_i].getLeft() == 1:
            self.amountOfavilableshifts_i = self.amountOfavilableshifts_i + 1
        if self.listofTiles_l[self.zeroPosition_i].getRight() == 1:
            self.amountOfavilableshifts_i = self.amountOfavilableshifts_i + 1
		# 2. Make list from next steps
        self.nextState_l = []
        self.nextStates_l = []														# declare list for available next states
        self.assistantVariable_i = 0												# declare assistant variable to contain the swep position - zero position 	
        if self.listofTiles_l[self.zeroPosition_i].getDown() == 1:
            self.nextState_l = list(self.numList_l)
            print ",".join(self.nextState_l)
            self.nextState_l[self.zeroPosition_i], self.nextState_l[self.zeroPosition_i + self.dimesion_i] = self.nextState_l[self.zeroPosition_i + self.dimesion_i], self.nextState_l[self.zeroPosition_i]
            self.assistantString_s = ",".join(self.nextState_l)
            self.nextStates_l.append(self.assistantString_s)			
        if self.listofTiles_l[self.zeroPosition_i].getUp() == 1:
            self.nextState_l = list(self.numList_l)
            print ",".join(self.nextState_l)
            self.nextState_l[self.zeroPosition_i], self.nextState_l[self.zeroPosition_i - self.dimesion_i] = self.nextState_l[self.zeroPosition_i - self.dimesion_i], self.nextState_l[self.zeroPosition_i]
            self.assistantString_s = ",".join(self.nextState_l)
            self.nextStates_l.append(self.assistantString_s)	
        if self.listofTiles_l[self.zeroPosition_i].getLeft() == 1:
            self.nextState_l = list(self.numList_l)
            print ",".join(self.nextState_l)
            self.nextState_l[self.zeroPosition_i], self.nextState_l[self.zeroPosition_i - 1] = self.nextState_l[self.zeroPosition_i - 1], self.nextState_l[self.zeroPosition_i]
            self.assistantString_s = ",".join(self.nextState_l)
            self.nextStates_l.append(self.assistantString_s)	
        if self.listofTiles_l[self.zeroPosition_i].getRight() == 1:
            self.nextState_l = list(self.numList_l)
            print ",".join(self.nextState_l)
            self.nextState_l[self.zeroPosition_i], self.nextState_l[self.zeroPosition_i + 1] = self.nextState_l[self.zeroPosition_i + 1], self.nextState_l[self.zeroPosition_i]
            self.assistantString_s = ",".join(self.nextState_l)
            self.nextStates_l.append(self.assistantString_s)	
		
            
    def getZeroPosition(self):
        print self.zeroPosition_i
		
    def getAmountOfAvailableShifts(self):
        print self.amountOfavilableshifts_i

    def getFirstAV(self):
        print "Orig :", self.numList_l
        print "Down :",self.nextStates_l[0]
        print "Up   :",self.nextStates_l[1]
        print "Left :",self.nextStates_l[2]
        print "Right:",self.nextStates_l[3]
	
#    for obj in listofTiles:
#        print(obj)
	
#    print listofTiles[1].getValue()

firstTable = Table('4,1,2,3,0,5,6,7,8')
print "Zeroposition",firstTable.getZeroPosition()
print "Available shift amont:",firstTable.getAmountOfAvailableShifts()
print firstTable.getFirstAV()

#stTil = Tiles('0,1,2,3,4,5,6,7,8')
#print(stTil)
#stTil.printNo()
#stTil.printFirst()
		





