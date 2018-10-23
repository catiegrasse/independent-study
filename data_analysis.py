from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
import pandas as pd
import numpy as np 


#input file should be a csv composed of feature and outcome columns with integer values
FILE_NAME = "testingProcessor.csv"


#col_names = ["Male", "Female", "White", "Black or African American", "Other", "Readmission"]
col_names = ["Age", "Sex", "Race", "Diabetes", "Readmission"]

#columns produced from csv_processor.py
SEX_COLUMNS = ["male", "female"]
RACE_COLUMNS = ["White", "Black or African American", "Unknown/Not Reported", "Asian", 
"Native Hawaiian or Pacific Islander", "American Indian or Alaska Native", "Other"]
COMORBIDITY_COLUMNS = []


#preliminary data analysis
diabetesPatientAges = []
nonDiabetesPatientAges = []
diabetesPatientGenders = []
nonDiabetesPatientGenders = []
diabetesPatientRaces = []
nonDiabetesPatientRaces = []

#group diabetes and non-diabetes patients together
numDiabetes = 0.0
numNonDiabetes = 0.0
with open(FILE_NAME, mode='r') as csv_file:
	for line in csv_file:
		line = line.split(",")
		if line[3] == "1":
			diabetesPatientAges.append(line[0])
			diabetesPatientGenders.append(line[1])
			diabetesPatientRaces.append(line[2])
			numDiabetes += 1
		else:
			nonDiabetesPatientAges.append(line[0])
			nonDiabetesPatientGenders.append(line[1])
			nonDiabetesPatientRaces.append(line[2])
			numNonDiabetes += 1

under40 = 0
above41less61 = 0
above61less81 = 0
above80 = 0
for val in diabetesPatientAges:
	if int(val) <= 40:
		under40 += 1
	elif int(val) <= 60:
		above41less61 += 1
	elif int(val) <= 80:
		above61less81 += 1
	else:
		above80 += 1

print len(diabetesPatientAges)
print under40
print "DM <= 40: ", under40/numDiabetes
print "DM 41 - 60: ", above41less61/numDiabetes
print "DM 61 - 80: ", above61less81/numDiabetes
print "DM > 80: ", above80/numDiabetes

under40 = 0
above41less61 = 0
above61less81 = 0
above80 = 0
for val in nonDiabetesPatientAges:
	if int(val) <= 40:
		under40 += 1
	elif int(val) <= 60:
		above41less61 += 1
	elif int(val) <= 80:
		above61less81 += 1
	else:
		above80 += 1

print "Non-DM <= 40: ", under40/numNonDiabetes
print "Non-DM 41 - 60: ", above41less61/numNonDiabetes
print "Non-DM 61 - 80: ", above61less81/numNonDiabetes
print "Non-DM > 80: ", above80/numNonDiabetes
print "Percent Male DM: ", sum([1 for item in diabetesPatientGenders if item == "1"])/numDiabetes
print "Percent Female DM: ", sum([1 for item in diabetesPatientGenders if item == "0"])/numDiabetes
print "Percent Male Non-DM: ", sum([1 for item in nonDiabetesPatientGenders if item == "1"])/numNonDiabetes
print "Percent Female Non-DM: ", sum([1 for item in nonDiabetesPatientGenders if item == "0"])/numNonDiabetes
print "Percent White DM: ", sum([1 for item in diabetesPatientRaces if item == "0"])/numDiabetes
print "Percent Black DM: ", sum([1 for item in diabetesPatientRaces if item == "1"])/numDiabetes
print "Percent Other DM: ", sum([1 for item in diabetesPatientRaces if item == "3"])/numDiabetes
print "Percent Unknown DM: ", sum([1 for item in diabetesPatientRaces if item == "2"])/numDiabetes
print "Percent White Non-DM: ", sum([1 for item in nonDiabetesPatientRaces if item == "0"])/numNonDiabetes
print "Percent Black Non-DM: ", sum([1 for item in nonDiabetesPatientRaces if item == "1"])/numNonDiabetes
print "Percent Other Non-DM: ", sum([1 for item in nonDiabetesPatientRaces if item == "3"])/numNonDiabetes
print "Percent Unknown Non-DM: ", sum([1 for item in nonDiabetesPatientRaces if item == "2"])/numNonDiabetes



