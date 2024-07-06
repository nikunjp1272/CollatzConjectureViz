import turtle

def collatz_sequence(n):
    """
    Generate the Collatz sequence for a given integer n.
    """
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

def draw_collatz_journey(t, sequence, left_angle=45, right_angle=45, line_length=10):
    """
    Draw the journey of a Collatz sequence using a turtle.

    Parameters:
        t (turtle.Turtle): The turtle to draw with.
        sequence (list): The Collatz sequence to draw.
        left_angle (float): The angle to turn when the number is even (to the left).
        right_angle (float): The angle to turn when the number is odd (to the right).
        line_length (float): The length of each line segment.
    """
    for number in sequence:
        if number % 2 == 0:
            t.left(left_angle)  # Turn left
        else:
            t.right(right_angle)  # Turn right
        t.forward(line_length)  # Move forward

def plot_collatz_journeys(n, left_angle=45, right_angle=45, line_length=10, speed=1):
    """
    Plot the journeys of the Collatz sequences for numbers from 1 to n using turtles.

    Parameters:
        n (int): The maximum number to consider.
        left_angle (float): The angle to turn when the number is even (to the left).
        right_angle (float): The angle to turn when the number is odd (to the right).
        line_length (float): The length of each line segment.
        speed (int): The speed of the turtle animation (1 to 10).
    """
    screen = turtle.Screen()
    screen.setup(width=1000, height=1000)
    screen.title("Collatz Sequence Journey")

    # Set the offset for starting point
    x_offset = -screen.window_width() / 2 + 100
    y_offset = -screen.window_height() / 2 + 100

    # Draw the journeys
    for i in range(1, n + 1):
        t = turtle.Turtle()
        t.speed(speed)
        t.penup()
        t.goto(x_offset, y_offset)
        t.pendown()
        t.hideturtle()

        sequence = collatz_sequence(i)
        draw_collatz_journey(t, sequence, left_angle, right_angle, line_length)

    turtle.done()

# Example usage with adjustable angles, line length, and animation speed:
plot_collatz_journeys(100, left_angle=-12, right_angle=12, line_length=10, speed=50)
