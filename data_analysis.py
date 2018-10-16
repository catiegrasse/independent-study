from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
import pandas as pd

col_names = ["Female", "Male", "Readmission"]

dataset = pd.read_csv("testingAnalysis.csv", header=None, names=col_names)

feature_cols = ["Female", "Male"]

X = dataset[feature_cols]
y = dataset.Readmission

# split into training and testing sets
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25, random_state=0)

# train the classifier
classifier = LogisticRegression(random_state=0)
classifier.fit(X_train, y_train)

# predict on the testing data
y_pred = classifier.predict(X_test)

print "Prediction: \n", y_pred
print "Test input: \n", X_test
print "Expected output: \n", y_test
