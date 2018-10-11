'''
Created on Oct 9, 2018

@author: catiegrasse
'''
import re

#Code to compute basic statistics from the NSQIP dataset

#global variables
INT_REGEX = "^[0-9]*$"
KEYS = ["male", "female"]

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
# 
#count number of records
#
# recordCount = 0
# for line in f14:
#     recordCount += 1
# 
# for line in f15:
#     recordCount += 1
# 
# for line in f16:
#     recordCount += 1
# 

#Find average age and sex breakdown

ageIndex14 = headers14.index("Age")
sexIndex14 = headers14.index("SEX")

ageIndex15 = headers15.index("Age")
sexIndex15 = headers15.index("SEX")

ageIndex16 = headers16.index("Age")
sexIndex16 = headers16.index("SEX")

intRegex = re.compile(INT_REGEX)

ageArray14 = []
sexDictionary14 = {key: 0 for key in KEYS}
for line in f14:
    age = line.split("\t")[ageIndex14]
    sex = line.split("\t")[sexIndex14].strip()
    if intRegex.match(age):
        ageArray14.append(int(age))
    if sex != "NULL":
        sexDictionary14[sex] += 1

print "2014 average age: ", sum(ageArray14)/(len(ageArray14) * 1.0)
print "% Males: ", sexDictionary14["male"]/(sexDictionary14["male"] + sexDictionary14["female"] * 1.0)
print "% Females: ", sexDictionary14["female"]/(sexDictionary14["male"] + sexDictionary14["female"] * 1.0)

ageArray15 = []
sexDictionary15 = {key: 0 for key in KEYS}
for line in f15:
    age = line.split("\t")[ageIndex15]
    sex = line.split("\t")[sexIndex15].strip()
    if intRegex.match(age):
        ageArray15.append(int(age))
    if sex != "NULL":
        sexDictionary15[sex] += 1

print "2015 average age: ", sum(ageArray15)/(len(ageArray15) * 1.0)
print "% Males: ", sexDictionary15["male"]/(sexDictionary15["male"] + sexDictionary15["female"] * 1.0)
print "% Females: ", sexDictionary15["female"]/(sexDictionary15["male"] + sexDictionary15["female"] * 1.0)
 
ageArray16 = []
sexDictionary16 = {key: 0 for key in KEYS}
for line in f16:
    age = line.split("\t")[ageIndex16]
    sex = line.split("\t")[sexIndex16].strip()
    if intRegex.match(age):
        ageArray16.append(int(age))
    if sex != "NULL":
        sexDictionary16[sex] += 1
 
print "2016 average age: ", sum(ageArray16)/(len(ageArray16) * 1.0)
print "% Males: ", sexDictionary16["male"]/(sexDictionary16["male"] + sexDictionary16["female"] * 1.0)
print "% Females: ", sexDictionary16["female"]/(sexDictionary16["male"] + sexDictionary16["female"] * 1.0)

totalAgeArray = ageArray14 + ageArray15 + ageArray16
print "Total average age: ", sum(totalAgeArray)/(len(totalAgeArray) * 1.0)
     
           
