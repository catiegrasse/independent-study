'''
Created on Oct 9, 2018

@author: catiegrasse
'''
import re
import csv

#Code to compute basic statistics from the NSQIP dataset
INT_REGEX = "^[0-9]*$"

#["31237", "31256", "31267", "31254", "31255", "31287", "31288"] CPT codes for Polypectomoy/biopsy, Maxillary antrostomy,
#Ethmoidectomy, and Spehnoidotomy

#possible filters
AGE_START = 0 #int
AGE_END = 30 #int
CPT_CODES = ["31237", "31256", "31267", "31254", "31255", "31287", "31288"] #lst
ICD_CODES = [] #lst
SEX = ["male", "female"] #lst
FILE_NAME= "testingFilter.csv"

#open files and remove headers
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

with open(FILE_NAME, mode='w') as filter_file:
    csv_writer = csv.writer(filter_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    #write headers to file 
    csv_writer.writerow(headers14)
    
    ageIndex14 = headers14.index("Age")
    sexIndex14 = headers14.index("SEX")
    
    ageIndex15 = headers15.index("Age")
    sexIndex15 = headers15.index("SEX")
    
    ageIndex16 = headers16.index("Age")
    sexIndex16 = headers16.index("SEX")
    
    intRegex = re.compile(INT_REGEX)
    
    ageArray14 = []
    sexDictionary14 = {key: 0 for key in SEX}
    for line in f14:
        line = line.split("\t")
        age = line[ageIndex14]
        sex = line[sexIndex14].strip()
        #filter by age
        if intRegex.match(age) and AGE_START < int(age) < AGE_END :

            #filter by sex
            if sex in SEX:

                #filter by CPT code
                if len(set(line).intersection(set(CPT_CODES))) > 0:
                    
                    #write to file
                    csv_writer.writerow(line)

    csv_writer.writerow(headers15)
    for line in f15:
        line = line.split("\t")
        age = line[ageIndex15]
        sex = line[sexIndex15].strip()
        #filter by age
        if intRegex.match(age) and AGE_START < int(age) < AGE_END :
            
            #filter by sex
            if sex in SEX:
                
                #filter by CPT code
                if len(set(line).intersection(set(CPT_CODES))) > 0:
                    
                    #write to file
                    csv_writer.writerow(line)

    csv_writer.writerow(headers16)
    for line in f16:
        line = line.split("\t")
        age = line[ageIndex16]
        sex = line[sexIndex16].strip()
        #filter by age
        if intRegex.match(age) and AGE_START < int(age) < AGE_END :
            
            #filter by sex
            if sex in SEX:
                
                #filter by CPT code
                if len(set(line).intersection(set(CPT_CODES))) > 0:
                    
                    #write to file
                    csv_writer.writerow(line)
               
