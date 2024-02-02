import numpy as np
import matplotlib.pyplot as plt
import random


def createRandomGrid(length, height, probability):

#creates a numpy array of desired height and lenght
#takes in a probability argument whch is used to randomly select alive cells

    gridShape = (length, height)
    grid = np.zeros(gridShape)

    for row in range(gridShape[0]):
        for column in range(gridShape[1]):
            aliveProbability = round(random.random(),1)
            if aliveProbability <= probability:
                grid[row, column] = 1
    
    return grid

def updateValue(element, aliveNeighbours):
    """
    Rules:
    1. Birth rule: An element that is currently 0 with exactly 3 neighbours is set to 1.
    2. Death rule 1 (loneliness): An element that is currently 1 with 1 or less neighbours is set to 0.
    3. Death rule 2 (starvation): An element that is currently 1 with 4 or more neighbours is set to 0.
    4. Survival rule: An element that is currently 1 with 2 or 3 neighbours is set to 1.
    """

    if element == 1:
        if aliveNeighbours < 2 or aliveNeighbours > 3:
            element = 0
    elif element == 0 and aliveNeighbours == 3:
        element = 1

    return element

def updateGrid(grid):
    #creates a copy of grid to maintain previous state

    newGrid = np.copy(grid)
    gridShape = np.shape(grid)

    for row in range(gridShape[0]):
        for column in range(gridShape[1]):
            element = grid[row, column]
            #max and min prevent going over index of grid array 
            neighbours = grid[max(0, row-1):min(gridShape[0], row+2), max(0, column-1):min(gridShape[1], column+2)]
            #np.sum() sums all selected cells and then remove current element
            aliveNeighbourSum = np.sum(neighbours) - element
            newGrid[row, column] = updateValue(element, aliveNeighbourSum)

    return newGrid


def display(ax, grid):
    #clear axis and then display current grid using imshow() with cmap used for colour coding
    ax.clear()
    ax.set_axis_off()
    ax.imshow(grid, interpolation='none', cmap='RdPu')
    plt.pause(1)
  
def main():

    test()

    nStep = 20
    grid = createRandomGrid(100,100, 0.3)
    
    fig, ax = plt.subplots(figsize=(10, 10))
        
    for i in range(nStep):
        display(ax, grid)
        grid = updateGrid(grid)
    
    plt.show()

def testUpdateGrid():

    # Assertion for differeent scenarios 
    assert (updateGrid(np.array([[1, 1, 0],
                                [0, 1, 0],
                                [0, 1, 1]], dtype=np.int8)) == 
            np.array([[1, 1, 0],
                    [0, 0, 0],
                    [0, 1, 1]], dtype=np.int8)).all() == True

    assert (updateGrid(np.array([[1, 1, 0, 0],
                                [1, 0, 1, 1],
                                [1, 0, 1, 0],
                                [0, 0, 1, 1]], dtype=np.int8)) == 
            np.array([[1, 1, 1, 0],
                    [1, 0, 1, 1],
                    [0, 0, 0, 0],
                    [0, 1, 1, 1]], dtype=np.int8)).all() == True

    assert (updateGrid(np.array([[0, 1, 1, 1, 0],
                                [0, 0, 1, 0, 1],
                                [0, 0, 1, 1, 0],], dtype=np.int8)) ==
            np.array([[0, 1, 1, 1, 0],
                    [0, 0, 0, 0, 1],
                    [0, 0, 1, 1, 0],], dtype=np.int8)).all() == True

    assert (updateGrid(np.array([[1, 0, 0, 1, 1, 1],
                                [0, 1, 0, 0, 0, 0],], dtype=np.int8)) == 
            np.array([[0, 0, 0, 0, 1, 0],
                    [0, 0, 0, 0, 1, 0],], dtype=np.int8)).all() == True


def test():
    print("running update grid test")
    testUpdateGrid()
    print("test successfull")

if __name__ == "__main__":
    main()

