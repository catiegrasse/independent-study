from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
import pandas as pd

col_names = ["Male", "Female", "Readmission"]

dataset = pd.read_csv("testingProcessor.csv", header=None, names=col_names)

feature_cols = ["Male", "Female"]

X = dataset[feature_cols]
y = dataset.Readmission

print sum([1 for num in y if num == 1])

# split into training and testing sets
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.10, random_state=0)

# train the classifier
classifier = LogisticRegression(random_state=0)
classifier.fit(X_train, y_train)

# predict on the testing data
y_pred = classifier.predict(X_test)

print "Prediction: \n", y_pred
print "Test input: \n", X_test
print "Expected output: \n", y_test
