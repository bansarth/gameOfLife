import random
import time

wState = 0
hState = 0
DEAD = 0
ALIVE = 1

state = []
nextState = []

def createState(width, height, type):
    wState = width
    hState = height
    if(type == "DEAD"):
        for i in range(height):
            line = []
            for j in range(width):
                line.append(DEAD);
            state.append(line);
    elif(type == "50/50"):
        for i in range(height):
            line = []
            for j in range(width):
                randomNum = random.random()
                if(randomNum >= .5):
                    line.append(ALIVE);
                else:
                    line.append(DEAD);
            state.append(line);
    else:
        for i in range(height):
            line = []
            for j in range(width):
                randomNum = random.random()
                if(randomNum >= .9):
                    line.append(ALIVE);
                else:
                    line.append(DEAD);
            state.append(line);

def printState():
    for i in range(len(state)):
        for j in range(len(state[i])):
            print(state[i][j], " ", end="")
        print("\n")

def pprintState():
    for i in range(len(state)):
        for j in range(len(state[i])):
            if(state[i][j] == DEAD):
                print(" ", end="")
            else:
                print(u"\u2588", end="");
        print("\n")

def nextCellState(x, y):
    alive = 0
    for i in range((x-1), (x+1)):
        if(i < 0 or i >= hState): continue
        for j in range((y-1), (y+1)):
            if(j < 0 or j >= wState): continue
            elif(x == i and y == j): continue
            if(state[i][j] == ALIVE): alive += 1

    if(state[x][y] == ALIVE):
        if(alive < 2): nextState[x][y] = DEAD
        elif(alive > 3): nextState[x][y] = DEAD
    elif(state[x][y] == DEAD):
        if(alive == 3): nextState[x][y] = ALIVE

def nextBoardState():
    for i in range(0, wState):
        for j in range(0, hState):
            nextCellState(i, j)

createState(150, 20, "RANDOM")
nextState = state
pprintState()

while True:
    nextBoardState()
    state = nextState
    pprintState()
    time.sleep(1)