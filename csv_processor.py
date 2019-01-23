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
OUTCOME_COLUMNS = ["OUPNEUMO", "REINTUB", "URNINFEC", "FAILWEAN"]


FILE_NAME= "testingProcessor.csv"

# open files and remove headers
csv_reader12 = csv.reader(open("filtered_csv12.csv"))
csv_reader13 = csv.reader(open("filtered_csv13.csv"))
csv_reader14 = csv.reader(open("filtered_csv14.csv"))
csv_reader15 = csv.reader(open("filtered_csv15.csv"))
csv_reader16 = csv.reader(open("filtered_csv16.csv"))

CSV_READER_LIST = [csv_reader12, csv_reader13, csv_reader14, csv_reader15, csv_reader16]
HEADERSLIST = [[]]*len(CSV_READER_LIST)

READMISSION_LIST = [[]]*len(CSV_READER_LIST)
UNPLANNED_READMISSION_LIST = [[]]*len(CSV_READER_LIST)

for i in range(len(CSV_READER_LIST)):
    for row in CSV_READER_LIST[i]:
        HEADERSLIST[i] = [x.upper() for x in row]
        break

readmissionRegex = re.compile(READMISSION_REGEX)

for i in range(len(HEADERSLIST)):
    readmissionIndices = []
    for j in range(len(HEADERSLIST[i])):
        if readmissionRegex.match(HEADERSLIST[i][j]):
            readmissionIndices.append(j)
    READMISSION_LIST[i].append(readmissionIndices)

unplannedReadmissionRegex = re.compile(UNPLANNED_READMISSION_REGEX)

for i in range(len(UNPLANNED_READMISSION_LIST)):
    for j in range(len(HEADERSLIST[i])):
        if unplannedReadmissionRegex.match(HEADERSLIST[i][j]):
            UNPLANNED_READMISSION_LIST[i].append(j)


# count number of patients with specified icd 
icdCount = 0

with open(FILE_NAME, mode='w') as filter_file:
    csv_writer = csv.writer(filter_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for i in range(len(HEADERSLIST)):
        csv_reader = CSV_READER_LIST[i]
        for row in csv_reader:
            
            age = row[HEADERSLIST[i].index("AGE")]
            sex = SEX_COLUMNS.index(row[HEADERSLIST[i].index("SEX")])
            height = row[HEADERSLIST[i].index("HEIGHT")]
            weight = row[HEADERSLIST[i].index("WEIGHT")]

            #create an other category
            if row[HEADERSLIST[i].index("RACE_NEW")] not in RACE_COLUMNS:
                race = len(RACE_COLUMNS)
            else:
                race = RACE_COLUMNS.index(row[HEADERSLIST[i].index("RACE_NEW")])

            diabetes = 0
            if row[HEADERSLIST[i].index("DIABETES")] != "NO" and row[HEADERSLIST[i].index("DIABETES")] != "NULL":
                diabetes = 1

            smoke = 0
            if row[HEADERSLIST[i].index("SMOKE")] == "Yes":
                smoke = 1

            dyspnea = 0
            if row[HEADERSLIST[i].index("DYSPNEA")] != "No" and row[HEADERSLIST[i].index("DYSPNEA") != "NULL"]:
                dyspnea = 1

            ventilator_dependent = 0
            if row[HEADERSLIST[i].index("VENTILAT")] == "Yes":
                ventilator_dependent = 1

            ascites = 0
            if row[HEADERSLIST[i].index("ASCITES")] == "Yes":
                ascites = 1

            copd = 0
            if row[HEADERSLIST[i].index("HXCOPD")] == "Yes":
                copd = 1

            cgf = 0
            if row[HEADERSLIST[i].index("HXCHF")] == "Yes":
                chf = 1

            hypertension = 0
            if row[HEADERSLIST[i].index("HYPERMED")] == "Yes":
                hypertension = 1

            acute_renal_failure = 0
            if row[HEADERSLIST[i].index("RENAFAIL")] == "Yes":
                acute_renal_failure = 1

            disseminated_cancer = 0
            if row[HEADERSLIST[i].index("DISCANCR")] == "Yes":
                disseminated_cancer = 1

            steroid = 0
            if row[HEADERSLIST[i].index("STEROID")] == "Yes":
                steroid = 1

            bleeding_disorder = 0
            if row[HEADERSLIST[i].index("BLEEDDIS")] == "Yes":
                bleeding_disorder = 1

            independent_functional_health_status = 0
            if row[HEADERSLIST[i].index("FNSTATUS2")] == "Independent":
                independent_functional_health_status = 1

            not_independent_functional_health_status = 0
            if row[HEADERSLIST[i].index("FNSTATUS2")] == "Partially Dependent" or row[HEADERSLIST[i].index("FNSTATUS2")] == "Totally Dependent":
                not_independent_functional_health_status = 1

            pneumonia = 0
            if row[HEADERSLIST[i].index("OUPNEUMO")] == "Pneumonia":
                pneumonia = 1

            reintubation = 0
            if row[HEADERSLIST[i].index("REINTUB")] == "Unplanned Intubation":
                reintubation = 1

            urinaryInfection = 0
            if row[HEADERSLIST[i].index("URNINFEC")] == "Urinary Tract Infection":
                urinaryInfection = 1

            ventilator = 0
            if row[HEADERSLIST[i].index("FAILWEAN")] == "On Ventilator greater than 48 Hours":
                ventilator = 1

            readmission = 0
            print(READMISSION_LIST[i])
            print(READMISSION_LIST)
            print(len(row))
            readmissionResponses = [row[ind] for ind in READMISSION_LIST[i] if row[ind] == "Yes"]
            if len(readmissionResponses) > 0:
                readmission = 1

            unplannedReadmission = 0
            unplannedReadmissionResponses = [row[ind] for ind in UNPLANNED_READMISSION_LIST[i] if row[ind] == "Yes"]
            if len(unplannedReadmissionResponses) > 0:
                unplannedReadmission = 1

            supInfec = 0
            if row[HEADERSLIST[i].index("SUPINFEC")] == "Superficial Incisional SSI":
                supInfec = 1

            deepSSI = 0
            if row[HEADERSLIST[i].index("WNDINFD")] == "Deep Incisional SSI":
                deepSSI = 1

            orgSpaceSSI = 0
            if row[HEADERSLIST[i].index("ORGSPCSSI")] == "Organ/Space SSI":
                orgSpaceSSI = 1

            woundDisruption = 0
            if row[HEADERSLIST[i].index("DEHIS")] == "Wound Disruption":
                woundDisruption = 1

            deepVeinThrombosis = 0
            if row[HEADERSLIST[i].index("OTHDVT")] == "DVT Requiring Therapy":
                deepVeinThrombosis = 1

            renalInsufficiency = 0
            if row[HEADERSLIST[i].index("RENAINSF")] == "Progressive Renal Insufficiency":
                renalInsufficiency = 1

            pulmonaryEmbolism = 0
            if row[HEADERSLIST[i].index("PULEMBOL")] == "Pulmonary Embolism":
                pulmonaryEmbolism = 1
        
            cva = 0
            if row[HEADERSLIST[i].index("CNSCVA")] == "Stroke/CVA":
                cva = 1

            cardiacArrest = 0
            if row[HEADERSLIST[i].index("CDARREST")] == "Cardiac Arrest Requiring CPR":
                cardiacArrest = 1

            myocardialInfarction = 0
            if row[HEADERSLIST[i].index("CDMI")] == "Myocardial Infarction":
                myocardialInfarction = 1

            sepsis = 0
            if row[HEADERSLIST[i].index("OTHSYSEP")] == "Sepsis":
                sepsis = 1

            inpatient = 0
            if row[HEADERSLIST[i].index("INOUT")] == "Inpatient":
                inpatient = 1

            newRow = [age, sex, height, weight, race, diabetes, smoke, dyspnea, ventilator_dependent, ascites, copd, cgf, hypertension, acute_renal_failure, disseminated_cancer, steroid, bleeding_disorder, independent_functional_health_status, not_independent_functional_health_status, pneumonia, reintubation, urinaryInfection, ventilator, unplannedReadmission, readmission,
            supInfec, deepSSI, orgSpaceSSI, woundDisruption, deepVeinThrombosis, renalInsufficiency, pulmonaryEmbolism, cva, cardiacArrest, myocardialInfarction, sepsis, inpatient] 
            csv_writer.writerow(newRow)

    
