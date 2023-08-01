import turtle

def draw_text(text, font_size, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.write(text, font=("Arial", font_size, "normal"))

if __name__ == "__main__":
    name = "Vivek"
    font_size = 40

    # Set up the turtle screen
    turtle.setup(width=600, height=300)
    turtle.bgcolor("white")

    # Draw the name in digital coloring form
    turtle.color("black")
    draw_text(name, font_size, -80, 0)

    # Hide the turtle and display the result
    turtle.hideturtle()
    turtle.done()
