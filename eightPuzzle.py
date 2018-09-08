import utilityFunctions

class EightPuzzleState:
    def __init__(self,positionSet,nameOfSet):
        #set the object varibales
        self.position=positionSet
        self.name=nameOfSet

    # A function which  will print the object In the type of a puzzle
    '''     Example:
            ---------------
            | 1 || 2 || 3 |
            | 4 || 5 || 6 |
            | 7 || 8 || x |
            ---------------   '''
    def printState(self,flag):
        if self.name!="Step":
            print(self.name+":")
        listToPrint=utilityFunctions.convertSetTolist(self.position)
        print("---------------")
        print("| " + str(listToPrint[0]) + " |" + "| " + str(listToPrint[1]) + " |" + "| " + str(listToPrint[2]) + " |")
        print("| " + str(listToPrint[3]) + " |" + "| " + str(listToPrint[4]) + " |" + "| " + str(listToPrint[5]) + " |")
        print("| " + str(listToPrint[6]) + " |" + "| " + str(listToPrint[7]) + " |" + "| " + str(listToPrint[8]) + " |")
        print("---------------")
        print("---------------")

        if flag==1:
            print("Strips State :")
            print(self.getAdjacentFields())
            print("---")
        print("---")



    #Function updates the state of object
    #The set of positions is updated fist by adding the new posistions then removing the ones which arent required.
    def updateObjectState(self,n,i,j,k,l):
        self.position.add(("on",n,i,j))
        self.position.add(("clear","x",k,l))
        self.position.remove(("clear","x",i,j))
        self.position.remove(("on",n,k,l))

    def getAdjacentFields(self):
        setAdj = set()
        for i in range(1, 4):
            for j in range(1, 4):
                if (i - 1) > 0:
                    setAdj.add(("Adj", i, j, i - 1, j))
                if (i + 1) < 4:
                    setAdj.add(("Adj", i, j, i + 1, j))
                if (j - 1) > 0:
                    setAdj.add(("Adj", i, j, i, j - 1))
                if (j + 1) < 4:
                    setAdj.add(("Adj", i, j, i, j + 1))
        return self.position.union(setAdj)
        # self.position=self.position.union(setAdj)
