import pandas as pd
import numpy as np 
import statsmodels.api as sm
import math
import csv

#input file should be a csv composed of feature and outcome columns with integer values
FILE_NAME = "testingProcessor.csv"

OUTPUT_FILE_NAME = "output.csv"

f = open(OUTPUT_FILE_NAME, "w")


col_names = ["Diabetes", "Smoke", "Dyspnea", "Ventilator Dependent", "Ascites",
"COPD", "CGF", "Hypertension", "Acute Renal Failure", "Disseminated Cancer", "Steroid", "Bleeding Disorder", "Independent Functional Health Status",
"Totally or Partially Dependent Functional Health Status", "Pneumonia", "Reintubation", "Urinary_Infection", "Ventilator", "Unplanned_Readmission", "Readmission", "Superficial_SSI", "Deep SSI",
"Organ_Space_SSI", "Wound Disruption", "Deep_Vein_Thrombosis", "Renal_Insufficiency", "Pulmonary_Embolism", "CVA with Neurologic Deficit",
"Cardiac Arrest", "Myocardial Infarction", "Sepsis", "Inpatient"]

dataset = pd.read_csv(FILE_NAME, header=None, names=col_names, index_col = False)

#create a data frame of only inpatient cases
datasetInpatient = dataset[dataset.Inpatient == 1]

#create a data frame of only outpatient cases
datasetOutpatient = dataset[dataset.Inpatient != 1]

feature_cols = ["Diabetes", "COPD", "Hypertension", "Independent Functional Health Status"]


X = dataset[feature_cols]
X = sm.add_constant(X)
y = dataset.Pneumonia


# testing out statsmodels library
np.warnings.filterwarnings('ignore')
logit_model=sm.Logit(y, X)
result=logit_model.fit(maxiter=100000, method = 'nm')

print(result.summary())
f.write(result.summary().as_csv())
f.write("\n")

def calculate_p_value(lower, upper, estimate):
	estimate = math.log(estimate)
	lower = math.log(lower)
	upper = math.log(upper)
	se = (upper - lower)/(2*1.96)
	z = estimate*1.0/se
	return math.exp(-0.717*z-0.416*z**2)


params = result.params
conf = result.conf_int()
conf['OR'] = params
conf.columns = ['2.5%', '97.5%', 'OR']
print(np.exp(conf))
for i in range(0, len(feature_cols)):
	print "p-value for", feature_cols[i],"=", calculate_p_value(np.exp(conf).iloc[i + 1]['2.5%'], np.exp(conf).iloc[i + 1]['97.5%'], np.exp(conf).iloc[i + 1]['OR'])






