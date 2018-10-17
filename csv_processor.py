'''
Created on Oct 9, 2018

@author: catiegrasse
'''

import re
import csv

# Code to convert NSQIP data to binary signals 

INT_REGEX = "^[0-9]*$"
READMISSION_REGEX = "^.*READM.*$"
REOPERATION_REGEX = "^.*REOP.*$"

# ["31237", "31256", "31267", "31254", "31255", "31287", "31288"] CPT codes for Polypectomoy/biopsy, Maxillary antrostomy,
# Ethmoidectomy, and Spehnoidotomy

# possible filters
AGE_START = 18 # int
AGE_END = 89 # int
CPT_CODES = ["31237", "31256", "31267", "31254", "31255", "31287", "31288"] # lst
ICD_CODES = [] # lst
SEX = ["male", "female"] # lst
FILE_NAME= "testingProcessor.csv"

# open files and remove headers
f14 = open("acs_nsqip_puf14.txt", "rb")
f15 = open("acs_nsqip_puf15_v2.txt", "rb")
f16 = open("acs_nsqip_puf16.txt", "rb")


for line in f14:
    headers14 = line.split("\t")
    break

for line in f15:
    headers15 = line.split("\t")
    break

for line in f16:
    headers16 = line.split("\t")
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

reoperationRegex = re.compile(REOPERATION_REGEX)
reoperationIndices14 = []
for i in range(len(headers14)):
    if reoperationRegex.match(headers14[i]):
        reoperationIndices14.append(i)

reoperationRegex = re.compile(REOPERATION_REGEX)
reoperationIndices15 = []
for i in range(len(headers15)):
    if reoperationRegex.match(headers15[i]):
        reoperationIndices15.append(i)

reoperationRegex = re.compile(REOPERATION_REGEX)
reoperationIndices16 = []
for i in range(len(headers16)):
    if reoperationRegex.match(headers16[i]):
        readmissionIndices16.append(i)

with open(FILE_NAME, mode='w') as filter_file:
    csv_writer = csv.writer(filter_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    # write headers to file
    
    ageIndex14 = headers14.index("Age")
    sexIndex14 = headers14.index("SEX")

    ageIndex15 = headers15.index("Age")
    sexIndex15 = headers15.index("SEX")

    ageIndex16 = headers16.index("Age")
    sexIndex16 = headers16.index("SEX")

    intRegex = re.compile(INT_REGEX)

    ageList = range(AGE_START, AGE_END + 1)
    ageArray14 = []
    sexDictionary14 = {key: 0 for key in SEX}
    recordCount = 0
    totalCount = 0
    for line in f14:
        line = line.split("\t")
        age = line[ageIndex14]
        sex = line[sexIndex14].strip()
        if sex == "male":
            maleBinary = 1
            femaleBinary = 0
        else:
            femaleBinary = 1
            maleBinary = 0
        
        readmissionResponses14 = [line[ind] for ind in readmissionIndices14]
        if "Yes" in readmissionResponses14:
            readmissionBinary = 1
        else:
            readmissionBinary = 0

            csv_writer.writerow([maleBinary, femaleBinary, readmissionBinary])

    for line in f15:
        line = line.split("\t")
        age = line[ageIndex15]
        if sex == "male":
            maleBinary = 1
            femaleBinary = 0
        else:
            femaleBinary = 1
            maleBinary = 0
        
        readmissionResponses15 = [line[ind] for ind in readmissionIndices15]
        if "Yes" in readmissionResponses15:
            readmissionBinary = 1
        else:
            readmissionBinary = 0

            csv_writer.writerow([maleBinary, femaleBinary, readmissionBinary])


    for line in f16:
        line = line.split("\t")
        age = line[ageIndex16]
        sex = line[sexIndex16].strip()
        if sex == "male":
            maleBinary = 1
            femaleBinary = 0
        else:
            femaleBinary = 1
            maleBinary = 0
        
        readmissionResponses16 = [line[ind] for ind in readmissionIndices16]
        if "Yes" in readmissionResponses16:
            readmissionBinary = 1
        else:
            readmissionBinary = 0

            csv_writer.writerow([maleBinary, femaleBinary, readmissionBinary])
