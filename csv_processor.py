'''
Created on Oct 9, 2018

@author: catiegrasse
'''

import re
import csv

# Code to convert NSQIP data to binary signals 

# ["31237", "31256", "31267", "31254", "31255", "31287", "31288"] CPT codes for Polypectomoy/biopsy, Maxillary antrostomy,
# Ethmoidectomy, and Spehnoidotomy

INT_REGEX = "^[0-9]*$"
READMISSION_REGEX = "^.*READM.*$"
REOPERATION_REGEX = "^.*REOP.*$"
DIABETES_REGEX = "(^250)|(^E11)"
NEGATIVE_REOPERATION_VALUES = ["NULL", "-99", "No"]
POLYPECTOMY_BIOPSY_CPT = ["31237"]
OTHER_ESS_CPT = ["31237", "31239", "31240", "31276", "31256", "31267", "31254", "31255", "31287", "31288"]
FEATURE_COLUMNS = ["male", "female", "White", "Black or African American", "Asian", 
"Native Hawaiian or Pacific Islander", "American Indian or Alaska Native", "Unknown/Not Reported", "Other",
"Diabetes"]


FILE_NAME= "testingProcessor.csv"

# open files and remove headers
csv_reader14 = csv.reader(open("filtered_csv14.csv"))
csv_reader15 = csv.reader(open("filtered_csv15.csv"))
csv_reader16 = csv.reader(open("filtered_csv16.csv"))


for row in csv_reader14:
    headers14 = row
    break

for row in csv_reader15:
    headers15 = row
    break

for row in csv_reader16:
    headers16 = row
    break

readmissionRegex = re.compile(READMISSION_REGEX)
readmissionIndices14 = []
for i in range(len(headers14)):
    if readmissionRegex.match(headers14[i]):
        readmissionIndices14.append(i)

readmissionRegex = re.compile(READMISSION_REGEX)
readmissionIndices15 = []
for i in range(len(headers15)):
    if readmissionRegex.match(headers15[i]):
        readmissionIndices15.append(i)

readmissionRegex = re.compile(READMISSION_REGEX)
readmissionIndices16 = []
for i in range(len(headers16)):
    if readmissionRegex.match(headers16[i]):
        readmissionIndices16.append(i)

# count number of patients with specified icd 
icdCount = 0

with open(FILE_NAME, mode='w') as filter_file:
    csv_writer = csv.writer(filter_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    ageIndex16 = headers16.index("Age")
    sexIndex16 = headers16.index("SEX")
    raceIndex16 = headers16.index("RACE_NEW")

    intRegex = re.compile(INT_REGEX)

    for row in csv_reader14:
        features = []
        age = row[headers14.index("Age")]
        sex = FEATURE_COLUMNS.index(row[headers14.index("SEX")])
        race = FEATURE_COLUMNS.index(row[headers14.index("RACE_NEW")])
        diabetes = 0
        for item in row:
            if re.compile(DIABETES_REGEX).match(item):
                print row
                icdCount += 1
                diabetes = 1
        readmissionResponses14 = [row[ind] for ind in readmissionIndices14 if row[ind] not in NEGATIVE_REOPERATION_VALUES]
        if len(readmissionResponses14) > 0:
            newRow = [age, sex, race, diabetes, 1] 
            csv_writer.writerow(newRow)
        else:
            newRow = [age, sex, race, diabetes, 0]
            csv_writer.writerow(newRow)

    for row in csv_reader15:
        age = row[headers15.index("Age")]
        sex = FEATURE_COLUMNS.index(row[headers15.index("SEX")])
        race = FEATURE_COLUMNS.index(row[headers15.index("RACE_NEW")])
        diabetes = 0
        for item in row:
            if re.compile(DIABETES_REGEX).match(item):
                print row
                icdCount += 1
                diabetes = 1
        readmissionResponses15 = [row[ind] for ind in readmissionIndices15 if row[ind] not in NEGATIVE_REOPERATION_VALUES]
        if len(readmissionResponses15) > 0:
            newRow = [age, sex, race, diabetes, 1] 
            csv_writer.writerow(newRow)

        else:
            newRow = [age, sex, race, diabetes, 0] 
            csv_writer.writerow(newRow)


    for row in csv_reader16:
        age = row[headers16.index("Age")]
        sex = FEATURE_COLUMNS.index(row[headers16.index("SEX")])
        race = FEATURE_COLUMNS.index(row[headers16.index("RACE_NEW")])
        diabetes = 0
        for item in row:
            if re.compile(DIABETES_REGEX).match(item):
                print row
                icdCount += 1
                diabetes = 1
        readmissionResponses16 = [row[ind] for ind in readmissionIndices16 if row[ind] not in NEGATIVE_REOPERATION_VALUES]
        if len(readmissionResponses16) > 0:
            newRow = [age, sex, race, diabetes, 1] 
            csv_writer.writerow(newRow)
        else:
            newRow = [age, sex, race, diabetes, 0] 
            csv_writer.writerow(newRow)

print "Total number of records with diabetes ICD code: ", icdCount