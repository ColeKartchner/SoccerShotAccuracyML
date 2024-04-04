import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

data = pd.read_csv(r'C:\Users\colek\OneDrive\Desktop\complete_shot_data.csv')
X = data[['x', 'y']]
y = data['outcome']

points = {1: 5, 2: 1, 3: 0}

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

rf = RandomForestClassifier(n_estimators=200, class_weight='balanced', random_state=42)

rf.fit(X_train, y_train)

probabilities = rf.predict_proba(X_test)

expected_scores = np.dot(probabilities, np.array([points[1], points[2], points[3]]))

print(f"Average expected score per shot: {np.mean(expected_scores)}")

y_pred = rf.predict(X_test)

print(classification_report(y_test, y_pred))
