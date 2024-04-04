import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.widgets import Cursor
import tkinter as tk
from tkinter import simpledialog

shots_data = []

def onclick(event):
    # Record x, y coordinates
    x, y = event.xdata, event.ydata

    ROOT = tk.Tk()
    ROOT.withdraw()
    outcome = simpledialog.askinteger("Input", "Enter shot outcome (1 for goal, 2 for on-target, 3 for off-target):",
                                      parent=ROOT, minvalue=1, maxvalue=3)
    ROOT.destroy()

    outcome_colors = {1: 'green', 2: 'blue', 3: 'red'}
    color = outcome_colors.get(outcome, 'gray')  # Default to 'gray' if an invalid number is entered

    shots_data.append([x, y, outcome])

    plt.plot(x, y, 'o', color=color, markersize=10)  # Adjust the marker size as needed
    plt.draw()  # Update the plot with the new dot

    print(f"Shot recorded at ({x:.2f}, {y:.2f}) with outcome {outcome}")

def collect_data(image_path):
    img = plt.imread(image_path)
    fig, ax = plt.subplots(figsize=(15, 10))
    ax.imshow(img)

    cursor = Cursor(ax, horizOn=True, vertOn=True, color='yellow', linewidth=1)

    grid_color = 'white'
    grid_width = 1
    num_x_lines = img.shape[1] // 50
    num_y_lines = img.shape[0] // 50

    for i in range(num_x_lines + 1):
        ax.axvline(i * 50, color=grid_color, linestyle='-', linewidth=grid_width)

    for i in range(num_y_lines + 1):
        ax.axhline(i * 50, color=grid_color, linestyle='-', linewidth=grid_width)

    plt.axis('off')
    fig.canvas.mpl_connect('button_press_event', onclick)
    plt.show()

    pd.DataFrame(shots_data, columns=['x', 'y', 'outcome']).to_csv(r'C:\Users\colek\OneDrive\Desktop\shot_data.csv', index=False)
    print("Data saved to shot_data.csv on the desktop")

collect_data(r'C:\Users\colek\OneDrive\Pictures\Screenshots\Screenshot (179).png')
