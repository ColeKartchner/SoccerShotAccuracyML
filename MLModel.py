import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from matplotlib.widgets import Cursor
import tkinter as tk

# Load data
data = pd.read_csv(r'C:\Users\colek\OneDrive\Desktop\complete_shot_data.csv')
X = data[['x', 'y']]
y = data['outcome']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
rf = RandomForestClassifier(n_estimators=200, class_weight='balanced', random_state=42)
rf.fit(X_train, y_train)

# Initialize tkinter
root = tk.Tk()
root.withdraw()

def display_prediction(x, y):
    prediction_input = pd.DataFrame([[x, y]], columns=['x', 'y'])
    probas = rf.predict_proba(prediction_input)[0]
    outcome_labels = ['Goal', 'On-target', 'Off-target']
    info_text = "\n".join([f"{label}: {prob*100:.2f}%" for label, prob in zip(outcome_labels, probas)])
    message_window = tk.Toplevel(root)
    message_window.title("Prediction Outcomes")
    tk.Message(message_window, text=info_text, padx=20, pady=20).pack()
    message_window.after(8000, message_window.destroy)


def onclick(event):
    if event.inaxes:
        display_prediction(event.xdata, event.ydata)

def visualize_field(image_path):
    img = plt.imread(image_path)
    fig, ax = plt.subplots(figsize=(15, 10))
    ax.imshow(img)
    cursor = Cursor(ax, useblit=True, color='yellow', linewidth=2)
    plt.axis('off')

    fig.canvas.mpl_connect('button_press_event', onclick)
    plt.show()

visualize_field(r'C:\Users\colek\OneDrive\Pictures\Screenshots\Screenshot (179).png')
