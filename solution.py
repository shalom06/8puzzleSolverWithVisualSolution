import utilityFunctions
import eightPuzzle
import copy

# taking input from user and converting to a set

startState = utilityFunctions.getInputfromUser()

# convert To a 8 puzzle object
startStateConfig = eightPuzzle.EightPuzzleState(startState, "startState")

# set the goal State
# for Assignment the goal state is already set but if you can change by inputting new one

goalStateConfig = eightPuzzle.EightPuzzleState(set(
    [("on", 1, 1, 1), ("on", 2, 1, 2), ("on", 3, 1, 3), ("on", 8, 2, 1), ("clear", "x", 2, 2),
     ("on", 4, 2, 3),
     ("on", 7, 3, 1), ("on", 6, 3, 2), ("on", 5, 3, 3)]), "GoalState")

# print StatrtState
startStateConfig.printState(1)

# print GoalState
goalStateConfig.printState(1)

# no Of Moves Before Exiting
noOfMoveslimit = int(raw_input("Enter the Number of Steps To check Before Quiting, Sir had Specified 10 "))
# Function creates a dictonary of all moves and thier possible pre conditions and  actions
allMovesDict = utilityFunctions.createStripsDictOfPossibleMoves()

# startOfStrips
# strips solves the problem from the buttom up so while solving our goal state is the current state .                                                                                                                                                                                                                                                                                         m up
currentState = eightPuzzle.EightPuzzleState(copy.copy(goalStateConfig.position), "currentState")
moves = 0

# initilize a few lists and sets required for processing
movesList = []
stepList = []
stepDict = {}
possibleMovesSet = set()




# begin of the loop
# loop will break if number of moves excceed the limit.
solutionFound = False
while (moves <= noOfMoveslimit):
    currentStateDict = {}
    currentStateKeyDict = {}
    # creates two dictionaries 1 which uses the  value as key and location as value and one which uses the locations as key and sets the values as values of the dictionary
    currentStateDict, currentStateKeyDict = utilityFunctions.convertSetToDict(currentState.position)

    # gets all possible moves of  particular position
    possibleMovesSet = utilityFunctions.getAllPossibleMoves(currentStateDict, currentStateKeyDict)

    # this is done so that no move is repeated  the moves which are already done are not added to the possible moves set
    possibleMovesSet = possibleMovesSet - set(movesList)
    selectedMove = utilityFunctions.selectMoveFromPossibleMoves(possibleMovesSet, allMovesDict,
                                                                startStateConfig.position, currentState)

    # current object is updated
    currentState.updateObjectState(selectedMove[0], selectedMove[1], selectedMove[2], selectedMove[3], selectedMove[4])

    # add move to a list of moves done
    movesList.append(selectedMove)
    tempState = eightPuzzle.EightPuzzleState(copy.copy(currentState.position), "CurrentState")
    stepList.append(tempState)

    if len(currentState.position.intersection(startStateConfig.position)) == 9:
        print("%%%%%%%%%%%%%%")
        print("Solution Found")
        print("%%%%%%%%%%%%%%")
        solutionFound = True
        break

    moves = moves + 1

if solutionFound:
    #reverse the list and print the states with moves
    stepList.insert(0,eightPuzzle.EightPuzzleState(goalStateConfig.position, "FinalState"))
    stepList.reverse()
    stepList.pop(0)

    movesList.reverse()

    noofMoves = len(movesList)
    index = 0
    for step in stepList:
        print("MOVE NO :" + str(index + 1))
        print("move(" + str(movesList[index][0]) + "," + str(movesList[index][1]) + "," + str(
            movesList[index][2]) + "," + str(movesList[index][3]) + "," + str(movesList[index][4]) + ")")
        print("---")
        step.printState(0)
        index += 1
elif solutionFound != True:
    print("Solution Not Found ")



print("END")
