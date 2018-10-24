'''
Created on Oct 9, 2018

@author: catiegrasse
'''

import re
import csv
import math

# Code to convert NSQIP data to binary signals 

# ["31237", "31256", "31267", "31254", "31255", "31287", "31288"] CPT codes for Polypectomoy/biopsy, Maxillary antrostomy,
# Ethmoidectomy, and Spehnoidotomy

READMISSION_REGEX = "^.*READM.*$"
UNPLANNED_READMISSION_REGEX = "^.*UNPLANNEDREADMISSION.*$"
REOPERATION_REGEX = "^.*REOP.*$"
NEGATIVE_REOPERATION_VALUES = ["NULL", "-99", "No"]
POLYPECTOMY_BIOPSY_CPT = ["31237"]
OTHER_ESS_CPT = ["31237", "31239", "31240", "31276", "31256", "31267", "31254", "31255", "31287", "31288"]
SEX_COLUMNS = ["male", "female"]
RACE_COLUMNS = ["White", "Black or African American", "Unknown/Not Reported"]
COMORBIDITY_COLUMNS = ["SMOKE", "DYSPNEA", "HYPERMED"]


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

unplannedReadmissionRegex = re.compile(UNPLANNED_READMISSION_REGEX)
unplannedReadmissionIndices14 = []
for i in range(len(headers14)):
    if unplannedReadmissionRegex.match(headers14[i]):
        unplannedReadmissionIndices14.append(i)

unplannedReadmissionRegex = re.compile(UNPLANNED_READMISSION_REGEX)
unplannedReadmissionIndices15 = []
for i in range(len(headers15)):
    if unplannedReadmissionRegex.match(headers15[i]):
        unplannedReadmissionIndices15.append(i)

unplannedReadmissionRegex = re.compile(UNPLANNED_READMISSION_REGEX)
unplannedReadmissionIndices16 = []
for i in range(len(headers16)):
    if unplannedReadmissionRegex.match(headers16[i]):
        unplannedReadmissionIndices16.append(i)

# count number of patients with specified icd 
icdCount = 0

with open(FILE_NAME, mode='w') as filter_file:
    csv_writer = csv.writer(filter_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    ageIndex16 = headers16.index("Age")
    sexIndex16 = headers16.index("SEX")
    raceIndex16 = headers16.index("RACE_NEW")

    for row in csv_reader14:
        features = []
        age = row[headers14.index("Age")]
        sex = SEX_COLUMNS.index(row[headers14.index("SEX")])

        #create an other category
        if row[headers14.index("RACE_NEW")] not in RACE_COLUMNS:
            race = len(RACE_COLUMNS)
        else:
            race = RACE_COLUMNS.index(row[headers14.index("RACE_NEW")])

        diabetes = 0
        if row[headers14.index("DIABETES")] != "NO" and row[headers14.index("DIABETES")] != "NULL":
            icdCount += 1
            diabetes = 1

        smoke = 0
        if row[headers14.index("SMOKE")] == "Yes":
            smoke = 1

        dyspnea = 0
        if row[headers14.index("DYSPNEA")] != "No" and row[headers14.index("DYSPNEA") != "NULL"]:
            dyspnea = 1

        hypertension = 0
        if row[headers14.index("HYPERMED")] == "Yes":
            hypertension = 1

        readmission = 0
        readmissionResponses14 = [row[ind] for ind in readmissionIndices14 if row[ind] == "Yes"]
        if len(readmissionResponses14) > 0:
            readmission = 1

        unplannedReadmission = 0
        unplannedReadmissionResponses14 = [row[ind] for ind in unplannedReadmissionIndices14 if row[ind] == "Yes"]
        if len(unplannedReadmissionResponses14) > 0:
            unplannedReadmission = 1
        
        newRow = [age, sex, race, diabetes, smoke, dyspnea, hypertension, unplannedReadmission, readmission] 
        csv_writer.writerow(newRow)

    for row in csv_reader15:
        age = row[headers15.index("Age")]
        sex = SEX_COLUMNS.index(row[headers15.index("SEX")])

        #create an other category
        if row[headers15.index("RACE_NEW")] not in RACE_COLUMNS:
            race = len(RACE_COLUMNS)
        else:
            race = RACE_COLUMNS.index(row[headers15.index("RACE_NEW")])

        diabetes = 0
        if row[headers15.index("DIABETES")] != "NO" and row[headers15.index("DIABETES")] != "NULL":
            icdCount += 1
            diabetes = 1

        smoke = 0
        if row[headers15.index("SMOKE")] == "Yes":
            smoke = 1

        dyspnea = 0
        if row[headers15.index("DYSPNEA")] != "No" and row[headers15.index("DYSPNEA") != "NULL"]:
            dyspnea = 1

        hypertension = 0
        if row[headers15.index("HYPERMED")] == "Yes":
            hypertension = 1

        readmission = 0
        readmissionResponses15 = [row[ind] for ind in readmissionIndices15 if row[ind] == "Yes"]
        if len(readmissionResponses15) > 0:
            readmission = 1

        unplannedReadmission = 0
        unplannedReadmissionResponses15 = [row[ind] for ind in unplannedReadmissionIndices15 if row[ind] == "Yes"]
        if len(unplannedReadmissionResponses15) > 0:
            unplannedReadmission = 1

        newRow = [age, sex, race, diabetes, smoke, dyspnea, hypertension, unplannedReadmission, readmission] 
        csv_writer.writerow(newRow)

    for row in csv_reader16:
        age = row[headers16.index("Age")]
        sex = SEX_COLUMNS.index(row[headers16.index("SEX")])

        #create an other category
        if row[headers16.index("RACE_NEW")] not in RACE_COLUMNS:
            race = len(RACE_COLUMNS)
        else:
            race = RACE_COLUMNS.index(row[headers16.index("RACE_NEW")])

        diabetes = 0
        if row[headers16.index("DIABETES")] != "NO" and row[headers16.index("DIABETES")] != "NULL":
            icdCount += 1
            diabetes = 1

        smoke = 0
        if row[headers16.index("SMOKE")] == "Yes":
            smoke = 1

        dyspnea = 0
        if row[headers16.index("DYSPNEA")] != "No" and row[headers16.index("DYSPNEA") != "NULL"]:
            dyspnea = 1

        hypertension = 0
        if row[headers16.index("HYPERMED")] == "Yes":
            hypertension = 1

        readmission = 0
        readmissionResponses16 = [row[ind] for ind in readmissionIndices16 if row[ind] == "Yes"]
        if len(readmissionResponses16) > 0:
            readmission = 1

        unplannedReadmission = 0
        unplannedReadmissionResponses16 = [row[ind] for ind in unplannedReadmissionIndices16 if row[ind] == "Yes"]
        if len(unplannedReadmissionResponses16) > 0:
            unplannedReadmission = 1

        newRow = [age, sex, race, diabetes, smoke, dyspnea, hypertension, unplannedReadmission, readmission] 
        csv_writer.writerow(newRow)

print "Total number of records with diabetes ICD code: ", icdCount
