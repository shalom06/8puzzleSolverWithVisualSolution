# Created By Shalom Mathews --Shal--
# This file contains Functions that required to maniplate input and execcute the program

import random
from collections import defaultdict
from eightPuzzle import EightPuzzleState
import copy


# Function takes input from User as string x represnt's space
def getInputfromUser():

    print("Please enter Start State as a Integer For Example : '1234567x'    ")
    print("Represention = ")
    print("---------------")
    print("| " + str(1) + " |" + "| " + str(2) + " |" + "| " + str(3) + " |")
    print("| " + str(4) + " |" + "| " + str(5) + " |" + "| " + str(6) + " |")
    print("| " + str(7) + " |" + "| " + str(8) + " |" + "| " + str("x") + " |")
    print("---------------")
    stateStr = raw_input("->")
    type(stateStr)

    return convertInputToSet(convertStateToList(stateStr))


# Function converts state  string to list
def convertStateToList(startState):
    startStateList = [str(ind) for ind in str(startState)]
    return startStateList


# Function convert list to set
# the reason for converting to set is that set is good for comparing
def convertInputToSet(inputList):
    ctr = 0
    setOfState = set()

    for i in range(1, 4):
        for j in range(1, 4):

            if inputList[ctr] == "x":
                setOfState.add(("clear", "x", i, j))
                ctr = ctr + 1
            elif inputList[ctr] != "x":
                setOfState.add(("on", int(inputList[ctr]), i, j))
                ctr = ctr + 1

    return setOfState


#
def convertSetTolist(inputSet):
    list = [None] * 9
    for n in inputSet:
        if n[2] == 1 and n[3] == 1:
            list[0] = n[1]
        elif n[2] == 1 and n[3] == 2:
            list[1] = n[1]
        elif n[2] == 1 and n[3] == 3:
            list[2] = n[1]
        elif n[2] == 2 and n[3] == 1:
            list[3] = n[1]
        elif n[2] == 2 and n[3] == 2:
            list[4] = n[1]
        elif n[2] == 2 and n[3] == 3:
            list[5] = n[1]
        elif n[2] == 3 and n[3] == 1:
            list[6] = n[1]
        elif n[2] == 3 and n[3] == 2:
            list[7] = n[1]
        elif n[2] == 3 and n[3] == 3:
            list[8] = n[1]

    return list


#function creates a dictonary of all moves where key= move and value is dict which contains pre conditions "p",add "a" and remove "r"
def createStripsDictOfPossibleMoves():
    moveOperator = {}

    for n in range(1, 9):
        for i in range(1, 4):
            for j in range(1, 4):
                if (i - 1) > 0:
                    tempList = [n, i, j, i - 1, j]
                    moveOperator[tempList[0], tempList[1], tempList[2], tempList[3], tempList[4]] = addMovetoDict(
                        tempList)
                if (i + 1) < 4:
                    tempList = [n, i, j, i + 1, j]

                    moveOperator[tempList[0], tempList[1], tempList[2], tempList[3], tempList[4]] = addMovetoDict(
                        tempList)
                if (j - 1) > 0:
                    tempList = [n, i, j, i, j - 1]

                    moveOperator[tempList[0], tempList[1], tempList[2], tempList[3], tempList[4]] = addMovetoDict(
                        tempList)
                if (j + 1) < 4:
                    tempList = [n, i, j, i, j + 1]

                    moveOperator[tempList[0], tempList[1], tempList[2], tempList[3], tempList[4]] = addMovetoDict(
                        tempList)
    return moveOperator


def addMovetoDict(tempList):
    dictElement = {
        "p": set(
            [("On", tempList[0], tempList[1], tempList[2]), ("Clear", "x", tempList[3], tempList[4]),
             ("Adj", tempList[1], tempList[2], tempList[3], tempList[4])]),
        "a": set(
            [("On", tempList[0], tempList[3], tempList[4]), ("Clear", "x", tempList[1], tempList[2])]),
        "r": set(
            [("On", tempList[0], tempList[1], tempList[2]), ("Clear", "x", tempList[3], tempList[4])])
    }

    return dictElement

#creates 2 ditonaries which will help in retriving positon of numbers and the value at positions
def convertSetToDict(statePosition):
    stateDict = {}
    keyDict = {}

    for position in statePosition:
        stateDict[position[1]] = [position[2], position[3]]
        keyDict[position[2], position[3]] = position[1]

    return stateDict, keyDict

#function creates a set of all possible moves at that state
def getAllPossibleMoves(stateDict, keyDict):

    possibleSteps = set()
    i, j = stateDict['x'][0], stateDict['x'][1]
    # checks if  upward move is possible
    if (i - 1) > 0:
        numberAtIndex = keyDict[i - 1, j]
        possibleSteps.add((numberAtIndex, i, j, i - 1, j))
        # checks if moving downward is possibel
    if (i + 1) < 4:
        numberAtIndex = keyDict[i + 1, j]
        possibleSteps.add(((numberAtIndex, i, j, i + 1, j)))
        # checks if rightward move is possible
    if (j - 1) > 0:
        numberAtIndex = keyDict[i, j - 1]
        possibleSteps.add((numberAtIndex, i, j, i, j - 1))
        # check if leftward moove is posible
    if (j + 1) < 4:
        numberAtIndex = keyDict[i, j + 1]
        possibleSteps.add((numberAtIndex, i, j, i, j + 1))
    return possibleSteps


def selectMoveFromPossibleMoves(possibleMovesSet, allMovesDict, startStatePosition, currentStateConfig):
    moveValueDict = defaultdict(list)

    #gets the move which has the most number of preconditions in the initial state
    # if there are multiple moves to choose from move is selected based on the move which has the highest value when the heuristic fuction is applied
    for m in possibleMovesSet:
        p = allMovesDict[m]['p']
        intersectionValue = len(p.intersection(startStatePosition))
        moveValueDict[intersectionValue].append(m)

    maximumIntersection = max(moveValueDict, key=int)

    return selectBetweenMovesUsingheuristicFunction(moveValueDict[maximumIntersection],currentStateConfig,startStatePosition)



def selectBetweenMovesUsingheuristicFunction(moveList, currentStateConfig, startStatePosition):
    valueDict = {}

    for m in moveList:
        #creates a temp future state after the move is applied
        tempState = EightPuzzleState(copy.copy(currentStateConfig.position), "tempState")
        #applies the move
        tempState.updateObjectState(m[0], m[1], m[2], m[3], m[4])

        futureState = EightPuzzleState(tempState.position, "futureState")

        #gets the value of similarity with the initial state
        getheuristicValue = calculateHeuristicValue(futureState, startStatePosition)

        #adds it to a dictionary where value of the heuristic function is key and move is value.

        valueDict[getheuristicValue] = m

    return valueDict[max(valueDict, key=int)]

#Function calculates the number of elememts which are common with start state
def calculateHeuristicValue(state, startStatePosition):
    noOfelementsOutOfPosition = len(state.position.intersection(startStatePosition))
    return noOfelementsOutOfPosition
