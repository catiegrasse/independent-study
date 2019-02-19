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

| | Non-Diabetes (N = 804.0) | Diabetes (N = 117.0) | p-value | 
| ------------- | ------------- | ------------- | ------------- |
 | Smoke | 19.9% | 18.8% | 0.7807 | 
 | Dyspnea | 3.234% | 6.838% | 0.05341 | 
 | Ventilator Dependent | 0.1244% | 0.8547% | 0.1128 | 
 | COPD | 2.861% | 6.838% | **0.02584** | 
 | Hypertension | 27.24% | 75.21% | **8.22e-25** | 
 | Disseminated Cancer | 2.114% | 0.8547% | 0.3577 | 
 | Steroid | 5.846% | 4.274% | 0.4912 | 
 | Bleeding Disorder | 1.119% | 2.564% | 0.1979 | 
 | Independent Functional Health Status | 98.51% | 93.16% | **0.0002104** | 
 | Totally or Partially Dependent Functional Health Status | 0.6219% | 4.274% | **0.0003694** | 


| | Non-Smoke (N = 739.0) | Smoke (N = 182.0) | p-value | 
| ------------- | ------------- | ------------- | ------------- |
 | Diabetes | 12.86% | 12.09% | 0.7807 | 
 | Dyspnea | 2.706% | 7.692% | **0.001396** | 
 | Ventilator Dependent | 0% | 1.099% | **0.004333** | 
 | COPD | 2.436% | 7.143% | **0.00161** | 
 | Hypertension | 31.39% | 41.21% | **0.01187** | 
 | Disseminated Cancer | 2.03% | 1.648% | 0.7392 | 
 | Steroid | 6.089% | 3.846% | 0.2402 | 
 | Bleeding Disorder | 1.488% | 0.5495% | 0.317 | 
 | Independent Functional Health Status | 97.97% | 97.25% | 0.5519 | 
 | Totally or Partially Dependent Functional Health Status | 0.9472% | 1.648% | 0.4136 | 


| | Non-Hypertension (N = 614.0) | Hypertension (N = 307.0) | p-value | 
| ------------- | ------------- | ------------- | ------------- |
 | Diabetes | 4.723% | 28.66% | **8.22e-25** | 
 | Smoke | 17.43% | 24.43% | **0.01187** | 
 | Dyspnea | 2.443% | 6.189% | **0.004482** | 
 | Ventilator Dependent | 0% | 0.6515% | **0.04527** | 
 | COPD | 1.954% | 6.189% | **0.0007822** | 
 | Disseminated Cancer | 2.28% | 1.303% | 0.3125 | 
 | Steroid | 4.886% | 7.166% | 0.1576 | 
 | Bleeding Disorder | 0.9772% | 1.954% | 0.2176 | 
 | Independent Functional Health Status | 98.21% | 97.07% | 0.2631 | 
 | Totally or Partially Dependent Functional Health Status | 0.8143% | 1.629% | 0.2609 | 


| | Non-Dyspnea (N = 887.0) | Dyspnea (N = 34.0) | p-value | 
| ------------- | ------------- | ------------- | ------------- |
 | Diabetes | 12.29% | 23.53% | 0.05341 | 
 | Smoke | 18.94% | 41.18% | **0.001396** | 
 | Ventilator Dependent | 0.2255% | 0% | 0.7816 | 
 | COPD | 2.368% | 29.41% | **9.418e-18** | 
 | Hypertension | 32.47% | 55.88% | **0.004482** | 
 | Disseminated Cancer | 1.804% | 5.882% | 0.0918 | 
 | Steroid | 5.637% | 5.882% | 0.9515 | 
 | Bleeding Disorder | 1.015% | 8.824% | **8.133e-05** | 
 | Independent Functional Health Status | 97.86% | 97.06% | 0.7537 | 
 | Totally or Partially Dependent Functional Health Status | 1.015% | 2.941% | 0.2874 | 


| | Non-COPD (N = 890.0) | COPD (N = 31.0) | p-value | 
| ------------- | ------------- | ------------- | ------------- |
 | Diabetes | 12.25% | 25.81% | **0.02584** | 
 | Smoke | 18.99% | 41.94% | **0.00161** | 
 | Dyspnea | 2.697% | 32.26% | **9.418e-18** | 
 | Ventilator Dependent | 0.2247% | 0% | 0.7916 | 
 | Hypertension | 32.36% | 61.29% | **0.0007822** | 
 | Disseminated Cancer | 1.91% | 3.226% | 0.6029 | 
 | Steroid | 5.393% | 12.9% | 0.07493 | 
 | Bleeding Disorder | 1.011% | 9.677% | **2.88e-05** | 
 | Independent Functional Health Status | 97.87% | 96.77% | 0.682 | 
 | Totally or Partially Dependent Functional Health Status | 1.011% | 3.226% | 0.2422 | 


| | Non-CGF (N = 915.0) | CGF (N = 6.0) | p-value | 
| ------------- | ------------- | ------------- | ------------- |
 | Diabetes | 12.57% | 33.33% | 0.1279 | 
 | Smoke | 19.67% | 33.33% | 0.4022 | 
 | Dyspnea | 3.607% | 16.67% | 0.09082 | 
 | Ventilator Dependent | 0.2186% | 0% | 0.9087 | 
 | COPD | 3.169% | 33.33% | **4.437e-05** | 
 | Hypertension | 33.01% | 83.33% | **0.009145** | 
 | Disseminated Cancer | 1.967% | 0% | 0.7286 | 
 | Steroid | 5.683% | 0% | 0.5477 | 
 | Bleeding Disorder | 1.311% | 0% | 0.7777 | 
 | Independent Functional Health Status | 98.03% | 66.67% | **1.487e-07** | 
 | Totally or Partially Dependent Functional Health Status | 0.8743% | 33.33% | **2.057e-14** | 


| | Non-Disseminated Cancer (N = 903.0) | Disseminated Cancer (N = 18.0) | p-value | 
| ------------- | ------------- | ------------- | ------------- |
 | Diabetes | 12.85% | 5.556% | 0.3577 | 
 | Smoke | 19.82% | 16.67% | 0.7392 | 
 | Dyspnea | 3.544% | 11.11% | 0.0918 | 
 | Ventilator Dependent | 0.2215% | 0% | 0.8416 | 
 | COPD | 3.322% | 5.556% | 0.6029 | 
 | Hypertension | 33.55% | 22.22% | 0.3125 | 
 | Steroid | 5.316% | 22.22% | **0.00209** | 
 | Bleeding Disorder | 0.9967% | 16.67% | **6.435e-09** | 
 | Independent Functional Health Status | 97.79% | 100.0% | 0.5232 | 
 | Totally or Partially Dependent Functional Health Status | 1.107% | 0% | 0.6535 | 


| | Non-Steroid (N = 869.0) | Steroid (N = 52.0) | p-value | 
| ------------- | ------------- | ------------- | ------------- |
 | Diabetes | 12.89% | 9.615% | 0.4912 | 
 | Smoke | 20.14% | 13.46% | 0.2402 | 
 | Dyspnea | 3.682% | 3.846% | 0.9515 | 
 | Ventilator Dependent | 0.2301% | 0% | 0.7291 | 
 | COPD | 3.107% | 7.692% | 0.07493 | 
 | Hypertension | 32.8% | 42.31% | 0.1576 | 
 | Disseminated Cancer | 1.611% | 7.692% | **0.00209** | 
 | Bleeding Disorder | 1.036% | 5.769% | **0.003457** | 
 | Independent Functional Health Status | 97.93% | 96.15% | 0.3937 | 
 | Totally or Partially Dependent Functional Health Status | 0.9206% | 3.846% | **0.048** | 


| | Non-Bleeding Disorder (N = 909.0) | Bleeding Disorder (N = 12.0) | p-value | 
| ------------- | ------------- | ------------- | ------------- |
 | Diabetes | 12.54% | 25.0% | 0.1979 | 
 | Smoke | 19.91% | 8.333% | 0.317 | 
 | Dyspnea | 3.41% | 25.0% | **8.133e-05** | 
 | Ventilator Dependent | 0.22% | 0% | 0.8708 | 
 | COPD | 3.08% | 25.0% | **2.88e-05** | 
 | Hypertension | 33.11% | 50.0% | 0.2176 | 
 | Disseminated Cancer | 1.65% | 25.0% | **6.435e-09** | 
 | Steroid | 5.391% | 25.0% | **0.003457** | 
 | Independent Functional Health Status | 97.91% | 91.67% | 0.1405 | 
 | Totally or Partially Dependent Functional Health Status | 1.1% | 0% | 0.7149 | 


| | Non-Independent Functional Health Status (N = 20.0) | Independent Functional Health Status (N = 901.0) | p-value | 
| ------------- | ------------- | ------------- | ------------- |
 | Diabetes | 40.0% | 12.1% | **0.0002104** | 
 | Smoke | 25.0% | 19.64% | 0.5519 | 
 | Dyspnea | 5.0% | 3.663% | 0.7537 | 
 | Ventilator Dependent | 5.0% | 0.111% | **3.388e-06** | 
 | COPD | 5.0% | 3.33% | 0.682 | 
 | Hypertension | 45.0% | 33.07% | 0.2631 | 
 | Disseminated Cancer | 0% | 1.998% | 0.5232 | 
 | Steroid | 10.0% | 5.549% | 0.3937 | 
 | Bleeding Disorder | 5.0% | 1.221% | 0.1405 | 
 | Totally or Partially Dependent Functional Health Status | 50.0% | 0% | **4.711e-101** | 


| | Non-Totally or Partially Dependent Functional Health Status (N = 911.0) | Totally or Partially Dependent Functional Health Status (N = 10.0) | p-value | 
| ------------- | ------------- | ------------- | ------------- |
 | Diabetes | 12.29% | 50.0% | **0.0003694** | 
 | Smoke | 19.65% | 30.0% | 0.4136 | 
 | Dyspnea | 3.622% | 10.0% | 0.2874 | 
 | Ventilator Dependent | 0.2195% | 0% | 0.8821 | 
 | COPD | 3.293% | 10.0% | 0.2422 | 
 | Hypertension | 33.15% | 50.0% | 0.2609 | 
 | Disseminated Cancer | 1.976% | 0% | 0.6535 | 
 | Steroid | 5.488% | 20.0% | **0.048** | 
 | Bleeding Disorder | 1.317% | 0% | 0.7149 | 
 | Independent Functional Health Status | 98.9% | 0% | **4.711e-101** | 

 ## Expanded Table 3
 
| | Non-Diabetes (N = 804.0) | Diabetes (N = 117.0) | p-value | 
| ------------- | ------------- | ------------- | ------------- |
 | Superficial SSI | 0.2488% | 0% | 0.5891 | 
 | Deep SSI | 0.1244% | 0% | 0.7027 | 
 | Organ/Space SSI | 0.8706% | 1.709% | 0.3888 | 
 | Wound Disruption | 0.2488% | 0% | 0.5891 | 
 | Pneumonia | 0.4975% | 5.983% | **3.34e-07** | 
 | Reintubation | 0.6219% | 5.128% | **2.761e-05** | 
 | Urinary Infection | 0.2488% | 1.709% | **0.02478** | 
 | Deep Vein Thrombosis | 0.2488% | 1.709% | **0.02478** | 
 | Renal Insufficiency | 0.1244% | 0.8547% | 0.1128 | 
 | Pulmonary Embolism | 0.4975% | 0% | 0.4445 | 
 | Ventilator | 0.7463% | 5.128% | **9.414e-05** | 
 | Acute Renal Failure | 0.1244% | 0% | 0.7027 | 
 | CVA with Neurologic Deficit | 0.2488% | 0% | 0.5891 | 
 | Myocardial Infarction | 0% | 0% | - | 
 | Sepsis | 0.7463% | 1.709% | 0.2942 | 
 | Readmission | 3.234% | 6.838% | 0.05341 | 
 | Unplanned Readmission | 2.736% | 6.838% | **0.01955** | 


| | Non-Smoke (N = 739.0) | Smoke (N = 182.0) | p-value | 
| ------------- | ------------- | ------------- | ------------- |
 | Superficial SSI | 0.2706% | 0% | 0.4823 | 
 | Deep SSI | 0.1353% | 0% | 0.6195 | 
 | Organ/Space SSI | 0.5413% | 2.747% | **0.006728** | 
 | Wound Disruption | 0.2706% | 0% | 0.4823 | 
 | Pneumonia | 1.353% | 0.5495% | 0.3713 | 
 | Reintubation | 1.083% | 1.648% | 0.5291 | 
 | Urinary Infection | 0.5413% | 0% | 0.3199 | 
 | Deep Vein Thrombosis | 0.2706% | 1.099% | 0.128 | 
 | Renal Insufficiency | 0.2706% | 0% | 0.4823 | 
 | Pulmonary Embolism | 0.2706% | 1.099% | 0.128 | 
 | Ventilator | 1.083% | 2.198% | 0.2346 | 
 | Acute Renal Failure | 0.1353% | 0% | 0.6195 | 
 | CVA with Neurologic Deficit | 0.1353% | 0.5495% | 0.2823 | 
 | Myocardial Infarction | 0% | 0% | - | 
 | Sepsis | 0.8119% | 1.099% | 0.7086 | 
 | Readmission | 3.383% | 4.945% | 0.3168 | 
 | Unplanned Readmission | 2.977% | 4.396% | 0.3342 | 


| | Non-Hypertension (N = 614.0) | Hypertension (N = 307.0) | p-value | 
| ------------- | ------------- | ------------- | ------------- |
 | Superficial SSI | 0% | 0.6515% | **0.04527** | 
 | Deep SSI | 0.1629% | 0% | 0.4793 | 
 | Organ/Space SSI | 0.6515% | 1.629% | 0.1553 | 
 | Wound Disruption | 0.1629% | 0.3257% | 0.6167 | 
 | Pneumonia | 0.8143% | 1.954% | 0.1333 | 
 | Reintubation | 0.8143% | 1.954% | 0.1333 | 
 | Urinary Infection | 0.3257% | 0.6515% | 0.4785 | 
 | Deep Vein Thrombosis | 0.3257% | 0.6515% | 0.4785 | 
 | Renal Insufficiency | 0% | 0.6515% | **0.04527** | 
 | Pulmonary Embolism | 0.4886% | 0.3257% | 0.7231 | 
 | Ventilator | 1.303% | 1.303% | 1.0 | 
 | Acute Renal Failure | 0% | 0.3257% | 0.1571 | 
 | CVA with Neurologic Deficit | 0.1629% | 0.3257% | 0.6167 | 
 | Myocardial Infarction | 0% | 0% | - | 
 | Sepsis | 0.3257% | 1.954% | **0.01204** | 
 | Readmission | 2.117% | 6.84% | **0.000339** | 
 | Unplanned Readmission | 1.954% | 5.863% | **0.001632** | 


| | Non-Dyspnea (N = 887.0) | Dyspnea (N = 34.0) | p-value | 
| ------------- | ------------- | ------------- | ------------- |
 | Superficial SSI | 0.2255% | 0% | 0.7816 | 
 | Deep SSI | 0.1127% | 0% | 0.8447 | 
 | Organ/Space SSI | 1.015% | 0% | 0.555 | 
 | Wound Disruption | 0.2255% | 0% | 0.7816 | 
 | Pneumonia | 1.24% | 0% | 0.5136 | 
 | Reintubation | 1.24% | 0% | 0.5136 | 
 | Urinary Infection | 0.3382% | 2.941% | **0.02351** | 
 | Deep Vein Thrombosis | 0.451% | 0% | 0.6947 | 
 | Renal Insufficiency | 0.2255% | 0% | 0.7816 | 
 | Pulmonary Embolism | 0.451% | 0% | 0.6947 | 
 | Ventilator | 1.353% | 0% | 0.4948 | 
 | Acute Renal Failure | 0% | 2.941% | **3.214e-07** | 
 | CVA with Neurologic Deficit | 0.2255% | 0% | 0.7816 | 
 | Myocardial Infarction | 0% | 0% | - | 
 | Sepsis | 0.9019% | 0% | 0.5781 | 
 | Readmission | 3.608% | 5.882% | 0.49 | 
 | Unplanned Readmission | 3.157% | 5.882% | 0.3796 | 


| | Non-COPD (N = 890.0) | COPD (N = 31.0) | p-value | 
| ------------- | ------------- | ------------- | ------------- |
 | Superficial SSI | 0.2247% | 0% | 0.7916 | 
 | Deep SSI | 0.1124% | 0% | 0.8519 | 
 | Organ/Space SSI | 0.8989% | 3.226% | 0.1954 | 
 | Wound Disruption | 0.2247% | 0% | 0.7916 | 
 | Pneumonia | 1.124% | 3.226% | 0.2895 | 
 | Reintubation | 1.124% | 3.226% | 0.2895 | 
 | Urinary Infection | 0.3371% | 3.226% | **0.0162** | 
 | Deep Vein Thrombosis | 0.3371% | 3.226% | **0.0162** | 
 | Renal Insufficiency | 0.1124% | 3.226% | **0.0002514** | 
 | Pulmonary Embolism | 0.4494% | 0% | 0.7083 | 
 | Ventilator | 1.236% | 3.226% | 0.3369 | 
 | Acute Renal Failure | 0% | 3.226% | **8.274e-08** | 
 | CVA with Neurologic Deficit | 0.2247% | 0% | 0.7916 | 
 | Myocardial Infarction | 0% | 0% | - | 
 | Sepsis | 0.6742% | 6.452% | **0.0006551** | 
 | Readmission | 3.483% | 9.677% | 0.07217 | 
 | Unplanned Readmission | 3.034% | 9.677% | **0.04052** | 


| | Non-CGF (N = 915.0) | CGF (N = 6.0) | p-value | 
| ------------- | ------------- | ------------- | ------------- |
 | Superficial SSI | 0.2186% | 0% | 0.9087 | 
 | Deep SSI | 0.1093% | 0% | 0.9354 | 
 | Organ/Space SSI | 0.9836% | 0% | 0.8071 | 
 | Wound Disruption | 0.2186% | 0% | 0.9087 | 
 | Pneumonia | 1.093% | 16.67% | **0.0004649** | 
 | Reintubation | 1.093% | 16.67% | **0.0004649** | 
 | Urinary Infection | 0.4372% | 0% | 0.8711 | 
 | Deep Vein Thrombosis | 0.4372% | 0% | 0.8711 | 
 | Renal Insufficiency | 0.2186% | 0% | 0.9087 | 
 | Pulmonary Embolism | 0.4372% | 0% | 0.8711 | 
 | Ventilator | 1.311% | 0% | 0.7777 | 
 | Acute Renal Failure | 0.1093% | 0% | 0.9354 | 
 | CVA with Neurologic Deficit | 0.2186% | 0% | 0.9087 | 
 | Myocardial Infarction | 0% | 0% | - | 
 | Sepsis | 0.8743% | 0% | 0.8181 | 
 | Readmission | 3.716% | 0% | 0.6304 | 
 | Unplanned Readmission | 3.279% | 0% | 0.652 | 


| | Non-Disseminated Cancer (N = 903.0) | Disseminated Cancer (N = 18.0) | p-value | 
| ------------- | ------------- | ------------- | ------------- |
 | Superficial SSI | 0.2215% | 0% | 0.8416 | 
 | Deep SSI | 0.1107% | 0% | 0.8877 | 
 | Organ/Space SSI | 0.9967% | 0% | 0.6704 | 
 | Wound Disruption | 0.2215% | 0% | 0.8416 | 
 | Pneumonia | 1.107% | 5.556% | 0.0854 | 
 | Reintubation | 1.218% | 0% | 0.6376 | 
 | Urinary Infection | 0.443% | 0% | 0.7772 | 
 | Deep Vein Thrombosis | 0.443% | 0% | 0.7772 | 
 | Renal Insufficiency | 0.2215% | 0% | 0.8416 | 
 | Pulmonary Embolism | 0.443% | 0% | 0.7772 | 
 | Ventilator | 1.218% | 5.556% | 0.1081 | 
 | Acute Renal Failure | 0% | 5.556% | **1.374e-12** | 
 | CVA with Neurologic Deficit | 0.2215% | 0% | 0.8416 | 
 | Myocardial Infarction | 0% | 0% | - | 
 | Sepsis | 0.8859% | 0% | 0.6884 | 
 | Readmission | 3.654% | 5.556% | 0.6719 | 
 | Unplanned Readmission | 3.212% | 5.556% | 0.5791 | 


| | Non-Steroid (N = 869.0) | Steroid (N = 52.0) | p-value | 
| ------------- | ------------- | ------------- | ------------- |
 | Superficial SSI | 0.2301% | 0% | 0.7291 | 
 | Deep SSI | 0% | 1.923% | **4.31e-05** | 
 | Organ/Space SSI | 0.8055% | 3.846% | **0.03038** | 
 | Wound Disruption | 0.1151% | 1.923% | **0.006516** | 
 | Pneumonia | 1.151% | 1.923% | 0.6185 | 
 | Reintubation | 1.036% | 3.846% | 0.06996 | 
 | Urinary Infection | 0.3452% | 1.923% | 0.09282 | 
 | Deep Vein Thrombosis | 0.3452% | 1.923% | 0.09282 | 
 | Renal Insufficiency | 0.2301% | 0% | 0.7291 | 
 | Pulmonary Embolism | 0.2301% | 3.846% | **0.0001173** | 
 | Ventilator | 1.151% | 3.846% | 0.09593 | 
 | Acute Renal Failure | 0% | 1.923% | **4.31e-05** | 
 | CVA with Neurologic Deficit | 0.2301% | 0% | 0.7291 | 
 | Myocardial Infarction | 0% | 0% | - | 
 | Sepsis | 0.5754% | 5.769% | **8.833e-05** | 
 | Readmission | 3.797% | 1.923% | 0.4862 | 
 | Unplanned Readmission | 3.337% | 1.923% | 0.5769 | 


| | Non-Bleeding Disorder (N = 909.0) | Bleeding Disorder (N = 12.0) | p-value | 
| ------------- | ------------- | ------------- | ------------- |
 | Superficial SSI | 0.22% | 0% | 0.8708 | 
 | Deep SSI | 0.11% | 0% | 0.9085 | 
 | Organ/Space SSI | 0.9901% | 0% | 0.7291 | 
 | Wound Disruption | 0.22% | 0% | 0.8708 | 
 | Pneumonia | 1.21% | 0% | 0.7014 | 
 | Reintubation | 1.21% | 0% | 0.7014 | 
 | Urinary Infection | 0.44% | 0% | 0.8179 | 
 | Deep Vein Thrombosis | 0.44% | 0% | 0.8179 | 
 | Renal Insufficiency | 0.22% | 0% | 0.8708 | 
 | Pulmonary Embolism | 0.44% | 0% | 0.8179 | 
 | Ventilator | 1.21% | 8.333% | **0.03064** | 
 | Acute Renal Failure | 0% | 8.333% | **3.088e-18** | 
 | CVA with Neurologic Deficit | 0.22% | 0% | 0.8708 | 
 | Myocardial Infarction | 0% | 0% | - | 
 | Sepsis | 0.8801% | 0% | 0.7441 | 
 | Readmission | 3.74% | 0% | 0.4948 | 
 | Unplanned Readmission | 3.3% | 0% | 0.5223 | 


| | Non-Independent Functional Health Status (N = 20.0) | Independent Functional Health Status (N = 901.0) | p-value | 
| ------------- | ------------- | ------------- | ------------- |
 | Superficial SSI | 5.0% | 0.111% | **3.388e-06** | 
 | Deep SSI | 0% | 0.111% | 0.8815 | 
 | Organ/Space SSI | 5.0% | 0.8879% | 0.06445 | 
 | Wound Disruption | 5.0% | 0.111% | **3.388e-06** | 
 | Pneumonia | 10.0% | 0.9989% | **0.0002472** | 
 | Reintubation | 10.0% | 0.9989% | **0.0002472** | 
 | Urinary Infection | 0% | 0.444% | 0.7652 | 
 | Deep Vein Thrombosis | 5.0% | 0.333% | **0.001693** | 
 | Renal Insufficiency | 0% | 0.222% | 0.8329 | 
 | Pulmonary Embolism | 0% | 0.444% | 0.7652 | 
 | Ventilator | 15.0% | 0.9989% | **4.726e-08** | 
 | Acute Renal Failure | 0% | 0.111% | 0.8815 | 
 | CVA with Neurologic Deficit | 0% | 0.222% | 0.8329 | 
 | Myocardial Infarction | 0% | 0% | - | 
 | Sepsis | 5.0% | 0.7769% | **0.04411** | 
 | Readmission | 5.0% | 3.663% | 0.7537 | 
 | Unplanned Readmission | 0% | 3.33% | 0.4067 | 


| | Non-Totally or Partially Dependent Functional Health Status (N = 911.0) | Totally or Partially Dependent Functional Health Status (N = 10.0) | p-value | 
| ------------- | ------------- | ------------- | ------------- |
 | Superficial SSI | 0.2195% | 0% | 0.8821 | 
 | Deep SSI | 0.1098% | 0% | 0.9165 | 
 | Organ/Space SSI | 0.8782% | 10.0% | **0.003541** | 
 | Wound Disruption | 0.1098% | 10.0% | **2.353e-11** | 
 | Pneumonia | 0.9879% | 20.0% | **3.707e-08** | 
 | Reintubation | 0.9879% | 20.0% | **3.707e-08** | 
 | Urinary Infection | 0.4391% | 0% | 0.8337 | 
 | Deep Vein Thrombosis | 0.3293% | 10.0% | **3.742e-06** | 
 | Renal Insufficiency | 0.2195% | 0% | 0.8821 | 
 | Pulmonary Embolism | 0.4391% | 0% | 0.8337 | 
 | Ventilator | 1.098% | 20.0% | **1.585e-07** | 
 | Acute Renal Failure | 0.1098% | 0% | 0.9165 | 
 | CVA with Neurologic Deficit | 0.2195% | 0% | 0.8821 | 
 | Myocardial Infarction | 0% | 0% | - | 
 | Sepsis | 0.7684% | 10.0% | **0.001755** | 
 | Readmission | 3.732% | 0% | 0.5336 | 
 | Unplanned Readmission | 3.293% | 0% | 0.5596 | 
 
 ## Expanded Table 4  
 
| | Outpatient Non-Diabetes (N = 556) | Outpatient Diabetes (N = 53) | p-value | Inpatient Non-Diabetes (N = 248) | Inpatient Diabetes (N = 64) | p-value |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
 | Superficial SSI | 0.18% | 0.00% | 0.7573|0.40% | 0.00% | 0.6109|
 | Deep SSI | 0.00% | 0.00% | -|0.40% | 0.00% | 0.6109|
 | Organ/Space SSI | 0.36% | 0.00% | 0.6619|2.02% | 3.12% | 0.5933|
 | Wound Disruption | 0.18% | 0.00% | 0.7573|0.40% | 0.00% | 0.6109|
 | Pneumonia | 0.00% | 0.00% | -|**1.61**% | **10.94**% | **0.0003108**|
 | Reintubation | 0.00% | 0.00% | -|**2.02**% | **9.38**% | **0.004428**|
 | Urinary Infection | 0.00% | 1.89% | **0.001189**|0.81% | 1.56% | 0.5805|
 | Deep Vein Thrombosis | 0.00% | 0.00% | -|0.81% | 3.12% | 0.1416|
 | Renal Insufficiency | 0.18% | 0.00% | 0.7573|**0.00**% | **1.56**% | **0.04865**|
 | Pulmonary Embolism | 0.18% | 0.00% | 0.7573|1.21% | 0.00% | 0.3766|
 | Ventilator | 0.00% | 0.00% | -|**2.42**% | **9.38**% | **0.009887**|
 | Acute Renal Failure | 0.00% | 0.00% | -|0.40% | 0.00% | 0.6109|
 | CVA with Neurologic Deficit | 0.18% | 0.00% | 0.7573|0.40% | 0.00% | 0.6109|
 | Myocardial Infarction | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Sepsis | 0.18% | 0.00% | 0.7573|2.02% | 3.12% | 0.5933|
 | Readmission | 2.70% | 3.77% | 0.6496|4.44% | 9.38% | 0.1206|
 | Unplanned Readmission | 2.52% | 3.77% | 0.585|**3.23**% | **9.38**% | **0.03413**|


| | Outpatient Non-Smoke (N = 500) | Outpatient Smoke (N = 109) | p-value | Inpatient Non-Smoke (N = 239) | Inpatient Smoke (N = 73) | p-value |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
 | Superficial SSI | 0.20% | 0.00% | 0.6403|0.42% | 0.00% | 0.5799|
 | Deep SSI | 0.00% | 0.00% | -|0.42% | 0.00% | 0.5799|
 | Organ/Space SSI | 0.40% | 0.00% | 0.5084|**0.84**% | **6.85**% | **0.002398**|
 | Wound Disruption | 0.20% | 0.00% | 0.6403|0.42% | 0.00% | 0.5799|
 | Pneumonia | 0.00% | 0.00% | -|4.18% | 1.37% | 0.2538|
 | Reintubation | 0.00% | 0.00% | -|3.35% | 4.11% | 0.7573|
 | Urinary Infection | 0.20% | 0.00% | 0.6403|1.26% | 0.00% | 0.3361|
 | Deep Vein Thrombosis | 0.00% | 0.00% | -|0.84% | 2.74% | 0.2059|
 | Renal Insufficiency | 0.20% | 0.00% | 0.6403|0.42% | 0.00% | 0.5799|
 | Pulmonary Embolism | 0.00% | 0.92% | **0.03207**|0.84% | 1.37% | 0.6829|
 | Ventilator | 0.00% | 0.00% | -|3.35% | 5.48% | 0.407|
 | Acute Renal Failure | 0.00% | 0.00% | -|0.42% | 0.00% | 0.5799|
 | CVA with Neurologic Deficit | 0.20% | 0.00% | 0.6403|0.00% | 1.37% | 0.06994|
 | Myocardial Infarction | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Sepsis | 0.20% | 0.00% | 0.6403|2.09% | 2.74% | 0.7436|
 | Readmission | 2.60% | 3.67% | 0.539|5.02% | 6.85% | 0.5469|
 | Unplanned Readmission | 2.40% | 3.67% | 0.4527|4.18% | 5.48% | 0.6399|


| | Outpatient Non-Hypertension (N = 445) | Outpatient Hypertension (N = 164) | p-value | Inpatient Non-Hypertension (N = 169) | Inpatient Hypertension (N = 143) | p-value |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
 | Superficial SSI | 0.00% | 0.61% | 0.09923|0.00% | 0.70% | 0.2762|
 | Deep SSI | 0.00% | 0.00% | -|0.59% | 0.00% | 0.3569|
 | Organ/Space SSI | 0.22% | 0.61% | 0.4613|1.78% | 2.80% | 0.5436|
 | Wound Disruption | 0.22% | 0.00% | 0.5435|0.00% | 0.70% | 0.2762|
 | Pneumonia | 0.00% | 0.00% | -|2.96% | 4.20% | 0.5549|
 | Reintubation | 0.00% | 0.00% | -|2.96% | 4.20% | 0.5549|
 | Urinary Infection | 0.00% | 0.61% | 0.09923|1.18% | 0.70% | 0.6624|
 | Deep Vein Thrombosis | 0.00% | 0.00% | -|1.18% | 1.40% | 0.8663|
 | Renal Insufficiency | 0.00% | 0.61% | 0.09923|0.00% | 0.70% | 0.2762|
 | Pulmonary Embolism | 0.22% | 0.00% | 0.5435|1.18% | 0.70% | 0.6624|
 | Ventilator | 0.00% | 0.00% | -|4.73% | 2.80% | 0.3755|
 | Acute Renal Failure | 0.00% | 0.00% | -|0.00% | 0.70% | 0.2762|
 | CVA with Neurologic Deficit | 0.00% | 0.61% | 0.09923|0.59% | 0.00% | 0.3569|
 | Myocardial Infarction | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Sepsis | 0.00% | 0.61% | 0.09923|1.18% | 3.50% | 0.1693|
 | Readmission | 2.02% | 4.88% | 0.05774|**2.37**% | **9.09**% | **0.009127**|
 | Unplanned Readmission | 2.02% | 4.27% | 0.1243|**1.78**% | **7.69**% | **0.01189**|


| | Outpatient Non-Dyspnea (N = 591) | Outpatient Dyspnea (N = 18) | p-value | Inpatient Non-Dyspnea (N = 296) | Inpatient Dyspnea (N = 16) | p-value |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
 | Superficial SSI | 0.17% | 0.00% | 0.8613|0.34% | 0.00% | 0.8159|
 | Deep SSI | 0.00% | 0.00% | -|0.34% | 0.00% | 0.8159|
 | Organ/Space SSI | 0.34% | 0.00% | 0.8047|2.36% | 0.00% | 0.5338|
 | Wound Disruption | 0.17% | 0.00% | 0.8613|0.34% | 0.00% | 0.8159|
 | Pneumonia | 0.00% | 0.00% | -|3.72% | 0.00% | 0.4324|
 | Reintubation | 0.00% | 0.00% | -|3.72% | 0.00% | 0.4324|
 | Urinary Infection | 0.00% | 5.56% | **9.766e-09**|1.01% | 0.00% | 0.6857|
 | Deep Vein Thrombosis | 0.00% | 0.00% | -|1.35% | 0.00% | 0.6398|
 | Renal Insufficiency | 0.17% | 0.00% | 0.8613|0.34% | 0.00% | 0.8159|
 | Pulmonary Embolism | 0.17% | 0.00% | 0.8613|1.01% | 0.00% | 0.6857|
 | Ventilator | 0.00% | 0.00% | -|4.05% | 0.00% | 0.4115|
 | Acute Renal Failure | 0.00% | 0.00% | -|**0.00**% | **6.25**% | **1.647e-05**|
 | CVA with Neurologic Deficit | 0.17% | 0.00% | 0.8613|0.34% | 0.00% | 0.8159|
 | Myocardial Infarction | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Sepsis | 0.17% | 0.00% | 0.8613|2.36% | 0.00% | 0.5338|
 | Readmission | 2.88% | 0.00% | 0.4655|5.07% | 12.50% | 0.202|
 | Unplanned Readmission | 2.71% | 0.00% | 0.4793|4.05% | 12.50% | 0.1119|


| | Outpatient Non-COPD (N = 593) | Outpatient COPD (N = 16) | p-value | Inpatient Non-COPD (N = 297) | Inpatient COPD (N = 15) | p-value |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
 | Superficial SSI | 0.17% | 0.00% | 0.8694|0.34% | 0.00% | 0.8219|
 | Deep SSI | 0.00% | 0.00% | -|0.34% | 0.00% | 0.8219|
 | Organ/Space SSI | 0.17% | 6.25% | **2.722e-05**|2.36% | 0.00% | 0.5476|
 | Wound Disruption | 0.17% | 0.00% | 0.8694|0.34% | 0.00% | 0.8219|
 | Pneumonia | 0.00% | 0.00% | -|3.37% | 6.67% | 0.499|
 | Reintubation | 0.00% | 0.00% | -|3.37% | 6.67% | 0.499|
 | Urinary Infection | 0.00% | 6.25% | **1.109e-09**|1.01% | 0.00% | 0.6957|
 | Deep Vein Thrombosis | 0.00% | 0.00% | -|1.01% | 6.67% | 0.05744|
 | Renal Insufficiency | 0.00% | 6.25% | **1.109e-09**|0.34% | 0.00% | 0.8219|
 | Pulmonary Embolism | 0.17% | 0.00% | 0.8694|1.01% | 0.00% | 0.6957|
 | Ventilator | 0.00% | 0.00% | -|3.70% | 6.67% | 0.5604|
 | Acute Renal Failure | 0.00% | 0.00% | -|**0.00**% | **6.67**% | **8.317e-06**|
 | CVA with Neurologic Deficit | 0.17% | 0.00% | 0.8694|0.34% | 0.00% | 0.8219|
 | Myocardial Infarction | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Sepsis | 0.00% | 6.25% | **1.109e-09**|2.02% | 6.67% | 0.2358|
 | Readmission | 2.70% | 6.25% | 0.3947|5.05% | 13.33% | 0.1679|
 | Unplanned Readmission | 2.53% | 6.25% | 0.3585|4.04% | 13.33% | 0.08984|


| | Outpatient Non-CGF (N = 607) | Outpatient CGF (N = 2) | p-value | Inpatient Non-CGF (N = 308) | Inpatient CGF (N = 4) | p-value |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
 | Superficial SSI | 0.16% | 0.00% | 0.9542|0.32% | 0.00% | 0.9091|
 | Deep SSI | 0.00% | 0.00% | -|0.32% | 0.00% | 0.9091|
 | Organ/Space SSI | 0.33% | 0.00% | 0.9352|2.27% | 0.00% | 0.7604|
 | Wound Disruption | 0.16% | 0.00% | 0.9542|0.32% | 0.00% | 0.9091|
 | Pneumonia | 0.00% | 0.00% | -|**3.25**% | **25.00**% | **0.01909**|
 | Reintubation | 0.00% | 0.00% | -|**3.25**% | **25.00**% | **0.01909**|
 | Urinary Infection | 0.16% | 0.00% | 0.9542|0.97% | 0.00% | 0.8428|
 | Deep Vein Thrombosis | 0.00% | 0.00% | -|1.30% | 0.00% | 0.8186|
 | Renal Insufficiency | 0.16% | 0.00% | 0.9542|0.32% | 0.00% | 0.9091|
 | Pulmonary Embolism | 0.16% | 0.00% | 0.9542|0.97% | 0.00% | 0.8428|
 | Ventilator | 0.00% | 0.00% | -|3.90% | 0.00% | 0.6873|
 | Acute Renal Failure | 0.00% | 0.00% | -|0.32% | 0.00% | 0.9091|
 | CVA with Neurologic Deficit | 0.16% | 0.00% | 0.9542|0.32% | 0.00% | 0.9091|
 | Myocardial Infarction | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Sepsis | 0.16% | 0.00% | 0.9542|2.27% | 0.00% | 0.7604|
 | Readmission | 2.80% | 0.00% | 0.8103|5.52% | 0.00% | 0.6289|
 | Unplanned Readmission | 2.64% | 0.00% | 0.816|4.55% | 0.00% | 0.6626|


| | Outpatient Non-Disseminated Cancer (N = 607) | Outpatient Disseminated Cancer (N = 2) | p-value | Inpatient Non-Disseminated Cancer (N = 296) | Inpatient Disseminated Cancer (N = 16) | p-value |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
 | Superficial SSI | 0.16% | 0.00% | 0.9542|0.34% | 0.00% | 0.8159|
 | Deep SSI | 0.00% | 0.00% | -|0.34% | 0.00% | 0.8159|
 | Organ/Space SSI | 0.33% | 0.00% | 0.9352|2.36% | 0.00% | 0.5338|
 | Wound Disruption | 0.16% | 0.00% | 0.9542|0.34% | 0.00% | 0.8159|
 | Pneumonia | 0.00% | 0.00% | -|3.38% | 6.25% | 0.5441|
 | Reintubation | 0.00% | 0.00% | -|3.72% | 0.00% | 0.4324|
 | Urinary Infection | 0.16% | 0.00% | 0.9542|1.01% | 0.00% | 0.6857|
 | Deep Vein Thrombosis | 0.00% | 0.00% | -|1.35% | 0.00% | 0.6398|
 | Renal Insufficiency | 0.16% | 0.00% | 0.9542|0.34% | 0.00% | 0.8159|
 | Pulmonary Embolism | 0.16% | 0.00% | 0.9542|1.01% | 0.00% | 0.6857|
 | Ventilator | 0.00% | 0.00% | -|3.72% | 6.25% | 0.6077|
 | Acute Renal Failure | 0.00% | 0.00% | -|**0.00**% | **6.25**% | **1.647e-05**|
 | CVA with Neurologic Deficit | 0.16% | 0.00% | 0.9542|0.34% | 0.00% | 0.8159|
 | Myocardial Infarction | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Sepsis | 0.16% | 0.00% | 0.9542|2.36% | 0.00% | 0.5338|
 | Readmission | 2.80% | 0.00% | 0.8103|5.41% | 6.25% | 0.8847|
 | Unplanned Readmission | 2.64% | 0.00% | 0.816|4.39% | 6.25% | 0.7266|


| | Outpatient Non-Steroid (N = 591) | Outpatient Steroid (N = 18) | p-value | Inpatient Non-Steroid (N = 278) | Inpatient Steroid (N = 34) | p-value |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
 | Superficial SSI | 0.17% | 0.00% | 0.8613|0.36% | 0.00% | 0.7261|
 | Deep SSI | 0.00% | 0.00% | -|**0.00**% | **2.94**% | **0.004183**|
 | Organ/Space SSI | 0.34% | 0.00% | 0.8047|1.80% | 5.88% | 0.1291|
 | Wound Disruption | 0.17% | 0.00% | 0.8613|**0.00**% | **2.94**% | **0.004183**|
 | Pneumonia | 0.00% | 0.00% | -|3.60% | 2.94% | 0.8448|
 | Reintubation | 0.00% | 0.00% | -|3.24% | 5.88% | 0.4299|
 | Urinary Infection | 0.17% | 0.00% | 0.8613|0.72% | 2.94% | 0.2102|
 | Deep Vein Thrombosis | 0.00% | 0.00% | -|1.08% | 2.94% | 0.3623|
 | Renal Insufficiency | 0.17% | 0.00% | 0.8613|0.36% | 0.00% | 0.7261|
 | Pulmonary Embolism | 0.17% | 0.00% | 0.8613|**0.36**% | **5.88**% | **0.00184**|
 | Ventilator | 0.00% | 0.00% | -|3.60% | 5.88% | 0.5131|
 | Acute Renal Failure | 0.00% | 0.00% | -|**0.00**% | **2.94**% | **0.004183**|
 | CVA with Neurologic Deficit | 0.17% | 0.00% | 0.8613|0.36% | 0.00% | 0.7261|
 | Myocardial Infarction | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Sepsis | 0.17% | 0.00% | 0.8613|**1.44**% | **8.82**% | **0.006059**|
 | Readmission | 2.88% | 0.00% | 0.4655|5.76% | 2.94% | 0.495|
 | Unplanned Readmission | 2.71% | 0.00% | 0.4793|4.68% | 2.94% | 0.6446|


| | Outpatient Non-Bleeding Disorder (N = 605) | Outpatient Bleeding Disorder (N = 4) | p-value | Inpatient Non-Bleeding Disorder (N = 304) | Inpatient Bleeding Disorder (N = 8) | p-value |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
 | Superficial SSI | 0.17% | 0.00% | 0.9351|0.33% | 0.00% | 0.8709|
 | Deep SSI | 0.00% | 0.00% | -|0.33% | 0.00% | 0.8709|
 | Organ/Space SSI | 0.33% | 0.00% | 0.9083|2.30% | 0.00% | 0.6642|
 | Wound Disruption | 0.17% | 0.00% | 0.9351|0.33% | 0.00% | 0.8709|
 | Pneumonia | 0.00% | 0.00% | -|3.62% | 0.00% | 0.5838|
 | Reintubation | 0.00% | 0.00% | -|3.62% | 0.00% | 0.5838|
 | Urinary Infection | 0.17% | 0.00% | 0.9351|0.99% | 0.00% | 0.7777|
 | Deep Vein Thrombosis | 0.00% | 0.00% | -|1.32% | 0.00% | 0.744|
 | Renal Insufficiency | 0.17% | 0.00% | 0.9351|0.33% | 0.00% | 0.8709|
 | Pulmonary Embolism | 0.17% | 0.00% | 0.9351|0.99% | 0.00% | 0.7777|
 | Ventilator | 0.00% | 0.00% | -|3.62% | 12.50% | 0.1972|
 | Acute Renal Failure | 0.00% | 0.00% | -|**0.00**% | **12.50**% | **6.645e-10**|
 | CVA with Neurologic Deficit | 0.17% | 0.00% | 0.9351|0.33% | 0.00% | 0.8709|
 | Myocardial Infarction | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Sepsis | 0.17% | 0.00% | 0.9351|2.30% | 0.00% | 0.6642|
 | Readmission | 2.81% | 0.00% | 0.7338|5.59% | 0.00% | 0.4915|
 | Unplanned Readmission | 2.64% | 0.00% | 0.7417|4.61% | 0.00% | 0.5346|


| | Outpatient Non-Independent Functional Health Status (N = 9) | Outpatient Independent Functional Health Status (N = 600) | p-value | Inpatient Non-Independent Functional Health Status (N = 11) | Inpatient Independent Functional Health Status (N = 301) | p-value |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
 | Superficial SSI | 11.11% | 0.00% | **3.041e-16**|0.00% | 0.33% | 0.8482|
 | Deep SSI | 0.00% | 0.00% | -|0.00% | 0.33% | 0.8482|
 | Organ/Space SSI | 0.00% | 0.33% | 0.8623|9.09% | 1.99% | 0.1185|
 | Wound Disruption | 0.00% | 0.17% | 0.9024|**9.09**% | **0.00**% | **1.611e-07**|
 | Pneumonia | 0.00% | 0.00% | -|**18.18**% | **2.99**% | **0.007288**|
 | Reintubation | 0.00% | 0.00% | -|**18.18**% | **2.99**% | **0.007288**|
 | Urinary Infection | 0.00% | 0.17% | 0.9024|0.00% | 1.00% | 0.7393|
 | Deep Vein Thrombosis | 0.00% | 0.00% | -|**9.09**% | **1.00**% | **0.01909**|
 | Renal Insufficiency | 0.00% | 0.17% | 0.9024|0.00% | 0.33% | 0.8482|
 | Pulmonary Embolism | 0.00% | 0.17% | 0.9024|0.00% | 1.00% | 0.7393|
 | Ventilator | 0.00% | 0.00% | -|**27.27**% | **2.99**% | **3.898e-05**|
 | Acute Renal Failure | 0.00% | 0.00% | -|0.00% | 0.33% | 0.8482|
 | CVA with Neurologic Deficit | 0.00% | 0.17% | 0.9024|0.00% | 0.33% | 0.8482|
 | Myocardial Infarction | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Sepsis | 0.00% | 0.17% | 0.9024|9.09% | 1.99% | 0.1185|
 | Readmission | 11.11% | 2.67% | 0.1269|0.00% | 5.65% | 0.4176|
 | Unplanned Readmission | 0.00% | 2.67% | 0.6196|0.00% | 4.65% | 0.4642|


| | Outpatient Non-Totally or Partially Dependent Functional Health Status (N = 606) | Outpatient Totally or Partially Dependent Functional Health Status (N = 3) | p-value | Inpatient Non-Totally or Partially Dependent Functional Health Status (N = 305) | Inpatient Totally or Partially Dependent Functional Health Status (N = 7) | p-value |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
 | Superficial SSI | 0.17% | 0.00% | 0.9439|0.33% | 0.00% | 0.8794|
 | Deep SSI | 0.00% | 0.00% | -|0.33% | 0.00% | 0.8794|
 | Organ/Space SSI | 0.33% | 0.00% | 0.9206|**1.97**% | **14.29**% | **0.02956**|
 | Wound Disruption | 0.17% | 0.00% | 0.9439|**0.00**% | **14.29**% | **3.805e-11**|
 | Pneumonia | 0.00% | 0.00% | -|**2.95**% | **28.57**% | **0.0002791**|
 | Reintubation | 0.00% | 0.00% | -|**2.95**% | **28.57**% | **0.0002791**|
 | Urinary Infection | 0.17% | 0.00% | 0.9439|0.98% | 0.00% | 0.792|
 | Deep Vein Thrombosis | 0.00% | 0.00% | -|**0.98**% | **14.29**% | **0.001981**|
 | Renal Insufficiency | 0.17% | 0.00% | 0.9439|0.33% | 0.00% | 0.8794|
 | Pulmonary Embolism | 0.17% | 0.00% | 0.9439|0.98% | 0.00% | 0.792|
 | Ventilator | 0.00% | 0.00% | -|**3.28**% | **28.57**% | **0.0005807**|
 | Acute Renal Failure | 0.00% | 0.00% | -|0.33% | 0.00% | 0.8794|
 | CVA with Neurologic Deficit | 0.17% | 0.00% | 0.9439|0.33% | 0.00% | 0.8794|
 | Myocardial Infarction | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Sepsis | 0.17% | 0.00% | 0.9439|**1.97**% | **14.29**% | **0.02956**|
 | Readmission | 2.81% | 0.00% | 0.7686|5.57% | 0.00% | 0.5206|
 | Unplanned Readmission | 2.64% | 0.00% | 0.7755|4.59% | 0.00% | 0.5619|

 

 ### Notes
 I did not perform this analysis for Ventilator Dependent, Ascites, and Acute Renal Failure due to lack of patients with the conditions in both outpatient and inpatient settings. 

 ## Multivariate Logistic Regression
 Calculating the odds ratios of specific outcomes for the variable smoking.
 
 Odds Ratio calculations made by including the variables: [Smoke]:

|   | Odds ratio (data) | 95% Confidence Interval | P-Value |
| -------------  | ------------- | ------------- | ------------- | 
| Organ/Space SSI  | 5.1263 | (1.354 - 19.409) | **0.0156** |
| Pulmonary Embolism  | 193242590233598.4  | (0 - inf) | |

The odds ratio for Pulmonary Embolism is likely so high because there were only 2 patients with this outcome and both were smokers (complete quasi-separation). 

#### Controlling for significant comorbidities
Calculating the odds ratios of specific outcomes for the variable smoking.  
Odds Ratio calculations made by including the variables: [Smoke, Dyspnea, COPD, Hypertension, Ventilator Dependent]:

|   | Odds ratio (data) | 95% Confidence Interval | P-Value |
| -------------  | ------------- | ------------- | ------------- | 
| Organ/Space SSI  | 4.125 | (0.990 - 17.202) | 0.0513 |
| Pulmonary Embolism  | 80.627 | (0.077 - 84254.00) | 0.2178 |

#### Inpatient vs Outpatient
From the expanded table 4, there was a significant difference in proportions of patients in the inpatient setting that smoked and had Organ/Space SSI complications following ESS and patients in the inpatient setting that *did not smoke* and had Organ/Space SSI complications following ESS. There was also a significant difference in proportions of patients in the outpatient setting that smoked and had Pulmonary Embolism complications following ESS and patients in the outpatient setting that *did not smoke* and had Pulmonary Embolism complications following ESS. However, since there was only one patient in the outpatient setting that reported smoking <1 year prior to surgery, the odds ratio and confidence intervals were not calculated for this result.

The following tables calculate the odds ratios of these outcomes for patients in either the inpatient or outpatient setting for the variable smoking. 
Odds Ratio calculations made by including the variables: [Smoke, Dyspnea, COPD, Hypertension, Ventilator Dependent]:

##### Multivariate Logistic Regression for Patients in Inpatient Setting who Reported Smoking <1 Year Prior to Surgery

|   | Odds ratio (data) | 95% Confidence Interval | P-Value |
| -------------  | ------------- | ------------- | ------------- | 
| Organ/Space SSI  | 2.082 | (0.3792 - 11.43) | 0.406 |



 








