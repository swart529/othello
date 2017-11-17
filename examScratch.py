#Exam Scratch
import turtle

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

def boardPosition():
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

def boardColor():
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

def colorChange(t,boardPos, row, col, color):
    t.shape('circle')
    t.goto(boardPos[row][col])
    if color =='W':
        t.color('white')
    elif color == 'B':
        t.color('black')
    t.stamp()



def isValidMove(boardCol, row, col, color):
    if boardCol[row][col] == 'U':
        return True
    if boardCol[row][col] == 'B':
        return False
    if boardCol[row][col] == 'W':
        return False

def main():
    turtle.setworldcoordinates(-10,-10,190,190)
    t = turtle.Turtle()
    grid(t)
    gridNum(t)
    boardCol = boardColor()
    boardPos = boardPosition()
    done = False
    while not done == True:
        moveRow = int(turtle.textinput("","Enter a row number: "))
        moveCol = int(turtle.textinput("","Enter a column number: "))
        color = turtle.textinput("","Enter a color: ")
        quit = turtle.textinput("","Enter y or n: ")
        check = isValidMove(boardCol, moveRow, moveCol, color)
        if check == True:
            colorChange(t,boardPos, moveRow, moveCol, color)
        if check == False:
            print("Not a valid move.")
        if quit == 'y':
            done = True

if __name__ == '__main__':
    main()
