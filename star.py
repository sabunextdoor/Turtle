import turtle
turtle.Screen().bgcolor("lavender")
turtle.Screen().setup(400,400)
turtle.title("star pattern")

board=turtle.Turtle()

board.forward(150)
board.left(120)
board.forward(150)
board.left(120)
board.forward(150)

board.penup()
board.right(150)
board.forward(70)
board.pendown()
board.right(90)
board.forward(150)
board.right(120)
board.forward(150)
board.right(120)
board.forward(150)
turtle.done()