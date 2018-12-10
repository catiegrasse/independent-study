## Analysis
#### Source: "Effect of diabetes mellitus on postoperative endoscopic sinus surgery outcomes"  
This paper analyzed the NSQIP database from the years 2005 - 2013 (our data: 2014 - 2016)  
From this group in the database, found 644 patients identified as having undergone ESS  (our data: 565 patients (approx .02% of total database)))
- Paper: 85/644 (13.2%) had DM vs Our data: 69/565 (12.2%) had DM 
- Paper: DM patients were significantly older than non-DM patients vs Our data: average age of patient with DM = 54 vs average age of patient without DM = 44
## Findings
|   | Non - Diabetics (N = 496) | Diabetics (N = 69) | p-Value from data | p-Value in paper |
| ------------- | ------------- | ------------- | -------------|------------- |
| <= 40 years  | 43.15%  | 17.39 % | < .001 | < .001 |
| 41-60 years  | 37.90%  | 33.33% | 0.541 | 0.038 |
| 61-80 years  | 16.73%  | 46.38% | < .001 | < .001 | 
| > 80 years   | 2.22%   | 2.90%  | 0.725 | 0.032 |
| Male | 47.18% | 44.93% | 0.726 | 0.920 |
| Female | 52.82% | 55.07% | ~ | ~ | 
| White | 73.79% | 68.11% | 0.320 | 0.217 |
| Black | 11.90% | 18.84% | 0.105 | 0.009 | 
| Other | 5.44% | 7.25% | 0.542 | 0.740 |
| Unknown | 8.87% | 5.80% | 0.392 | 0.108
| Smoking | 20.16% | 20.28% | 0.982 | 0.687 |
| Dyspnea | 3.63% | 7.24% | 0.155 | 0.004 |
| Hypertension | 29.03% | 76.81% | < .001 | < .001 |
| Unplanned Readmission | 3.83% | 5.79% | 0.440 | 0.252 |
| Pneumonia | 0.81% | 5.80% | | |


- Dyspnea (difficulty breathing) and hypertension were the only statistically significant comorbidities according to the paper
- In my analysis, only hypertension appeared to be statistically significant (p < 0.05)

## Logistic Regression
- Example logistic regression output using python statsmodels.py  
#### Outcome: Pneumonia

|   | coef | std err | z | P > abs(z) | 0.025 | 0.975 |
| ------------- | ------------- | ------------- | -------------|------------- | ------------- | ------------- |
| const  | -0.0983 | 0.746 | -0.132 | 0.895 | -1.560 | 1.363 |
| Age  | -0.0867  | 0.023 | -3.805 | 0.000 | -0.131 | -0.042 |
| Sex  | -0.1138  | 0.467 | -0.244 | 0.808 | -1.029 | 0.802 |
| Race  | 0.0560  | 0.258 | 0.217 | 0.828 | -0.450 | 0.562 |
| Diabetes   | 0.1080  | 0.932  | 0.116 | 0.908 | -1.719 | 1.935 |
| Smoking   | 0.0032   | 0.667  | 0.005 | 0.996 | -1.303 | 1.310 |
| Dyspnea  | 0.0974   | 1.629  | 0.060 | 0.952 | -3.095 | 3.290 |
| Hypertension   | 0.1012  | 0.734  | 0.138 | 0.890 | -1.338 | 1.540 |

- Example odds ratio calculation: exp(diabetes coef) = exp(0.1080) = 1.114

## Odds Ratio
Odds Ratio calculations made by including the variables: [Age, Sex, Race, Diabetes, Smoking, Dyspnea, Hypertension]:

|   | Odds ratio (data) | 0.025 | 0.975 | Odds ratio (paper) | 
| ------------- | ------------- | ------------- | ------------- | ------------- | 
| Pneumonia  | 1.114 | 0.869 | 0.933 | 13.283 | 
| Unplanned Readmission  | 1.499 | 0.191 | 5.296 | 3.413 | 
| Unplanned Reintubation | 1.076| 0.088 | 16.980 | 7.783 |
| Urinary Tract Infection | 1.039 | 0.001 | 502.21 | 6.205 |
| Ventilator | 1.022 | 0.184 | 5.490 | 12.276 |

## Odds Ratio
Odds Ratio calculations made by including the variables: [Diabetes]:

|   | Odds ratio (data) | Odds ratio (paper) | 
| -------------  | ------------- | ------------- | 
| Pneumonia  | 7.569 | 13.283 | 
| Unplanned Readmission  | 1.545 | 3.413 | 
| Unplanned Reintubation | 11.230 | 7.783 |
| Urinary Tract Infection | 3.686 | 6.205 |
| Ventilator | 4.906 | 12.276 |

## Recreating Table 3 from the Paper
|  | Non-Diabetics (N = 496) | Non-Diabetics (paper)| Diabetics (N = 69) | Diabetics (paper) | p-value | p-value (paper) |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | 
| Superficial SSI | 0.2% | 0.4% | 0.0% | 0.0% | | 1.000 |
| Deep SSI | 0.0% | 0.4% | 0.0% | 0.0% | | 1.000 |
| Organ/Space SSI | 3.9% | 0.0% | 1.4% | 0.0% | | - |
| Wound Disruption | 0.0% | 0.5% | 0.0% | 0.0% | | 1.000 |
| Pneumonia | 0.81% | 0.5% | 5.8% | 3.5% | | 0.033 |
| Unplanned Reintubation | 0.4% | 0.7% | 4.3% | 5.9% | | 0.033 |
| Urinary Tract Infection | 0.2% | 0.5% | 0.0% | 3.5% | | 0.033 |
| Deep Vein Thrombosis | 0.2% | 0.2% | 1.4% | 1.2% | | 0.247 |
| Renal Insufficiency | 0.2% | 0.0% | 0.0% | 1.2% | | 0.132 |
| Pulmonary Embolism | 0.4% | 0.5% | 0.0% | 0.0% |  | 1.000 |
| Ventilator > 48 Hours | 0.6% | 0.7% | 2.9% | 7.1% | | 0.001 |
| Acute Renal Failure | 0.2% | 0.0% | 0.0% | 0.0% | | - |
| CVA with Neurologic Deficit | 0.0% | 0.2% | 0.0% | 0.0% | | 1.000|
| Cardiac Arrest Requiring CPR | 0.0% | 0.0% | 0.0% | 0.0% | - | - |
| Myorcardial Infarction | 0.0% | 0.0% | 0.0% | 1.2% | - | 0.132 |
| Sepsis | 1.0% | 0.2% | 0.0% | 1.2% | | 0.247 |

## Diabetes Analysis
| | Non-Diabetes (N = 496.0) | Diabetes (N = 69.0) |
| ------------- | ------------- | ------------- |
 | Diabetes | 0.0 | 1.0 | 
 | Smoke | 1.44927536232 | 0.202898550725 | 
 | Dyspnea | 0.260869565217 | 0.0724637681159 | 
 | Ventilator Dependent | 0.0144927536232 | 0.0 | 
 | Ascites | 0.0 | 0.0 | 
 | COPD | 0.202898550725 | 0.101449275362 | 
 | CGF | 0.0289855072464 | 0.0144927536232 | 
 | Hypertension | 2.08695652174 | 0.768115942029 | 
 | Acute Renal Failure | 0.0144927536232 | 0.0 | 
 | Disseminated Cancer | 0.188405797101 | 0.0144927536232 | 
 | Steroid | 0.449275362319 | 0.0289855072464 | 
 | Bleeding Disorder | 0.101449275362 | 0.0289855072464 | 
 | Functional Health Status | 0.0434782608696 | 0.0434782608696 | 
 | Pneumonia | 0.0579710144928 | 0.0579710144928 | 
 | Reintubation | 0.0289855072464 | 0.0434782608696 | 
 | Urinary Infection | 0.0144927536232 | 0.0 | 
 | Ventilator | 0.0434782608696 | 0.0289855072464 | 
 | Unplanned Readmission | 0.275362318841 | 0.0579710144928 | 
 | Readmission | 0.304347826087 | 0.0579710144928 | 
 | Superficial SSI | 0.0144927536232 | 0.0 | 
 | Deep SSI | 0.0 | 0.0 | 
 | Organ/Space SSI | 0.101449275362 | 0.0289855072464 | 
 | Wound Disruption | 0.0 | 0.0 | 
 | Deep Vein Thrombosis | 0.0144927536232 | 0.0144927536232 | 
 | Renal Insufficiency | 0.0144927536232 | 0.0 | 
 | Pulmonary Embolism | 0.0289855072464 | 0.0 | 
 | CVA with Neurologic Deficit | 0.0 | 0.0 | 
 | Cardiac Arrest | 0.0 | 0.0 | 
 | Myocardial Infarction | 0.0 | 0.0 | 
 | Sepsis | 0.0724637681159 | 0.0 | 

| | Outpatient Non-Diabetes (N = 327) | Outpatient Diabetes (N = 30) |  Inpatient Non-Diabetes (N = 169) | Inpatient Diabetes (N = 39) |
| ------------- | ------------- | ------------- | ------------- | ------------- |
 | Diabetes | 0.0 | 1.0 | 0.0 | 1.0
 | Smoke | 0.189602446483 | 0.2 | 0.224852071006 | 0.205128205128
 | Dyspnea | 0.0336391437309 | 0.0333333333333 | 0.0414201183432 | 0.102564102564
 | Ventilator Dependent | 0.0 | 0.0 | 0.00591715976331 | 0.0
 | Ascites | 0.0 | 0.0 | 0.0 | 0.0
 | COPD | 0.0275229357798 | 0.0 | 0.0295857988166 | 0.179487179487
 | CGF | 0.00611620795107 | 0.0 | 0.0 | 0.025641025641
 | Hypertension | 0.241590214067 | 0.733333333333 | 0.384615384615 | 0.794871794872
 | Acute Renal Failure | 0.0 | 0.0 | 0.00591715976331 | 0.0
 | Disseminated Cancer | 0.00305810397554 | 0.0 | 0.0710059171598 | 0.025641025641
 | Steroid | 0.0366972477064 | 0.0 | 0.112426035503 | 0.0512820512821
 | Bleeding Disorder | 0.00917431192661 | 0.0 | 0.0236686390533 | 0.0512820512821
 | Functional Health Status | 0.00305810397554 | 0.0333333333333 | 0.0118343195266 | 0.0512820512821
 | Pneumonia | 0.0 | 0.0 | 0.0236686390533 | 0.102564102564
 | Reintubation | 0.0 | 0.0 | 0.0118343195266 | 0.0769230769231
 | Urinary Infection | 0.0 | 0.0 | 0.00591715976331 | 0.0
 | Ventilator | 0.0 | 0.0 | 0.0177514792899 | 0.0512820512821
 | Unplanned Readmission | 0.0366972477064 | 0.0333333333333 | 0.0414201183432 | 0.0769230769231
 | Readmission | 0.0366972477064 | 0.0333333333333 | 0.0532544378698 | 0.0769230769231
 | Superficial SSI | 0.0 | 0.0 | 0.00591715976331 | 0.0
 | Deep SSI | 0.0 | 0.0 | 0.0 | 0.0
 | Organ/Space SSI | 0.00611620795107 | 0.0 | 0.0295857988166 | 0.0512820512821
 | Wound Disruption | 0.0 | 0.0 | 0.0 | 0.0
 | Deep Vein Thrombosis | 0.0 | 0.0 | 0.00591715976331 | 0.025641025641
 | Renal Insufficiency | 0.00305810397554 | 0.0 | 0.0 | 0.0
 | Pulmonary Embolism | 0.00305810397554 | 0.0 | 0.00591715976331 | 0.0
 | CVA with Neurologic Deficit | 0.0 | 0.0 | 0.0 | 0.0
 | Cardiac Arrest | 0.0 | 0.0 | 0.0 | 0.0
 | Myocardial Infarction | 0.0 | 0.0 | 0.0 | 0.0
 | Sepsis | 0.00305810397554 | 0.0 | 0.0236686390533 | 0.0
 
 ## Smoking Analysis
 | | Non-Smoke (N = 451.0) | Smoke (N = 114.0) |
| ------------- | ------------- | ------------- |
 | Diabetes | 0.482456140351 | 0.122807017544 | 
 | Smoke | 0.0 | 1.0 | 
 | Dyspnea | 0.105263157895 | 0.0964912280702 | 
 | Ventilator Dependent | 0.0 | 0.00877192982456 | 
 | Ascites | 0.0 | 0.0 | 
 | COPD | 0.114035087719 | 0.0701754385965 | 
 | CGF | 0.0175438596491 | 0.00877192982456 | 
 | Hypertension | 1.22807017544 | 0.5 | 
 | Acute Renal Failure | 0.00877192982456 | 0.0 | 
 | Disseminated Cancer | 0.105263157895 | 0.0175438596491 | 
 | Steroid | 0.254385964912 | 0.0350877192982 | 
 | Bleeding Disorder | 0.0789473684211 | 0.0 | 
 | Functional Health Status | 0.0350877192982 | 0.0175438596491 | 
 | Pneumonia | 0.0614035087719 | 0.00877192982456 | 
 | Reintubation | 0.0350877192982 | 0.00877192982456 | 
 | Urinary Infection | 0.00877192982456 | 0.0 | 
 | Ventilator | 0.0263157894737 | 0.0175438596491 | 
 | Unplanned Readmission | 0.140350877193 | 0.0614035087719 | 
 | Readmission | 0.149122807018 | 0.0701754385965 | 
 | Superficial SSI | 0.00877192982456 | 0.0 | 
 | Deep SSI | 0.0 | 0.0 | 
 | Organ/Space SSI | 0.0350877192982 | 0.0438596491228 | 
 | Wound Disruption | 0.0 | 0.0 | 
 | Deep Vein Thrombosis | 0.00877192982456 | 0.00877192982456 | 
 | Renal Insufficiency | 0.00877192982456 | 0.0 | 
 | Pulmonary Embolism | 0.0 | 0.0175438596491 | 
 | CVA with Neurologic Deficit | 0.0 | 0.0 | 
 | Cardiac Arrest | 0.0 | 0.0 | 
 | Myocardial Infarction | 0.0 | 0.0 | 
 | Sepsis | 0.0263157894737 | 0.0175438596491 | 
 
| | Outpatient Non-Smoke (N = 289) | Outpatient Smoke (N = 68) |  Inpatient Non-Smoke (N = 162) | Inpatient Smoke (N = 46) |
| ------------- | ------------- | ------------- | ------------- | ------------- |
 | Diabetes | 0.083044982699 | 0.0882352941176 | 0.191358024691 | 0.173913043478
 | Smoke | 0.0 | 1.0 | 0.0 | 1.0
 | Dyspnea | 0.0242214532872 | 0.0735294117647 | 0.0308641975309 | 0.130434782609
 | Ventilator Dependent | 0.0 | 0.0 | 0.0 | 0.0217391304348
 | Ascites | 0.0 | 0.0 | 0.0 | 0.0
 | COPD | 0.0173010380623 | 0.0588235294118 | 0.0493827160494 | 0.0869565217391
 | CGF | 0.00346020761246 | 0.0147058823529 | 0.00617283950617 | 0.0
 | Hypertension | 0.23875432526 | 0.470588235294 | 0.438271604938 | 0.54347826087
 | Acute Renal Failure | 0.0 | 0.0 | 0.00617283950617 | 0.0
 | Disseminated Cancer | 0.00346020761246 | 0.0 | 0.0679012345679 | 0.0434782608696
 | Steroid | 0.0346020761246 | 0.0294117647059 | 0.117283950617 | 0.0434782608696
 | Bleeding Disorder | 0.0103806228374 | 0.0 | 0.037037037037 | 0.0
 | Functional Health Status | 0.00346020761246 | 0.0147058823529 | 0.0185185185185 | 0.0217391304348
 | Pneumonia | 0.0 | 0.0 | 0.0432098765432 | 0.0217391304348
 | Reintubation | 0.0 | 0.0 | 0.0246913580247 | 0.0217391304348
 | Urinary Infection | 0.0 | 0.0 | 0.00617283950617 | 0.0
 | Ventilator | 0.0 | 0.0 | 0.0185185185185 | 0.0434782608696
 | Unplanned Readmission | 0.0311418685121 | 0.0588235294118 | 0.0432098765432 | 0.0652173913043
 | Readmission | 0.0311418685121 | 0.0588235294118 | 0.0493827160494 | 0.0869565217391
 | Superficial SSI | 0.0 | 0.0 | 0.00617283950617 | 0.0
 | Deep SSI | 0.0 | 0.0 | 0.0 | 0.0
 | Organ/Space SSI | 0.00692041522491 | 0.0 | 0.0123456790123 | 0.108695652174
 | Wound Disruption | 0.0 | 0.0 | 0.0 | 0.0
 | Deep Vein Thrombosis | 0.0 | 0.0 | 0.00617283950617 | 0.0217391304348
 | Renal Insufficiency | 0.00346020761246 | 0.0 | 0.0 | 0.0
 | Pulmonary Embolism | 0.0 | 0.0147058823529 | 0.0 | 0.0217391304348
 | CVA with Neurologic Deficit | 0.0 | 0.0 | 0.0 | 0.0
 | Cardiac Arrest | 0.0 | 0.0 | 0.0 | 0.0
 | Myocardial Infarction | 0.0 | 0.0 | 0.0 | 0.0
 | Sepsis | 0.00346020761246 | 0.0 | 0.0123456790123 | 0.0434782608696
 
 ## Hypertension Analysis
 | | Non-Hypertension (N = 368.0) | Hypertension (N = 197.0) |
| ------------- | ------------- | ------------- |
 | Diabetes | 0.0812182741117 | 0.269035532995 | 
 | Smoke | 0.289340101523 | 0.289340101523 | 
 | Dyspnea | 0.0406091370558 | 0.0761421319797 | 
 | Ventilator Dependent | 0.0 | 0.00507614213198 | 
 | Ascites | 0.0 | 0.0 | 
 | COPD | 0.0253807106599 | 0.0812182741117 | 
 | CGF | 0.0 | 0.0152284263959 | 
 | Hypertension | 0.0 | 1.0 | 
 | Acute Renal Failure | 0.0 | 0.00507614213198 | 
 | Disseminated Cancer | 0.0507614213198 | 0.0203045685279 | 
 | Steroid | 0.0964467005076 | 0.0710659898477 | 
 | Bleeding Disorder | 0.0253807106599 | 0.0203045685279 | 
 | Functional Health Status | 0.010152284264 | 0.0203045685279 | 
 | Pneumonia | 0.0152284263959 | 0.0253807106599 | 
 | Reintubation | 0.010152284264 | 0.0152284263959 | 
 | Urinary Infection | 0.00507614213198 | 0.0 | 
 | Ventilator | 0.0203045685279 | 0.00507614213198 | 
 | Unplanned Readmission | 0.0507614213198 | 0.0659898477157 | 
 | Readmission | 0.0507614213198 | 0.0761421319797 | 
 | Superficial SSI | 0.0 | 0.00507614213198 | 
 | Deep SSI | 0.0 | 0.0 | 
 | Organ/Space SSI | 0.0203045685279 | 0.0253807106599 | 
 | Wound Disruption | 0.0 | 0.0 | 
 | Deep Vein Thrombosis | 0.00507614213198 | 0.00507614213198 | 
 | Renal Insufficiency | 0.0 | 0.00507614213198 | 
 | Pulmonary Embolism | 0.00507614213198 | 0.00507614213198 | 
 | CVA with Neurologic Deficit | 0.0 | 0.0 | 
 | Cardiac Arrest | 0.0 | 0.0 | 
 | Myocardial Infarction | 0.0 | 0.0 | 
 | Sepsis | 0.00507614213198 | 0.0203045685279 | 
 
| | Outpatient Non-Hypertension (N = 256) | Outpatient Hypertension (N = 101) |  Inpatient Non-Hypertension (N = 112) | Inpatient Hypertension (N = 96) |
| ------------- | ------------- | ------------- | ------------- | ------------- |
 | Diabetes | 0.03125 | 0.217821782178 | 0.0714285714286 | 0.322916666667
 | Smoke | 0.140625 | 0.316831683168 | 0.1875 | 0.260416666667
 | Dyspnea | 0.01953125 | 0.0693069306931 | 0.0267857142857 | 0.0833333333333
 | Ventilator Dependent | 0.0 | 0.0 | 0.0 | 0.0104166666667
 | Ascites | 0.0 | 0.0 | 0.0 | 0.0
 | COPD | 0.0078125 | 0.0693069306931 | 0.0267857142857 | 0.09375
 | CGF | 0.0 | 0.019801980198 | 0.0 | 0.0104166666667
 | Hypertension | 0.0 | 1.0 | 0.0 | 1.0
 | Acute Renal Failure | 0.0 | 0.0 | 0.0 | 0.0104166666667
 | Disseminated Cancer | 0.0 | 0.00990099009901 | 0.0892857142857 | 0.03125
 | Steroid | 0.02734375 | 0.049504950495 | 0.107142857143 | 0.09375
 | Bleeding Disorder | 0.0078125 | 0.00990099009901 | 0.0267857142857 | 0.03125
 | Functional Health Status | 0.0 | 0.019801980198 | 0.0178571428571 | 0.0208333333333
 | Pneumonia | 0.0 | 0.0 | 0.0267857142857 | 0.0520833333333
 | Reintubation | 0.0 | 0.0 | 0.0178571428571 | 0.03125
 | Urinary Infection | 0.0 | 0.0 | 0.00892857142857 | 0.0
 | Ventilator | 0.0 | 0.0 | 0.0357142857143 | 0.0104166666667
 | Unplanned Readmission | 0.03125 | 0.049504950495 | 0.0178571428571 | 0.0833333333333
 | Readmission | 0.03125 | 0.049504950495 | 0.0178571428571 | 0.104166666667
 | Superficial SSI | 0.0 | 0.0 | 0.0 | 0.0104166666667
 | Deep SSI | 0.0 | 0.0 | 0.0 | 0.0
 | Organ/Space SSI | 0.00390625 | 0.00990099009901 | 0.0267857142857 | 0.0416666666667
 | Wound Disruption | 0.0 | 0.0 | 0.0 | 0.0
 | Deep Vein Thrombosis | 0.0 | 0.0 | 0.00892857142857 | 0.0104166666667
 | Renal Insufficiency | 0.0 | 0.00990099009901 | 0.0 | 0.0
 | Pulmonary Embolism | 0.00390625 | 0.0 | 0.0 | 0.0104166666667
 | CVA with Neurologic Deficit | 0.0 | 0.0 | 0.0 | 0.0
 | Cardiac Arrest | 0.0 | 0.0 | 0.0 | 0.0
 | Myocardial Infarction | 0.0 | 0.0 | 0.0 | 0.0
 | Sepsis | 0.0 | 0.00990099009901 | 0.00892857142857 | 0.03125
 
 ## Dyspnea Analysis
 
| | Non-Dyspnea (N = 542.0) | Dyspnea (N = 23.0) |
| ------------- | ------------- | ------------- |
 | Diabetes | 2.78260869565 | 0.217391304348 | 
 | Smoke | 4.47826086957 | 0.478260869565 | 
 | Dyspnea | 0.0 | 1.0 | 
 | Ventilator Dependent | 0.0434782608696 | 0.0 | 
 | Ascites | 0.0 | 0.0 | 
 | COPD | 0.608695652174 | 0.304347826087 | 
 | CGF | 0.130434782609 | 0.0 | 
 | Hypertension | 7.91304347826 | 0.652173913043 | 
 | Acute Renal Failure | 0.0 | 0.0434782608696 | 
 | Disseminated Cancer | 0.521739130435 | 0.0869565217391 | 
 | Steroid | 1.34782608696 | 0.0869565217391 | 
 | Bleeding Disorder | 0.304347826087 | 0.0869565217391 | 
 | Functional Health Status | 0.260869565217 | 0.0 | 
 | Pneumonia | 0.347826086957 | 0.0 | 
 | Reintubation | 0.217391304348 | 0.0 | 
 | Urinary Infection | 0.0434782608696 | 0.0 | 
 | Ventilator | 0.217391304348 | 0.0 | 
 | Unplanned Readmission | 0.95652173913 | 0.0434782608696 | 
 | Readmission | 1.04347826087 | 0.0434782608696 | 
 | Superficial SSI | 0.0434782608696 | 0.0 | 
 | Deep SSI | 0.0 | 0.0 | 
 | Organ/Space SSI | 0.391304347826 | 0.0 | 
 | Wound Disruption | 0.0 | 0.0 | 
 | Deep Vein Thrombosis | 0.0869565217391 | 0.0 | 
 | Renal Insufficiency | 0.0434782608696 | 0.0 | 
 | Pulmonary Embolism | 0.0869565217391 | 0.0 | 
 | CVA with Neurologic Deficit | 0.0 | 0.0 | 
 | Cardiac Arrest | 0.0 | 0.0 | 
 | Myocardial Infarction | 0.0 | 0.0 | 
 | Sepsis | 0.217391304348 | 0.0 | 
 
| | Outpatient Non-Dyspnea (N = 345) | Outpatient Dyspnea (N = 12) |  Inpatient Non-Dyspnea (N = 197) | Inpatient Dyspnea (N = 11) |
| ------------- | ------------- | ------------- | ------------- | ------------- |
 | Diabetes | 0.0840579710145 | 0.0833333333333 | 0.177664974619 | 0.363636363636
 | Smoke | 0.182608695652 | 0.416666666667 | 0.203045685279 | 0.545454545455
 | Dyspnea | 0.0 | 1.0 | 0.0 | 1.0
 | Ventilator Dependent | 0.0 | 0.0 | 0.00507614213198 | 0.0
 | Ascites | 0.0 | 0.0 | 0.0 | 0.0
 | COPD | 0.0202898550725 | 0.166666666667 | 0.0355329949239 | 0.454545454545
 | CGF | 0.00579710144928 | 0.0 | 0.00507614213198 | 0.0
 | Hypertension | 0.272463768116 | 0.583333333333 | 0.446700507614 | 0.727272727273
 | Acute Renal Failure | 0.0 | 0.0 | 0.0 | 0.0909090909091
 | Disseminated Cancer | 0.00289855072464 | 0.0 | 0.0558375634518 | 0.181818181818
 | Steroid | 0.031884057971 | 0.0833333333333 | 0.10152284264 | 0.0909090909091
 | Bleeding Disorder | 0.00579710144928 | 0.0833333333333 | 0.0253807106599 | 0.0909090909091
 | Functional Health Status | 0.00579710144928 | 0.0 | 0.0203045685279 | 0.0
 | Pneumonia | 0.0 | 0.0 | 0.0406091370558 | 0.0
 | Reintubation | 0.0 | 0.0 | 0.0253807106599 | 0.0
 | Urinary Infection | 0.0 | 0.0 | 0.00507614213198 | 0.0
 | Ventilator | 0.0 | 0.0 | 0.0253807106599 | 0.0
 | Unplanned Readmission | 0.0376811594203 | 0.0 | 0.0456852791878 | 0.0909090909091
 | Readmission | 0.0376811594203 | 0.0 | 0.0558375634518 | 0.0909090909091
 | Superficial SSI | 0.0 | 0.0 | 0.00507614213198 | 0.0
 | Deep SSI | 0.0 | 0.0 | 0.0 | 0.0
 | Organ/Space SSI | 0.00579710144928 | 0.0 | 0.0355329949239 | 0.0
 | Wound Disruption | 0.0 | 0.0 | 0.0 | 0.0
 | Deep Vein Thrombosis | 0.0 | 0.0 | 0.010152284264 | 0.0
 | Renal Insufficiency | 0.00289855072464 | 0.0 | 0.0 | 0.0
 | Pulmonary Embolism | 0.00289855072464 | 0.0 | 0.00507614213198 | 0.0
 | CVA with Neurologic Deficit | 0.0 | 0.0 | 0.0 | 0.0
 | Cardiac Arrest | 0.0 | 0.0 | 0.0 | 0.0
 | Myocardial Infarction | 0.0 | 0.0 | 0.0 | 0.0
 | Sepsis | 0.00289855072464 | 0.0 | 0.0203045685279 | 0.0
 
 ## COPD Analysis
 | | Non-COPD (N = 544.0) | COPD (N = 21.0) |
| ------------- | ------------- | ------------- |
 | Diabetes | 2.95238095238 | 0.333333333333 | 
 | Smoke | 5.04761904762 | 0.380952380952 | 
 | Dyspnea | 0.761904761905 | 0.333333333333 | 
 | Ventilator Dependent | 0.047619047619 | 0.0 | 
 | Ascites | 0.0 | 0.0 | 
 | COPD | 0.0 | 1.0 | 
 | CGF | 0.047619047619 | 0.0952380952381 | 
 | Hypertension | 8.61904761905 | 0.761904761905 | 
 | Acute Renal Failure | 0.0 | 0.047619047619 | 
 | Disseminated Cancer | 0.619047619048 | 0.047619047619 | 
 | Steroid | 1.42857142857 | 0.142857142857 | 
 | Bleeding Disorder | 0.333333333333 | 0.0952380952381 | 
 | Functional Health Status | 0.285714285714 | 0.0 | 
 | Pneumonia | 0.333333333333 | 0.047619047619 | 
 | Reintubation | 0.190476190476 | 0.047619047619 | 
 | Urinary Infection | 0.047619047619 | 0.0 | 
 | Ventilator | 0.190476190476 | 0.047619047619 | 
 | Unplanned Readmission | 0.952380952381 | 0.142857142857 | 
 | Readmission | 1.04761904762 | 0.142857142857 | 
 | Superficial SSI | 0.047619047619 | 0.0 | 
 | Deep SSI | 0.0 | 0.0 | 
 | Organ/Space SSI | 0.380952380952 | 0.047619047619 | 
 | Wound Disruption | 0.0 | 0.0 | 
 | Deep Vein Thrombosis | 0.047619047619 | 0.047619047619 | 
 | Renal Insufficiency | 0.0 | 0.047619047619 | 
 | Pulmonary Embolism | 0.0952380952381 | 0.0 | 
 | CVA with Neurologic Deficit | 0.0 | 0.0 | 
 | Cardiac Arrest | 0.0 | 0.0 | 
 | Myocardial Infarction | 0.0 | 0.0 | 
 | Sepsis | 0.142857142857 | 0.0952380952381 | 
 
| | Outpatient Non-COPD (N = 348) | Outpatient COPD (N = 9) |  Inpatient Non-COPD (N = 196) | Inpatient COPD (N = 12) |
| ------------- | ------------- | ------------- | ------------- | ------------- |
 | Diabetes | 0.0862068965517 | 0.0 | 0.163265306122 | 0.583333333333
 | Smoke | 0.183908045977 | 0.444444444444 | 0.214285714286 | 0.333333333333
 | Dyspnea | 0.0287356321839 | 0.222222222222 | 0.030612244898 | 0.416666666667
 | Ventilator Dependent | 0.0 | 0.0 | 0.00510204081633 | 0.0
 | Ascites | 0.0 | 0.0 | 0.0 | 0.0
 | COPD | 0.0 | 1.0 | 0.0 | 1.0
 | CGF | 0.0 | 0.222222222222 | 0.00510204081633 | 0.0
 | Hypertension | 0.270114942529 | 0.777777777778 | 0.44387755102 | 0.75
 | Acute Renal Failure | 0.0 | 0.0 | 0.0 | 0.0833333333333
 | Disseminated Cancer | 0.00287356321839 | 0.0 | 0.0612244897959 | 0.0833333333333
 | Steroid | 0.0316091954023 | 0.111111111111 | 0.0969387755102 | 0.166666666667
 | Bleeding Disorder | 0.00574712643678 | 0.111111111111 | 0.0255102040816 | 0.0833333333333
 | Functional Health Status | 0.00574712643678 | 0.0 | 0.0204081632653 | 0.0
 | Pneumonia | 0.0 | 0.0 | 0.0357142857143 | 0.0833333333333
 | Reintubation | 0.0 | 0.0 | 0.0204081632653 | 0.0833333333333
 | Urinary Infection | 0.0 | 0.0 | 0.00510204081633 | 0.0
 | Ventilator | 0.0 | 0.0 | 0.0204081632653 | 0.0833333333333
 | Unplanned Readmission | 0.0344827586207 | 0.111111111111 | 0.0408163265306 | 0.166666666667
 | Readmission | 0.0344827586207 | 0.111111111111 | 0.0510204081633 | 0.166666666667
 | Superficial SSI | 0.0 | 0.0 | 0.00510204081633 | 0.0
 | Deep SSI | 0.0 | 0.0 | 0.0 | 0.0
 | Organ/Space SSI | 0.00287356321839 | 0.111111111111 | 0.0357142857143 | 0.0
 | Wound Disruption | 0.0 | 0.0 | 0.0 | 0.0
 | Deep Vein Thrombosis | 0.0 | 0.0 | 0.00510204081633 | 0.0833333333333
 | Renal Insufficiency | 0.0 | 0.111111111111 | 0.0 | 0.0
 | Pulmonary Embolism | 0.00287356321839 | 0.0 | 0.00510204081633 | 0.0
 | CVA with Neurologic Deficit | 0.0 | 0.0 | 0.0 | 0.0
 | Cardiac Arrest | 0.0 | 0.0 | 0.0 | 0.0
 | Myocardial Infarction | 0.0 | 0.0 | 0.0 | 0.0
 | Sepsis | 0.0 | 0.111111111111 | 0.015306122449 | 0.0833333333333
 
 ## Congestive Heart Failure Analysis
 | | Non-CGF (N = 562.0) | CGF (N = 3.0) |
| ------------- | ------------- | ------------- |
 | Diabetes | 22.6666666667 | 0.333333333333 | 
 | Smoke | 37.6666666667 | 0.333333333333 | 
 | Dyspnea | 7.66666666667 | 0.0 | 
 | Ventilator Dependent | 0.333333333333 | 0.0 | 
 | Ascites | 0.0 | 0.0 | 
 | COPD | 6.33333333333 | 0.666666666667 | 
 | CGF | 0.0 | 1.0 | 
 | Hypertension | 64.6666666667 | 1.0 | 
 | Acute Renal Failure | 0.333333333333 | 0.0 | 
 | Disseminated Cancer | 4.66666666667 | 0.0 | 
 | Steroid | 11.0 | 0.0 | 
 | Bleeding Disorder | 3.0 | 0.0 | 
 | Functional Health Status | 1.66666666667 | 0.333333333333 | 
 | Pneumonia | 2.33333333333 | 0.333333333333 | 
 | Reintubation | 1.33333333333 | 0.333333333333 | 
 | Urinary Infection | 0.333333333333 | 0.0 | 
 | Ventilator | 1.66666666667 | 0.0 | 
 | Unplanned Readmission | 7.66666666667 | 0.0 | 
 | Readmission | 8.33333333333 | 0.0 | 
 | Superficial SSI | 0.333333333333 | 0.0 | 
 | Deep SSI | 0.0 | 0.0 | 
 | Organ/Space SSI | 3.0 | 0.0 | 
 | Wound Disruption | 0.0 | 0.0 | 
 | Deep Vein Thrombosis | 0.666666666667 | 0.0 | 
 | Renal Insufficiency | 0.333333333333 | 0.0 | 
 | Pulmonary Embolism | 0.666666666667 | 0.0 | 
 | CVA with Neurologic Deficit | 0.0 | 0.0 | 
 | Cardiac Arrest | 0.0 | 0.0 | 
 | Myocardial Infarction | 0.0 | 0.0 | 
 | Sepsis | 1.66666666667 | 0.0 | 
 
| | Outpatient Non-CGF (N = 355) | Outpatient CGF (N = 2) |  Inpatient Non-CGF (N = 207) | Inpatient CGF (N = 1) |
| ------------- | ------------- | ------------- | ------------- | ------------- |
 | Diabetes | 0.0845070422535 | 0.0 | 0.183574879227 | 1.0
 | Smoke | 0.188732394366 | 0.5 | 0.222222222222 | 0.0
 | Dyspnea | 0.0338028169014 | 0.0 | 0.0531400966184 | 0.0
 | Ventilator Dependent | 0.0 | 0.0 | 0.0048309178744 | 0.0
 | Ascites | 0.0 | 0.0 | 0.0 | 0.0
 | COPD | 0.0197183098592 | 1.0 | 0.0579710144928 | 0.0
 | CGF | 0.0 | 1.0 | 0.0 | 1.0
 | Hypertension | 0.278873239437 | 1.0 | 0.458937198068 | 1.0
 | Acute Renal Failure | 0.0 | 0.0 | 0.0048309178744 | 0.0
 | Disseminated Cancer | 0.00281690140845 | 0.0 | 0.0628019323671 | 0.0
 | Steroid | 0.0338028169014 | 0.0 | 0.101449275362 | 0.0
 | Bleeding Disorder | 0.00845070422535 | 0.0 | 0.0289855072464 | 0.0
 | Functional Health Status | 0.0056338028169 | 0.0 | 0.0144927536232 | 1.0
 | Pneumonia | 0.0 | 0.0 | 0.0338164251208 | 1.0
 | Reintubation | 0.0 | 0.0 | 0.0193236714976 | 1.0
 | Urinary Infection | 0.0 | 0.0 | 0.0048309178744 | 0.0
 | Ventilator | 0.0 | 0.0 | 0.024154589372 | 0.0
 | Unplanned Readmission | 0.0366197183099 | 0.0 | 0.048309178744 | 0.0
 | Readmission | 0.0366197183099 | 0.0 | 0.0579710144928 | 0.0
 | Superficial SSI | 0.0 | 0.0 | 0.0048309178744 | 0.0
 | Deep SSI | 0.0 | 0.0 | 0.0 | 0.0
 | Organ/Space SSI | 0.0056338028169 | 0.0 | 0.0338164251208 | 0.0
 | Wound Disruption | 0.0 | 0.0 | 0.0 | 0.0
 | Deep Vein Thrombosis | 0.0 | 0.0 | 0.00966183574879 | 0.0
 | Renal Insufficiency | 0.00281690140845 | 0.0 | 0.0 | 0.0
 | Pulmonary Embolism | 0.00281690140845 | 0.0 | 0.0048309178744 | 0.0
 | CVA with Neurologic Deficit | 0.0 | 0.0 | 0.0 | 0.0
 | Cardiac Arrest | 0.0 | 0.0 | 0.0 | 0.0
 | Myocardial Infarction | 0.0 | 0.0 | 0.0 | 0.0
 | Sepsis | 0.00281690140845 | 0.0 | 0.0193236714976 | 0.0
 
 ## Disseminated Cancer Analysis
 | | Non-Disseminated Cancer (N = 551.0) | Disseminated Cancer (N = 14.0) |
| ------------- | ------------- | ------------- |
 | Diabetes | 4.85714285714 | 0.0714285714286 | 
 | Smoke | 8.0 | 0.142857142857 | 
 | Dyspnea | 1.5 | 0.142857142857 | 
 | Ventilator Dependent | 0.0714285714286 | 0.0 | 
 | Ascites | 0.0 | 0.0 | 
 | COPD | 1.42857142857 | 0.0714285714286 | 
 | CGF | 0.214285714286 | 0.0 | 
 | Hypertension | 13.7857142857 | 0.285714285714 | 
 | Acute Renal Failure | 0.0 | 0.0714285714286 | 
 | Disseminated Cancer | 0.0 | 1.0 | 
 | Steroid | 2.14285714286 | 0.214285714286 | 
 | Bleeding Disorder | 0.428571428571 | 0.214285714286 | 
 | Functional Health Status | 0.428571428571 | 0.0 | 
 | Pneumonia | 0.5 | 0.0714285714286 | 
 | Reintubation | 0.357142857143 | 0.0 | 
 | Urinary Infection | 0.0714285714286 | 0.0 | 
 | Ventilator | 0.285714285714 | 0.0714285714286 | 
 | Unplanned Readmission | 1.57142857143 | 0.0714285714286 | 
 | Readmission | 1.71428571429 | 0.0714285714286 | 
 | Superficial SSI | 0.0714285714286 | 0.0 | 
 | Deep SSI | 0.0 | 0.0 | 
 | Organ/Space SSI | 0.642857142857 | 0.0 | 
 | Wound Disruption | 0.0 | 0.0 | 
 | Deep Vein Thrombosis | 0.142857142857 | 0.0 | 
 | Renal Insufficiency | 0.0714285714286 | 0.0 | 
 | Pulmonary Embolism | 0.142857142857 | 0.0 | 
 | CVA with Neurologic Deficit | 0.0 | 0.0 | 
 | Cardiac Arrest | 0.0 | 0.0 | 
 | Myocardial Infarction | 0.0 | 0.0 | 
 | Sepsis | 0.357142857143 | 0.0 | 
 
| | Outpatient Non-Disseminated Cancer (N = 356) | Outpatient Disseminated Cancer (N = 1) |  Inpatient Non-Disseminated Cancer (N = 195) | Inpatient Disseminated Cancer (N = 13) |
| ------------- | ------------- | ------------- | ------------- | ------------- |
 | Diabetes | 0.0842696629213 | 0.0 | 0.194871794872 | 0.0769230769231
 | Smoke | 0.191011235955 | 0.0 | 0.225641025641 | 0.153846153846
 | Dyspnea | 0.0337078651685 | 0.0 | 0.0461538461538 | 0.153846153846
 | Ventilator Dependent | 0.0 | 0.0 | 0.00512820512821 | 0.0
 | Ascites | 0.0 | 0.0 | 0.0 | 0.0
 | COPD | 0.0252808988764 | 0.0 | 0.0564102564103 | 0.0769230769231
 | CGF | 0.00561797752809 | 0.0 | 0.00512820512821 | 0.0
 | Hypertension | 0.280898876404 | 1.0 | 0.476923076923 | 0.230769230769
 | Acute Renal Failure | 0.0 | 0.0 | 0.0 | 0.0769230769231
 | Disseminated Cancer | 0.0 | 1.0 | 0.0 | 1.0
 | Steroid | 0.0337078651685 | 0.0 | 0.0923076923077 | 0.230769230769
 | Bleeding Disorder | 0.00842696629213 | 0.0 | 0.0153846153846 | 0.230769230769
 | Functional Health Status | 0.00561797752809 | 0.0 | 0.0205128205128 | 0.0
 | Pneumonia | 0.0 | 0.0 | 0.0358974358974 | 0.0769230769231
 | Reintubation | 0.0 | 0.0 | 0.025641025641 | 0.0
 | Urinary Infection | 0.0 | 0.0 | 0.00512820512821 | 0.0
 | Ventilator | 0.0 | 0.0 | 0.0205128205128 | 0.0769230769231
 | Unplanned Readmission | 0.0365168539326 | 0.0 | 0.0461538461538 | 0.0769230769231
 | Readmission | 0.0365168539326 | 0.0 | 0.0564102564103 | 0.0769230769231
 | Superficial SSI | 0.0 | 0.0 | 0.00512820512821 | 0.0
 | Deep SSI | 0.0 | 0.0 | 0.0 | 0.0
 | Organ/Space SSI | 0.00561797752809 | 0.0 | 0.0358974358974 | 0.0
 | Wound Disruption | 0.0 | 0.0 | 0.0 | 0.0
 | Deep Vein Thrombosis | 0.0 | 0.0 | 0.0102564102564 | 0.0
 | Renal Insufficiency | 0.00280898876404 | 0.0 | 0.0 | 0.0
 | Pulmonary Embolism | 0.00280898876404 | 0.0 | 0.00512820512821 | 0.0
 | CVA with Neurologic Deficit | 0.0 | 0.0 | 0.0 | 0.0
 | Cardiac Arrest | 0.0 | 0.0 | 0.0 | 0.0
 | Myocardial Infarction | 0.0 | 0.0 | 0.0 | 0.0
 | Sepsis | 0.00280898876404 | 0.0 | 0.0205128205128 | 0.0
 
 ## Steroid Analysis
 | | Non-Steroid (N = 532.0) | Steroid (N = 33.0) |
| ------------- | ------------- | ------------- |
 | Diabetes | 2.0303030303 | 0.0606060606061 | 
 | Smoke | 3.33333333333 | 0.121212121212 | 
 | Dyspnea | 0.636363636364 | 0.0606060606061 | 
 | Ventilator Dependent | 0.030303030303 | 0.0 | 
 | Ascites | 0.0 | 0.0 | 
 | COPD | 0.545454545455 | 0.0909090909091 | 
 | CGF | 0.0909090909091 | 0.0 | 
 | Hypertension | 5.54545454545 | 0.424242424242 | 
 | Acute Renal Failure | 0.0 | 0.030303030303 | 
 | Disseminated Cancer | 0.333333333333 | 0.0909090909091 | 
 | Steroid | 0.0 | 1.0 | 
 | Bleeding Disorder | 0.181818181818 | 0.0909090909091 | 
 | Functional Health Status | 0.151515151515 | 0.030303030303 | 
 | Pneumonia | 0.212121212121 | 0.030303030303 | 
 | Reintubation | 0.121212121212 | 0.030303030303 | 
 | Urinary Infection | 0.030303030303 | 0.0 | 
 | Ventilator | 0.0909090909091 | 0.0606060606061 | 
 | Unplanned Readmission | 0.69696969697 | 0.0 | 
 | Readmission | 0.757575757576 | 0.0 | 
 | Superficial SSI | 0.030303030303 | 0.0 | 
 | Deep SSI | 0.0 | 0.0 | 
 | Organ/Space SSI | 0.212121212121 | 0.0606060606061 | 
 | Wound Disruption | 0.0 | 0.0 | 
 | Deep Vein Thrombosis | 0.0606060606061 | 0.0 | 
 | Renal Insufficiency | 0.030303030303 | 0.0 | 
 | Pulmonary Embolism | 0.030303030303 | 0.030303030303 | 
 | CVA with Neurologic Deficit | 0.0 | 0.0 | 
 | Cardiac Arrest | 0.0 | 0.0 | 
 | Myocardial Infarction | 0.0 | 0.0 | 
 | Sepsis | 0.0909090909091 | 0.0606060606061 | 
 
| | Outpatient Non-Steroid (N = 345) | Outpatient Steroid (N = 12) |  Inpatient Non-Steroid (N = 187) | Inpatient Steroid (N = 21) |
| ------------- | ------------- | ------------- | ------------- | ------------- |
 | Diabetes | 0.0869565217391 | 0.0 | 0.197860962567 | 0.0952380952381
 | Smoke | 0.191304347826 | 0.166666666667 | 0.235294117647 | 0.0952380952381
 | Dyspnea | 0.031884057971 | 0.0833333333333 | 0.0534759358289 | 0.047619047619
 | Ventilator Dependent | 0.0 | 0.0 | 0.00534759358289 | 0.0
 | Ascites | 0.0 | 0.0 | 0.0 | 0.0
 | COPD | 0.0231884057971 | 0.0833333333333 | 0.0534759358289 | 0.0952380952381
 | CGF | 0.00579710144928 | 0.0 | 0.00534759358289 | 0.0
 | Hypertension | 0.278260869565 | 0.416666666667 | 0.465240641711 | 0.428571428571
 | Acute Renal Failure | 0.0 | 0.0 | 0.0 | 0.047619047619
 | Disseminated Cancer | 0.00289855072464 | 0.0 | 0.0534759358289 | 0.142857142857
 | Steroid | 0.0 | 1.0 | 0.0 | 1.0
 | Bleeding Disorder | 0.00869565217391 | 0.0 | 0.0160427807487 | 0.142857142857
 | Functional Health Status | 0.00579710144928 | 0.0 | 0.0160427807487 | 0.047619047619
 | Pneumonia | 0.0 | 0.0 | 0.0374331550802 | 0.047619047619
 | Reintubation | 0.0 | 0.0 | 0.0213903743316 | 0.047619047619
 | Urinary Infection | 0.0 | 0.0 | 0.00534759358289 | 0.0
 | Ventilator | 0.0 | 0.0 | 0.0160427807487 | 0.0952380952381
 | Unplanned Readmission | 0.0376811594203 | 0.0 | 0.0534759358289 | 0.0
 | Readmission | 0.0376811594203 | 0.0 | 0.0641711229947 | 0.0
 | Superficial SSI | 0.0 | 0.0 | 0.00534759358289 | 0.0
 | Deep SSI | 0.0 | 0.0 | 0.0 | 0.0
 | Organ/Space SSI | 0.00579710144928 | 0.0 | 0.0267379679144 | 0.0952380952381
 | Wound Disruption | 0.0 | 0.0 | 0.0 | 0.0
 | Deep Vein Thrombosis | 0.0 | 0.0 | 0.0106951871658 | 0.0
 | Renal Insufficiency | 0.00289855072464 | 0.0 | 0.0 | 0.0
 | Pulmonary Embolism | 0.00289855072464 | 0.0 | 0.0 | 0.047619047619
 | CVA with Neurologic Deficit | 0.0 | 0.0 | 0.0 | 0.0
 | Cardiac Arrest | 0.0 | 0.0 | 0.0 | 0.0
 | Myocardial Infarction | 0.0 | 0.0 | 0.0 | 0.0
 | Sepsis | 0.00289855072464 | 0.0 | 0.0106951871658 | 0.0952380952381
 
 ## Bleeding Disorder
 
| | Non-Bleeding Disorder (N = 556.0) | Bleeding Disorder (N = 9.0) |
| ------------- | ------------- | ------------- |
 | Diabetes | 7.44444444444 | 0.222222222222 | 
 | Smoke | 12.6666666667 | 0.0 | 
 | Dyspnea | 2.33333333333 | 0.222222222222 | 
 | Ventilator Dependent | 0.111111111111 | 0.0 | 
 | Ascites | 0.0 | 0.0 | 
 | COPD | 2.11111111111 | 0.222222222222 | 
 | CGF | 0.333333333333 | 0.0 | 
 | Hypertension | 21.4444444444 | 0.444444444444 | 
 | Acute Renal Failure | 0.0 | 0.111111111111 | 
 | Disseminated Cancer | 1.22222222222 | 0.333333333333 | 
 | Steroid | 3.33333333333 | 0.333333333333 | 
 | Bleeding Disorder | 0.0 | 1.0 | 
 | Functional Health Status | 0.666666666667 | 0.0 | 
 | Pneumonia | 0.888888888889 | 0.0 | 
 | Reintubation | 0.555555555556 | 0.0 | 
 | Urinary Infection | 0.111111111111 | 0.0 | 
 | Ventilator | 0.444444444444 | 0.111111111111 | 
 | Unplanned Readmission | 2.55555555556 | 0.0 | 
 | Readmission | 2.77777777778 | 0.0 | 
 | Superficial SSI | 0.111111111111 | 0.0 | 
 | Deep SSI | 0.0 | 0.0 | 
 | Organ/Space SSI | 1.0 | 0.0 | 
 | Wound Disruption | 0.0 | 0.0 | 
 | Deep Vein Thrombosis | 0.222222222222 | 0.0 | 
 | Renal Insufficiency | 0.111111111111 | 0.0 | 
 | Pulmonary Embolism | 0.222222222222 | 0.0 | 
 | CVA with Neurologic Deficit | 0.0 | 0.0 | 
 | Cardiac Arrest | 0.0 | 0.0 | 
 | Myocardial Infarction | 0.0 | 0.0 | 
 | Sepsis | 0.555555555556 | 0.0 | 
 
| | Outpatient Non-Bleeding Disorder (N = 354) | Outpatient Bleeding Disorder (N = 3) |  Inpatient Non-Bleeding Disorder (N = 202) | Inpatient Bleeding Disorder (N = 6) |
| ------------- | ------------- | ------------- | ------------- | ------------- |
 | Diabetes | 0.0847457627119 | 0.0 | 0.183168316832 | 0.333333333333
 | Smoke | 0.19209039548 | 0.0 | 0.227722772277 | 0.0
 | Dyspnea | 0.0310734463277 | 0.333333333333 | 0.049504950495 | 0.166666666667
 | Ventilator Dependent | 0.0 | 0.0 | 0.0049504950495 | 0.0
 | Ascites | 0.0 | 0.0 | 0.0 | 0.0
 | COPD | 0.0225988700565 | 0.333333333333 | 0.0544554455446 | 0.166666666667
 | CGF | 0.00564971751412 | 0.0 | 0.0049504950495 | 0.0
 | Hypertension | 0.282485875706 | 0.333333333333 | 0.460396039604 | 0.5
 | Acute Renal Failure | 0.0 | 0.0 | 0.0 | 0.166666666667
 | Disseminated Cancer | 0.00282485875706 | 0.0 | 0.049504950495 | 0.5
 | Steroid | 0.0338983050847 | 0.0 | 0.0891089108911 | 0.5
 | Bleeding Disorder | 0.0 | 1.0 | 0.0 | 1.0
 | Functional Health Status | 0.00564971751412 | 0.0 | 0.019801980198 | 0.0
 | Pneumonia | 0.0 | 0.0 | 0.039603960396 | 0.0
 | Reintubation | 0.0 | 0.0 | 0.0247524752475 | 0.0
 | Urinary Infection | 0.0 | 0.0 | 0.0049504950495 | 0.0
 | Ventilator | 0.0 | 0.0 | 0.019801980198 | 0.166666666667
 | Unplanned Readmission | 0.0367231638418 | 0.0 | 0.049504950495 | 0.0
 | Readmission | 0.0367231638418 | 0.0 | 0.0594059405941 | 0.0
 | Superficial SSI | 0.0 | 0.0 | 0.0049504950495 | 0.0
 | Deep SSI | 0.0 | 0.0 | 0.0 | 0.0
 | Organ/Space SSI | 0.00564971751412 | 0.0 | 0.0346534653465 | 0.0
 | Wound Disruption | 0.0 | 0.0 | 0.0 | 0.0
 | Deep Vein Thrombosis | 0.0 | 0.0 | 0.00990099009901 | 0.0
 | Renal Insufficiency | 0.00282485875706 | 0.0 | 0.0 | 0.0
 | Pulmonary Embolism | 0.00282485875706 | 0.0 | 0.0049504950495 | 0.0
 | CVA with Neurologic Deficit | 0.0 | 0.0 | 0.0 | 0.0
 | Cardiac Arrest | 0.0 | 0.0 | 0.0 | 0.0
 | Myocardial Infarction | 0.0 | 0.0 | 0.0 | 0.0
 | Sepsis | 0.00282485875706 | 0.0 | 0.019801980198 | 0.0
 
 ## Functional Health Status Analysis
 | | Non-Functional Health Status (N = 559.0) | Functional Health Status (N = 6.0) |
| ------------- | ------------- | ------------- |
 | Diabetes | 11.0 | 0.5 | 
 | Smoke | 18.6666666667 | 0.333333333333 | 
 | Dyspnea | 3.83333333333 | 0.0 | 
 | Ventilator Dependent | 0.166666666667 | 0.0 | 
 | Ascites | 0.0 | 0.0 | 
 | COPD | 3.5 | 0.0 | 
 | CGF | 0.333333333333 | 0.166666666667 | 
 | Hypertension | 32.1666666667 | 0.666666666667 | 
 | Acute Renal Failure | 0.166666666667 | 0.0 | 
 | Disseminated Cancer | 2.33333333333 | 0.0 | 
 | Steroid | 5.33333333333 | 0.166666666667 | 
 | Bleeding Disorder | 1.5 | 0.0 | 
 | Functional Health Status | 0.0 | 1.0 | 
 | Pneumonia | 1.16666666667 | 0.166666666667 | 
 | Reintubation | 0.666666666667 | 0.166666666667 | 
 | Urinary Infection | 0.166666666667 | 0.0 | 
 | Ventilator | 0.666666666667 | 0.166666666667 | 
 | Unplanned Readmission | 3.83333333333 | 0.0 | 
 | Readmission | 4.16666666667 | 0.0 | 
 | Superficial SSI | 0.166666666667 | 0.0 | 
 | Deep SSI | 0.0 | 0.0 | 
 | Organ/Space SSI | 1.33333333333 | 0.166666666667 | 
 | Wound Disruption | 0.0 | 0.0 | 
 | Deep Vein Thrombosis | 0.333333333333 | 0.0 | 
 | Renal Insufficiency | 0.166666666667 | 0.0 | 
 | Pulmonary Embolism | 0.333333333333 | 0.0 | 
 | CVA with Neurologic Deficit | 0.0 | 0.0 | 
 | Cardiac Arrest | 0.0 | 0.0 | 
 | Myocardial Infarction | 0.0 | 0.0 | 
 | Sepsis | 0.833333333333 | 0.0 | 
 
| | Outpatient Non-Functional Health Status (N = 355) | Outpatient Functional Health Status (N = 2) |  Inpatient Non-Functional Health Status (N = 204) | Inpatient Functional Health Status (N = 4) |
| ------------- | ------------- | ------------- | ------------- | ------------- |
 | Diabetes | 0.0816901408451 | 0.5 | 0.18137254902 | 0.5
 | Smoke | 0.188732394366 | 0.5 | 0.220588235294 | 0.25
 | Dyspnea | 0.0338028169014 | 0.0 | 0.0539215686275 | 0.0
 | Ventilator Dependent | 0.0 | 0.0 | 0.00490196078431 | 0.0
 | Ascites | 0.0 | 0.0 | 0.0 | 0.0
 | COPD | 0.0253521126761 | 0.0 | 0.0588235294118 | 0.0
 | CGF | 0.0056338028169 | 0.0 | 0.0 | 0.25
 | Hypertension | 0.278873239437 | 1.0 | 0.460784313725 | 0.5
 | Acute Renal Failure | 0.0 | 0.0 | 0.00490196078431 | 0.0
 | Disseminated Cancer | 0.00281690140845 | 0.0 | 0.0637254901961 | 0.0
 | Steroid | 0.0338028169014 | 0.0 | 0.0980392156863 | 0.25
 | Bleeding Disorder | 0.00845070422535 | 0.0 | 0.0294117647059 | 0.0
 | Functional Health Status | 0.0 | 1.0 | 0.0 | 1.0
 | Pneumonia | 0.0 | 0.0 | 0.0343137254902 | 0.25
 | Reintubation | 0.0 | 0.0 | 0.0196078431373 | 0.25
 | Urinary Infection | 0.0 | 0.0 | 0.00490196078431 | 0.0
 | Ventilator | 0.0 | 0.0 | 0.0196078431373 | 0.25
 | Unplanned Readmission | 0.0366197183099 | 0.0 | 0.0490196078431 | 0.0
 | Readmission | 0.0366197183099 | 0.0 | 0.0588235294118 | 0.0
 | Superficial SSI | 0.0 | 0.0 | 0.00490196078431 | 0.0
 | Deep SSI | 0.0 | 0.0 | 0.0 | 0.0
 | Organ/Space SSI | 0.0056338028169 | 0.0 | 0.0294117647059 | 0.25
 | Wound Disruption | 0.0 | 0.0 | 0.0 | 0.0
 | Deep Vein Thrombosis | 0.0 | 0.0 | 0.00980392156863 | 0.0
 | Renal Insufficiency | 0.00281690140845 | 0.0 | 0.0 | 0.0
 | Pulmonary Embolism | 0.00281690140845 | 0.0 | 0.00490196078431 | 0.0
 | CVA with Neurologic Deficit | 0.0 | 0.0 | 0.0 | 0.0
 | Cardiac Arrest | 0.0 | 0.0 | 0.0 | 0.0
 | Myocardial Infarction | 0.0 | 0.0 | 0.0 | 0.0
 | Sepsis | 0.00281690140845 | 0.0 | 0.0196078431373 | 0.0
 
 
 ### Notes
 I did not perform this analysis for Ventilator Dependent, Ascites, and Acute Renal Failure due to lack of patients with the conditions in both outpatient and inpatient settings. 








