import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg

def collatz(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

def draw_collatz_path(n, odd_angle, even_angle):
    sequence = collatz(n)
    x, y = 0, 0
    path = [(x, y)]
    angle = 0
    for num in sequence[1:]:
        if num % 2 == 0:
            angle += even_angle
        else:
            angle += odd_angle
        x += np.cos(np.radians(angle))
        y += np.sin(np.radians(angle))
        path.append((x, y))
    return path

def generate_plot(linewidth, alpha, num_paths, odd_angle, even_angle):
    fig, ax = plt.subplots(figsize=(12, 12))

    for i in range(1, num_paths + 1):
        path = draw_collatz_path(i, odd_angle, even_angle)
        x, y = zip(*path)
        ax.plot(x, y, linewidth=linewidth, alpha=alpha)

    ax.set_title(f"Collatz Conjecture Paths (1-{num_paths})\nOdd angle: {odd_angle}°, Even angle: {even_angle}°")
    ax.axis('off')
    plt.tight_layout()

    # Save the plot as an image
    canvas = FigureCanvasAgg(fig)
    canvas.draw()
    plt.savefig("collatz_plot.png", dpi=300, bbox_inches='tight')
    plt.close(fig)

    print("Plot saved as 'collatz_plot.png'")

# Get input parameters from the user
linewidth = float(input("Enter line width (e.g., 0.5): "))
alpha = float(input("Enter alpha (transparency, e.g., 0.5): "))
num_paths = int(input("Enter number of paths (e.g., 100): "))
odd_angle = float(input("Enter odd angle (e.g., 10): "))
even_angle = float(input("Enter even angle (e.g., -10): "))

# Generate the plot
generate_plot(linewidth, alpha, num_paths, odd_angle, even_angle)
