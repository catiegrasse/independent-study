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
 | Diabetes | 0.0% | 100.0% | 
 | Smoke | 144.927536232% | 20.2898550725% | 
 | Dyspnea | 26.0869565217% | 7.24637681159% | 
 | Ventilator Dependent | 1.44927536232% | 0.0% | 
 | Ascites | 0.0% | 0.0% | 
 | COPD | 20.2898550725% | 10.1449275362% | 
 | CGF | 2.89855072464% | 1.44927536232% | 
 | Hypertension | 208.695652174% | 76.8115942029% | 
 | Acute Renal Failure | 1.44927536232% | 0.0% | 
 | Disseminated Cancer | 18.8405797101% | 1.44927536232% | 
 | Steroid | 44.9275362319% | 2.89855072464% | 
 | Bleeding Disorder | 10.1449275362% | 2.89855072464% | 
 | Functional Health Status | 4.34782608696% | 4.34782608696% | 
 | Pneumonia | 5.79710144928% | 5.79710144928% | 
 | Reintubation | 2.89855072464% | 4.34782608696% | 
 | Urinary Infection | 1.44927536232% | 0.0% | 
 | Ventilator | 4.34782608696% | 2.89855072464% | 
 | Unplanned Readmission | 27.5362318841% | 5.79710144928% | 
 | Readmission | 30.4347826087% | 5.79710144928% | 
 | Superficial SSI | 1.44927536232% | 0.0% | 
 | Deep SSI | 0.0% | 0.0% | 
 | Organ/Space SSI | 10.1449275362% | 2.89855072464% | 
 | Wound Disruption | 0.0% | 0.0% | 
 | Deep Vein Thrombosis | 1.44927536232% | 1.44927536232% | 
 | Renal Insufficiency | 1.44927536232% | 0.0% | 
 | Pulmonary Embolism | 2.89855072464% | 0.0% | 
 | CVA with Neurologic Deficit | 0.0% | 0.0% | 
 | Cardiac Arrest | 0.0% | 0.0% | 
 | Myocardial Infarction | 0.0% | 0.0% | 
 | Sepsis | 7.24637681159% | 0.0% | 
 
| | Outpatient Non-Diabetes (N = 327) | Outpatient Diabetes (N = 30) |  Inpatient Non-Diabetes (N = 169) | Inpatient Diabetes (N = 39) |
| ------------- | ------------- | ------------- | ------------- | ------------- |
 | Diabetes | 0.0% | 100.0% | 0.0% | 100.0% | 
 | Smoke | 18.9602446483% | 20.0% | 22.4852071006% | 20.5128205128% | 
 | Dyspnea | 3.36391437309% | 3.33333333333% | 4.14201183432% | 10.2564102564% | 
 | Ventilator Dependent | 0.0% | 0.0% | 0.591715976331% | 0.0% | 
 | Ascites | 0.0% | 0.0% | 0.0% | 0.0% | 
 | COPD | 2.75229357798% | 0.0% | 2.95857988166% | 17.9487179487% | 
 | CGF | 0.611620795107% | 0.0% | 0.0% | 2.5641025641% | 
 | Hypertension | 24.1590214067% | 73.3333333333% | 38.4615384615% | 79.4871794872% | 
 | Acute Renal Failure | 0.0% | 0.0% | 0.591715976331% | 0.0% | 
 | Disseminated Cancer | 0.305810397554% | 0.0% | 7.10059171598% | 2.5641025641% | 
 | Steroid | 3.66972477064% | 0.0% | 11.2426035503% | 5.12820512821% | 
 | Bleeding Disorder | 0.917431192661% | 0.0% | 2.36686390533% | 5.12820512821% | 
 | Functional Health Status | 0.305810397554% | 3.33333333333% | 1.18343195266% | 5.12820512821% | 
 | Pneumonia | 0.0% | 0.0% | 2.36686390533% | 10.2564102564% | 
 | Reintubation | 0.0% | 0.0% | 1.18343195266% | 7.69230769231% | 
 | Urinary Infection | 0.0% | 0.0% | 0.591715976331% | 0.0% | 
 | Ventilator | 0.0% | 0.0% | 1.77514792899% | 5.12820512821% | 
 | Unplanned Readmission | 3.66972477064% | 3.33333333333% | 4.14201183432% | 7.69230769231% | 
 | Readmission | 3.66972477064% | 3.33333333333% | 5.32544378698% | 7.69230769231% | 
 | Superficial SSI | 0.0% | 0.0% | 0.591715976331% | 0.0% | 
 | Deep SSI | 0.0% | 0.0% | 0.0% | 0.0% | 
 | Organ/Space SSI | 0.611620795107% | 0.0% | 2.95857988166% | 5.12820512821% | 
 | Wound Disruption | 0.0% | 0.0% | 0.0% | 0.0% | 
 | Deep Vein Thrombosis | 0.0% | 0.0% | 0.591715976331% | 2.5641025641% | 
 | Renal Insufficiency | 0.305810397554% | 0.0% | 0.0% | 0.0% | 
 | Pulmonary Embolism | 0.305810397554% | 0.0% | 0.591715976331% | 0.0% | 
 | CVA with Neurologic Deficit | 0.0% | 0.0% | 0.0% | 0.0% | 
 | Cardiac Arrest | 0.0% | 0.0% | 0.0% | 0.0% | 
 | Myocardial Infarction | 0.0% | 0.0% | 0.0% | 0.0% | 
 | Sepsis | 0.305810397554% | 0.0% | 2.36686390533% | 0.0% | 
 
 ## Smoking Analysis
| | Non-Smoke (N = 451.0) | Smoke (N = 114.0) |
| ------------- | ------------- | ------------- |
 | Diabetes | 48.2456140351% | 12.2807017544% | 
 | Smoke | 0.0% | 100.0% | 
 | Dyspnea | 10.5263157895% | 9.64912280702% | 
 | Ventilator Dependent | 0.0% | 0.877192982456% | 
 | Ascites | 0.0% | 0.0% | 
 | COPD | 11.4035087719% | 7.01754385965% | 
 | CGF | 1.75438596491% | 0.877192982456% | 
 | Hypertension | 122.807017544% | 50.0% | 
 | Acute Renal Failure | 0.877192982456% | 0.0% | 
 | Disseminated Cancer | 10.5263157895% | 1.75438596491% | 
 | Steroid | 25.4385964912% | 3.50877192982% | 
 | Bleeding Disorder | 7.89473684211% | 0.0% | 
 | Functional Health Status | 3.50877192982% | 1.75438596491% | 
 | Pneumonia | 6.14035087719% | 0.877192982456% | 
 | Reintubation | 3.50877192982% | 0.877192982456% | 
 | Urinary Infection | 0.877192982456% | 0.0% | 
 | Ventilator | 2.63157894737% | 1.75438596491% | 
 | Unplanned Readmission | 14.0350877193% | 6.14035087719% | 
 | Readmission | 14.9122807018% | 7.01754385965% | 
 | Superficial SSI | 0.877192982456% | 0.0% | 
 | Deep SSI | 0.0% | 0.0% | 
 | Organ/Space SSI | 3.50877192982% | 4.38596491228% | 
 | Wound Disruption | 0.0% | 0.0% | 
 | Deep Vein Thrombosis | 0.877192982456% | 0.877192982456% | 
 | Renal Insufficiency | 0.877192982456% | 0.0% | 
 | Pulmonary Embolism | 0.0% | 1.75438596491% | 
 | CVA with Neurologic Deficit | 0.0% | 0.0% | 
 | Cardiac Arrest | 0.0% | 0.0% | 
 | Myocardial Infarction | 0.0% | 0.0% | 
 | Sepsis | 2.63157894737% | 1.75438596491% | 


| | Outpatient Non-Smoke (N = 289) | Outpatient Smoke (N = 68) |  Inpatient Non-Smoke (N = 162) | Inpatient Smoke (N = 46) |
| ------------- | ------------- | ------------- | ------------- | ------------- |
 | Diabetes | 8.3044982699% | 8.82352941176% | 19.1358024691% | 17.3913043478% | 
 | Smoke | 0.0% | 100.0% | 0.0% | 100.0% | 
 | Dyspnea | 2.42214532872% | 7.35294117647% | 3.08641975309% | 13.0434782609% | 
 | Ventilator Dependent | 0.0% | 0.0% | 0.0% | 2.17391304348% | 
 | Ascites | 0.0% | 0.0% | 0.0% | 0.0% | 
 | COPD | 1.73010380623% | 5.88235294118% | 4.93827160494% | 8.69565217391% | 
 | CGF | 0.346020761246% | 1.47058823529% | 0.617283950617% | 0.0% | 
 | Hypertension | 23.875432526% | 47.0588235294% | 43.8271604938% | 54.347826087% | 
 | Acute Renal Failure | 0.0% | 0.0% | 0.617283950617% | 0.0% | 
 | Disseminated Cancer | 0.346020761246% | 0.0% | 6.79012345679% | 4.34782608696% | 
 | Steroid | 3.46020761246% | 2.94117647059% | 11.7283950617% | 4.34782608696% | 
 | Bleeding Disorder | 1.03806228374% | 0.0% | 3.7037037037% | 0.0% | 
 | Functional Health Status | 0.346020761246% | 1.47058823529% | 1.85185185185% | 2.17391304348% | 
 | Pneumonia | 0.0% | 0.0% | 4.32098765432% | 2.17391304348% | 
 | Reintubation | 0.0% | 0.0% | 2.46913580247% | 2.17391304348% | 
 | Urinary Infection | 0.0% | 0.0% | 0.617283950617% | 0.0% | 
 | Ventilator | 0.0% | 0.0% | 1.85185185185% | 4.34782608696% | 
 | Unplanned Readmission | 3.11418685121% | 5.88235294118% | 4.32098765432% | 6.52173913043% | 
 | Readmission | 3.11418685121% | 5.88235294118% | 4.93827160494% | 8.69565217391% | 
 | Superficial SSI | 0.0% | 0.0% | 0.617283950617% | 0.0% | 
 | Deep SSI | 0.0% | 0.0% | 0.0% | 0.0% | 
 | Organ/Space SSI | 0.692041522491% | 0.0% | 1.23456790123% | 10.8695652174% | 
 | Wound Disruption | 0.0% | 0.0% | 0.0% | 0.0% | 
 | Deep Vein Thrombosis | 0.0% | 0.0% | 0.617283950617% | 2.17391304348% | 
 | Renal Insufficiency | 0.346020761246% | 0.0% | 0.0% | 0.0% | 
 | Pulmonary Embolism | 0.0% | 1.47058823529% | 0.0% | 2.17391304348% | 
 | CVA with Neurologic Deficit | 0.0% | 0.0% | 0.0% | 0.0% | 
 | Cardiac Arrest | 0.0% | 0.0% | 0.0% | 0.0% | 
 | Myocardial Infarction | 0.0% | 0.0% | 0.0% | 0.0% | 
 | Sepsis | 0.346020761246% | 0.0% | 1.23456790123% | 4.34782608696% | 
 
 ## Hypertension Analysis
 | | Non-Hypertension (N = 368.0) | Hypertension (N = 197.0) |
| ------------- | ------------- | ------------- |
 | Diabetes | 8.12182741117% | 26.9035532995% | 
 | Smoke | 28.9340101523% | 28.9340101523% | 
 | Dyspnea | 4.06091370558% | 7.61421319797% | 
 | Ventilator Dependent | 0.0% | 0.507614213198% | 
 | Ascites | 0.0% | 0.0% | 
 | COPD | 2.53807106599% | 8.12182741117% | 
 | CGF | 0.0% | 1.52284263959% | 
 | Hypertension | 0.0% | 100.0% | 
 | Acute Renal Failure | 0.0% | 0.507614213198% | 
 | Disseminated Cancer | 5.07614213198% | 2.03045685279% | 
 | Steroid | 9.64467005076% | 7.10659898477% | 
 | Bleeding Disorder | 2.53807106599% | 2.03045685279% | 
 | Functional Health Status | 1.0152284264% | 2.03045685279% | 
 | Pneumonia | 1.52284263959% | 2.53807106599% | 
 | Reintubation | 1.0152284264% | 1.52284263959% | 
 | Urinary Infection | 0.507614213198% | 0.0% | 
 | Ventilator | 2.03045685279% | 0.507614213198% | 
 | Unplanned Readmission | 5.07614213198% | 6.59898477157% | 
 | Readmission | 5.07614213198% | 7.61421319797% | 
 | Superficial SSI | 0.0% | 0.507614213198% | 
 | Deep SSI | 0.0% | 0.0% | 
 | Organ/Space SSI | 2.03045685279% | 2.53807106599% | 
 | Wound Disruption | 0.0% | 0.0% | 
 | Deep Vein Thrombosis | 0.507614213198% | 0.507614213198% | 
 | Renal Insufficiency | 0.0% | 0.507614213198% | 
 | Pulmonary Embolism | 0.507614213198% | 0.507614213198% | 
 | CVA with Neurologic Deficit | 0.0% | 0.0% | 
 | Cardiac Arrest | 0.0% | 0.0% | 
 | Myocardial Infarction | 0.0% | 0.0% | 
 | Sepsis | 0.507614213198% | 2.03045685279% | 


| | Outpatient Non-Hypertension (N = 256) | Outpatient Hypertension (N = 101) |  Inpatient Non-Hypertension (N = 112) | Inpatient Hypertension (N = 96) |
| ------------- | ------------- | ------------- | ------------- | ------------- |
 | Diabetes | 3.125% | 21.7821782178% | 7.14285714286% | 32.2916666667% | 
 | Smoke | 14.0625% | 31.6831683168% | 18.75% | 26.0416666667% | 
 | Dyspnea | 1.953125% | 6.93069306931% | 2.67857142857% | 8.33333333333% | 
 | Ventilator Dependent | 0.0% | 0.0% | 0.0% | 1.04166666667% | 
 | Ascites | 0.0% | 0.0% | 0.0% | 0.0% | 
 | COPD | 0.78125% | 6.93069306931% | 2.67857142857% | 9.375% | 
 | CGF | 0.0% | 1.9801980198% | 0.0% | 1.04166666667% | 
 | Hypertension | 0.0% | 100.0% | 0.0% | 100.0% | 
 | Acute Renal Failure | 0.0% | 0.0% | 0.0% | 1.04166666667% | 
 | Disseminated Cancer | 0.0% | 0.990099009901% | 8.92857142857% | 3.125% | 
 | Steroid | 2.734375% | 4.9504950495% | 10.7142857143% | 9.375% | 
 | Bleeding Disorder | 0.78125% | 0.990099009901% | 2.67857142857% | 3.125% | 
 | Functional Health Status | 0.0% | 1.9801980198% | 1.78571428571% | 2.08333333333% | 
 | Pneumonia | 0.0% | 0.0% | 2.67857142857% | 5.20833333333% | 
 | Reintubation | 0.0% | 0.0% | 1.78571428571% | 3.125% | 
 | Urinary Infection | 0.0% | 0.0% | 0.892857142857% | 0.0% | 
 | Ventilator | 0.0% | 0.0% | 3.57142857143% | 1.04166666667% | 
 | Unplanned Readmission | 3.125% | 4.9504950495% | 1.78571428571% | 8.33333333333% | 
 | Readmission | 3.125% | 4.9504950495% | 1.78571428571% | 10.4166666667% | 
 | Superficial SSI | 0.0% | 0.0% | 0.0% | 1.04166666667% | 
 | Deep SSI | 0.0% | 0.0% | 0.0% | 0.0% | 
 | Organ/Space SSI | 0.390625% | 0.990099009901% | 2.67857142857% | 4.16666666667% | 
 | Wound Disruption | 0.0% | 0.0% | 0.0% | 0.0% | 
 | Deep Vein Thrombosis | 0.0% | 0.0% | 0.892857142857% | 1.04166666667% | 
 | Renal Insufficiency | 0.0% | 0.990099009901% | 0.0% | 0.0% | 
 | Pulmonary Embolism | 0.390625% | 0.0% | 0.0% | 1.04166666667% | 
 | CVA with Neurologic Deficit | 0.0% | 0.0% | 0.0% | 0.0% | 
 | Cardiac Arrest | 0.0% | 0.0% | 0.0% | 0.0% | 
 | Myocardial Infarction | 0.0% | 0.0% | 0.0% | 0.0% | 
 | Sepsis | 0.0% | 0.990099009901% | 0.892857142857% | 3.125% | 
 
 ## Dyspnea Analysis
 
| | Non-Dyspnea (N = 542.0) | Dyspnea (N = 23.0) |
| ------------- | ------------- | ------------- |
 | Diabetes | 278.260869565% | 21.7391304348% | 
 | Smoke | 447.826086957% | 47.8260869565% | 
 | Dyspnea | 0.0% | 100.0% | 
 | Ventilator Dependent | 4.34782608696% | 0.0% | 
 | Ascites | 0.0% | 0.0% | 
 | COPD | 60.8695652174% | 30.4347826087% | 
 | CGF | 13.0434782609% | 0.0% | 
 | Hypertension | 791.304347826% | 65.2173913043% | 
 | Acute Renal Failure | 0.0% | 4.34782608696% | 
 | Disseminated Cancer | 52.1739130435% | 8.69565217391% | 
 | Steroid | 134.782608696% | 8.69565217391% | 
 | Bleeding Disorder | 30.4347826087% | 8.69565217391% | 
 | Functional Health Status | 26.0869565217% | 0.0% | 
 | Pneumonia | 34.7826086957% | 0.0% | 
 | Reintubation | 21.7391304348% | 0.0% | 
 | Urinary Infection | 4.34782608696% | 0.0% | 
 | Ventilator | 21.7391304348% | 0.0% | 
 | Unplanned Readmission | 95.652173913% | 4.34782608696% | 
 | Readmission | 104.347826087% | 4.34782608696% | 
 | Superficial SSI | 4.34782608696% | 0.0% | 
 | Deep SSI | 0.0% | 0.0% | 
 | Organ/Space SSI | 39.1304347826% | 0.0% | 
 | Wound Disruption | 0.0% | 0.0% | 
 | Deep Vein Thrombosis | 8.69565217391% | 0.0% | 
 | Renal Insufficiency | 4.34782608696% | 0.0% | 
 | Pulmonary Embolism | 8.69565217391% | 0.0% | 
 | CVA with Neurologic Deficit | 0.0% | 0.0% | 
 | Cardiac Arrest | 0.0% | 0.0% | 
 | Myocardial Infarction | 0.0% | 0.0% | 
 | Sepsis | 21.7391304348% | 0.0% | 


| | Outpatient Non-Dyspnea (N = 345) | Outpatient Dyspnea (N = 12) |  Inpatient Non-Dyspnea (N = 197) | Inpatient Dyspnea (N = 11) |
| ------------- | ------------- | ------------- | ------------- | ------------- |
 | Diabetes | 8.40579710145% | 8.33333333333% | 17.7664974619% | 36.3636363636% | 
 | Smoke | 18.2608695652% | 41.6666666667% | 20.3045685279% | 54.5454545455% | 
 | Dyspnea | 0.0% | 100.0% | 0.0% | 100.0% | 
 | Ventilator Dependent | 0.0% | 0.0% | 0.507614213198% | 0.0% | 
 | Ascites | 0.0% | 0.0% | 0.0% | 0.0% | 
 | COPD | 2.02898550725% | 16.6666666667% | 3.55329949239% | 45.4545454545% | 
 | CGF | 0.579710144928% | 0.0% | 0.507614213198% | 0.0% | 
 | Hypertension | 27.2463768116% | 58.3333333333% | 44.6700507614% | 72.7272727273% | 
 | Acute Renal Failure | 0.0% | 0.0% | 0.0% | 9.09090909091% | 
 | Disseminated Cancer | 0.289855072464% | 0.0% | 5.58375634518% | 18.1818181818% | 
 | Steroid | 3.1884057971% | 8.33333333333% | 10.152284264% | 9.09090909091% | 
 | Bleeding Disorder | 0.579710144928% | 8.33333333333% | 2.53807106599% | 9.09090909091% | 
 | Functional Health Status | 0.579710144928% | 0.0% | 2.03045685279% | 0.0% | 
 | Pneumonia | 0.0% | 0.0% | 4.06091370558% | 0.0% | 
 | Reintubation | 0.0% | 0.0% | 2.53807106599% | 0.0% | 
 | Urinary Infection | 0.0% | 0.0% | 0.507614213198% | 0.0% | 
 | Ventilator | 0.0% | 0.0% | 2.53807106599% | 0.0% | 
 | Unplanned Readmission | 3.76811594203% | 0.0% | 4.56852791878% | 9.09090909091% | 
 | Readmission | 3.76811594203% | 0.0% | 5.58375634518% | 9.09090909091% | 
 | Superficial SSI | 0.0% | 0.0% | 0.507614213198% | 0.0% | 
 | Deep SSI | 0.0% | 0.0% | 0.0% | 0.0% | 
 | Organ/Space SSI | 0.579710144928% | 0.0% | 3.55329949239% | 0.0% | 
 | Wound Disruption | 0.0% | 0.0% | 0.0% | 0.0% | 
 | Deep Vein Thrombosis | 0.0% | 0.0% | 1.0152284264% | 0.0% | 
 | Renal Insufficiency | 0.289855072464% | 0.0% | 0.0% | 0.0% | 
 | Pulmonary Embolism | 0.289855072464% | 0.0% | 0.507614213198% | 0.0% | 
 | CVA with Neurologic Deficit | 0.0% | 0.0% | 0.0% | 0.0% | 
 | Cardiac Arrest | 0.0% | 0.0% | 0.0% | 0.0% | 
 | Myocardial Infarction | 0.0% | 0.0% | 0.0% | 0.0% | 
 | Sepsis | 0.289855072464% | 0.0% | 2.03045685279% | 0.0% | 
 
 ## COPD Analysis
 | | Non-COPD (N = 544.0) | COPD (N = 21.0) |
| ------------- | ------------- | ------------- |
 | Diabetes | 295.238095238% | 33.3333333333% | 
 | Smoke | 504.761904762% | 38.0952380952% | 
 | Dyspnea | 76.1904761905% | 33.3333333333% | 
 | Ventilator Dependent | 4.7619047619% | 0.0% | 
 | Ascites | 0.0% | 0.0% | 
 | COPD | 0.0% | 100.0% | 
 | CGF | 4.7619047619% | 9.52380952381% | 
 | Hypertension | 861.904761905% | 76.1904761905% | 
 | Acute Renal Failure | 0.0% | 4.7619047619% | 
 | Disseminated Cancer | 61.9047619048% | 4.7619047619% | 
 | Steroid | 142.857142857% | 14.2857142857% | 
 | Bleeding Disorder | 33.3333333333% | 9.52380952381% | 
 | Functional Health Status | 28.5714285714% | 0.0% | 
 | Pneumonia | 33.3333333333% | 4.7619047619% | 
 | Reintubation | 19.0476190476% | 4.7619047619% | 
 | Urinary Infection | 4.7619047619% | 0.0% | 
 | Ventilator | 19.0476190476% | 4.7619047619% | 
 | Unplanned Readmission | 95.2380952381% | 14.2857142857% | 
 | Readmission | 104.761904762% | 14.2857142857% | 
 | Superficial SSI | 4.7619047619% | 0.0% | 
 | Deep SSI | 0.0% | 0.0% | 
 | Organ/Space SSI | 38.0952380952% | 4.7619047619% | 
 | Wound Disruption | 0.0% | 0.0% | 
 | Deep Vein Thrombosis | 4.7619047619% | 4.7619047619% | 
 | Renal Insufficiency | 0.0% | 4.7619047619% | 
 | Pulmonary Embolism | 9.52380952381% | 0.0% | 
 | CVA with Neurologic Deficit | 0.0% | 0.0% | 
 | Cardiac Arrest | 0.0% | 0.0% | 
 | Myocardial Infarction | 0.0% | 0.0% | 
 | Sepsis | 14.2857142857% | 9.52380952381% | 


| | Outpatient Non-COPD (N = 348) | Outpatient COPD (N = 9) |  Inpatient Non-COPD (N = 196) | Inpatient COPD (N = 12) |
| ------------- | ------------- | ------------- | ------------- | ------------- |
 | Diabetes | 8.62068965517% | 0.0% | 16.3265306122% | 58.3333333333% | 
 | Smoke | 18.3908045977% | 44.4444444444% | 21.4285714286% | 33.3333333333% | 
 | Dyspnea | 2.87356321839% | 22.2222222222% | 3.0612244898% | 41.6666666667% | 
 | Ventilator Dependent | 0.0% | 0.0% | 0.510204081633% | 0.0% | 
 | Ascites | 0.0% | 0.0% | 0.0% | 0.0% | 
 | COPD | 0.0% | 100.0% | 0.0% | 100.0% | 
 | CGF | 0.0% | 22.2222222222% | 0.510204081633% | 0.0% | 
 | Hypertension | 27.0114942529% | 77.7777777778% | 44.387755102% | 75.0% | 
 | Acute Renal Failure | 0.0% | 0.0% | 0.0% | 8.33333333333% | 
 | Disseminated Cancer | 0.287356321839% | 0.0% | 6.12244897959% | 8.33333333333% | 
 | Steroid | 3.16091954023% | 11.1111111111% | 9.69387755102% | 16.6666666667% | 
 | Bleeding Disorder | 0.574712643678% | 11.1111111111% | 2.55102040816% | 8.33333333333% | 
 | Functional Health Status | 0.574712643678% | 0.0% | 2.04081632653% | 0.0% | 
 | Pneumonia | 0.0% | 0.0% | 3.57142857143% | 8.33333333333% | 
 | Reintubation | 0.0% | 0.0% | 2.04081632653% | 8.33333333333% | 
 | Urinary Infection | 0.0% | 0.0% | 0.510204081633% | 0.0% | 
 | Ventilator | 0.0% | 0.0% | 2.04081632653% | 8.33333333333% | 
 | Unplanned Readmission | 3.44827586207% | 11.1111111111% | 4.08163265306% | 16.6666666667% | 
 | Readmission | 3.44827586207% | 11.1111111111% | 5.10204081633% | 16.6666666667% | 
 | Superficial SSI | 0.0% | 0.0% | 0.510204081633% | 0.0% | 
 | Deep SSI | 0.0% | 0.0% | 0.0% | 0.0% | 
 | Organ/Space SSI | 0.287356321839% | 11.1111111111% | 3.57142857143% | 0.0% | 
 | Wound Disruption | 0.0% | 0.0% | 0.0% | 0.0% | 
 | Deep Vein Thrombosis | 0.0% | 0.0% | 0.510204081633% | 8.33333333333% | 
 | Renal Insufficiency | 0.0% | 11.1111111111% | 0.0% | 0.0% | 
 | Pulmonary Embolism | 0.287356321839% | 0.0% | 0.510204081633% | 0.0% | 
 | CVA with Neurologic Deficit | 0.0% | 0.0% | 0.0% | 0.0% | 
 | Cardiac Arrest | 0.0% | 0.0% | 0.0% | 0.0% | 
 | Myocardial Infarction | 0.0% | 0.0% | 0.0% | 0.0% | 
 | Sepsis | 0.0% | 11.1111111111% | 1.5306122449% | 8.33333333333% | 
 
 ## Congestive Heart Failure Analysis
 | | Non-CGF (N = 562.0) | CGF (N = 3.0) |
| ------------- | ------------- | ------------- |
 | Diabetes | 2266.66666667% | 33.3333333333% | 
 | Smoke | 3766.66666667% | 33.3333333333% | 
 | Dyspnea | 766.666666667% | 0.0% | 
 | Ventilator Dependent | 33.3333333333% | 0.0% | 
 | Ascites | 0.0% | 0.0% | 
 | COPD | 633.333333333% | 66.6666666667% | 
 | CGF | 0.0% | 100.0% | 
 | Hypertension | 6466.66666667% | 100.0% | 
 | Acute Renal Failure | 33.3333333333% | 0.0% | 
 | Disseminated Cancer | 466.666666667% | 0.0% | 
 | Steroid | 1100.0% | 0.0% | 
 | Bleeding Disorder | 300.0% | 0.0% | 
 | Functional Health Status | 166.666666667% | 33.3333333333% | 
 | Pneumonia | 233.333333333% | 33.3333333333% | 
 | Reintubation | 133.333333333% | 33.3333333333% | 
 | Urinary Infection | 33.3333333333% | 0.0% | 
 | Ventilator | 166.666666667% | 0.0% | 
 | Unplanned Readmission | 766.666666667% | 0.0% | 
 | Readmission | 833.333333333% | 0.0% | 
 | Superficial SSI | 33.3333333333% | 0.0% | 
 | Deep SSI | 0.0% | 0.0% | 
 | Organ/Space SSI | 300.0% | 0.0% | 
 | Wound Disruption | 0.0% | 0.0% | 
 | Deep Vein Thrombosis | 66.6666666667% | 0.0% | 
 | Renal Insufficiency | 33.3333333333% | 0.0% | 
 | Pulmonary Embolism | 66.6666666667% | 0.0% | 
 | CVA with Neurologic Deficit | 0.0% | 0.0% | 
 | Cardiac Arrest | 0.0% | 0.0% | 
 | Myocardial Infarction | 0.0% | 0.0% | 
 | Sepsis | 166.666666667% | 0.0% | 


| | Outpatient Non-CGF (N = 355) | Outpatient CGF (N = 2) |  Inpatient Non-CGF (N = 207) | Inpatient CGF (N = 1) |
| ------------- | ------------- | ------------- | ------------- | ------------- |
 | Diabetes | 8.45070422535% | 0.0% | 18.3574879227% | 100.0% | 
 | Smoke | 18.8732394366% | 50.0% | 22.2222222222% | 0.0% | 
 | Dyspnea | 3.38028169014% | 0.0% | 5.31400966184% | 0.0% | 
 | Ventilator Dependent | 0.0% | 0.0% | 0.48309178744% | 0.0% | 
 | Ascites | 0.0% | 0.0% | 0.0% | 0.0% | 
 | COPD | 1.97183098592% | 100.0% | 5.79710144928% | 0.0% | 
 | CGF | 0.0% | 100.0% | 0.0% | 100.0% | 
 | Hypertension | 27.8873239437% | 100.0% | 45.8937198068% | 100.0% | 
 | Acute Renal Failure | 0.0% | 0.0% | 0.48309178744% | 0.0% | 
 | Disseminated Cancer | 0.281690140845% | 0.0% | 6.28019323671% | 0.0% | 
 | Steroid | 3.38028169014% | 0.0% | 10.1449275362% | 0.0% | 
 | Bleeding Disorder | 0.845070422535% | 0.0% | 2.89855072464% | 0.0% | 
 | Functional Health Status | 0.56338028169% | 0.0% | 1.44927536232% | 100.0% | 
 | Pneumonia | 0.0% | 0.0% | 3.38164251208% | 100.0% | 
 | Reintubation | 0.0% | 0.0% | 1.93236714976% | 100.0% | 
 | Urinary Infection | 0.0% | 0.0% | 0.48309178744% | 0.0% | 
 | Ventilator | 0.0% | 0.0% | 2.4154589372% | 0.0% | 
 | Unplanned Readmission | 3.66197183099% | 0.0% | 4.8309178744% | 0.0% | 
 | Readmission | 3.66197183099% | 0.0% | 5.79710144928% | 0.0% | 
 | Superficial SSI | 0.0% | 0.0% | 0.48309178744% | 0.0% | 
 | Deep SSI | 0.0% | 0.0% | 0.0% | 0.0% | 
 | Organ/Space SSI | 0.56338028169% | 0.0% | 3.38164251208% | 0.0% | 
 | Wound Disruption | 0.0% | 0.0% | 0.0% | 0.0% | 
 | Deep Vein Thrombosis | 0.0% | 0.0% | 0.966183574879% | 0.0% | 
 | Renal Insufficiency | 0.281690140845% | 0.0% | 0.0% | 0.0% | 
 | Pulmonary Embolism | 0.281690140845% | 0.0% | 0.48309178744% | 0.0% | 
 | CVA with Neurologic Deficit | 0.0% | 0.0% | 0.0% | 0.0% | 
 | Cardiac Arrest | 0.0% | 0.0% | 0.0% | 0.0% | 
 | Myocardial Infarction | 0.0% | 0.0% | 0.0% | 0.0% | 
 | Sepsis | 0.281690140845% | 0.0% | 1.93236714976% | 0.0% | 
 
 ## Disseminated Cancer Analysis
 | | Non-Disseminated Cancer (N = 551.0) | Disseminated Cancer (N = 14.0) |
| ------------- | ------------- | ------------- |
 | Diabetes | 485.714285714% | 7.14285714286% | 
 | Smoke | 800.0% | 14.2857142857% | 
 | Dyspnea | 150.0% | 14.2857142857% | 
 | Ventilator Dependent | 7.14285714286% | 0.0% | 
 | Ascites | 0.0% | 0.0% | 
 | COPD | 142.857142857% | 7.14285714286% | 
 | CGF | 21.4285714286% | 0.0% | 
 | Hypertension | 1378.57142857% | 28.5714285714% | 
 | Acute Renal Failure | 0.0% | 7.14285714286% | 
 | Disseminated Cancer | 0.0% | 100.0% | 
 | Steroid | 214.285714286% | 21.4285714286% | 
 | Bleeding Disorder | 42.8571428571% | 21.4285714286% | 
 | Functional Health Status | 42.8571428571% | 0.0% | 
 | Pneumonia | 50.0% | 7.14285714286% | 
 | Reintubation | 35.7142857143% | 0.0% | 
 | Urinary Infection | 7.14285714286% | 0.0% | 
 | Ventilator | 28.5714285714% | 7.14285714286% | 
 | Unplanned Readmission | 157.142857143% | 7.14285714286% | 
 | Readmission | 171.428571429% | 7.14285714286% | 
 | Superficial SSI | 7.14285714286% | 0.0% | 
 | Deep SSI | 0.0% | 0.0% | 
 | Organ/Space SSI | 64.2857142857% | 0.0% | 
 | Wound Disruption | 0.0% | 0.0% | 
 | Deep Vein Thrombosis | 14.2857142857% | 0.0% | 
 | Renal Insufficiency | 7.14285714286% | 0.0% | 
 | Pulmonary Embolism | 14.2857142857% | 0.0% | 
 | CVA with Neurologic Deficit | 0.0% | 0.0% | 
 | Cardiac Arrest | 0.0% | 0.0% | 
 | Myocardial Infarction | 0.0% | 0.0% | 
 | Sepsis | 35.7142857143% | 0.0% | 


| | Outpatient Non-Disseminated Cancer (N = 356) | Outpatient Disseminated Cancer (N = 1) |  Inpatient Non-Disseminated Cancer (N = 195) | Inpatient Disseminated Cancer (N = 13) |
| ------------- | ------------- | ------------- | ------------- | ------------- |
 | Diabetes | 8.42696629213% | 0.0% | 19.4871794872% | 7.69230769231% | 
 | Smoke | 19.1011235955% | 0.0% | 22.5641025641% | 15.3846153846% | 
 | Dyspnea | 3.37078651685% | 0.0% | 4.61538461538% | 15.3846153846% | 
 | Ventilator Dependent | 0.0% | 0.0% | 0.512820512821% | 0.0% | 
 | Ascites | 0.0% | 0.0% | 0.0% | 0.0% | 
 | COPD | 2.52808988764% | 0.0% | 5.64102564103% | 7.69230769231% | 
 | CGF | 0.561797752809% | 0.0% | 0.512820512821% | 0.0% | 
 | Hypertension | 28.0898876404% | 100.0% | 47.6923076923% | 23.0769230769% | 
 | Acute Renal Failure | 0.0% | 0.0% | 0.0% | 7.69230769231% | 
 | Disseminated Cancer | 0.0% | 100.0% | 0.0% | 100.0% | 
 | Steroid | 3.37078651685% | 0.0% | 9.23076923077% | 23.0769230769% | 
 | Bleeding Disorder | 0.842696629213% | 0.0% | 1.53846153846% | 23.0769230769% | 
 | Functional Health Status | 0.561797752809% | 0.0% | 2.05128205128% | 0.0% | 
 | Pneumonia | 0.0% | 0.0% | 3.58974358974% | 7.69230769231% | 
 | Reintubation | 0.0% | 0.0% | 2.5641025641% | 0.0% | 
 | Urinary Infection | 0.0% | 0.0% | 0.512820512821% | 0.0% | 
 | Ventilator | 0.0% | 0.0% | 2.05128205128% | 7.69230769231% | 
 | Unplanned Readmission | 3.65168539326% | 0.0% | 4.61538461538% | 7.69230769231% | 
 | Readmission | 3.65168539326% | 0.0% | 5.64102564103% | 7.69230769231% | 
 | Superficial SSI | 0.0% | 0.0% | 0.512820512821% | 0.0% | 
 | Deep SSI | 0.0% | 0.0% | 0.0% | 0.0% | 
 | Organ/Space SSI | 0.561797752809% | 0.0% | 3.58974358974% | 0.0% | 
 | Wound Disruption | 0.0% | 0.0% | 0.0% | 0.0% | 
 | Deep Vein Thrombosis | 0.0% | 0.0% | 1.02564102564% | 0.0% | 
 | Renal Insufficiency | 0.280898876404% | 0.0% | 0.0% | 0.0% | 
 | Pulmonary Embolism | 0.280898876404% | 0.0% | 0.512820512821% | 0.0% | 
 | CVA with Neurologic Deficit | 0.0% | 0.0% | 0.0% | 0.0% | 
 | Cardiac Arrest | 0.0% | 0.0% | 0.0% | 0.0% | 
 | Myocardial Infarction | 0.0% | 0.0% | 0.0% | 0.0% | 
 | Sepsis | 0.280898876404% | 0.0% | 2.05128205128% | 0.0% | 
 
 ## Steroid Analysis
 | | Non-Steroid (N = 532.0) | Steroid (N = 33.0) |
| ------------- | ------------- | ------------- |
 | Diabetes | 203.03030303% | 6.06060606061% | 
 | Smoke | 333.333333333% | 12.1212121212% | 
 | Dyspnea | 63.6363636364% | 6.06060606061% | 
 | Ventilator Dependent | 3.0303030303% | 0.0% | 
 | Ascites | 0.0% | 0.0% | 
 | COPD | 54.5454545455% | 9.09090909091% | 
 | CGF | 9.09090909091% | 0.0% | 
 | Hypertension | 554.545454545% | 42.4242424242% | 
 | Acute Renal Failure | 0.0% | 3.0303030303% | 
 | Disseminated Cancer | 33.3333333333% | 9.09090909091% | 
 | Steroid | 0.0% | 100.0% | 
 | Bleeding Disorder | 18.1818181818% | 9.09090909091% | 
 | Functional Health Status | 15.1515151515% | 3.0303030303% | 
 | Pneumonia | 21.2121212121% | 3.0303030303% | 
 | Reintubation | 12.1212121212% | 3.0303030303% | 
 | Urinary Infection | 3.0303030303% | 0.0% | 
 | Ventilator | 9.09090909091% | 6.06060606061% | 
 | Unplanned Readmission | 69.696969697% | 0.0% | 
 | Readmission | 75.7575757576% | 0.0% | 
 | Superficial SSI | 3.0303030303% | 0.0% | 
 | Deep SSI | 0.0% | 0.0% | 
 | Organ/Space SSI | 21.2121212121% | 6.06060606061% | 
 | Wound Disruption | 0.0% | 0.0% | 
 | Deep Vein Thrombosis | 6.06060606061% | 0.0% | 
 | Renal Insufficiency | 3.0303030303% | 0.0% | 
 | Pulmonary Embolism | 3.0303030303% | 3.0303030303% | 
 | CVA with Neurologic Deficit | 0.0% | 0.0% | 
 | Cardiac Arrest | 0.0% | 0.0% | 
 | Myocardial Infarction | 0.0% | 0.0% | 
 | Sepsis | 9.09090909091% | 6.06060606061% | 


| | Outpatient Non-Steroid (N = 345) | Outpatient Steroid (N = 12) |  Inpatient Non-Steroid (N = 187) | Inpatient Steroid (N = 21) |
| ------------- | ------------- | ------------- | ------------- | ------------- |
 | Diabetes | 8.69565217391% | 0.0% | 19.7860962567% | 9.52380952381% | 
 | Smoke | 19.1304347826% | 16.6666666667% | 23.5294117647% | 9.52380952381% | 
 | Dyspnea | 3.1884057971% | 8.33333333333% | 5.34759358289% | 4.7619047619% | 
 | Ventilator Dependent | 0.0% | 0.0% | 0.534759358289% | 0.0% | 
 | Ascites | 0.0% | 0.0% | 0.0% | 0.0% | 
 | COPD | 2.31884057971% | 8.33333333333% | 5.34759358289% | 9.52380952381% | 
 | CGF | 0.579710144928% | 0.0% | 0.534759358289% | 0.0% | 
 | Hypertension | 27.8260869565% | 41.6666666667% | 46.5240641711% | 42.8571428571% | 
 | Acute Renal Failure | 0.0% | 0.0% | 0.0% | 4.7619047619% | 
 | Disseminated Cancer | 0.289855072464% | 0.0% | 5.34759358289% | 14.2857142857% | 
 | Steroid | 0.0% | 100.0% | 0.0% | 100.0% | 
 | Bleeding Disorder | 0.869565217391% | 0.0% | 1.60427807487% | 14.2857142857% | 
 | Functional Health Status | 0.579710144928% | 0.0% | 1.60427807487% | 4.7619047619% | 
 | Pneumonia | 0.0% | 0.0% | 3.74331550802% | 4.7619047619% | 
 | Reintubation | 0.0% | 0.0% | 2.13903743316% | 4.7619047619% | 
 | Urinary Infection | 0.0% | 0.0% | 0.534759358289% | 0.0% | 
 | Ventilator | 0.0% | 0.0% | 1.60427807487% | 9.52380952381% | 
 | Unplanned Readmission | 3.76811594203% | 0.0% | 5.34759358289% | 0.0% | 
 | Readmission | 3.76811594203% | 0.0% | 6.41711229947% | 0.0% | 
 | Superficial SSI | 0.0% | 0.0% | 0.534759358289% | 0.0% | 
 | Deep SSI | 0.0% | 0.0% | 0.0% | 0.0% | 
 | Organ/Space SSI | 0.579710144928% | 0.0% | 2.67379679144% | 9.52380952381% | 
 | Wound Disruption | 0.0% | 0.0% | 0.0% | 0.0% | 
 | Deep Vein Thrombosis | 0.0% | 0.0% | 1.06951871658% | 0.0% | 
 | Renal Insufficiency | 0.289855072464% | 0.0% | 0.0% | 0.0% | 
 | Pulmonary Embolism | 0.289855072464% | 0.0% | 0.0% | 4.7619047619% | 
 | CVA with Neurologic Deficit | 0.0% | 0.0% | 0.0% | 0.0% | 
 | Cardiac Arrest | 0.0% | 0.0% | 0.0% | 0.0% | 
 | Myocardial Infarction | 0.0% | 0.0% | 0.0% | 0.0% | 
 | Sepsis | 0.289855072464% | 0.0% | 1.06951871658% | 9.52380952381% | 
 
 ## Bleeding Disorder
 
| | Non-Bleeding Disorder (N = 556.0) | Bleeding Disorder (N = 9.0) |
| ------------- | ------------- | ------------- |
 | Diabetes | 744.444444444% | 22.2222222222% | 
 | Smoke | 1266.66666667% | 0.0% | 
 | Dyspnea | 233.333333333% | 22.2222222222% | 
 | Ventilator Dependent | 11.1111111111% | 0.0% | 
 | Ascites | 0.0% | 0.0% | 
 | COPD | 211.111111111% | 22.2222222222% | 
 | CGF | 33.3333333333% | 0.0% | 
 | Hypertension | 2144.44444444% | 44.4444444444% | 
 | Acute Renal Failure | 0.0% | 11.1111111111% | 
 | Disseminated Cancer | 122.222222222% | 33.3333333333% | 
 | Steroid | 333.333333333% | 33.3333333333% | 
 | Bleeding Disorder | 0.0% | 100.0% | 
 | Functional Health Status | 66.6666666667% | 0.0% | 
 | Pneumonia | 88.8888888889% | 0.0% | 
 | Reintubation | 55.5555555556% | 0.0% | 
 | Urinary Infection | 11.1111111111% | 0.0% | 
 | Ventilator | 44.4444444444% | 11.1111111111% | 
 | Unplanned Readmission | 255.555555556% | 0.0% | 
 | Readmission | 277.777777778% | 0.0% | 
 | Superficial SSI | 11.1111111111% | 0.0% | 
 | Deep SSI | 0.0% | 0.0% | 
 | Organ/Space SSI | 100.0% | 0.0% | 
 | Wound Disruption | 0.0% | 0.0% | 
 | Deep Vein Thrombosis | 22.2222222222% | 0.0% | 
 | Renal Insufficiency | 11.1111111111% | 0.0% | 
 | Pulmonary Embolism | 22.2222222222% | 0.0% | 
 | CVA with Neurologic Deficit | 0.0% | 0.0% | 
 | Cardiac Arrest | 0.0% | 0.0% | 
 | Myocardial Infarction | 0.0% | 0.0% | 
 | Sepsis | 55.5555555556% | 0.0% | 


| | Outpatient Non-Bleeding Disorder (N = 354) | Outpatient Bleeding Disorder (N = 3) |  Inpatient Non-Bleeding Disorder (N = 202) | Inpatient Bleeding Disorder (N = 6) |
| ------------- | ------------- | ------------- | ------------- | ------------- |
 | Diabetes | 8.47457627119% | 0.0% | 18.3168316832% | 33.3333333333% | 
 | Smoke | 19.209039548% | 0.0% | 22.7722772277% | 0.0% | 
 | Dyspnea | 3.10734463277% | 33.3333333333% | 4.9504950495% | 16.6666666667% | 
 | Ventilator Dependent | 0.0% | 0.0% | 0.49504950495% | 0.0% | 
 | Ascites | 0.0% | 0.0% | 0.0% | 0.0% | 
 | COPD | 2.25988700565% | 33.3333333333% | 5.44554455446% | 16.6666666667% | 
 | CGF | 0.564971751412% | 0.0% | 0.49504950495% | 0.0% | 
 | Hypertension | 28.2485875706% | 33.3333333333% | 46.0396039604% | 50.0% | 
 | Acute Renal Failure | 0.0% | 0.0% | 0.0% | 16.6666666667% | 
 | Disseminated Cancer | 0.282485875706% | 0.0% | 4.9504950495% | 50.0% | 
 | Steroid | 3.38983050847% | 0.0% | 8.91089108911% | 50.0% | 
 | Bleeding Disorder | 0.0% | 100.0% | 0.0% | 100.0% | 
 | Functional Health Status | 0.564971751412% | 0.0% | 1.9801980198% | 0.0% | 
 | Pneumonia | 0.0% | 0.0% | 3.9603960396% | 0.0% | 
 | Reintubation | 0.0% | 0.0% | 2.47524752475% | 0.0% | 
 | Urinary Infection | 0.0% | 0.0% | 0.49504950495% | 0.0% | 
 | Ventilator | 0.0% | 0.0% | 1.9801980198% | 16.6666666667% | 
 | Unplanned Readmission | 3.67231638418% | 0.0% | 4.9504950495% | 0.0% | 
 | Readmission | 3.67231638418% | 0.0% | 5.94059405941% | 0.0% | 
 | Superficial SSI | 0.0% | 0.0% | 0.49504950495% | 0.0% | 
 | Deep SSI | 0.0% | 0.0% | 0.0% | 0.0% | 
 | Organ/Space SSI | 0.564971751412% | 0.0% | 3.46534653465% | 0.0% | 
 | Wound Disruption | 0.0% | 0.0% | 0.0% | 0.0% | 
 | Deep Vein Thrombosis | 0.0% | 0.0% | 0.990099009901% | 0.0% | 
 | Renal Insufficiency | 0.282485875706% | 0.0% | 0.0% | 0.0% | 
 | Pulmonary Embolism | 0.282485875706% | 0.0% | 0.49504950495% | 0.0% | 
 | CVA with Neurologic Deficit | 0.0% | 0.0% | 0.0% | 0.0% | 
 | Cardiac Arrest | 0.0% | 0.0% | 0.0% | 0.0% | 
 | Myocardial Infarction | 0.0% | 0.0% | 0.0% | 0.0% | 
 | Sepsis | 0.282485875706% | 0.0% | 1.9801980198% | 0.0% | 
 
 ## Functional Health Status Analysis
| | Non-Functional Health Status (N = 559.0) | Functional Health Status (N = 6.0) |
| ------------- | ------------- | ------------- |
 | Diabetes | 1100.0% | 50.0% | 
 | Smoke | 1866.66666667% | 33.3333333333% | 
 | Dyspnea | 383.333333333% | 0.0% | 
 | Ventilator Dependent | 16.6666666667% | 0.0% | 
 | Ascites | 0.0% | 0.0% | 
 | COPD | 350.0% | 0.0% | 
 | CGF | 33.3333333333% | 16.6666666667% | 
 | Hypertension | 3216.66666667% | 66.6666666667% | 
 | Acute Renal Failure | 16.6666666667% | 0.0% | 
 | Disseminated Cancer | 233.333333333% | 0.0% | 
 | Steroid | 533.333333333% | 16.6666666667% | 
 | Bleeding Disorder | 150.0% | 0.0% | 
 | Functional Health Status | 0.0% | 100.0% | 
 | Pneumonia | 116.666666667% | 16.6666666667% | 
 | Reintubation | 66.6666666667% | 16.6666666667% | 
 | Urinary Infection | 16.6666666667% | 0.0% | 
 | Ventilator | 66.6666666667% | 16.6666666667% | 
 | Unplanned Readmission | 383.333333333% | 0.0% | 
 | Readmission | 416.666666667% | 0.0% | 
 | Superficial SSI | 16.6666666667% | 0.0% | 
 | Deep SSI | 0.0% | 0.0% | 
 | Organ/Space SSI | 133.333333333% | 16.6666666667% | 
 | Wound Disruption | 0.0% | 0.0% | 
 | Deep Vein Thrombosis | 33.3333333333% | 0.0% | 
 | Renal Insufficiency | 16.6666666667% | 0.0% | 
 | Pulmonary Embolism | 33.3333333333% | 0.0% | 
 | CVA with Neurologic Deficit | 0.0% | 0.0% | 
 | Cardiac Arrest | 0.0% | 0.0% | 
 | Myocardial Infarction | 0.0% | 0.0% | 
 | Sepsis | 83.3333333333% | 0.0% | 


| | Outpatient Non-Functional Health Status (N = 355) | Outpatient Functional Health Status (N = 2) |  Inpatient Non-Functional Health Status (N = 204) | Inpatient Functional Health Status (N = 4) |
| ------------- | ------------- | ------------- | ------------- | ------------- |
 | Diabetes | 8.16901408451% | 50.0% | 18.137254902% | 50.0% | 
 | Smoke | 18.8732394366% | 50.0% | 22.0588235294% | 25.0% | 
 | Dyspnea | 3.38028169014% | 0.0% | 5.39215686275% | 0.0% | 
 | Ventilator Dependent | 0.0% | 0.0% | 0.490196078431% | 0.0% | 
 | Ascites | 0.0% | 0.0% | 0.0% | 0.0% | 
 | COPD | 2.53521126761% | 0.0% | 5.88235294118% | 0.0% | 
 | CGF | 0.56338028169% | 0.0% | 0.0% | 25.0% | 
 | Hypertension | 27.8873239437% | 100.0% | 46.0784313725% | 50.0% | 
 | Acute Renal Failure | 0.0% | 0.0% | 0.490196078431% | 0.0% | 
 | Disseminated Cancer | 0.281690140845% | 0.0% | 6.37254901961% | 0.0% | 
 | Steroid | 3.38028169014% | 0.0% | 9.80392156863% | 25.0% | 
 | Bleeding Disorder | 0.845070422535% | 0.0% | 2.94117647059% | 0.0% | 
 | Functional Health Status | 0.0% | 100.0% | 0.0% | 100.0% | 
 | Pneumonia | 0.0% | 0.0% | 3.43137254902% | 25.0% | 
 | Reintubation | 0.0% | 0.0% | 1.96078431373% | 25.0% | 
 | Urinary Infection | 0.0% | 0.0% | 0.490196078431% | 0.0% | 
 | Ventilator | 0.0% | 0.0% | 1.96078431373% | 25.0% | 
 | Unplanned Readmission | 3.66197183099% | 0.0% | 4.90196078431% | 0.0% | 
 | Readmission | 3.66197183099% | 0.0% | 5.88235294118% | 0.0% | 
 | Superficial SSI | 0.0% | 0.0% | 0.490196078431% | 0.0% | 
 | Deep SSI | 0.0% | 0.0% | 0.0% | 0.0% | 
 | Organ/Space SSI | 0.56338028169% | 0.0% | 2.94117647059% | 25.0% | 
 | Wound Disruption | 0.0% | 0.0% | 0.0% | 0.0% | 
 | Deep Vein Thrombosis | 0.0% | 0.0% | 0.980392156863% | 0.0% | 
 | Renal Insufficiency | 0.281690140845% | 0.0% | 0.0% | 0.0% | 
 | Pulmonary Embolism | 0.281690140845% | 0.0% | 0.490196078431% | 0.0% | 
 | CVA with Neurologic Deficit | 0.0% | 0.0% | 0.0% | 0.0% | 
 | Cardiac Arrest | 0.0% | 0.0% | 0.0% | 0.0% | 
 | Myocardial Infarction | 0.0% | 0.0% | 0.0% | 0.0% | 
 | Sepsis | 0.281690140845% | 0.0% | 1.96078431373% | 0.0% | 
 
 
 ### Notes
 I did not perform this analysis for Ventilator Dependent, Ascites, and Acute Renal Failure due to lack of patients with the conditions in both outpatient and inpatient settings. 








