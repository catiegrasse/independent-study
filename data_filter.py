'''
Created on Oct 9, 2018

@author: catiegrasse
'''

import re
import csv

# Code to filter data from the NSQIP dataset

# ["31237", "31256", "31267", "31254", "31255", "31287", "31288"] CPT codes for Polypectomoy/biopsy, Maxillary antrostomy,
# Ethmoidectomy, and Spehnoidotomy
# Comprehensive ESS codes: ["31237", "31239", "31240", "31256", "31267", "31276", "31254", "31255", "31287", "31288"]

# possible filters
CPT_CODES = ["31237", "31239", "31240", "31256", "31267", "31276", "31254", "31255", "31287", "31288"] # lst

# open files and remove headers
f6 = open("ACS_NSQIP_PUF_05_06_vr1.txt", "rb")
f7 = open("ACS_NSQIP_PUF07_TXT.txt", "rb")
f8 = open("ACS_NSQIP_PUF08_TXT.txt", "rb")
f9 = open("ACS_NSQIP_PUF09_TXT.txt", "rb")
f10 = open("ACS_NSQIP_PUF10_TXT.txt", "rb")
f11 = open("ACS_NSQIP_PUF11_TXT.txt", "rb")
f12 = open("acs_nsqip_puf12.txt", "rb")
f13 = open("acs_nsqip_puf13.txt", "rb")
f14 = open("acs_nsqip_puf14.txt", "rb")
f15 = open("acs_nsqip_puf15_v2.txt", "rb")
f16 = open("acs_nsqip_puf16.txt", "rb")

for line in f6:
    headers6 = line.split("\t")
    break

for line in f7:
    headers7 = line.split("\t")
    break

for line in f8:
    headers8 = line.split("\t")
    break

for line in f9:
    headers9 = line.split("\t")
    break

for line in f10:
    headers10 = line.split("\t")
    break

for line in f11:
    headers11 = line.split("\t")
    break

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


with open("filtered_csv6.csv", mode = 'wb') as filter_file6, open("filtered_csv7.csv", mode = 'wb') as filter_file7, open("filtered_csv8.csv", mode = 'wb') as filter_file8, open("filtered_csv9.csv", mode = 'wb') as filter_file9, open("filtered_csv10.csv", mode = 'wb') as filter_file10, open("filtered_csv11.csv", mode = 'wb') as filter_file11, open("filtered_csv12.csv", mode='wb') as filter_file12, open("filtered_csv13.csv", mode='wb') as filter_file13, open("filtered_csv14.csv", mode='wb') as filter_file14, open("filtered_csv15.csv", mode = 'wb') as filter_file15, open("filtered_csv16.csv", mode = 'wb') as filter_file16:
    
    csv_writer = csv.writer(filter_file6, delimiter=',')  
    csv_writer.writerow(headers6)

    recordCount = 0
    totalCount = 0
    for line in f6:
        totalCount += 1
        line = line.split("\t")

        # filter by CPT code
        if len(set(line).intersection(set(CPT_CODES))) > 0:

            # write to file
            print "WRITING TO FILE ", set(line).intersection(set(CPT_CODES))
            recordCount += 1

    csv_writer = csv.writer(filter_file7, delimiter=',')  
    csv_writer.writerow(headers7)

    for line in f7:
        totalCount += 1
        line = line.split("\t")

        # filter by CPT code
        if len(set(line).intersection(set(CPT_CODES))) > 0:

            # write to file
            print "WRITING TO FILE ", set(line).intersection(set(CPT_CODES))
            recordCount += 1

    csv_writer = csv.writer(filter_file8, delimiter=',')  
    csv_writer.writerow(headers8)

    for line in f8:
        totalCount += 1
        line = line.split("\t")

        # filter by CPT code
        if len(set(line).intersection(set(CPT_CODES))) > 0:

            # write to file
            print "WRITING TO FILE ", set(line).intersection(set(CPT_CODES))
            recordCount += 1

    csv_writer = csv.writer(filter_file9, delimiter=',')  
    csv_writer.writerow(headers9)

    for line in f9:
        totalCount += 1
        line = line.split("\t")

        # filter by CPT code
        if len(set(line).intersection(set(CPT_CODES))) > 0:

            # write to file
            print "WRITING TO FILE ", set(line).intersection(set(CPT_CODES))
            recordCount += 1

    csv_writer = csv.writer(filter_file10, delimiter=',')  
    csv_writer.writerow(headers10)

    for line in f10:
        totalCount += 1
        line = line.split("\t")

        # filter by CPT code
        if len(set(line).intersection(set(CPT_CODES))) > 0:

            # write to file
            print "WRITING TO FILE ", set(line).intersection(set(CPT_CODES))
            recordCount += 1
            csv_writer.writerow(line) 

    csv_writer = csv.writer(filter_file11, delimiter=',')  
    csv_writer.writerow(headers11)

    for line in f11:
        totalCount += 1
        line = line.split("\t")

        # filter by CPT code
        if len(set(line).intersection(set(CPT_CODES))) > 0:

            # write to file
            print "WRITING TO FILE ", set(line).intersection(set(CPT_CODES))
            recordCount += 1
            csv_writer.writerow(line) 

    csv_writer = csv.writer(filter_file12, delimiter=',')  
    csv_writer.writerow(headers12)

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

