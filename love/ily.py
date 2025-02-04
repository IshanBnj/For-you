import matplotlib.pyplot as plt
import numpy as np
import random
from matplotlib.animation import FuncAnimation

# Set up the figure and axes
fig, ax = plt.subplots(figsize=(10, 8))
ax.set_facecolor('black')
ax.set_xlim(-500, 500)
ax.set_ylim(-400, 400)
ax.axis('off')  # Turn off the axis

# Function to draw a heart
def heart(t, size=1):
    x = size * 16 * np.sin(t)**3
    y = size * (13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t))
    return x, y

# Create a scatter plot for the flowers
flowers = ax.scatter([], [], color=[], s=[], alpha=0.8)

# Function to draw a flower
def draw_flower():
    x = random.randint(-400, 400)
    y = random.randint(-300, 300)
    size = random.randint(100, 300)
    color = random.choice(['red', 'yellow', 'blue', 'pink', 'purple', 'orange'])
    return x, y, size, color

# Function to update the heart size
heart_line, = ax.plot([], [], color='red', lw=3)

# Function to animate the heart growing
def update_heart(frame):
    t = np.linspace(0, 2 * np.pi, 1000)
    x, y = heart(t, size=(frame + 1) * 0.5)  # Grow the heart with each frame
    heart_line.set_data(x, y)
    return heart_line,

# Function to animate flowers
def animate_flowers(frame):
    if frame % 10 == 0:  # Add a new flower every 10 frames
        x, y, size, color = draw_flower()
        flowers.set_offsets(np.append(flowers.get_offsets(), [[x, y]], axis=0))
        flowers.set_sizes(np.append(flowers.get_sizes(), [size], axis=0))
        flowers.set_color(np.append(flowers.get_facecolor(), [color], axis=0))
    return flowers,

# Function to animate the "I love you" message
message = ax.text(0, -250, "", color='white', fontsize=30, ha='center')

def animate_message(frame):
    message.set_text(f"I love you\n" + '.' * (frame % 4))
    message.set_fontsize(30 + frame * 2)  # Gradually increase the font size
    return message,

# Create the animation using FuncAnimation
def update(frame):
    update_heart(frame)
    animate_flowers(frame)
    animate_message(frame)
    return heart_line, flowers, message

# Create the animation
ani = FuncAnimation(fig, update, frames=50, interval=100, blit=False)

# Show the plot
plt.show()
