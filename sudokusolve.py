row = 0
col = 0
num = 0
def reduceNumberPool(pool):
    a = 0
    for i in range(len(pool)):
        if pool[i-a] == 0:
            pool.pop(i-a)
            a = a + 1

def checkRow(row, num):
    for a in range(9):
        if len(availableNumbers[row][a]) != 1:
            m = 0
            for b in range(len(availableNumbers[row][a])):
                if availableNumbers[row][a][b - m] == num:
                    availableNumbers[row][a].pop(b)
                    m = m + 1


def checkColumn(col, num):
    for a in range(9):
        if len(availableNumbers[a][col]) != 1:
            m = 0
            for b in range(len(availableNumbers[a][col])):
                if availableNumbers[a][col][b - m] == num:
                    availableNumbers[a][col].pop(b)
                    m = m + 1

def checkThreeByThree(x, y, num):
    for i in range(3):
        for j in range(3):
            if len(availableNumbers[i+x][j+y]) != 1:
                m = 0
                for k in range(len(availableNumbers[i+x][j+y])):
                    if availableNumbers[i+x][j+y][k - m] == num:
                        availableNumbers[i+x][j+y].pop(k)
                        m = m + 1

def checkThreeByThreeRowsCols(x, y):
    testGrid = []
    testGrid.append([0, 0, 0])
    testGrid.append([0, 0, 0])
    testGrid.append([0, 0, 0])

    numberPool2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for a in range(3):
        for b in range(3):
            if len(availableNumbers[x + a][y + b]) != 1:
                testGrid[a][b] = 11
            else:
                numberPool2[availableNumbers[x + a][y + b][0] - 1] = 0
    reduceNumberPool(numberPool2)

    for number in range(len(numberPool2)):
        for rows in range(3):
            for cols in range(3):
                if testGrid[rows][cols] == 11:
                    for cell in range(9):
                        if len(availableNumbers[rows + x][cell]) == 1:
                            if availableNumbers[rows + x][cell][0] == numberPool2[number]:
                                testGrid[rows][cols] = numberPool2[number]
                        if len(availableNumbers[cell][cols + y]) == 1:
                            if availableNumbers[cell][cols + y][0] == numberPool2[number]:
                                testGrid[rows][cols] = numberPool2[number]

        numberOfBlanks = 0
        for a in range(3):
            for b in range(3):
                if testGrid[a][b] == 11:
                    numberOfBlanks += 1
        if numberOfBlanks == 1:
            for a in range(3):
                for b in range(3):
                    if testGrid[a][b] == 11:
                        m = 0
                        for k in range(len(availableNumbers[a + x][b + y])):
                            if availableNumbers[a + x][b + y][k - m] != numberPool2[number]:
                                availableNumbers[a + x][b + y].pop(k - m)
                                m = m + 1

        for a in range(3):
            for b in range(3):
                if len(availableNumbers[a + x][b + y]) != 1:
                    testGrid[a][b] = 11


sudokuGrid = []
sudokuGrid.append([0, 0, 8, 0, 0, 0, 0, 1, 0])
sudokuGrid.append([0, 9, 0, 0, 0, 0, 0, 0, 0])
sudokuGrid.append([3, 4, 0, 5, 9, 0, 0, 0, 7])
sudokuGrid.append([6, 8, 0, 0, 0, 0, 4, 0, 0])
sudokuGrid.append([0, 0, 0, 0, 7, 0, 0, 0, 0])
sudokuGrid.append([0, 0, 4, 8, 0, 0, 1, 0, 0])
sudokuGrid.append([0, 0, 6, 0, 8, 0, 0, 0, 5])
sudokuGrid.append([0, 5, 1, 0, 0, 0, 0, 2, 0])
sudokuGrid.append([0, 0, 0, 0, 2, 0, 0, 9, 0])

availableNumbers = []

for i in range(9):
    availableNumbers.append([])
    for j in range(9):
        availableNumbers[i].append([])
        if sudokuGrid[i][j] == 0:
            availableNumbers[i][j] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        else:
            availableNumbers[i][j].append(sudokuGrid[i][j])
cond = -1
for test in range(9):
    cond = cond + 1
    for squareX in range(3):
        for squareY in range(3):
            for i in range(3):
                for j in range(3):
                    row = i + (squareX * 3)
                    col = j + (squareY * 3)
                    num = availableNumbers[i + squareX*3][j + squareY*3]
                    if len(availableNumbers[i+squareX*3][j+squareY*3]) == 1:
                        row = i + (squareX*3)
                        col = j + (squareY*3)
                        num = availableNumbers[i+squareX*3][j+squareY*3][0]
                        checkRow(row, num)
                        checkColumn(col, num)
                        checkThreeByThree(squareX*3, squareY*3, num)
                        checkThreeByThreeRowsCols(squareX*3, squareY*3)

                        correct = 0
    for a in range(9):
        for b in range(9):
            if len(availableNumbers[a][b]) == 1:
                sudokuGrid[a][b] = availableNumbers[a][b]
    print("")
    for i in range(9):
        print(availableNumbers[i])

