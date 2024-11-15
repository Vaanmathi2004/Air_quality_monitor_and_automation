import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

# Load the data
data = pd.read_csv('data.csv')

# Separate features and target
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=5)

# Plot target distribution
sns.countplot(x='Target', data=data)
plt.show()

# Initialize the KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors=5)

# Train the model
model.fit(X_train, y_train)

# Save the model to disk
filename = 'knn_model.sav'
pickle.dump(model, open(filename, 'wb'))

# Predict on the test set
y_pred = model.predict(X_test)

# Calculate accuracy
acc = metrics.accuracy_score(y_pred, y_test)
print("Accuracy is:", acc)

# Confusion matrix
cm = metrics.confusion_matrix(y_pred, y_test)
print('Confusion Matrix : \n', cm)

# Classification report
classification_report = metrics.classification_report(y_pred, y_test)
print('Classification Report:\n', classification_report)