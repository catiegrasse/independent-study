from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
import pandas as pd
import numpy as np 
import statsmodels.api as sm
import statsmodels.formula.api as smf
import math
import csv

#input file should be a csv composed of feature and outcome columns with integer values
FILE_NAME = "testingProcessor.csv"

OUTPUT_FILE_NAME = "output.csv"

f = open(OUTPUT_FILE_NAME, "w")


col_names = ["Age", "Sex", "Height", "Weight", "Race", "Diabetes", "Smoking", "Dyspnea", "Ventilator Dependent", 
"Ascites", "COPD", "Congestive Heart Failure", "Hypertension", "Acute Renal Failure", "Disseminated Cancer" ,
"Steroid", "Bleeding Disorder", "Functional Health Status", "Pneumonia", "Unplanned_Reintubation", 
"Urinary_Tract_Infection", "Ventilator", "Unplanned_Readmission"]

dataset = pd.read_csv(FILE_NAME, header=None, names=col_names, index_col = False)

outcome_cols = ["Pneumonia", "Unplanned_Reintubation", "Urinary_Tract_Infection", "Ventilator", "Unplanned_Readmission"]

#feature_cols = ["Age", "Sex", "Height", "Weight", "Race", "Diabetes", "Smoking", "Dyspnea", "Ventilator Dependent",
#"Ascites", "COPD", "Congestive Heart Failure", "Hypertension", "Acute Renal Failure", "Disseminated Cancer", 
#"Steroid", "Bleeding Disorder"]

feature_cols = ["Diabetes"]

X = dataset[feature_cols]
X = sm.add_constant(X)
y = dataset.Ventilator

#print (X.values)
print(X)
#print(y)

with open("testing_regression.csv", mode='wb') as csvFile:
	csv_writer = csv.writer(csvFile, delimiter=',')
	for row in X.values:
		csv_writer.writerow(row)

# testing out statsmodels library
logit_model=sm.Logit(y, X)
result=logit_model.fit(maxiter=200, method = 'nm')

print(result.summary())
f.write(result.summary().as_csv())
f.write("\n")
coefficients = result.params.values
for i in range(len(coefficients) - 1):
	print("Odds ratio for " + feature_cols[i] + " = ", math.exp(coefficients[i + 1]))
	f.write("Odds ratio for " + feature_cols[i] + " = " + str(math.exp(coefficients[i + 1])) + "\n")


