# This program positions the cube and helps it do certain movements

## Scrambled moved: R U R' U' R U R' U' L' U' L U B B U U R U R R 

# The Up face 
upFace = [
    ['B', 'W', 'Y'],
    ['W', 'W', 'Y'],
    ['B', 'Y', 'O']
]

# The Down face
downFace = [
    ['Y', 'W', 'G'],
    ['Y', 'Y', 'B'],
    ['W', 'G', 'O']
]

# The Right face
rightFace = [
    ['G', 'B', 'R'],
    ['O', 'R', 'R'],
    ['R', 'O', 'W']
]

# The Left face
leftFace = [
    ['Y', 'G', 'O'],
    ['R', 'O', 'R'],
    ['R', 'O', 'B']
]

# The Front face
frontFace = [
    ['W', 'G', 'Y'],
    ['Y', 'G', 'W'],
    ['O', 'B', 'W']
]

# The Back face
backFace = [
    ['G', 'R', 'R'],
    ['G', 'B', 'B'],
    ['G', 'O', 'B']
]

## Prints the cube in the format:
##            [upFace]
## [leftFace] [frontFace] [rightFace] [backFace]
##            [downFace]
## Example: 
##         W W W
##         W W W
##         W W W 

## O O O   G G G   R R R   B B B   
## O O O   G G G   R R R   B B B 
## O O O   G G G   R R R   B B B , 

##         Y Y Y 
##         Y Y Y 
##         Y Y Y 
def printCube():
    # print upFace 
    for i in range(3):
        print(9 * ' ', end = '')
        for j in range(3):
            print(upFace[i][j] + ' ', end = '')
        print()
    print()

    # print leftFace, frontFace, rightFace, backFace 
    for i in range(3):
        for j in range(3):
            print(leftFace[i][j] + ' ', end = '')
        print((3* ' '), end = '')
        for j in range(3):
            print(frontFace[i][j] + ' ', end = '')
        print((3* ' '), end = '')
        for j in range(3):
            print(rightFace[i][j] + ' ', end = '')
        print((3* ' '), end = '')
        for j in range(3):
            print(backFace[i][j] + ' ', end = '')
        print()
    print()

    # print downFace
    for i in range(3):
        print(9 * ' ', end = '')
        for j in range(3):
            print(downFace[i][j] + ' ', end = '')
        print()

## All moves:
## R, R'
## L, L'
## F, F'
## U, U' 
## B, B'
## D, D'

def r():
    # store moving pieces in temp array 
    tempFront = [frontFace[0][2], frontFace[1][2], frontFace[2][2]]
    tempUp = [upFace[0][2], upFace[1][2], upFace[2][2]]
    tempBack = [backFace[0][2], backFace[1][2], backFace[2][2]]
    tempDown = [downFace[0][2], downFace[1][2], downFace[2][2]]

    # move front pieces to upFace
    upFace[0][2] = frontFace[0][2]
    upFace[1][2] = frontFace[1][2]
    upFace[2][2] = frontFace[2][2]

    # move up pieces to backFace
    backFace[0][2] = tempUp[0]
    backFace[1][2] = tempUp[1]
    backFace[2][2] = tempUp[2]

## fix from here!
    # move back pieces to downFace
    downFace[0][2] = tempBack[0]
    downFace[1][2] = tempBack[1]
    downFace[2][2] = tempBack[2]

    # move down pieces to frontFace
    frontFace[0][2] = tempDown[0]
    frontFace[1][2] = tempDown[1]
    frontFace[2][2] = tempDown[2]



def main():
    print("Original Cube:")
    printCube()
    print("Cube after R:")
    r()
    printCube()

main()
