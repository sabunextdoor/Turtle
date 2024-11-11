import turtle
turtle.Screen().bgcolor("pink")
turtle.Screen().setup(400,400)
turtle.title("square on canvas")

board=turtle.Turtle()
for i in range(4):
    board.forward(100)
    board.right(90)
turtle.done()