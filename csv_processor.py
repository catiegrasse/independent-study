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
        height = row[headers14.index("HEIGHT")]
        weight = row[headers14.index("WEIGHT")]

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

        ventilator_dependent = 0
        if row[headers14.index("VENTILAT")] == "Yes":
            ventilator_dependent = 1

        ascites = 0
        if row[headers14.index("ASCITES")] == "Yes":
            ascites = 1

        copd = 0
        if row[headers14.index("HXCOPD")] == "Yes":
            copd = 1

        cgf = 0
        if row[headers14.index("HXCHF")] == "Yes":
            chf = 1

        hypertension = 0
        if row[headers14.index("HYPERMED")] == "Yes":
            hypertension = 1

        acute_renal_failure = 0
        if row[headers14.index("RENAFAIL")] == "Yes":
            acute_renal_failure = 1

        disseminated_cancer = 0
        if row[headers14.index("DISCANCR")] == "Yes":
            disseminated_cancer = 1

        steroid = 0
        if row[headers14.index("STEROID")] == "Yes":
            steroid = 1

        bleeding_disorder = 0
        if row[headers14.index("BLEEDDIS")] == "Yes":
            bleeding_disorder = 1

        independent_functional_health_status = 0
        if row[headers14.index("FNSTATUS2")] == "Independent":
            independent_functional_health_status = 1

        not_independent_functional_health_status = 0
        if row[headers14.index("FNSTATUS2")] == "Partially Dependent" or row[headers14.index("FNSTATUS2")] == "Totally Dependent":
            not_independent_functional_health_status = 1

        pneumonia = 0
        if row[headers14.index("OUPNEUMO")] == "Pneumonia":
            pneumonia = 1

        reintubation = 0
        if row[headers14.index("REINTUB")] == "Unplanned Intubation":
            reintubation = 1

        urinaryInfection = 0
        if row[headers14.index("URNINFEC")] == "Urinary Tract Infection":
            urinaryInfection = 1

        ventilator = 0
        if row[headers14.index("FAILWEAN")] == "On Ventilator greater than 48 Hours":
            ventilator = 1

        readmission = 0
        readmissionResponses14 = [row[ind] for ind in readmissionIndices14 if row[ind] == "Yes"]
        if len(readmissionResponses14) > 0:
            readmission = 1

        unplannedReadmission = 0
        unplannedReadmissionResponses14 = [row[ind] for ind in unplannedReadmissionIndices14 if row[ind] == "Yes"]
        if len(unplannedReadmissionResponses14) > 0:
            unplannedReadmission = 1

        supInfec = 0
        if row[headers14.index("SUPINFEC")] == "Superficial Incisional SSI":
            supInfec = 1

        deepSSI = 0
        if row[headers14.index("WNDINFD")] == "Deep Incisional SSI":
            deepSSI = 1

        orgSpaceSSI = 0
        if row[headers14.index("ORGSPCSSI")] == "Organ/Space SSI":
            orgSpaceSSI = 1

        woundDisruption = 0
        if row[headers14.index("DEHIS")] == "Wound Disruption":
            woundDisruption = 1

        deepVeinThrombosis = 0
        if row[headers14.index("OTHDVT")] == "DVT Requiring Therapy":
            deepVeinThrombosis = 1

        renalInsufficiency = 0
        if row[headers14.index("RENAINSF")] == "Progressive Renal Insufficiency":
            renalInsufficiency = 1

        pulmonaryEmbolism = 0
        if row[headers14.index("PULEMBOL")] == "Pulmonary Embolism":
            pulmonaryEmbolism = 1
        
        cva = 0
        if row[headers14.index("CNSCVA")] == "Stroke/CVA":
            cva = 1

        cardiacArrest = 0
        if row[headers14.index("CDARREST")] == "Cardiac Arrest Requiring CPR":
            cardiacArrest = 1

        myocardialInfarction = 0
        if row[headers14.index("CDMI")] == "Myocardial Infarction":
            myocardialInfarction = 1

        sepsis = 0
        if row[headers14.index("OTHSYSEP")] == "Sepsis":
            sepsis = 1

        inpatient = 0
        if row[headers14.index("INOUT")] == "Inpatient":
            inpatient = 1

        newRow = [age, sex, height, weight, race, diabetes, smoke, dyspnea, ventilator_dependent, ascites, copd, cgf, hypertension, acute_renal_failure, disseminated_cancer, steroid, bleeding_disorder, independent_functional_health_status, not_independent_functional_health_status, pneumonia, reintubation, urinaryInfection, ventilator, unplannedReadmission, readmission,
        supInfec, deepSSI, orgSpaceSSI, woundDisruption, deepVeinThrombosis, renalInsufficiency, pulmonaryEmbolism, cva, cardiacArrest, myocardialInfarction, sepsis, inpatient] 
        csv_writer.writerow(newRow)

    for row in csv_reader15:
        age = row[headers15.index("Age")]
        sex = SEX_COLUMNS.index(row[headers15.index("SEX")])
        height = row[headers15.index("HEIGHT")]
        weight = row[headers15.index("WEIGHT")]


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

        ventilator_dependent = 0
        if row[headers15.index("VENTILAT")] == "Yes":
            ventilator_dependent = 1

        ascites = 0
        if row[headers15.index("ASCITES")] == "Yes":
            ascites = 1

        copd = 0
        if row[headers15.index("HXCOPD")] == "Yes":
            copd = 1

        cgf = 0
        if row[headers15.index("HXCHF")] == "Yes":
            cgf = 1

        hypertension = 0
        if row[headers15.index("HYPERMED")] == "Yes":
            hypertension = 1

        acute_renal_failure = 0
        if row[headers15.index("RENAFAIL")] == "Yes":
            acute_renal_failure = 1

        disseminated_cancer = 0
        if row[headers15.index("DISCANCR")] == "Yes":
            disseminated_cancer = 1

        steroid = 0
        if row[headers15.index("STEROID")] == "Yes":
            steroid = 1

        bleeding_disorder = 0
        if row[headers15.index("BLEEDDIS")] == "Yes":
            bleeding_disorder = 1

        independent_functional_health_status = 0
        if row[headers15.index("FNSTATUS2")] == "Independent":
            independent_functional_health_status = 1

        not_independent_functional_health_status = 0
        if row[headers15.index("FNSTATUS2")] == "Partially Dependent" or row[headers14.index("FNSTATUS2")] == "Totally Dependent":
            not_independent_functional_health_status = 1

        pneumonia = 0
        if row[headers15.index("OUPNEUMO")] == "Pneumonia":
            pneumonia = 1

        reintubation = 0
        if row[headers15.index("REINTUB")] == "Unplanned Intubation":
            reintubation = 1

        urinaryInfection = 0
        if row[headers15.index("URNINFEC")] == "Urinary Tract Infection":
            urinaryInfection = 1

        ventilator = 0
        if row[headers15.index("FAILWEAN")] == "On Ventilator greater than 48 Hours":
            ventilator = 1

        readmission = 0
        readmissionResponses15 = [row[ind] for ind in readmissionIndices15 if row[ind] == "Yes"]
        if len(readmissionResponses15) > 0:
            readmission = 1

        unplannedReadmission = 0
        unplannedReadmissionResponses15 = [row[ind] for ind in unplannedReadmissionIndices15 if row[ind] == "Yes"]
        if len(unplannedReadmissionResponses15) > 0:
            unplannedReadmission = 1

        supInfec = 0
        if row[headers15.index("SUPINFEC")] == "Superficial Incisional SSI":
            supInfec = 1

        deepSSI = 0
        if row[headers15.index("WNDINFD")] == "Deep Incisional SSI":
            deepSSI = 1

        orgSpaceSSI = 0
        if row[headers15.index("ORGSPCSSI")] == "Organ/Space SSI":
            orgSpaceSSI = 1

        woundDisruption = 0
        if row[headers15.index("DEHIS")] == "Wound Disruption":
            woundDisruption = 1

        deepVeinThrombosis = 0
        if row[headers15.index("OTHDVT")] == "DVT Requiring Therapy":
            deepVeinThrombosis = 1

        renalInsufficiency = 0
        if row[headers15.index("RENAINSF")] == "Progressive Renal Insufficiency":
            renalInsufficiency = 1

        pulmonaryEmbolism = 0
        if row[headers15.index("PULEMBOL")] == "Pulmonary Embolism":
            pulmonaryEmbolism = 1

        cva = 0
        if row[headers15.index("CNSCVA")] == "Stroke/CVA":
            cva = 1

        cardiacArrest = 0
        if row[headers15.index("CDARREST")] == "Cardiac Arrest Requiring CPR":
            cardiacArrest = 1

        myocardialInfarction = 0
        if row[headers15.index("CDMI")] == "Myocardial Infarction":
            myocardialInfarction = 1

        sepsis = 0
        if row[headers15.index("OTHSYSEP")] == "Sepsis":
            sepsis = 1

        inpatient = 0
        if row[headers15.index("INOUT")] == "Inpatient":
            inpatient = 1

        newRow = [age, sex, height, weight, race, diabetes, smoke, dyspnea, ventilator_dependent, ascites, copd, cgf, hypertension, acute_renal_failure, disseminated_cancer, steroid, bleeding_disorder, independent_functional_health_status, not_independent_functional_health_status, pneumonia, reintubation, urinaryInfection, ventilator, unplannedReadmission, readmission,
        supInfec, deepSSI, orgSpaceSSI, woundDisruption, deepVeinThrombosis, renalInsufficiency, pulmonaryEmbolism, cva, cardiacArrest, myocardialInfarction, sepsis, inpatient] 
        csv_writer.writerow(newRow)

    for row in csv_reader16:
        age = row[headers16.index("Age")]
        sex = SEX_COLUMNS.index(row[headers16.index("SEX")])
        height = row[headers16.index("HEIGHT")]
        weight = row[headers16.index("WEIGHT")]


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

        ventilator_dependent = 0
        if row[headers16.index("VENTILAT")] == "Yes":
            ventilator_dependent = 1

        ascites = 0
        if row[headers16.index("ASCITES")] == "Yes":
            ascites = 1

        copd = 0
        if row[headers16.index("HXCOPD")] == "Yes":
            copd = 1

        cgf = 0
        if row[headers16.index("HXCHF")] == "Yes":
            cgf = 1

        hypertension = 0
        if row[headers16.index("HYPERMED")] == "Yes":
            hypertension = 1

        acute_renal_failure = 0
        if row[headers16.index("RENAFAIL")] == "Yes":
            acute_renal_failure = 1

        disseminated_cancer = 0
        if row[headers16.index("DISCANCR")] == "Yes":
            disseminated_cancer = 1

        steroid = 0
        if row[headers16.index("STEROID")] == "Yes":
            steroid = 1

        bleeding_disorder = 0
        if row[headers16.index("BLEEDDIS")] == "Yes":
            bleeding_disorder = 1

        independent_functional_health_status = 0
        if row[headers16.index("FNSTATUS2")] == "Independent":
            independent_functional_health_status = 1

        not_independent_functional_health_status = 0
        if row[headers16.index("FNSTATUS2")] == "Partially Dependent" or row[headers14.index("FNSTATUS2")] == "Totally Dependent":
            not_independent_functional_health_status = 1

        pneumonia = 0
        if row[headers16.index("OUPNEUMO")] == "Pneumonia":
            pneumonia = 1

        reintubation = 0
        if row[headers16.index("REINTUB")] == "Unplanned Intubation":
            reintubation = 1

        urinaryInfection = 0
        if row[headers16.index("URNINFEC")] == "Urinary Tract Infection":
            urinaryInfection = 1

        ventilator = 0
        if row[headers16.index("FAILWEAN")] == "On Ventilator greater than 48 Hours":
            ventilator = 1

        readmission = 0
        readmissionResponses16 = [row[ind] for ind in readmissionIndices16 if row[ind] == "Yes"]
        if len(readmissionResponses16) > 0:
            readmission = 1

        unplannedReadmission = 0
        unplannedReadmissionResponses16 = [row[ind] for ind in unplannedReadmissionIndices16 if row[ind] == "Yes"]
        if len(unplannedReadmissionResponses16) > 0:
            unplannedReadmission = 1

        supInfec = 0
        if row[headers16.index("SUPINFEC")] == "Superficial Incisional SSI":
            supInfec = 1

        deepSSI = 0
        if row[headers16.index("WNDINFD")] == "Deep Incisional SSI":
            deepSSI = 1

        orgSpaceSSI = 0
        if row[headers16.index("ORGSPCSSI")] == "Organ/Space SSI":
            orgSpaceSSI = 1

        woundDisruption = 0
        if row[headers16.index("DEHIS")] == "Wound Disruption":
            woundDisruption = 1

        deepVeinThrombosis = 0
        if row[headers16.index("OTHDVT")] == "DVT Requiring Therapy":
            deepVeinThrombosis = 1

        renalInsufficiency = 0
        if row[headers16.index("RENAINSF")] == "Progressive Renal Insufficiency":
            renalInsufficiency = 1

        pulmonaryEmbolism = 0
        if row[headers16.index("PULEMBOL")] == "Pulmonary Embolism":
            pulmonaryEmbolism = 1

        cva = 0
        if row[headers16.index("CNSCVA")] == "Stroke/CVA":
            cva = 1

        cardiacArrest = 0
        if row[headers16.index("CDARREST")] == "Cardiac Arrest Requiring CPR":
            cardiacArrest = 1

        myocardialInfarction = 0
        if row[headers16.index("CDMI")] == "Myocardial Infarction":
            myocardialInfarction = 1

        sepsis = 0
        if row[headers16.index("OTHSYSEP")] == "Sepsis":
            sepsis = 1

        inpatient = 0
        if row[headers16.index("INOUT")] == "Inpatient":
            inpatient = 1

        newRow = [age, sex, height, weight, race, diabetes, smoke, dyspnea, ventilator_dependent, ascites, copd, cgf, hypertension, acute_renal_failure, disseminated_cancer, steroid, bleeding_disorder, independent_functional_health_status, not_independent_functional_health_status, pneumonia, reintubation, urinaryInfection, ventilator, unplannedReadmission, readmission,
        supInfec, deepSSI, orgSpaceSSI, woundDisruption, deepVeinThrombosis, renalInsufficiency, pulmonaryEmbolism, cva, cardiacArrest, myocardialInfarction, sepsis, inpatient] 
        csv_writer.writerow(newRow)

print "Total number of records with diabetes ICD code: ", icdCount
