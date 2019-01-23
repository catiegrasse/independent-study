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
# Comprehensive ESS codes: ["31237", "31239", "31240", "31256", "31267", "31276", "31254", "31255", "31287", "31288"]

# possible filters
AGE_START = 0 # int
AGE_END = 100 # int
CPT_CODES = ["31237", "31239", "31240", "31256", "31267", "31276", "31254", "31255", "31287", "31288"] # lst
ICD_CODES = [] # lst

# open files and remove headers
f12 = open("acs_nsqip_puf12.txt", "rb")
f13 = open("acs_nsqip_puf13.txt", "rb")
f14 = open("acs_nsqip_puf14.txt", "rb")
f15 = open("acs_nsqip_puf15_v2.txt", "rb")
f16 = open("acs_nsqip_puf16.txt", "rb")

for line in f12:
    headers12 = line.split("\t")
    break

for line in f13:
    headers13 = line.split("\t")
    break

for line in f14:
    headers14 = line.split("\t")
    break

for line in f15:
    headers15 = line.split("\t")
    break

for line in f16:
    headers16 = line.split("\t")
    break


with open("filtered_csv12.csv", mode='wb') as filter_file12, open("filtered_csv13.csv", mode='wb') as filter_file13, open("filtered_csv14.csv", mode='wb') as filter_file14, open("filtered_csv15.csv", mode = 'wb') as filter_file15, open("filtered_csv16.csv", mode = 'wb') as filter_file16:
    
    csv_writer = csv.writer(filter_file12, delimiter=',')  
    csv_writer.writerow(headers12)

    recordCount = 0
    totalCount = 0
    for line in f12:
        totalCount += 1
        line = line.split("\t")

        # filter by CPT code
        if len(set(line).intersection(set(CPT_CODES))) > 0:

            # write to file
            print "WRITING TO FILE ", set(line).intersection(set(CPT_CODES))
            recordCount += 1
            csv_writer.writerow(line) 


    csv_writer = csv.writer(filter_file13, delimiter=',')  
    csv_writer.writerow(headers13)

    recordCount = 0
    totalCount = 0
    for line in f13:
        totalCount += 1
        line = line.split("\t")

        # filter by CPT code
        if len(set(line).intersection(set(CPT_CODES))) > 0:

            # write to file
            print "WRITING TO FILE ", set(line).intersection(set(CPT_CODES))
            recordCount += 1
            csv_writer.writerow(line)


    csv_writer = csv.writer(filter_file14, delimiter=',')  
    csv_writer.writerow(headers14)

    recordCount = 0
    totalCount = 0
    for line in f14:
        totalCount += 1
        line = line.split("\t")

        # filter by CPT code
        if len(set(line).intersection(set(CPT_CODES))) > 0:

            # write to file
            print "WRITING TO FILE ", set(line).intersection(set(CPT_CODES))
            recordCount += 1
            csv_writer.writerow(line)


    csv_writer = csv.writer(filter_file15, delimiter=',')
    csv_writer.writerow(headers15)
    for line in f15:
        totalCount += 1
        line = line.split("\t")

        # filter by CPT code
        if len(set(line).intersection(set(CPT_CODES))) > 0:

            # write to file
            print "WRITING TO FILE ", set(line).intersection(set(CPT_CODES))
            recordCount += 1
            csv_writer.writerow(line)


    csv_writer = csv.writer(filter_file16, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL) 
    csv_writer.writerow(headers16)
            
    for line in f16:
        totalCount += 1
        line = line.split("\t")
        
        # filter by CPT code
        if len(set(line).intersection(set(CPT_CODES))) > 0:

            # write to file
            print "WRITING TO FILE ", set(line).intersection(set(CPT_CODES))
            recordCount += 1
            csv_writer.writerow(line)

print "TOTAL NUMBER OF RECORDS PROCESSED: ", totalCount
print "NUMBER OF RECORDS ADDED: ", recordCount

