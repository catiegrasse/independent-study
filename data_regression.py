from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
import pandas as pd
import numpy as np 
import statsmodels.api as sm
import statsmodels.formula.api as smf

#input file should be a csv composed of feature and outcome columns with integer values
FILE_NAME = "testingProcessor.csv"


#col_names = ["Male", "Female", "White", "Black or African American", "Other", "Readmission"]
col_names = ["Age", "Sex", "Height", "Weight", "Race", "Diabetes", "Smoking", "Dyspnea", "Ventilator Dependent", 
"Ascites", "COPD", "Congestive Heart Failure", "Hypertension", "Acute Renal Failure", "Disseminated Cancer" ,
"Steroid", "Bleeding Disorder", "Functional Health Status", "Pneumonia", "Unplanned_Reintubation", 
"Urinary_Tract_Infection", "Ventilator", "Unplanned_Readmission", "Readmission"]
dataset = pd.read_csv(FILE_NAME, header=None, names=col_names)

feature_cols = ["Age", "Sex", "Height", "Weight", "Race", "Diabetes", "Smoking", "Dyspnea", "Hypertension"]

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

# predict on the testing data
y_pred = classifier.predict(X_test)


