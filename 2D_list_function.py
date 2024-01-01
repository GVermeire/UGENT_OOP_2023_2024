import random

def create_2DList_with_input():
    matrix = [] # Create an empty list
    numberOfRows = eval(input("Enter the number of rows: "))
    numberOfColumns = eval(input("Enter the number of columns: "))

    for row in range(0, numberOfRows):
        matrix.append([]) # Add an empty new row
        for column in range(0, numberOfColumns):
            value = eval(input("Enter an element and press Enter: "))
            matrix[row].append(value)
    return matrix

def create_2DList_random():
    matrix = []  # Create an empty list
    numberOfRows = eval(input("Enter the number of rows: "))
    numberOfColumns = eval(input("Enter the number of columns: "))
    for row in range(0, numberOfRows):
        matrix.append([])  # Add an empty new row
        for column in range(0, numberOfColumns):
            matrix[row].append(random.randrange(0, 100))
    return matrix

def print2DList(matrix):
   for row in range(0, len(matrix)):
        for column in range(0, len(matrix[row])):
            print(matrix[row][column], end=" ")
        print()  # Print a newline

def sum2DList(matrix):
    total = 0
    for row in range(0, len(matrix)):
        for column in range(0, len(matrix[row])):
            total += matrix[row][column]

    print("Total is " + str(total))  # Print the total
    return total

def sum2DListByColumn(matrix):

    sumColumns = []

    for column in range(0, len(matrix[0])):
        total = 0
        for row in range(0, len(matrix)):
            total += matrix[row][column]
        print("Sum for column " + str(column) + " is " + str(total))
        sumColumns.append(total)
    return sumColumns

def sum2DListByRow(matrix):

    sumRows = []
    for row in range(0, len(matrix)):
        total = sum(matrix[row])
        print("Sum for row " + str(row) + " is " + str(total))
        sumRows.append(total)
    return sumRows

def maxSumRow(matrix):
    maxRow = sum(matrix[0])  # Get sum of the first row in maxRow
    indexOfMaxRow = 0
    for row in range(1, len(matrix)):
        if sum(matrix[row]) > maxRow:
            maxRow = sum(matrix[row])
            indexOfMaxRow = row

    print("Row " + str(indexOfMaxRow))
    return indexOfMaxRow

def shuffleMatrix(matrix):
    for row in range(0, len(matrix)):
        for column in range(0, len(matrix[row])):
            i = random.randrange(0, len(matrix))
            j = random.randrange(0, len(matrix[row]))
            # Swap matrix[row][column] with matrix[i][j]
            matrix[row][column], matrix[i][j] = \
                matrix[i][j], matrix[row][column]

    return matrix


def main():
    #matrix = create_2DList_with_input()
    matrix = create_2DList_random()
    #print(matrix)
    print2DList(matrix)
    sum2DListByColumn(matrix)
    #sum2DListByRow(matrix)
    #maxSumRow(matrix)
    #matrix2 = shuffleMatrix(matrix)
    #print2DList(matrix2)

main()