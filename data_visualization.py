# Don't use choice 4 yet it doesn't work properly

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def visualize_shots(csv_path, field_image_path):
    data = pd.read_csv(csv_path)

    outcome_colors = {1: 'green', 2: 'blue', 3: 'red'}

    choice = int(input("Enter 1 for goals, 2 for on-target, 3 for off-target, 0 for all, 4 for heatmap: "))

    field_img = plt.imread(field_image_path)

    plt.figure(figsize=(10, 7))
    plt.imshow(field_img, extent=[0, field_img.shape[1], 0, field_img.shape[0]])

    if choice in [1, 2, 3]:
        outcome_data = data[data['outcome'] == choice]
        plt.scatter(outcome_data['x'], outcome_data['y'], color=outcome_colors[choice], label=f'Outcome {choice}')
    elif choice == 0:
        for outcome, color in outcome_colors.items():
            outcome_data = data[data['outcome'] == outcome]
            plt.scatter(outcome_data['x'], outcome_data['y'], color=color, label=f'Outcome {outcome}')
    elif choice == 4:
        sns.kdeplot(x=data['x'], y=data['y'], levels=5, color='green', fill=True)
    else:
        print("Invalid choice. Please enter a number between 0 and 4.")
        return

    plt.axis('off')
    plt.legend()
    plt.show()

visualize_shots(r'C:\Users\colek\OneDrive\Desktop\complete_shot_data.csv', r'C:\Users\colek\OneDrive\Pictures\Screenshots\Screenshot (179).png')
