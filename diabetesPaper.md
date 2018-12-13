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

## Expanded Table 2

#### The following recreations of tables 2 and 3 from the paper checks for significant differences between populations with and without a specific health condition. p-values were generated using two-sample z-test for the difference of proportions. Bolded values indicate that the results were statistically significant (p < 0.05).

| | Non-Diabetes (N = 496.0) | Diabetes (N = 69.0) | p-value | 
| ------------- | ------------- | ------------- | ------------- |
 | Smoke | 20.16% | 20.29% | 0.9801 | 
 | Dyspnea | 3.629% | 7.246% | 0.1543 | 
 | Ventilator Dependent | 0.2016% | 0% | 0.7089 | 
 | COPD | 2.823% | 10.14% | **0.002591** | 
 | Hypertension | 29.03% | 76.81% | **6.036e-15** | 
 | Disseminated Cancer | 2.621% | 1.449% | 0.5575 | 
 | Steroid | 6.25% | 2.899% | 0.266 | 
 | Bleeding Disorder | 1.411% | 2.899% | 0.3552 | 
 | Independent Functional Health Status | 98.39% | 92.75% | **0.003452** | 
 | Totally or Partially Dependent Functional Health Status | 0.6048% | 4.348% | **0.004483** | 


| | Non-Smoke (N = 947.0) | Smoke (N = 183.0) | p-value | 
| ------------- | ------------- | ------------- | ------------- |
 | Diabetes | 5.808% | 45.36% | **1.389e-50** | 
 | Dyspnea | 3.168% | 8.743% | **0.000476** | 
 | Ventilator Dependent | 0.1056% | 0.5464% | 0.194 | 
 | COPD | 2.851% | 8.197% | **0.0004662** | 
 | Hypertension | 29.99% | 60.11% | **4.989e-15** | 
 | Disseminated Cancer | 2.64% | 1.639% | 0.4254 | 
 | Steroid | 6.336% | 3.279% | 0.1064 | 
 | Bleeding Disorder | 1.69% | 1.093% | 0.5551 | 
 | Independent Functional Health Status | 98.1% | 95.63% | **0.04126** | 
 | Totally or Partially Dependent Functional Health Status | 0.7392% | 2.732% | **0.01604** | 


| | Non-Hypertension (N = 1315.0) | Hypertension (N = 380.0) | p-value | 
| ------------- | ------------- | ------------- | ------------- |
 | Diabetes | 5.399% | 35.79% | **3.549e-57** | 
 | Smoke | 11.94% | 48.68% | **1.088e-55** | 
 | Dyspnea | 2.89% | 8.158% | **4.709e-06** | 
 | Ventilator Dependent | 0.07605% | 0.5263% | 0.06587 | 
 | COPD | 2.433% | 8.158% | **2.04e-07** | 
 | Disseminated Cancer | 2.662% | 1.842% | 0.3654 | 
 | Steroid | 6.008% | 5.263% | 0.5857 | 
 | Bleeding Disorder | 1.597% | 1.579% | 0.9803 | 
 | Independent Functional Health Status | 98.02% | 96.58% | 0.09823 | 
 | Totally or Partially Dependent Functional Health Status | 0.6844% | 2.368% | **0.00479** | 


| | Non-Dyspnea (N = 1857.0) | Dyspnea (N = 403.0) | p-value | 
| ------------- | ------------- | ------------- | ------------- |
 | Diabetes | 7.27% | 34.99% | **1.528e-53** | 
 | Smoke | 14.0% | 48.64% | **1.415e-55** | 
 | Ventilator Dependent | 0.1077% | 0.4963% | 0.09252 | 
 | COPD | 2.477% | 9.429% | **2.27e-11** | 
 | Hypertension | 25.09% | 79.9% | **2.977e-97** | 
 | Disseminated Cancer | 2.531% | 2.233% | 0.7275 | 
 | Steroid | 5.924% | 5.459% | 0.7185 | 
 | Bleeding Disorder | 1.508% | 1.985% | 0.4879 | 
 | Independent Functional Health Status | 97.9% | 96.77% | 0.1719 | 
 | Totally or Partially Dependent Functional Health Status | 0.8078% | 2.233% | **0.01138** | 


| | Non-COPD (N = 2401.0) | COPD (N = 424.0) | p-value | 
| ------------- | ------------- | ------------- | ------------- |
 | Diabetes | 8.205% | 34.91% | **4.721e-54** | 
 | Smoke | 15.24% | 48.11% | **1.644e-54** | 
 | Dyspnea | 2.249% | 14.39% | **2.045e-31** | 
 | Ventilator Dependent | 0.1249% | 0.4717% | 0.1173 | 
 | Hypertension | 26.95% | 79.72% | **4.241e-98** | 
 | Disseminated Cancer | 2.499% | 2.358% | 0.8638 | 
 | Steroid | 5.831% | 5.896% | 0.9578 | 
 | Bleeding Disorder | 1.458% | 2.358% | 0.172 | 
 | Independent Functional Health Status | 97.88% | 96.7% | 0.1359 | 
 | Totally or Partially Dependent Functional Health Status | 0.8746% | 2.123% | **0.02082** | 


| | Non-CGF (N = 2963.0) | CGF (N = 427.0) | p-value | 
| ------------- | ------------- | ------------- | ------------- |
 | Diabetes | 8.944% | 34.89% | **6.411e-53** | 
 | Smoke | 16.17% | 48.01% | **4.915e-53** | 
 | Dyspnea | 2.599% | 14.29% | **3.126e-30** | 
 | Ventilator Dependent | 0.135% | 0.4684% | 0.1255 | 
 | COPD | 2.194% | 14.29% | **4.958e-35** | 
 | Hypertension | 28.38% | 79.86% | **1.05e-96** | 
 | Disseminated Cancer | 2.497% | 2.342% | 0.8467 | 
 | Steroid | 5.839% | 5.855% | 0.9894 | 
 | Bleeding Disorder | 1.485% | 2.342% | 0.1861 | 
 | Independent Functional Health Status | 97.87% | 96.49% | 0.07398 | 
 | Totally or Partially Dependent Functional Health Status | 0.8775% | 2.342% | **0.005779** | 


| | Non-Disseminated Cancer (N = 3514.0) | Disseminated Cancer (N = 441.0) | p-value | 
| ------------- | ------------- | ------------- | ------------- |
 | Diabetes | 9.476% | 34.01% | **8.844e-50** | 
 | Smoke | 16.82% | 46.94% | **6.32e-50** | 
 | Dyspnea | 2.789% | 14.29% | **1.093e-30** | 
 | Ventilator Dependent | 0.1423% | 0.4535% | 0.1427 | 
 | COPD | 2.419% | 14.06% | **3.981e-34** | 
 | Hypertension | 29.43% | 78.23% | **2.238e-91** | 
 | Steroid | 5.777% | 6.349% | 0.629 | 
 | Bleeding Disorder | 1.423% | 2.948% | **0.01591** | 
 | Independent Functional Health Status | 97.84% | 96.6% | 0.102 | 
 | Totally or Partially Dependent Functional Health Status | 0.9106% | 2.268% | **0.008782** | 


| | Non-Steroid (N = 4046.0) | Steroid (N = 474.0) | p-value | 
| ------------- | ------------- | ------------- | ------------- |
 | Diabetes | 9.886% | 32.07% | **2.971e-44** | 
 | Smoke | 17.33% | 44.51% | **2.927e-44** | 
 | Dyspnea | 2.941% | 13.71% | **2.964e-29** | 
 | Ventilator Dependent | 0.1483% | 0.4219% | 0.1799 | 
 | COPD | 2.546% | 13.71% | **5.095e-34** | 
 | Hypertension | 30.08% | 75.74% | **1.064e-86** | 
 | Disseminated Cancer | 2.101% | 5.696% | **1.897e-06** | 
 | Bleeding Disorder | 1.384% | 3.376% | **0.001052** | 
 | Independent Functional Health Status | 97.83% | 96.62% | 0.09907 | 
 | Totally or Partially Dependent Functional Health Status | 0.9145% | 2.321% | **0.004716** | 


| | Non-Bleeding Disorder (N = 4602.0) | Bleeding Disorder (N = 483.0) | p-value | 
| ------------- | ------------- | ------------- | ------------- |
 | Diabetes | 10.15% | 31.88% | **8.447e-44** | 
 | Smoke | 17.71% | 43.69% | **1.007e-41** | 
 | Dyspnea | 3.042% | 13.87% | **2.154e-30** | 
 | Ventilator Dependent | 0.1521% | 0.4141% | 0.1926 | 
 | COPD | 2.651% | 13.87% | **2.58e-35** | 
 | Hypertension | 30.64% | 75.16% | **6.046e-85** | 
 | Disseminated Cancer | 2.086% | 6.211% | **2.887e-08** | 
 | Steroid | 5.063% | 13.25% | **2.89e-13** | 
 | Independent Functional Health Status | 97.83% | 96.48% | 0.06039 | 
 | Totally or Partially Dependent Functional Health Status | 0.9344% | 2.277% | **0.006154** | 


| | Non-Independent Functional Health Status (N = 4615.0) | Independent Functional Health Status (N = 1035.0) | p-value | 
| ------------- | ------------- | ------------- | ------------- |
 | Diabetes | 10.23% | 21.06% | **6.471e-22** | 
 | Smoke | 17.72% | 31.11% | **3.063e-22** | 
 | Dyspnea | 3.034% | 8.696% | **8.023e-17** | 
 | Ventilator Dependent | 0.1517% | 0.2899% | 0.3392 | 
 | COPD | 2.665% | 8.406% | **1.112e-18** | 
 | Hypertension | 30.66% | 53.62% | **1.354e-44** | 
 | Disseminated Cancer | 2.08% | 4.251% | **4.891e-05** | 
 | Steroid | 5.07% | 9.275% | **1.853e-07** | 
 | Bleeding Disorder | 1.235% | 3.188% | **5.728e-06** | 
 | Totally or Partially Dependent Functional Health Status | 1.062% | 1.063% | 0.9976 | 


| | Non-Totally or Partially Dependent Functional Health Status (N = 5174.0) | Totally or Partially Dependent Functional Health Status (N = 1041.0) | p-value | 
| ------------- | ------------- | ------------- | ------------- |
 | Diabetes | 10.4% | 21.23% | **2.068e-22** | 
 | Smoke | 17.97% | 31.12% | **5.127e-22** | 
 | Dyspnea | 3.15% | 8.646% | **2.695e-16** | 
 | Ventilator Dependent | 0.1546% | 0.2882% | 0.3496 | 
 | COPD | 2.783% | 8.357% | **4.157e-18** | 
 | Hypertension | 31.08% | 53.7% | **2.268e-44** | 
 | Disseminated Cancer | 2.126% | 4.227% | **6.943e-05** | 
 | Steroid | 5.141% | 9.318% | **1.577e-07** | 
 | Bleeding Disorder | 1.276% | 3.17% | **8.415e-06** | 
 | Independent Functional Health Status | 97.68% | 97.79% | 0.8292 | 
 
 ## Expanded Table 3
 
| | Non-Diabetes (N = 496.0) | Diabetes (N = 69.0) | p-value | 
| ------------- | ------------- | ------------- | ------------- |
 | Superficial SSI | 0.2016% | 0% | 0.7089 | 
 | Deep SSI | 0% | 0% | - | 
 | Organ/Space SSI | 1.411% | 2.899% | 0.3552 | 
 | Wound Disruption | 0% | 0% | - | 
 | Pneumonia | 0.8065% | 5.797% | **0.001011** | 
 | Reintubation | 0.4032% | 4.348% | **0.001045** | 
 | Urinary Infection | 0.2016% | 0% | 0.7089 | 
 | Deep Vein Thrombosis | 0.2016% | 1.449% | 0.102 | 
 | Renal Insufficiency | 0.2016% | 0% | 0.7089 | 
 | Pulmonary Embolism | 0.4032% | 0% | 0.5972 | 
 | Ventilator Dependent | 0.2016% | 0% | 0.7089 | 
 | Acute Renal Failure | 0.2016% | 0% | 0.7089 | 
 | CVA with Neurologic Deficit | 0% | 0% | - | 
 | Myocardial Infarction | 0% | 0% | - | 
 | Sepsis | 1.008% | 0% | 0.4022 | 
 | Readmission | 4.234% | 5.797% | 0.5541 | 
 | Unplanned Readmission | 3.831% | 5.797% | 0.4386 | 


| | Non-Smoke (N = 947.0) | Smoke (N = 183.0) | p-value | 
| ------------- | ------------- | ------------- | ------------- |
 | Superficial SSI | 0.2112% | 0% | 0.5338 | 
 | Deep SSI | 0% | 0% | - | 
 | Organ/Space SSI | 1.162% | 3.825% | **0.008423** | 
 | Wound Disruption | 0% | 0% | - | 
 | Pneumonia | 1.162% | 2.732% | 0.09969 | 
 | Reintubation | 0.6336% | 2.186% | **0.04012** | 
 | Urinary Infection | 0.2112% | 0% | 0.5338 | 
 | Deep Vein Thrombosis | 0.2112% | 1.093% | 0.06599 | 
 | Renal Insufficiency | 0.2112% | 0% | 0.5338 | 
 | Pulmonary Embolism | 0.2112% | 1.093% | 0.06599 | 
 | Ventilator Dependent | 0.1056% | 0.5464% | 0.194 | 
 | Acute Renal Failure | 0.2112% | 0% | 0.5338 | 
 | CVA with Neurologic Deficit | 0% | 0% | - | 
 | Myocardial Infarction | 0% | 0% | - | 
 | Sepsis | 0.8448% | 1.093% | 0.7428 | 
 | Readmission | 4.013% | 6.557% | 0.1254 | 
 | Unplanned Readmission | 3.696% | 6.011% | 0.1468 | 


| | Non-Hypertension (N = 1315.0) | Hypertension (N = 380.0) | p-value | 
| ------------- | ------------- | ------------- | ------------- |
 | Superficial SSI | 0.1521% | 0.2632% | 0.65 | 
 | Deep SSI | 0% | 0% | - | 
 | Organ/Space SSI | 1.141% | 3.158% | **0.005668** | 
 | Wound Disruption | 0% | 0% | - | 
 | Pneumonia | 1.065% | 2.632% | **0.02278** | 
 | Reintubation | 0.6084% | 1.842% | **0.02371** | 
 | Urinary Infection | 0.2281% | 0% | 0.3514 | 
 | Deep Vein Thrombosis | 0.2281% | 0.7895% | 0.1046 | 
 | Renal Insufficiency | 0.1521% | 0.2632% | 0.65 | 
 | Pulmonary Embolism | 0.2281% | 0.7895% | 0.1046 | 
 | Ventilator Dependent | 0.07605% | 0.5263% | 0.06587 | 
 | Acute Renal Failure | 0.1521% | 0.2632% | 0.65 | 
 | CVA with Neurologic Deficit | 0% | 0% | - | 
 | Myocardial Infarction | 0% | 0% | - | 
 | Sepsis | 0.6844% | 1.579% | 0.101 | 
 | Readmission | 3.65% | 7.105% | **0.003917** | 
 | Unplanned Readmission | 3.422% | 6.316% | **0.01193** | 


| | Non-Dyspnea (N = 1857.0) | Dyspnea (N = 403.0) | p-value | 
| ------------- | ------------- | ------------- | ------------- |
 | Superficial SSI | 0.1616% | 0.2481% | 0.7078 | 
 | Deep SSI | 0% | 0% | - | 
 | Organ/Space SSI | 1.292% | 2.978% | **0.01431** | 
 | Wound Disruption | 0% | 0% | - | 
 | Pneumonia | 1.185% | 2.481% | **0.04581** | 
 | Reintubation | 0.7001% | 1.737% | **0.04393** | 
 | Urinary Infection | 0.2154% | 0% | 0.3511 | 
 | Deep Vein Thrombosis | 0.2693% | 0.7444% | 0.1454 | 
 | Renal Insufficiency | 0.1616% | 0.2481% | 0.7078 | 
 | Pulmonary Embolism | 0.2693% | 0.7444% | 0.1454 | 
 | Ventilator Dependent | 0.1077% | 0.4963% | 0.09252 | 
 | Acute Renal Failure | 0.1077% | 0.4963% | 0.09252 | 
 | CVA with Neurologic Deficit | 0% | 0% | - | 
 | Myocardial Infarction | 0% | 0% | - | 
 | Sepsis | 0.7539% | 1.489% | 0.1533 | 
 | Readmission | 3.877% | 6.948% | **0.006584** | 
 | Unplanned Readmission | 3.608% | 6.203% | **0.01685** | 


| | Non-COPD (N = 2401.0) | COPD (N = 424.0) | p-value | 
| ------------- | ------------- | ------------- | ------------- |
 | Superficial SSI | 0.1666% | 0.2358% | 0.7545 | 
 | Deep SSI | 0% | 0% | - | 
 | Organ/Space SSI | 1.333% | 3.066% | **0.008589** | 
 | Wound Disruption | 0% | 0% | - | 
 | Pneumonia | 1.208% | 2.594% | **0.0259** | 
 | Reintubation | 0.708% | 1.887% | **0.01688** | 
 | Urinary Infection | 0.2082% | 0% | 0.347 | 
 | Deep Vein Thrombosis | 0.2499% | 0.9434% | **0.02665** | 
 | Renal Insufficiency | 0.1249% | 0.4717% | 0.1173 | 
 | Pulmonary Embolism | 0.2915% | 0.7075% | 0.1836 | 
 | Ventilator Dependent | 0.1249% | 0.4717% | 0.1173 | 
 | Acute Renal Failure | 0.0833% | 0.7075% | **0.004813** | 
 | CVA with Neurologic Deficit | 0% | 0% | - | 
 | Myocardial Infarction | 0% | 0% | - | 
 | Sepsis | 0.708% | 1.887% | **0.01688** | 
 | Readmission | 3.915% | 7.311% | **0.001718** | 
 | Unplanned Readmission | 3.623% | 6.604% | **0.004197** | 


| | Non-CGF (N = 2963.0) | CGF (N = 427.0) | p-value | 
| ------------- | ------------- | ------------- | ------------- |
 | Superficial SSI | 0.1687% | 0.2342% | 0.7636 | 
 | Deep SSI | 0% | 0% | - | 
 | Organ/Space SSI | 1.384% | 3.044% | **0.01039** | 
 | Wound Disruption | 0% | 0% | - | 
 | Pneumonia | 1.215% | 2.81% | **0.009092** | 
 | Reintubation | 0.7087% | 2.108% | **0.003904** | 
 | Urinary Infection | 0.2025% | 0% | 0.352 | 
 | Deep Vein Thrombosis | 0.27% | 0.9368% | **0.03009** | 
 | Renal Insufficiency | 0.135% | 0.4684% | 0.1255 | 
 | Pulmonary Embolism | 0.3037% | 0.7026% | 0.1945 | 
 | Ventilator Dependent | 0.135% | 0.4684% | 0.1255 | 
 | Acute Renal Failure | 0.1012% | 0.7026% | **0.005714** | 
 | CVA with Neurologic Deficit | 0% | 0% | - | 
 | Myocardial Infarction | 0% | 0% | - | 
 | Sepsis | 0.7425% | 1.874% | **0.01964** | 
 | Readmission | 4.016% | 7.26% | **0.002309** | 
 | Unplanned Readmission | 3.712% | 6.557% | **0.005415** | 


| | Non-Disseminated Cancer (N = 3514.0) | Disseminated Cancer (N = 441.0) | p-value | 
| ------------- | ------------- | ------------- | ------------- |
 | Superficial SSI | 0.1707% | 0.2268% | 0.792 | 
 | Deep SSI | 0% | 0% | - | 
 | Organ/Space SSI | 1.423% | 2.948% | **0.01591** | 
 | Wound Disruption | 0% | 0% | - | 
 | Pneumonia | 1.224% | 2.948% | **0.003868** | 
 | Reintubation | 0.7399% | 2.041% | **0.005967** | 
 | Urinary Infection | 0.1992% | 0% | 0.3482 | 
 | Deep Vein Thrombosis | 0.2846% | 0.907% | **0.03802** | 
 | Renal Insufficiency | 0.1423% | 0.4535% | 0.1427 | 
 | Pulmonary Embolism | 0.313% | 0.6803% | 0.221 | 
 | Ventilator Dependent | 0.1423% | 0.4535% | 0.1427 | 
 | Acute Renal Failure | 0.08537% | 0.907% | **0.0001091** | 
 | CVA with Neurologic Deficit | 0% | 0% | - | 
 | Myocardial Infarction | 0% | 0% | - | 
 | Sepsis | 0.7684% | 1.814% | **0.02709** | 
 | Readmission | 4.069% | 7.256% | **0.002159** | 
 | Unplanned Readmission | 3.756% | 6.576% | **0.004738** | 


| | Non-Steroid (N = 4046.0) | Steroid (N = 474.0) | p-value | 
| ------------- | ------------- | ------------- | ------------- |
 | Superficial SSI | 0.173% | 0.211% | 0.8524 | 
 | Deep SSI | 0% | 0% | - | 
 | Organ/Space SSI | 1.409% | 3.165% | **0.00387** | 
 | Wound Disruption | 0% | 0% | - | 
 | Pneumonia | 1.236% | 2.954% | **0.002745** | 
 | Reintubation | 0.7415% | 2.11% | **0.002619** | 
 | Urinary Infection | 0.1977% | 0% | 0.3326 | 
 | Deep Vein Thrombosis | 0.2966% | 0.8439% | 0.05768 | 
 | Renal Insufficiency | 0.1483% | 0.4219% | 0.1799 | 
 | Pulmonary Embolism | 0.2966% | 0.8439% | 0.05768 | 
 | Ventilator Dependent | 0.1483% | 0.4219% | 0.1799 | 
 | Acute Renal Failure | 0.07415% | 1.055% | **1.54e-06** | 
 | CVA with Neurologic Deficit | 0% | 0% | - | 
 | Myocardial Infarction | 0% | 0% | - | 
 | Sepsis | 0.7415% | 2.11% | **0.002619** | 
 | Readmission | 4.152% | 6.751% | **0.009239** | 
 | Unplanned Readmission | 3.831% | 6.118% | **0.01712** | 


| | Non-Bleeding Disorder (N = 4602.0) | Bleeding Disorder (N = 483.0) | p-value | 
| ------------- | ------------- | ------------- | ------------- |
 | Superficial SSI | 0.1738% | 0.207% | 0.8688 | 
 | Deep SSI | 0% | 0% | - | 
 | Organ/Space SSI | 1.434% | 3.106% | **0.005252** | 
 | Wound Disruption | 0% | 0% | - | 
 | Pneumonia | 1.26% | 2.899% | **0.003743** | 
 | Reintubation | 0.7605% | 2.07% | **0.003454** | 
 | Urinary Infection | 0.1956% | 0% | 0.3307 | 
 | Deep Vein Thrombosis | 0.3042% | 0.8282% | 0.06512 | 
 | Renal Insufficiency | 0.1521% | 0.4141% | 0.1926 | 
 | Pulmonary Embolism | 0.3042% | 0.8282% | 0.06512 | 
 | Ventilator Dependent | 0.1521% | 0.4141% | 0.1926 | 
 | Acute Renal Failure | 0.06519% | 1.242% | **4.779e-09** | 
 | CVA with Neurologic Deficit | 0% | 0% | - | 
 | Myocardial Infarction | 0% | 0% | - | 
 | Sepsis | 0.7605% | 2.07% | **0.003454** | 
 | Readmission | 4.194% | 6.625% | **0.01344** | 
 | Unplanned Readmission | 3.868% | 6.004% | **0.02381** | 


| | Non-Independent Functional Health Status (N = 4615.0) | Independent Functional Health Status (N = 1035.0) | p-value | 
| ------------- | ------------- | ------------- | ------------- |
 | Superficial SSI | 0.1733% | 0.1932% | 0.8906 | 
 | Deep SSI | 0% | 0% | - | 
 | Organ/Space SSI | 1.452% | 2.222% | 0.07358 | 
 | Wound Disruption | 0% | 0% | - | 
 | Pneumonia | 1.3% | 1.932% | 0.1197 | 
 | Reintubation | 0.8017% | 1.256% | 0.1584 | 
 | Urinary Infection | 0.195% | 0.09662% | 0.4961 | 
 | Deep Vein Thrombosis | 0.325% | 0.4831% | 0.439 | 
 | Renal Insufficiency | 0.1517% | 0.2899% | 0.3392 | 
 | Pulmonary Embolism | 0.3034% | 0.5797% | 0.1761 | 
 | Ventilator Dependent | 0.1517% | 0.2899% | 0.3392 | 
 | Acute Renal Failure | 0.06501% | 0.6763% | **2.35e-05** | 
 | CVA with Neurologic Deficit | 0% | 0% | - | 
 | Myocardial Infarction | 0% | 0% | - | 
 | Sepsis | 0.7584% | 1.449% | **0.03196** | 
 | Readmission | 4.182% | 5.507% | 0.06097 | 
 | Unplanned Readmission | 3.857% | 5.024% | 0.08592 | 


| | Non-Totally or Partially Dependent Functional Health Status (N = 5174.0) | Totally or Partially Dependent Functional Health Status (N = 1041.0) | p-value | 
| ------------- | ------------- | ------------- | ------------- |
 | Superficial SSI | 0.1739% | 0.1921% | 0.8987 | 
 | Deep SSI | 0% | 0% | - | 
 | Organ/Space SSI | 1.45% | 2.305% | **0.04416** | 
 | Wound Disruption | 0% | 0% | - | 
 | Pneumonia | 1.295% | 2.017% | 0.07188 | 
 | Reintubation | 0.7924% | 1.345% | 0.08248 | 
 | Urinary Infection | 0.1933% | 0.09606% | 0.496 | 
 | Deep Vein Thrombosis | 0.3286% | 0.4803% | 0.452 | 
 | Renal Insufficiency | 0.1546% | 0.2882% | 0.3496 | 
 | Pulmonary Embolism | 0.3092% | 0.5764% | 0.1855 | 
 | Ventilator Dependent | 0.1546% | 0.2882% | 0.3496 | 
 | Acute Renal Failure | 0.07731% | 0.6724% | **3.072e-05** | 
 | CVA with Neurologic Deficit | 0% | 0% | - | 
 | Myocardial Infarction | 0% | 0% | - | 
 | Sepsis | 0.7731% | 1.441% | **0.0358** | 
 | Readmission | 4.213% | 5.476% | 0.0708 | 
 | Unplanned Readmission | 3.885% | 4.995% | 0.09809 | 
 
 ## Expanded Table 4  
 
| | Outpatient Non-Diabetes (N = 327) | Outpatient Diabetes (N = 30) | p-value | Inpatient Non-Diabetes (N = 169) | Inpatient Diabetes (N = 39) | p-value |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
 | Superficial SSI | 0.00% | 0.00% | -|0.59% | 0.00% | 0.6301|
 | Deep SSI | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Organ/Space SSI | 0.61% | 0.00% | 0.6675|2.96% | 5.13% | 0.4983|
 | Wound Disruption | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Pneumonia | 0.00% | 0.00% | -|**2.37**% | **10.26**% | **0.02092**|
 | Reintubation | 0.00% | 0.00% | -|**1.18**% | **7.69**% | **0.01675**|
 | Urinary Infection | 0.00% | 0.00% | -|0.59% | 0.00% | 0.6301|
 | Deep Vein Thrombosis | 0.00% | 0.00% | -|0.59% | 2.56% | 0.2552|
 | Renal Insufficiency | 0.31% | 0.00% | 0.7616|0.00% | 0.00% | -|
 | Pulmonary Embolism | 0.31% | 0.00% | 0.7616|0.59% | 0.00% | 0.6301|
 | Ventilator Dependent | 0.00% | 0.00% | -|0.59% | 0.00% | 0.6301|
 | Acute Renal Failure | 0.00% | 0.00% | -|0.59% | 0.00% | 0.6301|
 | CVA with Neurologic Deficit | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Myocardial Infarction | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Sepsis | 0.31% | 0.00% | 0.7616|2.37% | 0.00% | 0.332|
 | Readmission | 3.67% | 3.33% | 0.925|5.33% | 7.69% | 0.5677|
 | Unplanned Readmission | 3.67% | 3.33% | 0.925|4.14% | 7.69% | 0.3502|


| | Outpatient Non-Smoke (N = 616) | Outpatient Smoke (N = 98) | p-value | Inpatient Non-Smoke (N = 331) | Inpatient Smoke (N = 85) | p-value |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
 | Superficial SSI | 0.00% | 0.00% | -|0.60% | 0.00% | 0.4725|
 | Deep SSI | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Organ/Space SSI | 0.65% | 0.00% | 0.4237|**2.11**% | **8.24**% | **0.005253**|
 | Wound Disruption | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Pneumonia | 0.00% | 0.00% | -|3.32% | 5.88% | 0.2738|
 | Reintubation | 0.00% | 0.00% | -|1.81% | 4.71% | 0.1203|
 | Urinary Infection | 0.00% | 0.00% | -|0.60% | 0.00% | 0.4725|
 | Deep Vein Thrombosis | 0.00% | 0.00% | -|0.60% | 2.35% | 0.1406|
 | Renal Insufficiency | 0.32% | 0.00% | 0.5722|0.00% | 0.00% | -|
 | Pulmonary Embolism | 0.16% | 1.02% | 0.1355|0.30% | 1.18% | 0.2986|
 | Ventilator Dependent | 0.00% | 0.00% | -|0.30% | 1.18% | 0.2986|
 | Acute Renal Failure | 0.00% | 0.00% | -|0.60% | 0.00% | 0.4725|
 | CVA with Neurologic Deficit | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Myocardial Infarction | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Sepsis | 0.32% | 0.00% | 0.5722|1.81% | 2.35% | 0.7463|
 | Readmission | 3.41% | 5.10% | 0.406|5.14% | 8.24% | 0.2743|
 | Unplanned Readmission | 3.41% | 5.10% | 0.406|4.23% | 7.06% | 0.2768|


| | Outpatient Non-Hypertension (N = 872) | Outpatient Hypertension (N = 199) | p-value | Inpatient Non-Hypertension (N = 443) | Inpatient Hypertension (N = 181) | p-value |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
 | Superficial SSI | 0.00% | 0.00% | -|0.45% | 0.55% | 0.8685|
 | Deep SSI | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Organ/Space SSI | 0.57% | 0.50% | 0.9038|**2.26**% | **6.08**% | **0.01634**|
 | Wound Disruption | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Pneumonia | 0.00% | 0.00% | -|3.16% | 5.52% | 0.1634|
 | Reintubation | 0.00% | 0.00% | -|1.81% | 3.87% | 0.1271|
 | Urinary Infection | 0.00% | 0.00% | -|0.68% | 0.00% | 0.2671|
 | Deep Vein Thrombosis | 0.00% | 0.00% | -|0.68% | 1.66% | 0.2548|
 | Renal Insufficiency | 0.23% | 0.50% | 0.5106|0.00% | 0.00% | -|
 | Pulmonary Embolism | 0.23% | 0.50% | 0.5106|0.23% | 1.10% | 0.1496|
 | Ventilator Dependent | 0.00% | 0.00% | -|0.23% | 1.10% | 0.1496|
 | Acute Renal Failure | 0.00% | 0.00% | -|0.45% | 0.55% | 0.8685|
 | CVA with Neurologic Deficit | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Myocardial Infarction | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Sepsis | 0.23% | 0.50% | 0.5106|1.58% | 2.76% | 0.3291|
 | Readmission | 3.33% | 5.03% | 0.2482|**4.29**% | **9.39**% | **0.0131**|
 | Unplanned Readmission | 3.33% | 5.03% | 0.2482|**3.61**% | **7.73**% | **0.02891**|


| | Outpatient Non-Dyspnea (N = 1217) | Outpatient Dyspnea (N = 211) | p-value | Inpatient Non-Dyspnea (N = 640) | Inpatient Dyspnea (N = 192) | p-value |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
 | Superficial SSI | 0.00% | 0.00% | -|0.47% | 0.52% | 0.9271|
 | Deep SSI | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Organ/Space SSI | 0.58% | 0.47% | 0.8557|**2.66**% | **5.73**% | **0.03837**|
 | Wound Disruption | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Pneumonia | 0.00% | 0.00% | -|3.44% | 5.21% | 0.2631|
 | Reintubation | 0.00% | 0.00% | -|2.03% | 3.65% | 0.2002|
 | Urinary Infection | 0.00% | 0.00% | -|0.62% | 0.00% | 0.2722|
 | Deep Vein Thrombosis | 0.00% | 0.00% | -|0.78% | 1.56% | 0.3306|
 | Renal Insufficiency | 0.25% | 0.47% | 0.5639|0.00% | 0.00% | -|
 | Pulmonary Embolism | 0.25% | 0.47% | 0.5639|0.31% | 1.04% | 0.2002|
 | Ventilator Dependent | 0.00% | 0.00% | -|0.31% | 1.04% | 0.2002|
 | Acute Renal Failure | 0.00% | 0.00% | -|0.31% | 1.04% | 0.2002|
 | CVA with Neurologic Deficit | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Myocardial Infarction | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Sepsis | 0.25% | 0.47% | 0.5639|1.72% | 2.60% | 0.4333|
 | Readmission | 3.45% | 4.74% | 0.3564|**4.69**% | **9.38**% | **0.01456**|
 | Unplanned Readmission | 3.45% | 4.74% | 0.3564|**3.91**% | **7.81**% | **0.02648**|


| | Outpatient Non-COPD (N = 1565) | Outpatient COPD (N = 220) | p-value | Inpatient Non-COPD (N = 836) | Inpatient COPD (N = 204) | p-value |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
 | Superficial SSI | 0.00% | 0.00% | -|0.48% | 0.49% | 0.9827|
 | Deep SSI | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Organ/Space SSI | 0.51% | 0.91% | 0.4591|2.87% | 5.39% | 0.07339|
 | Wound Disruption | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Pneumonia | 0.00% | 0.00% | -|3.47% | 5.39% | 0.2003|
 | Reintubation | 0.00% | 0.00% | -|2.03% | 3.92% | 0.1144|
 | Urinary Infection | 0.00% | 0.00% | -|0.60% | 0.00% | 0.2682|
 | Deep Vein Thrombosis | 0.00% | 0.00% | -|0.72% | 1.96% | 0.1028|
 | Renal Insufficiency | 0.19% | 0.91% | 0.05941|0.00% | 0.00% | -|
 | Pulmonary Embolism | 0.26% | 0.45% | 0.6011|0.36% | 0.98% | 0.2499|
 | Ventilator Dependent | 0.00% | 0.00% | -|0.36% | 0.98% | 0.2499|
 | Acute Renal Failure | 0.00% | 0.00% | -|**0.24**% | **1.47**% | **0.02263**|
 | CVA with Neurologic Deficit | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Myocardial Infarction | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Sepsis | 0.19% | 0.91% | 0.05941|1.67% | 2.94% | 0.2376|
 | Readmission | 3.45% | 5.00% | 0.2506|**4.78**% | **9.80**% | **0.005839**|
 | Unplanned Readmission | 3.45% | 5.00% | 0.2506|**3.95**% | **8.33**% | **0.008654**|


| | Outpatient Non-CGF (N = 1920) | Outpatient CGF (N = 222) | p-value | Inpatient Non-CGF (N = 1043) | Inpatient CGF (N = 205) | p-value |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
 | Superficial SSI | 0.00% | 0.00% | -|0.48% | 0.49% | 0.9873|
 | Deep SSI | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Organ/Space SSI | 0.52% | 0.90% | 0.4726|2.97% | 5.37% | 0.08232|
 | Wound Disruption | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Pneumonia | 0.00% | 0.00% | -|3.45% | 5.85% | 0.1021|
 | Reintubation | 0.00% | 0.00% | -|**2.01**% | **4.39**% | **0.04224**|
 | Urinary Infection | 0.00% | 0.00% | -|0.58% | 0.00% | 0.2763|
 | Deep Vein Thrombosis | 0.00% | 0.00% | -|0.77% | 1.95% | 0.1122|
 | Renal Insufficiency | 0.21% | 0.90% | 0.06453|0.00% | 0.00% | -|
 | Pulmonary Embolism | 0.26% | 0.45% | 0.612|0.38% | 0.98% | 0.2625|
 | Ventilator Dependent | 0.00% | 0.00% | -|0.38% | 0.98% | 0.2625|
 | Acute Renal Failure | 0.00% | 0.00% | -|**0.29**% | **1.46**% | **0.02609**|
 | CVA with Neurologic Deficit | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Myocardial Infarction | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Sepsis | 0.21% | 0.90% | 0.06453|1.73% | 2.93% | 0.2523|
 | Readmission | 3.49% | 4.95% | 0.2698|**4.99**% | **9.76**% | **0.007405**|
 | Unplanned Readmission | 3.49% | 4.95% | 0.2698|**4.12**% | **8.29**% | **0.01073**|


| | Outpatient Non-Disseminated Cancer (N = 2276) | Outpatient Disseminated Cancer (N = 223) | p-value | Inpatient Non-Disseminated Cancer (N = 1238) | Inpatient Disseminated Cancer (N = 218) | p-value |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
 | Superficial SSI | 0.00% | 0.00% | -|0.48% | 0.46% | 0.9593|
 | Deep SSI | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Organ/Space SSI | 0.53% | 0.90% | 0.4803|3.07% | 5.05% | 0.1357|
 | Wound Disruption | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Pneumonia | 0.00% | 0.00% | -|3.47% | 5.96% | 0.07793|
 | Reintubation | 0.00% | 0.00% | -|2.10% | 4.13% | 0.07141|
 | Urinary Infection | 0.00% | 0.00% | -|0.57% | 0.00% | 0.2657|
 | Deep Vein Thrombosis | 0.00% | 0.00% | -|0.81% | 1.83% | 0.1519|
 | Renal Insufficiency | 0.22% | 0.90% | 0.06785|0.00% | 0.00% | -|
 | Pulmonary Embolism | 0.26% | 0.45% | 0.6182|0.40% | 0.92% | 0.3121|
 | Ventilator Dependent | 0.00% | 0.00% | -|0.40% | 0.92% | 0.3121|
 | Acute Renal Failure | 0.00% | 0.00% | -|**0.24**% | **1.83**% | **0.001721**|
 | CVA with Neurologic Deficit | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Myocardial Infarction | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Sepsis | 0.22% | 0.90% | 0.06785|1.78% | 2.75% | 0.3336|
 | Readmission | 3.51% | 4.93% | 0.2807|**5.09**% | **9.63**% | **0.007968**|
 | Unplanned Readmission | 3.51% | 4.93% | 0.2807|**4.20**% | **8.26**% | **0.009833**|


| | Outpatient Non-Steroid (N = 2621) | Outpatient Steroid (N = 235) | p-value | Inpatient Non-Steroid (N = 1425) | Inpatient Steroid (N = 239) | p-value |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
 | Superficial SSI | 0.00% | 0.00% | -|0.49% | 0.42% | 0.8803|
 | Deep SSI | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Organ/Space SSI | 0.53% | 0.85% | 0.5329|3.02% | 5.44% | 0.0547|
 | Wound Disruption | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Pneumonia | 0.00% | 0.00% | -|3.51% | 5.86% | 0.08056|
 | Reintubation | 0.00% | 0.00% | -|2.11% | 4.18% | 0.05217|
 | Urinary Infection | 0.00% | 0.00% | -|0.56% | 0.00% | 0.2456|
 | Deep Vein Thrombosis | 0.00% | 0.00% | -|0.84% | 1.67% | 0.2228|
 | Renal Insufficiency | 0.23% | 0.85% | 0.08386|0.00% | 0.00% | -|
 | Pulmonary Embolism | 0.27% | 0.43% | 0.6597|0.35% | 1.26% | 0.06142|
 | Ventilator Dependent | 0.00% | 0.00% | -|0.42% | 0.84% | 0.3898|
 | Acute Renal Failure | 0.00% | 0.00% | -|**0.21**% | **2.09**% | **9.962e-05**|
 | CVA with Neurologic Deficit | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Myocardial Infarction | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Sepsis | 0.23% | 0.85% | 0.08386|1.68% | 3.35% | 0.0832|
 | Readmission | 3.55% | 4.68% | 0.3746|**5.26**% | **8.79**% | **0.03062**|
 | Unplanned Readmission | 3.55% | 4.68% | 0.3746|**4.35**% | **7.53**% | **0.03342**|


| | Outpatient Non-Bleeding Disorder (N = 2975) | Outpatient Bleeding Disorder (N = 238) | p-value | Inpatient Non-Bleeding Disorder (N = 1627) | Inpatient Bleeding Disorder (N = 245) | p-value |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
 | Superficial SSI | 0.00% | 0.00% | -|0.49% | 0.41% | 0.8601|
 | Deep SSI | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Organ/Space SSI | 0.54% | 0.84% | 0.5474|3.07% | 5.31% | 0.07078|
 | Wound Disruption | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Pneumonia | 0.00% | 0.00% | -|3.56% | 5.71% | 0.1029|
 | Reintubation | 0.00% | 0.00% | -|2.15% | 4.08% | 0.0659|
 | Urinary Infection | 0.00% | 0.00% | -|0.55% | 0.00% | 0.2432|
 | Deep Vein Thrombosis | 0.00% | 0.00% | -|0.86% | 1.63% | 0.2482|
 | Renal Insufficiency | 0.24% | 0.84% | 0.08924|0.00% | 0.00% | -|
 | Pulmonary Embolism | 0.27% | 0.42% | 0.6709|0.37% | 1.22% | 0.07104|
 | Ventilator Dependent | 0.00% | 0.00% | -|0.43% | 0.82% | 0.4154|
 | Acute Renal Failure | 0.00% | 0.00% | -|**0.18**% | **2.45**% | **1.776e-06**|
 | CVA with Neurologic Deficit | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Myocardial Infarction | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Sepsis | 0.24% | 0.84% | 0.08924|1.72% | 3.27% | 0.1008|
 | Readmission | 3.56% | 4.62% | 0.4014|**5.35**% | **8.57**% | **0.04361**|
 | Unplanned Readmission | 3.56% | 4.62% | 0.4014|**4.43**% | **7.35**% | **0.04628**|


| | Outpatient Non-Independent Functional Health Status (N = 2980) | Outpatient Independent Functional Health Status (N = 590) | p-value | Inpatient Non-Independent Functional Health Status (N = 1635) | Inpatient Independent Functional Health Status (N = 445) | p-value |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
 | Superficial SSI | 0.00% | 0.00% | -|0.49% | 0.45% | 0.9142|
 | Deep SSI | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Organ/Space SSI | 0.54% | 0.68% | 0.6749|3.12% | 4.27% | 0.2328|
 | Wound Disruption | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Pneumonia | 0.00% | 0.00% | -|3.67% | 4.49% | 0.4225|
 | Reintubation | 0.00% | 0.00% | -|2.26% | 2.92% | 0.4215|
 | Urinary Infection | 0.00% | 0.00% | -|0.55% | 0.22% | 0.3784|
 | Deep Vein Thrombosis | 0.00% | 0.00% | -|0.92% | 1.12% | 0.6928|
 | Renal Insufficiency | 0.23% | 0.51% | 0.2507|0.00% | 0.00% | -|
 | Pulmonary Embolism | 0.27% | 0.34% | 0.7671|0.37% | 0.90% | 0.1504|
 | Ventilator Dependent | 0.00% | 0.00% | -|0.43% | 0.67% | 0.5059|
 | Acute Renal Failure | 0.00% | 0.00% | -|**0.18**% | **1.57**% | **0.0001719**|
 | CVA with Neurologic Deficit | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Myocardial Infarction | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Sepsis | 0.23% | 0.51% | 0.2507|1.71% | 2.70% | 0.1802|
 | Readmission | 3.56% | 4.07% | 0.5451|5.32% | 7.42% | 0.09292|
 | Unplanned Readmission | 3.56% | 4.07% | 0.5451|4.40% | 6.29% | 0.09874|


| | Outpatient Non-Totally or Partially Dependent Functional Health Status (N = 3335) | Outpatient Totally or Partially Dependent Functional Health Status (N = 592) | p-value | Inpatient Non-Totally or Partially Dependent Functional Health Status (N = 1839) | Inpatient Totally or Partially Dependent Functional Health Status (N = 449) | p-value |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
 | Superficial SSI | 0.00% | 0.00% | -|0.49% | 0.45% | 0.9039|
 | Deep SSI | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Organ/Space SSI | 0.54% | 0.68% | 0.683|3.10% | 4.45% | 0.1535|
 | Wound Disruption | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Pneumonia | 0.00% | 0.00% | -|3.64% | 4.68% | 0.3072|
 | Reintubation | 0.00% | 0.00% | -|2.23% | 3.12% | 0.2704|
 | Urinary Infection | 0.00% | 0.00% | -|0.54% | 0.22% | 0.3779|
 | Deep Vein Thrombosis | 0.00% | 0.00% | -|0.92% | 1.11% | 0.7127|
 | Renal Insufficiency | 0.24% | 0.51% | 0.2575|0.00% | 0.00% | -|
 | Pulmonary Embolism | 0.27% | 0.34% | 0.7731|0.38% | 0.89% | 0.1611|
 | Ventilator Dependent | 0.00% | 0.00% | -|0.44% | 0.67% | 0.522|
 | Acute Renal Failure | 0.00% | 0.00% | -|**0.22**% | **1.56**% | **0.0002293**|
 | CVA with Neurologic Deficit | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Myocardial Infarction | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Sepsis | 0.24% | 0.51% | 0.2575|1.74% | 2.67% | 0.1971|
 | Readmission | 3.57% | 4.05% | 0.5609|5.38% | 7.35% | 0.1091|
 | Unplanned Readmission | 3.57% | 4.05% | 0.5609|4.46% | 6.24% | 0.1145|
 
 
 ### Notes
 I did not perform this analysis for Ventilator Dependent, Ascites, and Acute Renal Failure due to lack of patients with the conditions in both outpatient and inpatient settings. 








