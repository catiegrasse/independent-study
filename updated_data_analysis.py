from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
import pandas as pd
import numpy as np 


#input file should be a csv composed of feature and outcome columns with integer value
#input file is generated from csv_processor.py
FILE_NAME = "testingProcessor.csv"

#columns of testingProcessor.csv
col_names = ["Age", "Sex", "Height", "Weight", "Race", "Diabetes", "Smoke", "Dyspnea", "Ventilator Dependent", "Ascites",
"COPD", "CGF", "Hypertension", "Acute Renal Failure", "Disseminated Cancer", "Steroid", "Bleeding Disorder", "Functional Health Status",
"Pneumonia", "Reintubation", "Urinary Infection", "Ventilator", "Unplanned Readmission", "Readmission", "Superficial SSI", "Deep SSI",
"Organ/Space SSI", "Wound Disruption", "Deep Vein Thrombosis", "Renal Insufficiency", "Pulmonary Embolism", "CVA with Neurologic Deficit",
"Cardiac Arrest", "Myocardial Infarction", "Sepsis", "Inpatient"]

#Set the feature you are interested in studying
feature = "Diabetes"

#Count 
numFeature = 0.0
numNonFeature = 0.0

#List of all entries
listFeature = []
listNonFeature = []

with open(FILE_NAME, mode='r') as csv_file:
	for line in csv_file:
		line = line.split(",")
		if line[col_names.index(feature)] == "1":
			listFeature.append(line)
			numFeature += 1
		else:
			listNonFeature.append(line)
			numNonFeature += 1

print "Number of Patients with " + feature, numFeature
print "Number of Patients without " + feature, numNonFeature

for i in range(5, len(col_names) - 1):
	print "Number of " + feature + " Patients with " + col_names[i] + " ", sum([1 for x in listFeature if x[i] == "1"])*1.0/numFeature
	print "Number of non-" + feature + " Patients with " + col_names[i] + " ", sum(1 for x in listNonFeature if x[i] == "1")*1.0/numNonFeature
	print "\n"

print "DIVIDING BY INPATIENT AND OUTPATIENT"

for i in range(5, len(col_names) - 1):
	print "INPATIENT: Number of " + feature + " Patients with " + col_names[i] + " ", sum([1 for x in listFeature if x[i] == "1" and x[col_names.index("Inpatient")] == "1\r\n"])*1.0/numFeature
	print "OUTPATIENT: Number of " + feature + " Patients with " + col_names[i] + " ", sum([1 for x in listFeature if x[i] == "1" and x[col_names.index("Inpatient")] == "0\r\n"])*1.0/numFeature
	print("\n")
	print "INPATIENT: Number of non-" + feature + " Patients with " + col_names[i] + " ", sum(1 for x in listNonFeature if x[i] == "1" and x[col_names.index("Inpatient")] == "1\r\n")*1.0/numNonFeature
	print "OUTPATIENT: Number of non-" + feature + " Patients with " + col_names[i] + " ", sum(1 for x in listNonFeature if x[i] == "1" and x[col_names.index("Inpatient")] == "0\r\n")*1.0/numNonFeature
	print("\n")

print "TESTING"
print listFeature[1]

