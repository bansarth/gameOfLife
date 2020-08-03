import random

DEAD = 0;
ALIVE = 1;

state = [];

def createState(width, height, type):
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
                randomNum = random.random
                if(randomNum > .5):
                    line.append(ALIVE);
                else:
                    line.append(DEAD);
            state.append(line);
    else:
        for i in range(height):
            line = []
            for j in range(width):
                randomNum = random.random
                if(randomNum > .9):
                    line.append(ALIVE);
                else:
                    line.append(DEAD);
            state.append(line);

def printState():
    for i in range(len(state)):
        for j in range(len(state[i])):
            print(state[i][j] + " ")
        print("\n")

createState(10, 10, "DEAD")
printState()
