import numpy as np
import matplotlib.pyplot as plt

import random


def createRandomGrid(length, height, probability):

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
    update value based on rules
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

    newGrid = np.copy(grid)
    gridShape = np.shape(grid)

    for row in range(gridShape[0]):
        for column in range(gridShape[1]):
            element = grid[row, column]
            neighbours = grid[max(0, row-1):min(gridShape[0], row+2), max(0, column-1):min(gridShape[1], column+2)]
            aliveNeighbourSum = np.sum(neighbours) - element
            newGrid[row, column] = updateValue(element, aliveNeighbourSum)

    return newGrid

def display(grid):

    ax = plt.axes()
    ax.set_axis_off()

    ax.imshow(grid, interpolation='none', cmap='RdPu')
    plt.pause(0.1)

def display(ax, grid):

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

    # Assertion for Initial Grid 1 (3x3)
    assert (updateGrid(np.array([[1, 1, 0],
                                [0, 1, 0],
                                [0, 1, 1]], dtype=np.int8)) == 
            np.array([[1, 1, 0],
                    [0, 0, 0],
                    [0, 1, 1]], dtype=np.int8)).all() == True

    # Assertion for Initial Grid 2 (4x4)
    assert (updateGrid(np.array([[1, 1, 0, 0],
                                [1, 0, 1, 1],
                                [1, 0, 1, 0],
                                [0, 0, 1, 1]], dtype=np.int8)) == 
            np.array([[1, 1, 1, 0],
                    [1, 0, 1, 1],
                    [0, 0, 0, 0],
                    [0, 1, 1, 1]], dtype=np.int8)).all() == True

    # Assertion for Initial Grid 3 (5x5)
    assert (updateGrid(np.array([[0, 1, 1, 1, 0],
                                [0, 0, 1, 0, 1],
                                [0, 0, 1, 1, 0],], dtype=np.int8)) ==
            np.array([[0, 1, 1, 1, 0],
                    [0, 0, 0, 0, 1],
                    [0, 0, 1, 1, 0],], dtype=np.int8)).all() == True

    # Assertion for Initial Grid 4 (6x6)
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
