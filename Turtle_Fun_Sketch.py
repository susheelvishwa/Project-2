import turtle


def Fun_Sketch():
    window = turtle.Screen()
    window.setup(
        width=1.0,
        height=1.0,
    )
    window.title("Fun_Sketch")
    return window


def setup_pen():
    pen = turtle.Turtle()
    pen.speed(0)
    pen.width(5)
    return pen


def draw_forward():
    pen.forward(10)


def draw_backward():
    pen.backward(10)


def turn_left():
    pen.left(10)


def turn_right():
    pen.right(10)


def clear_drawing():
    pen.clear()


def setup_keyboard_controls():
    window.listen()
    window.onkeypress(draw_forward, "Up")
    window.onkeypress(draw_backward, "Down")
    window.onkeypress(turn_left, "Left")
    window.onkeypress(turn_right, "Right")
    window.onkeypress(clear_drawing, "space")


def display_comment(text, left=True):
    comment_pen = turtle.Turtle()
    comment_pen.penup()
    if left == True:
        comment_pen.goto(-window.window_width() / 3, window.window_height() / 3)
    else:
        comment_pen.goto(+window.window_width() / 3, window.window_height() / 3)
    comment_pen.write(
        text, align="center", font=("Cascadia Mono SemiBold", 12, "normal")
    )
    comment_pen.hideturtle()


def main():
    global window, pen
    window = Fun_Sketch()
    pen = setup_pen()
    setup_keyboard_controls()
    display_comment(
        "Use the arrow keys to draw. Press space to clear\nDraw_forward	Up  :	Move forward/upward\nDraw_backwar	Down:   Move backward/downward\nTurn_left	Left: 	Turn left\nTurn_right	Right: 	Turn right\nClear_drawing 	Space: 	Clear the drawing "
    )
    display_comment(
        "Name: Susheel Vishwakarma\nStudent code:   cap01_064\nproject name: Fun sketch",
        False,
    )

    window.mainloop()


if __name__ == "__main__":
    main()
