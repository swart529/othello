#Exam Scratch
import turtle

turtle.setworldcoordinates(-10,-10,190,190)

def grid(t):
    t.shapesize(3.5)
    t.speed(0)
    t.shape("square")
    t.color('green')
    t.pu()
    x = 10
    y = 10
    while (x <= 200) and (y <= 200):
        if (x == 190) and (y == 167.5):
            x += 10
            y += 10
        if (x == 190) and (y != 167.5):
            x = 10
            y += 22.5
        else:
            t.goto(x,y)
            t.stamp()
            x += 22.5

def gridNum(t):
    t.pu()
    t.color('black')
    x = -5
    y = 7.5
    num = 7
    while y != 187.5:
        t.goto(x,y)
        t.write(num, True, align = "left", font=("Arial",12,"normal"))
        num -= 1
        y += 22.5
    if y == 187.5:
        x = 7.5
        y = 180
        num = 0
        while x != 187.5:
            t.goto(x,y)
            t.write(num, True, align = "left", font=("Arial",12,"normal"))
            num += 1
            x += 22.5

def boardPos():
    boardMatrix = []
    for i in range(8):
        boardMatrix.append([0,1,2,3,4,5,6,7])
    fill = False
    x = 10
    y = 10
    row = 7
    col = 0
    while fill == False:
        if x == 167.5 and y != 167.5:
            boardMatrix[row][col] = x,y
            y += 22.5
            x = 10
            col = 0
            row -= 1
        if x == 167.5 and y == 167.5:
            boardMatrix[row][col] = x,y
            fill = True
        else:
            boardMatrix[row][col] = x,y
            x += 22.5
            col += 1
    return boardMatrix

def boardCol():
    boardMatrix = []
    row = 0
    col = 0
    fill = False
    for i in range(8):
        boardMatrix.append([0,1,2,3,4,5,6,7])
    while fill == False:
        if col == 7 and row != 7:
            boardMatrix[row][col] = 'U'
            col = 0
            row += 1
        if col == 7 and row == 7:
            boardMatrix[row][col] = 'U'
            fill = True
        else:
            boardMatrix[row][col] = 'U'
            col += 1
    return boardMatrix
