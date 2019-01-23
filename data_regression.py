import pandas as pd
import numpy as np 
import statsmodels.api as sm
import math
import csv

#input file should be a csv composed of feature and outcome columns with integer values
FILE_NAME = "testingProcessor.csv"

OUTPUT_FILE_NAME = "output.csv"

f = open(OUTPUT_FILE_NAME, "w")


col_names = ["Age", "Sex", "Height", "Weight", "Race", "Diabetes", "Smoke", "Dyspnea", "Ventilator Dependent", "Ascites",
"COPD", "CGF", "Hypertension", "Acute Renal Failure", "Disseminated Cancer", "Steroid", "Bleeding Disorder", "Independent Functional Health Status",
"Totally or Partially Dependent Functional Health Status", "Pneumonia", "Reintubation", "Urinary Infection", "Ventilator", "Unplanned Readmission", "Readmission", "Superficial SSI", "Deep SSI",
"Organ_Space_SSI", "Wound Disruption", "Deep Vein Thrombosis", "Renal Insufficiency", "Pulmonary_Embolism", "CVA with Neurologic Deficit",
"Cardiac Arrest", "Myocardial Infarction", "Sepsis", "Inpatient"]

dataset = pd.read_csv(FILE_NAME, header=None, names=col_names, index_col = False)

#create a data frame of only inpatient cases
datasetInpatient = dataset[dataset.Inpatient == 1]

#create a data frame of only outpatient cases
datasetOutpatient = dataset[dataset.Inpatient != 1]

outcome_cols = ["Organ_Space_SSI", "Pulmonary_Embolism"]

feature_cols = ["Smoke", "Dyspnea", "COPD", "Hypertension", "Ventilator Dependent"]
#feature_cols = ["Smoke"]


X = datasetOutpatient[feature_cols]
X = sm.add_constant(X)
y = datasetOutpatient.Pulmonary_Embolism


# testing out statsmodels library
logit_model=sm.Logit(y, X)
result=logit_model.fit(maxiter=600, method = 'nm')

print(result.summary())
f.write(result.summary().as_csv())
f.write("\n")
coefficients = result.params.values
for i in range(len(coefficients) - 1):
	print("Odds ratio for " + feature_cols[i] + " = ", math.exp(coefficients[i + 1]))
	f.write("Odds ratio for " + feature_cols[i] + " = " + str(math.exp(coefficients[i + 1])) + "\n")

params = result.params
conf = result.conf_int()
conf['OR'] = params
conf.columns = ['2.5%', '97.5%', 'OR']
print(np.exp(conf))


def calculate_p_value(lower, upper, estimate):
	estimate = math.log(estimate)
	lower = math.log(lower)
	upper = math.log(upper)
	se = (upper - lower)/(2*1.96)
	z = estimate*1.0/se
	return math.exp(-0.717*z-0.416*z**2)



print(calculate_p_value(0.379196, 11.430702, 2.081941))




