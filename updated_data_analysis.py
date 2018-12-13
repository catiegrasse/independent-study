from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
import pandas as pd
import numpy as np 
import math
import scipy
from math import log10, floor

#input file should be a csv composed of feature and outcome columns with integer value
#input file is generated from csv_processor.py
FILE_NAME = "testingProcessor.csv"

#columns of testingProcessor.csv
col_names = ["Age", "Sex", "Height", "Weight", "Race", "Diabetes", "Smoke", "Dyspnea", "Ventilator Dependent", "Ascites",
"COPD", "CGF", "Hypertension", "Acute Renal Failure", "Disseminated Cancer", "Steroid", "Bleeding Disorder", "Independent Functional Health Status",
"Totally or Partially Dependent Functional Health Status", "Pneumonia", "Reintubation", "Urinary Infection", "Ventilator", "Unplanned Readmission", "Readmission", "Superficial SSI", "Deep SSI",
"Organ/Space SSI", "Wound Disruption", "Deep Vein Thrombosis", "Renal Insufficiency", "Pulmonary Embolism", "CVA with Neurologic Deficit",
"Cardiac Arrest", "Myocardial Infarction", "Sepsis", "Inpatient"]

comorbidities = ["Diabetes", "Smoke", "Dyspnea", "Ventilator Dependent", "COPD", "Hypertension", "Disseminated Cancer", "Steroid", "Bleeding Disorder",
"Independent Functional Health Status", "Totally or Partially Dependent Functional Health Status"]
comorbidities_index = [col_names.index(val) for val in comorbidities]

surgical_complications = ["Superficial SSI", "Deep SSI", "Organ/Space SSI", "Wound Disruption"]
medical_complications = ["Pneumonia", "Reintubation", "Urinary Infection", "Deep Vein Thrombosis", "Renal Insufficiency",
"Pulmonary Embolism", "Ventilator Dependent", "Acute Renal Failure", "CVA with Neurologic Deficit", "Myocardial Infarction", "Sepsis"]
other_complications = ["Readmission", "Unplanned Readmission"]

all_complications = surgical_complications + medical_complications + other_complications
all_complications_index = [col_names.index(val) for val in all_complications]

features = ["Diabetes", "Smoke", "Hypertension", "Dyspnea", "COPD", "CGF", "Disseminated Cancer", "Steroid", "Bleeding Disorder",
"Independent Functional Health Status", "Totally or Partially Dependent Functional Health Status"]


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

def format(pValue):
	if pValue == "-":
		return pValue
	if pValue == 0:
		return str(0)
	if pValue < 0.05:
		return "**" + str(round_sig(pValue)) + "**"
	return str(round_sig(pValue))

def round_sig(x, sig=4):
	if x == 0:
		return 0
	return round(x, sig-int(floor(log10(abs(x))))-1)

for feature in features:

	with open(FILE_NAME, mode='r') as csv_file:
		for line in csv_file:
			line = line.split(",")
			if line[col_names.index(feature)] == "1":
				listFeature.append(line)
				numFeature += 1
			else:
				listNonFeature.append(line)
				numNonFeature += 1


	#print "Number of Patients with " + feature, numFeature
	#print "Number of Patients without " + feature, numNonFeature
	#print "\n"

	numFeatureIP = sum([1 for x in listFeature if x[-1] == "1\r\n"])
	numFeatureOP = sum([1 for x in listFeature if x[-1] != "1\r\n"])
	numNonFeatureIP = sum([1 for x in listNonFeature if x[-1] == "1\r\n"])
	numNonFeatureOP = sum([1 for x in listNonFeature if x[-1] != "1\r\n"])

	#print "Number of Inpatient Patients with " + feature, numFeatureIP
	#print "Number of Inpatient Patients without " + feature, numNonFeatureIP
	#print "Number of Outpatient Patients with " + feature, numFeatureOP
	#print "Number of Outpatient Patients without " + feature, numNonFeatureOP


	# print("| | Non-" + feature + " (N = " + str(numNonFeature) + ") | " + feature + " (N = " + str(numFeature) + ") | p-value | ")
	# print ("| ------------- | ------------- | ------------- | ------------- |")
	# for i in all_complications_index:
	# 	if col_names[i] != feature:
	# 		successFeature = sum([1 for x in listFeature if x[i] == "1"])*1.0
	# 		successNonFeature = sum(1 for x in listNonFeature if x[i] == "1")*1.0
	# 		if (successFeature != 0.0) or (successNonFeature != 0.0):
	# 			pValue = calculate_p_value(successFeature, successNonFeature, numFeature, numNonFeature)
	# 		else:
	# 			pValue = "-"
	# 		markdown = (" | " + col_names[i] + " | " + str(round_sig((successNonFeature/numNonFeature)*100.0)) + "% | " + str(round_sig((successFeature/numFeature)*100.0)) + "% | " + format(pValue) + " | ")
	# 		print(markdown)
	# print("\n")


	print("| | Outpatient Non-" + feature + " (N = " + str(numNonFeatureOP) + ") | Outpatient " + feature + " (N = " + str(numFeatureOP) + ") | p-value |" +
		" Inpatient Non-" + feature + " (N = " + str(numNonFeatureIP) + ") | Inpatient " + feature + " (N = " + str(numFeatureIP)) + ") | p-value |"
	print("| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |")
	for i in all_complications_index:
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
		if pValueIP < 0.05:
			markdown = (" | " + col_names[i] + " | " + "{0:.2f}".format(successNonFeatureOP/numNonFeatureOP*100.0) + "% | " + "{0:.2f}".format(successFeatureOP/numFeatureOP*100.0) + "% | " + format(pValueOP) + "|" + 
				"**" + "{0:.2f}".format(successNonFeatureIP/numNonFeatureIP*100.0) + "**" + "% | " + "**" + "{0:.2f}".format(successFeatureIP/numFeatureIP*100.0) + "**" + "% | " + format(pValueIP) + "|")
		else:
			markdown = (" | " + col_names[i] + " | " + "{0:.2f}".format(successNonFeatureOP/numNonFeatureOP*100.0) + "% | " + "{0:.2f}".format(successFeatureOP/numFeatureOP*100.0) + "% | " + format(pValueOP) + "|" + 
				 "{0:.2f}".format(successNonFeatureIP/numNonFeatureIP*100.0) + "% | "  + "{0:.2f}".format(successFeatureIP/numFeatureIP*100.0) + "% | " + format(pValueIP) + "|")
		print(markdown)
	print("\n")


