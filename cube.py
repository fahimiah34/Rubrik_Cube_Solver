# This program positions the cube and helps it do certain movements

# The Up face 
upFace = [
    ['W', 'W', 'W'],
    ['W', 'W', 'W'],
    ['W', 'W', 'W']
]

# The Down face
downFace = [
    ['Y', 'Y', 'Y'],
    ['Y', 'Y', 'Y'],
    ['Y', 'Y', 'Y']
]

# The Right face
rightFace = [
    ['R', 'R', 'R'],
    ['R', 'R', 'R'],
    ['R', 'R', 'R']
]

# The Left face
leftFace = [
    ['O', 'O', 'O'],
    ['O', 'O', 'O'],
    ['O', 'O', 'O']
]

# The Front face
frontFace = [
    ['G', 'G', 'G'],
    ['G', 'G', 'G'],
    ['G', 'G', 'G']
]

# The Back face
backFace = [
    ['B', 'B', 'B'],
    ['B', 'B', 'B'],
    ['B', 'B', 'B']
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

printCube()
