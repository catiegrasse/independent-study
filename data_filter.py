'''
Created on Oct 9, 2018

@author: catiegrasse
'''

import re
import csv

# Code to filter data from the NSQIP dataset
INT_REGEX = "^[0-9]*$"
READMISSION_REGEX = "^.*READM.*$"
REOPERATION_REGEX = "^.*REOP.*$"

# ["31237", "31256", "31267", "31254", "31255", "31287", "31288"] CPT codes for Polypectomoy/biopsy, Maxillary antrostomy,
# Ethmoidectomy, and Spehnoidotomy

# possible filters
AGE_START = 0 # int
AGE_END = 100 # int
CPT_CODES = ["31237", "31256", "31267", "31254", "31255", "31287", "31288"] # lst
ICD_CODES = [] # lst
SEX = ["male", "female"] # lst
FILTER_BY_READMISSION = False
FILTER_BY_REOPERATION = False

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
    
    ageIndex14 = headers14.index("Age")
    sexIndex14 = headers14.index("SEX")

    ageIndex15 = headers15.index("Age")
    sexIndex15 = headers15.index("SEX")

    ageIndex16 = headers16.index("Age")
    sexIndex16 = headers16.index("SEX")

    intRegex = re.compile(INT_REGEX)

    with open("filtered_csv14.csv", mode='w') as filter_file14:
        csv_writer14 = csv.writer(filter_file14, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
        # write headers to file
        csv_writer14.writerow(headers14)

        ageList = range(AGE_START, AGE_END + 1)
        ageArray14 = []
        sexDictionary14 = {key: 0 for key in SEX}
        recordCount = 0
        totalCount = 0
        for line in f14:
            totalCount += 1
            line = line.split("\t")
            age = line[ageIndex14]
            sex = line[sexIndex14].strip()
            # filter by age
            if intRegex.match(age) and AGE_START <= int(age) <= AGE_END:

                # filter by sex
                if sex in SEX:

                    # filter by CPT code
                    if len(set(line).intersection(set(CPT_CODES))) > 0:

                        if FILTER_BY_READMISSION is True:

                            # filter by readmission
                            readmissionResponses14 = [line[ind] for ind in readmissionIndices14]
                            if "Yes" in readmissionResponses14:

                                # write to file
                                print "WRITING TO FILE"
                                recordCount += 1
                                csv_writer14.writerow(line)
                                filter_file14.flush()

                        elif FILTER_BY_REOPERATION is True:

                            # filter by reoperation
                            reoperationResponses14 = [line[ind] for ind in reoperationIndices14]
                            if "Yes" in reoperationResponses14:

                                #write to file
                                print "WRITING TO FILE"
                                recordCount += 1
                                csv_writer14.writerow(line)
                                filter_file14.flush()

                        else:

                            # write to file
                            print "WRITING TO FILE"
                            recordCount += 1
                            csv_writer14.writerow(line)
                            filter_file14.flush()

        with open("filtered_csv15.csv", mode='w') as filter_file15:
            csv_writer15 = csv.writer(filter_file15, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
            csv_writer15.writerow(headers15)
            for line in f15:
                totalCount += 1
                line = line.split("\t")
                age = line[ageIndex15]
                sex = line[sexIndex15].strip()
                # filter by age
                if intRegex.match(age) and AGE_START <= int(age) <= AGE_END:
                    
                    # filter by sex
                    if sex in SEX:
                        
                        # filter by CPT code
                        if len(set(line).intersection(set(CPT_CODES))) > 0:

                            if FILTER_BY_READMISSION is True:

                                # filter by readmission
                                readmissionResponses15 = [line[ind] for ind in readmissionIndices15]
                                if "Yes" in readmissionResponses14:

                                    # write to file
                                    print "WRITING TO FILE"
                                    recordCount += 1
                                    csv_writer15.writerow(line)
                                    filter_file15.flush()

                            elif FILTER_BY_REOPERATION is True:

                                #filter by reoperation
                                reoperationResponses15 = [line[ind] for ind in reoperationIndices15]
                                if "Yes" in reoperationResponses15:

                                    #write to file
                                    print "WRITING TO FILE"
                                    recordCount += 1
                                    csv_writer15.writerow(line)
                                    filter_file15.flush()

                            else:

                                # write to file
                                print "WRITING TO FILE"
                                recordCount += 1
                                csv_writer15.writerow(line)
                                filter_file15.flush()

        with open("filtered_csv16.csv", mode='w') as filter_file16:
            csv_writer16 = csv.writer(filter_file16, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer16.writerow(headers16)
            
            for line in f16:
                totalCount += 1
                line = line.split("\t")
                age = line[ageIndex16]
                sex = line[sexIndex16].strip()
                # filter by age
                if intRegex.match(age) and AGE_START <= int(age) <= AGE_END:
                    
                    # filter by sex
                    if sex in SEX:
                        
                        # filter by CPT code
                        if len(set(line).intersection(set(CPT_CODES))) > 0:

                            if FILTER_BY_READMISSION is True:

                                # filter by readmission
                                readmissionResponses16 = [line[ind] for ind in readmissionIndices16]
                                if "Yes" in readmissionResponses16:

                                    # write to file
                                    print "WRITING TO FILE"
                                    recordCount += 1
                                    csv_writer16.writerow(line)
                                    filter_file16.flush()

                            elif FILTER_BY_REOPERATION is True:

                                #filter by reoperation
                                reoperationResponses16 = [line[ind] for ind in reoperationIndices16]
                                if "Yes" in reoperationResponses16:

                                    # write to file
                                    print "WRITING TO FILE"
                                    recordCount += 1
                                    csv_writer16.writerow(line)
                                    filter_file16.flush()

                            else:

                                # write to file
                                print "WRITING TO FILE"
                                recordCount += 1
                                csv_writer16.writerow(line)
                                filter_file16.flush()
