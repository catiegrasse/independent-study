from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
import pandas as pd
import numpy as np 
import statsmodels.api as sm
import statsmodels.formula.api as smf
import math

#input file should be a csv composed of feature and outcome columns with integer values
FILE_NAME = "testingProcessor.csv"

OUTPUT_FILE_NAME = "output.csv"

f = open(OUTPUT_FILE_NAME, "w")


col_names = ["Age", "Sex", "Height", "Weight", "Race", "Diabetes", "Smoking", "Dyspnea", "Ventilator Dependent", 
"Ascites", "COPD", "Congestive Heart Failure", "Hypertension", "Acute Renal Failure", "Disseminated Cancer" ,
"Steroid", "Bleeding Disorder", "Functional Health Status", "Pneumonia", "Unplanned_Reintubation", 
"Urinary_Tract_Infection", "Ventilator", "Unplanned_Readmission"]
dataset = pd.read_csv(FILE_NAME, header=None, names=col_names)

outcome_cols = ["Pneumonia", "Unplanned_Reintubation", "Urinary_Tract_Infection", "Ventilator", "Unplanned_Readmission"]

feature_cols = ["Age", "Sex", "Height", "Weight", "Race", "Diabetes", "Smoking", "Dyspnea", "Ventilator Dependent",
"Ascites", "COPD", "Congestive Heart Failure", "Hypertension", "Acute Renal Failure", "Disseminated Cancer", 
"Steroid", "Bleeding Disorder"]

X = dataset[feature_cols]
y = dataset.Pneumonia

# split into training and testing sets
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25, random_state=0)

# train the classifier
classifier = LogisticRegression(random_state=0)
classifier.fit(X_train, y_train)

# testing out statsmodels library
logit_model=sm.Logit(y_train,X_train)
result=logit_model.fit(maxiter=200, method = 'nm')

print(result.summary())
f.write(result.summary().as_csv())
f.write("\n")
coefficients = result.params.values
for i in range(len(coefficients)):
	print("Odds ratio for " + feature_cols[i] + " = ", math.exp(coefficients[i]))
	f.write("Odds ratio for " + feature_cols[i] + " = " + str(math.exp(coefficients[i])) + "\n")

# predict on the testing data
y_pred = classifier.predict(X_test)

X = dataset[feature_cols]
y = dataset.Unplanned_Reintubation

# split into training and testing sets
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25, random_state=0)

# train the classifier
classifier = LogisticRegression(random_state=0)
classifier.fit(X_train, y_train)

# testing out statsmodels library
logit_model=sm.Logit(y_train,X_train)
result=logit_model.fit(maxiter=200, method = 'nm')

print(result.summary())
f.write(result.summary().as_csv())
f.write("\n")
coefficients = result.params.values
for i in range(len(coefficients)):
	print("Odds ratio for " + feature_cols[i] + " = ", math.exp(coefficients[i]))
	f.write("Odds ratio for " + feature_cols[i] + " = " + str(math.exp(coefficients[i])) + "\n")

# predict on the testing data
y_pred = classifier.predict(X_test)

X = dataset[feature_cols]
y = dataset.Urinary_Tract_Infection

# split into training and testing sets
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25, random_state=0)

# train the classifier
classifier = LogisticRegression(random_state=0)
classifier.fit(X_train, y_train)

# testing out statsmodels library
logit_model=sm.Logit(y_train,X_train)
result=logit_model.fit(maxiter=200, method = 'nm')

print(result.summary())
f.write(result.summary().as_csv())
f.write("\n")
coefficients = result.params.values
for i in range(len(coefficients)):
	print("Odds ratio for " + feature_cols[i] + " = ", math.exp(coefficients[i]))
	f.write("Odds ratio for " + feature_cols[i] + " = " + str(math.exp(coefficients[i])) + "\n")

# predict on the testing data
y_pred = classifier.predict(X_test)

X = dataset[feature_cols]
y = dataset.Ventilator

# split into training and testing sets
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25, random_state=0)

# train the classifier
classifier = LogisticRegression(random_state=0)
classifier.fit(X_train, y_train)

# testing out statsmodels library
logit_model=sm.Logit(y_train,X_train)
result=logit_model.fit(maxiter=400, method = 'nm')

print(result.summary())
f.write(result.summary().as_csv())
f.write("\n")
coefficients = result.params.values
for i in range(len(coefficients)):
	print("Odds ratio for " + feature_cols[i] + " = ", math.exp(coefficients[i]))
	f.write("Odds ratio for " + feature_cols[i] + " = " + str(math.exp(coefficients[i])) + "\n")

# predict on the testing data
y_pred = classifier.predict(X_test)

X = dataset[feature_cols]
y = dataset.Unplanned_Readmission

# split into training and testing sets
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25, random_state=0)

# train the classifier
classifier = LogisticRegression(random_state=0)
classifier.fit(X_train, y_train)

# testing out statsmodels library
logit_model=sm.Logit(y_train,X_train)
result=logit_model.fit(maxiter=400, method = 'nm')

print(result.summary())
f.write(result.summary().as_csv())
f.write("\n")
coefficients = result.params.values
for i in range(len(coefficients)):
	print("Odds ratio for " + feature_cols[i] + " = ", math.exp(coefficients[i]))
	f.write("Odds ratio for " + feature_cols[i] + " = " + str(math.exp(coefficients[i])) + "\n")

