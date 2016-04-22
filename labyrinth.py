# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 15:30:20 2016

@author: galen
@email: gjwilkerson@gmail.com

Represent a ball-maze / labyrinth in very simple format.

Useful for various kinds of testing.
"""

import math
import matplotlib.pyplot as plt
import numpy as np

class Labyrinth:

    '''
    Data members:
    
    The maze:
    0's for open space.
    1's for walls,
    
    Instruction alphabet:
    L = Left
    R = Right
    U = Up
    D = Down
    '''

    def __init__(self):
    
        # the default ball maze
        self.ballMaze = [[0, 0, 0, 1, 0],
                         [1, 1, 0, 1, 0],
                         [0, 0, 0, 1, 0],
                         [0, 1, 1, 0, 0],
                         [0, 0, 0, 0, 1]]            
    
        # goal location
        self.goalLocation = (0, 4)
    
        # the current ball location
        self.ballLocation = (0, 0)
    
        # the alphabet of instructions
        self.moveAlphabet = set(["L", "R", "U", "D"])

        # count total number of moves and move attempts (into walls etc)
        self.totalNumberOfMoves = 0
    
    # create a maze from an input list of 0's 1's and 2's
    def createMaze(self,inputMaze):
        self.ballMaze = inputMaze    
    
    # reset ball to (0,0) and total move count to 0
    def resetBall(self):
        self.ballLocation = (0, 0)
        self.totalNumberOfMoves = 0
    
    # place the ball in the maze
    def setBallLocation(self, row, col):
        
        if(self.ballMaze[row][col] == 1):               
            return
            #throw("Invalid ball location")
        else:
            self.ballLocation = (row, col)

    def getMoveAlphabet(self):
        return self.moveAlphabet

    # return the dimensions of the entire maze
    def getDimensions(self):
        return (len(self.ballMaze), len(self.ballMaze[0]))

    # return the number of 0's, plus 1 for the goal        
    def getMaxNumberOfMoves(self):
        (M, N) = self.getDimensions()
        
        totalCount = 0
        for i in range(M):
           totalCount += (self.ballMaze[i]).count(0)
           
        return(totalCount + 1)

        
    # print the state of the maze, B for ball and G for goal
    def printState(self):
        
        for i in range(len(self.ballMaze)):
            for j in range(len(self.ballMaze[0])):
                if ((i,j) == self.ballLocation):
                    print("B", end = ' ')
                    continue
                elif ((i,j) == self.goalLocation):
                    print("G", end = ' ')
                    continue
                else:
                    print(self.ballMaze[i][j], end = ' ')
            print(end = '\n')
        print(end = '\n')


    def drawState(self):
        '''
        Draw the state of the maze!        
        
        walls as black squares
        ball as a black circle
        goal as a red circle
        '''
        
        mazeImage = np.array(self.ballMaze)
        mazeImage[self.ballLocation] = 2        
        mazeImage[self.goalLocation] = 3
        plt.imshow(mazeImage, interpolation = 'none')
        plt.show()
#        fig = plt.Figure()
#        for i in range(len(self.ballMaze)):
#            for j in range(len(self.ballMaze[0])):
#                plt.plot()
                
        
        
        
                    
    # move the ball one step in the direction of motion from the alphabet
    # return the new location
    def runMove(self, moveDirection):
    
        # get the ball location row and column
        (row, col) = self.ballLocation
        newRow = row
        newCol = col
    
        # check for edge of maze and walls in the move direction        
        if(moveDirection == "L"):
            if(col > 0 and self.ballMaze[row][col - 1] != 1):
                newCol -= 1                
                
        elif(moveDirection == "R"):
            if(col < len(self.ballMaze[:][0]) and self.ballMaze[row][col + 1] != 1):
                newCol += 1
                
        elif(moveDirection == "U"):
            if(row != 0 and self.ballMaze[row - 1][col] != 1):
                newRow -= 1
                
        elif(moveDirection == "D"):
            if(col < len(self.ballMaze[0][:]) and self.ballMaze[row + 1][col] != 1):
                newRow += 1                
    
        # make sure the old location is still zero
        self.ballMaze[row][col] = 0
        
        # set the new ball location
        self.ballLocation = (newRow, newCol)

        # count all moves and attempted moves
        self.totalNumberOfMoves += 1

    
    # move the ball according to the move instructions
    # input:  a list of moves from the move alphabet
    def runMoveSequence(self, movesList):
        
        for move in movesList:
            self.runMove(move)        
    
    # check if we've reached the goal
    def reachedGoal(self):
        if (self.ballLocation == self.goalLocation):
            return True
        else:
            return False

    # return the Euclidean distance between the ball and goal
    def euclideanDistance(self):
        (ballRow, ballCol) = self.ballLocation
        (goalRow, goalCol) = self.goalLocation

        distance = float(math.sqrt((goalRow - ballRow)**2 + (goalCol - ballCol)**2))
        return distance
    
    
def main():

    maze = Labyrinth()

    # print the state, including ball (3) and goal (2) locations
    print("Maze State: ")
    maze.printState()
    print("Distance: " + str(maze.euclideanDistance()), end = '\n\n')
    
    maze.drawState()    
    
    # try a move that hits a wall
    move = "D"
    print("Move: " + move)
    maze.runMove(move)
    print("State: ")
    maze.printState()

    # try a move that goes off the edge
    move = "U"
    print("Move: " + move)
    maze.runMove(move)
    print("State: ")
    maze.printState()
    
    # try a move that moves one right
    move = "R"
    print("Move: " + move)
    maze.runMove(move)
    print("State: ")
    maze.printState()
    
    print("Distance: " + str(maze.euclideanDistance()), end = '\n\n')

    print(maze.getDimensions())
    print(maze.getMaxNumberOfMoves())
    
     # try a move that moves one right again
    move = "R"
    print("Move: " + move)
    maze.runMove(move)
    print("State: ")
    maze.printState()
    
     # try a move that moves one right
    move = "R"
    print("Move: " + move)
    maze.runMove(move)
    print("State: ")
    maze.printState()

    # try a move sequence
    moveSequence = ["D","D","L"]
    print("Sequence: ", "".join(moveSequence))
    maze.runMoveSequence(moveSequence)
    print("State: ")
    maze.printState()
    print("Distance: " + str(maze.euclideanDistance()), end = '\n')
    print("Reached goal? " + str(maze.reachedGoal()), end = '\n')
    print
    
    # reset the maze (we'll need this later)
    print("Resetting maze")
    maze.resetBall()
    print("State: ")
    maze.printState()
    
    # try the winning sequence
    moveString = "RRDDLLDDRRRURUUU"
    print("one last try: ", moveString)
    moveSequence = list(moveString)
    maze.runMoveSequence(moveSequence)
    print("State: ")
    maze.printState()
    print("Distance: " + str(maze.euclideanDistance()), end = '\n')
    print("Reached goal? " + str(maze.reachedGoal()))
    print("Ball location: ", maze.ballLocation)
    print("Goal location: ", maze.goalLocation)

    maze.drawState()

if __name__ == '__main__':
    main()

