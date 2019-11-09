# https://leetcode.com/problems/set-matrix-zeroes/
# Cracking The Coding Interview 1.8: Zero Matrix

def setZeroes(m):
    # Do nothing if matrix is empty or consists of empty arrays
    if not len(m) or not len(m[0]):
        return False

    firstRowHasZero = False
    firstColHasZero = False

    # First check first row and col if they had 0 originally
    # because we'll use them as flags
    for i in range(len(m)):
        if m[i][0] == 0:
            firstColHasZero = True
            break

    for j in range(len(m[0])):
        if m[0][j] == 0:
            firstRowHasZero = True

    # Catch all zeroes, flag row and column in it contains 0
    for i in range(1, len(m)):
        for j in range(1, len(m[i])):
            if m[i][j] == 0:
                m[i][0] = 0
                m[0][j] = 0

    # Go to first column, except first cell. First row contains flags, so it's a special case.
    # If the value is 0, set entire row to 0
    for i in range(1, len(m)):
        if m[i][0] == 0:
            for j in range(1, len(m[i])):
                m[i][j] = 0

    # Check first row. If 0, set column to 0
    for j in range(1, len(m[0])):
        if m[0][j] == 0:
            for i in range(len(m)):
                m[i][j] = 0

    if firstRowHasZero:
        for j in range(len(m[0])):
            m[0][j] = 0

    if firstColHasZero:
        for i in range(len(m)):
            m[i][0] = 0

    return True




# Test cases
emptyMatrix = []
sampleMatrix = [[1,1,1],[1,0,1],[1,1,1]]
expectedMatrix = [[1,0,1],[0,0,0],[1,0,1]]

sampleMatrix2 = [
    [0,1,2,0],
    [3,4,5,2],
    [1,3,1,5]
]

expectedMatrix2 = [
    [0,0,0,0],
    [0,4,5,0],
    [0,3,1,0]
]

sampleWithZeroFirstRow = [[1,0,1], [1,1,1], [1,1,1]]
expectedWithZeroFirstRow = [[0,0,0], [1,0,1], [1,0,1]]

sampleWithZeroFirstRow = [[1,0,1], [1,1,1], [1,1,1]]
expectedWithZeroFirstRow = [[0,0,0], [1,0,1], [1,0,1]]

sampleWithZeroFirstCol = [[1,1,1],[0,1,1], [1,1,1]]
expectedWithZeroFirstCol = [[0,1,1],[0,0,0], [0,1,1]]

print("============Test cases============")
setZeroes(emptyMatrix)
print(emptyMatrix)
print("============")
setZeroes(sampleMatrix)
print(sampleMatrix)
print(expectedMatrix)
print("============")
setZeroes(sampleMatrix2)
print(sampleMatrix2)
print(expectedMatrix2)
print("============")
setZeroes(sampleWithZeroFirstRow)
print(sampleWithZeroFirstRow)
print(expectedWithZeroFirstRow)
print("============")
setZeroes(sampleWithZeroFirstCol)
print(sampleWithZeroFirstCol)
print(expectedWithZeroFirstCol)