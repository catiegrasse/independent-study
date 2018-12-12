from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
import pandas as pd
import numpy as np 
import math
import scipy

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

# function to calculate p-values
def calculate_p_value(successFeature, successNonFeature, numFeature, numNonFeature):
	#print(successFeature, successNonFeature, numFeature, numNonFeature)
	p_c = ((successFeature + successNonFeature)*1.0)/(numFeature + numNonFeature)
	#print("p_c", p_c)
	p_feature = successFeature*1.0/numFeature
	#print("p_feature", p_feature)
	p_nonFeature = successNonFeature*1.0/numNonFeature
	#print("p_nonFeature", p_nonFeature)
	z_numerator = (p_feature - p_nonFeature)
	#print("z_numerator", z_numerator)
	z_denominator = math.sqrt((p_c*(1-p_c)*1.0/numFeature) + (p_c*(1-p_c)*1.0/numNonFeature))
	#print("z_denominator", z_denominator)
	z_score = z_numerator/z_denominator
	#print("z_score", z_score)
	p_value = scipy.stats.norm.sf(abs(z_score))*2
	return p_value

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
print "\n"

numFeatureIP = sum([1 for x in listFeature if x[-1] == "1\r\n"])
numFeatureOP = sum([1 for x in listFeature if x[-1] != "1\r\n"])
numNonFeatureIP = sum([1 for x in listNonFeature if x[-1] == "1\r\n"])
numNonFeatureOP = sum([1 for x in listNonFeature if x[-1] != "1\r\n"])

print "Number of Inpatient Patients with " + feature, numFeatureIP
print "Number of Inpatient Patients without " + feature, numNonFeatureIP
print "Number of Outpatient Patients with " + feature, numFeatureOP
print "Number of Outpatient Patients without " + feature, numNonFeatureOP

for i in range(5, len(col_names) - 1):
	successFeature = sum([1 for x in listFeature if x[i] == "1"])*1.0
	successNonFeature = sum(1 for x in listNonFeature if x[i] == "1")*1.0
	if (successFeature != 0.0) or (successNonFeature != 0.0):
		pValue = calculate_p_value(successFeature, successNonFeature, numFeature, numNonFeature)
	else:
		pValue = "-"
	print "Number of " + feature + " Patients with " + col_names[i] + " ", successFeature/numFeature
	print "Number of non-" + feature + " Patients with " + col_names[i] + " ", successNonFeature/numNonFeature
	print "\n"

print("| | Non-" + feature + " (N = " + str(numNonFeature) + ") | " + feature + " (N = " + str(numFeature) + ") | p-value | ")
print ("| ------------- | ------------- | ------------- | ------------- |")
for i in range(5, len(col_names) - 1):
	successFeature = sum([1 for x in listFeature if x[i] == "1"])*1.0
	successNonFeature = sum(1 for x in listNonFeature if x[i] == "1")*1.0
	if (successFeature != 0.0) or (successNonFeature != 0.0):
		pValue = calculate_p_value(successFeature, successNonFeature, numFeature, numNonFeature)
	else:
		pValue = "-"
	print(" | " + col_names[i] + " | " + str((successNonFeature/numNonFeature)*100.0) + "% | " + str((successFeature/numFeature)*100.0) + "% | " + str(pValue) + " | ")

print("\n")


print("| | Outpatient Non-" + feature + " (N = " + str(numNonFeatureOP) + ") | Outpatient " + feature + " (N = " + str(numFeatureOP) + ") | p-value |" +
	" Inpatient Non-" + feature + " (N = " + str(numNonFeatureIP) + ") | Inpatient " + feature + " (N = " + str(numFeatureIP)) + ") | p-value |"
print("| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |")
for i in range(5, len(col_names) - 1):
	successNonFeatureOP = (sum([1 for x in listNonFeature if x[i] == "1" and x[-1] != "1\r\n"])*1.0)
	successFeatureOP = (sum([1 for x in listFeature if x[i] == "1" and x[-1] != "1\r\n"])*1.0)
	successNonFeatureIP = (sum([1 for x in listNonFeature if x[i] == "1" and x[-1] == "1\r\n"])*1.0)
	successFeatureIP = (sum([1 for x in listFeature if x[i] == "1" and x[-1] == "1\r\n"])*1.0)
	if (successFeatureOP != 0.0) or (successNonFeatureOP != 0.0):
		pValueOP = calculate_p_value(successFeatureOP, successNonFeatureOP, numFeatureOP, numNonFeatureOP)
	else:
		pValueOP = "-"
	if (successFeatureIP != 0.0) or (successNonFeatureIP != 0.0):
		pValueIP = calculate_p_value(successFeatureIP, successNonFeatureIP, numFeatureIP, numNonFeatureIP)
	else:
		pValueIP = "-"
	print(" | " + col_names[i] + " | " + str(successNonFeatureOP/numNonFeatureOP*100.0) + "% | " + str(successFeatureOP/numFeatureOP*100.0) + "% | " + str(pValueOP) + "|" + 
		str(successNonFeatureIP/numNonFeatureIP*100.0) + "% | " + str(successFeatureIP/numFeatureIP*100.0) + "% | " + str(pValueIP) + "|")



