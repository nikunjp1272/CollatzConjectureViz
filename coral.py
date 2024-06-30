import matplotlib.pyplot as plt
import numpy as np

def collatz(n):
    # Generate the Collatz sequence for a given starting number
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

def draw_collatz_path(n, odd_angle, even_angle):
    # Generate a visual path for the Collatz sequence of a number
    sequence = collatz(n)
    x, y = 0, 0  # Start at the origin
    path = [(x, y)]
    angle = 0
    for num in sequence[1:]:  # Skip the first number as it's the starting point
        if num % 2 == 0:
            angle += even_angle  # Turn by even_angle for even numbers
        else:
            angle += odd_angle  # Turn by odd_angle for odd numbers
        # Move one unit in the direction of the current angle
        x += np.cos(np.radians(angle))
        y += np.sin(np.radians(angle))
        path.append((x, y))
    return path

# Set up the plot
fig, ax = plt.subplots(figsize=(12, 12))

# Set angles for odd and even numbers
odd_angle = 9   # Turn 9 degrees for odd numbers
even_angle = -9  # Turn -9 degrees for even numbers

# Draw paths for numbers 1 to 250
for i in range(1, 251):
    path = draw_collatz_path(i, odd_angle, even_angle)
    x, y = zip(*path)
    # Plot each path with a line width of 2 and 90% opacity
    ax.plot(x, y, linewidth=2, alpha=0.9)

# Set the title of the plot
ax.set_title(f"Collatz Conjecture Paths (1-250)\nOdd angle: {odd_angle}°, Even angle: {even_angle}°")
ax.axis('off')  # Turn off the axes
plt.tight_layout()
plt.show()
