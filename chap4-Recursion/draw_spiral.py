# Below is only compatible with python-2.7
import turtle


def drawSpiral(my_turtle, line_len):
    if line_len > 0:
        my_turtle.forward(line_len)
        my_turtle.right(90)
        drawSpiral(my_turtle, line_len - 5)


def main():
    my_turtle = turtle.Turtle()
    my_win = turtle.Screen()
    drawSpiral(my_turtle, 100)
    my_win.exitonclick()


if __name__ == '__main__':
    main()
