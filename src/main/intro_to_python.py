# Intro to GitHub and Python
# COT4500 Spring 2023
# Alanna Hill, al538601
import numpy as np

# This funtion takes in two paramters, a matrix and a boolean
# It prints out the matrix, and if the boolean is true, it prints
# a new line after it
def printMatrix(matrix, line):
    for row in matrix:
        print(*row)
    if line == True:
        print()

# This function creates and prints the three matricies specifid in the assignment
def main():

    # The first matrix is the identity matrix
    matrix = np.identity(3, int);

    printMatrix(matrix, True)
    
    # All rows != 1 are set to 3
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if (matrix[row][col] < 1):
                matrix[row][col] = 3

    printMatrix(matrix, True)
    
    # Last column is removed
    matrix = np.delete(matrix, 2, 1)

    printMatrix(matrix, False)

if (__name__ == "__main__"):
    main()
