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


| | Non-Smoke (N = 451.0) | Smoke (N = 114.0) | p-value | 
| ------------- | ------------- | ------------- | ------------- |
 | Diabetes | 12.2% | 12.28% | 0.9801 | 
 | Dyspnea | 2.661% | 9.649% | **0.0007423** | 
 | Ventilator Dependent | 0% | 0.8772% | **0.04651** | 
 | COPD | 2.882% | 7.018% | **0.03706** | 
 | Hypertension | 31.04% | 50.0% | **0.0001477** | 
 | Disseminated Cancer | 2.661% | 1.754% | 0.5781 | 
 | Steroid | 6.43% | 3.509% | 0.2347 | 
 | Bleeding Disorder | 1.996% | 0% | 0.1284 | 
 | Independent Functional Health Status | 97.78% | 97.37% | 0.7921 | 
 | Totally or Partially Dependent Functional Health Status | 0.8869% | 1.754% | 0.4195 | 


| | Non-Hypertension (N = 368.0) | Hypertension (N = 197.0) | p-value | 
| ------------- | ------------- | ------------- | ------------- |
 | Diabetes | 4.348% | 26.9% | **6.036e-15** | 
 | Smoke | 15.49% | 28.93% | **0.0001477** | 
 | Dyspnea | 2.174% | 7.614% | **0.001818** | 
 | Ventilator Dependent | 0% | 0.5076% | 0.1713 | 
 | COPD | 1.359% | 8.122% | **5.129e-05** | 
 | Disseminated Cancer | 2.717% | 2.03% | 0.6167 | 
 | Steroid | 5.163% | 7.107% | 0.3478 | 
 | Bleeding Disorder | 1.359% | 2.03% | 0.5433 | 
 | Independent Functional Health Status | 97.83% | 97.46% | 0.7832 | 
 | Totally or Partially Dependent Functional Health Status | 0.5435% | 2.03% | 0.1003 | 


| | Non-Dyspnea (N = 542.0) | Dyspnea (N = 23.0) | p-value | 
| ------------- | ------------- | ------------- | ------------- |
 | Diabetes | 11.81% | 21.74% | 0.1543 | 
 | Smoke | 19.0% | 47.83% | **0.0007423** | 
 | Ventilator Dependent | 0.1845% | 0% | 0.8366 | 
 | COPD | 2.583% | 30.43% | **4.658e-12** | 
 | Hypertension | 33.58% | 65.22% | **0.001818** | 
 | Disseminated Cancer | 2.214% | 8.696% | 0.05017 | 
 | Steroid | 5.72% | 8.696% | 0.5511 | 
 | Bleeding Disorder | 1.292% | 8.696% | **0.005473** | 
 | Independent Functional Health Status | 97.6% | 100.0% | 0.4524 | 
 | Totally or Partially Dependent Functional Health Status | 1.107% | 0% | 0.6119 | 


| | Non-COPD (N = 544.0) | COPD (N = 21.0) | p-value | 
| ------------- | ------------- | ------------- | ------------- |
 | Diabetes | 11.4% | 33.33% | **0.002591** | 
 | Smoke | 19.49% | 38.1% | **0.03706** | 
 | Dyspnea | 2.941% | 33.33% | **4.658e-12** | 
 | Ventilator Dependent | 0.1838% | 0% | 0.8441 | 
 | Hypertension | 33.27% | 76.19% | **5.129e-05** | 
 | Disseminated Cancer | 2.39% | 4.762% | 0.4926 | 
 | Steroid | 5.515% | 14.29% | 0.09261 | 
 | Bleeding Disorder | 1.287% | 9.524% | **0.003093** | 
 | Independent Functional Health Status | 97.79% | 95.24% | 0.4433 | 
 | Totally or Partially Dependent Functional Health Status | 1.103% | 0% | 0.6285 | 


| | Non-CGF (N = 562.0) | CGF (N = 3.0) | p-value | 
| ------------- | ------------- | ------------- | ------------- |
 | Diabetes | 12.1% | 33.33% | 0.2626 | 
 | Smoke | 20.11% | 33.33% | 0.5691 | 
 | Dyspnea | 4.093% | 0% | 0.7205 | 
 | Ventilator Dependent | 0.1779% | 0% | 0.9417 | 
 | COPD | 3.381% | 66.67% | **7.516e-09** | 
 | Hypertension | 34.52% | 100.0% | **0.01762** | 
 | Disseminated Cancer | 2.491% | 0% | 0.7819 | 
 | Steroid | 5.872% | 0% | 0.6654 | 
 | Bleeding Disorder | 1.601% | 0% | 0.8251 | 
 | Independent Functional Health Status | 97.86% | 66.67% | **0.000325** | 
 | Totally or Partially Dependent Functional Health Status | 0.8897% | 33.33% | **4.56e-08** | 


| | Non-Disseminated Cancer (N = 551.0) | Disseminated Cancer (N = 14.0) | p-value | 
| ------------- | ------------- | ------------- | ------------- |
 | Diabetes | 12.34% | 7.143% | 0.5575 | 
 | Smoke | 20.33% | 14.29% | 0.5781 | 
 | Dyspnea | 3.811% | 14.29% | 0.05017 | 
 | Ventilator Dependent | 0.1815% | 0% | 0.8732 | 
 | COPD | 3.63% | 7.143% | 0.4926 | 
 | Hypertension | 35.03% | 28.57% | 0.6167 | 
 | Steroid | 5.445% | 21.43% | **0.01179** | 
 | Bleeding Disorder | 1.089% | 21.43% | **1.94e-09** | 
 | Independent Functional Health Status | 97.64% | 100.0% | 0.5609 | 
 | Totally or Partially Dependent Functional Health Status | 1.089% | 0% | 0.6947 | 


| | Non-Steroid (N = 532.0) | Steroid (N = 33.0) | p-value | 
| ------------- | ------------- | ------------- | ------------- |
 | Diabetes | 12.59% | 6.061% | 0.266 | 
 | Smoke | 20.68% | 12.12% | 0.2347 | 
 | Dyspnea | 3.947% | 6.061% | 0.5511 | 
 | Ventilator Dependent | 0.188% | 0% | 0.8031 | 
 | COPD | 3.383% | 9.091% | 0.09261 | 
 | Hypertension | 34.4% | 42.42% | 0.3478 | 
 | Disseminated Cancer | 2.068% | 9.091% | **0.01179** | 
 | Bleeding Disorder | 1.128% | 9.091% | **0.0003921** | 
 | Independent Functional Health Status | 97.74% | 96.97% | 0.7733 | 
 | Totally or Partially Dependent Functional Health Status | 0.9398% | 3.03% | 0.2556 | 


| | Non-Bleeding Disorder (N = 556.0) | Bleeding Disorder (N = 9.0) | p-value | 
| ------------- | ------------- | ------------- | ------------- |
 | Diabetes | 12.05% | 22.22% | 0.3552 | 
 | Smoke | 20.5% | 0% | 0.1284 | 
 | Dyspnea | 3.777% | 22.22% | **0.005473** | 
 | Ventilator Dependent | 0.1799% | 0% | 0.8987 | 
 | COPD | 3.417% | 22.22% | **0.003093** | 
 | Hypertension | 34.71% | 44.44% | 0.5433 | 
 | Disseminated Cancer | 1.978% | 33.33% | **1.94e-09** | 
 | Steroid | 5.396% | 33.33% | **0.0003921** | 
 | Independent Functional Health Status | 97.84% | 88.89% | 0.07556 | 
 | Totally or Partially Dependent Functional Health Status | 1.079% | 0% | 0.754 | 


| | Non-Independent Functional Health Status (N = 13.0) | Independent Functional Health Status (N = 552.0) | p-value | 
| ------------- | ------------- | ------------- | ------------- |
 | Diabetes | 38.46% | 11.59% | **0.003452** | 
 | Smoke | 23.08% | 20.11% | 0.7921 | 
 | Dyspnea | 0% | 4.167% | 0.4524 | 
 | Ventilator Dependent | 0% | 0.1812% | 0.8779 | 
 | COPD | 7.692% | 3.623% | 0.4433 | 
 | Hypertension | 38.46% | 34.78% | 0.7832 | 
 | Disseminated Cancer | 0% | 2.536% | 0.5609 | 
 | Steroid | 7.692% | 5.797% | 0.7733 | 
 | Bleeding Disorder | 7.692% | 1.449% | 0.07556 | 
 | Totally or Partially Dependent Functional Health Status | 46.15% | 0% | **6.007e-58** | 


| | Non-Totally or Partially Dependent Functional Health Status (N = 559.0) | Totally or Partially Dependent Functional Health Status (N = 6.0) | p-value | 
| ------------- | ------------- | ------------- | ------------- |
 | Diabetes | 11.81% | 50.0% | **0.004483** | 
 | Smoke | 20.04% | 33.33% | 0.4195 | 
 | Dyspnea | 4.114% | 0% | 0.6119 | 
 | Ventilator Dependent | 0.1789% | 0% | 0.9174 | 
 | COPD | 3.757% | 0% | 0.6285 | 
 | Hypertension | 34.53% | 66.67% | 0.1003 | 
 | Disseminated Cancer | 2.504% | 0% | 0.6947 | 
 | Steroid | 5.725% | 16.67% | 0.2556 | 
 | Bleeding Disorder | 1.61% | 0% | 0.754 | 
 
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
 | Ventilator | 0.6048% | 2.899% | 0.05664 | 
 | Acute Renal Failure | 0.2016% | 0% | 0.7089 | 
 | CVA with Neurologic Deficit | 0% | 0% | - | 
 | Myocardial Infarction | 0% | 0% | - | 
 | Sepsis | 1.008% | 0% | 0.4022 | 
 | Readmission | 4.234% | 5.797% | 0.5541 | 
 | Unplanned Readmission | 3.831% | 5.797% | 0.4386 | 


| | Non-Smoke (N = 451.0) | Smoke (N = 114.0) | p-value | 
| ------------- | ------------- | ------------- | ------------- |
 | Superficial SSI | 0.2217% | 0% | 0.6148 | 
 | Deep SSI | 0% | 0% | - | 
 | Organ/Space SSI | 0.8869% | 4.386% | **0.007677** | 
 | Wound Disruption | 0% | 0% | - | 
 | Pneumonia | 1.552% | 0.8772% | 0.5858 | 
 | Reintubation | 0.8869% | 0.8772% | 0.9921 | 
 | Urinary Infection | 0.2217% | 0% | 0.6148 | 
 | Deep Vein Thrombosis | 0.2217% | 0.8772% | 0.2924 | 
 | Renal Insufficiency | 0.2217% | 0% | 0.6148 | 
 | Pulmonary Embolism | 0% | 1.754% | **0.004834** | 
 | Ventilator | 0.6652% | 1.754% | 0.2673 | 
 | Acute Renal Failure | 0.2217% | 0% | 0.6148 | 
 | CVA with Neurologic Deficit | 0% | 0% | - | 
 | Myocardial Infarction | 0% | 0% | - | 
 | Sepsis | 0.6652% | 1.754% | 0.2673 | 
 | Readmission | 3.769% | 7.018% | 0.1319 | 
 | Unplanned Readmission | 3.548% | 6.14% | 0.2107 | 


| | Non-Hypertension (N = 368.0) | Hypertension (N = 197.0) | p-value | 
| ------------- | ------------- | ------------- | ------------- |
 | Superficial SSI | 0% | 0.5076% | 0.1713 | 
 | Deep SSI | 0% | 0% | - | 
 | Organ/Space SSI | 1.087% | 2.538% | 0.1892 | 
 | Wound Disruption | 0% | 0% | - | 
 | Pneumonia | 0.8152% | 2.538% | 0.09858 | 
 | Reintubation | 0.5435% | 1.523% | 0.2362 | 
 | Urinary Infection | 0.2717% | 0% | 0.464 | 
 | Deep Vein Thrombosis | 0.2717% | 0.5076% | 0.6528 | 
 | Renal Insufficiency | 0% | 0.5076% | 0.1713 | 
 | Pulmonary Embolism | 0.2717% | 0.5076% | 0.6528 | 
 | Ventilator | 1.087% | 0.5076% | 0.4835 | 
 | Acute Renal Failure | 0% | 0.5076% | 0.1713 | 
 | CVA with Neurologic Deficit | 0% | 0% | - | 
 | Myocardial Infarction | 0% | 0% | - | 
 | Sepsis | 0.2717% | 2.03% | **0.03341** | 
 | Readmission | 2.717% | 7.614% | **0.006991** | 
 | Unplanned Readmission | 2.717% | 6.599% | **0.02608** | 


| | Non-Dyspnea (N = 542.0) | Dyspnea (N = 23.0) | p-value | 
| ------------- | ------------- | ------------- | ------------- |
 | Superficial SSI | 0.1845% | 0% | 0.8366 | 
 | Deep SSI | 0% | 0% | - | 
 | Organ/Space SSI | 1.661% | 0% | 0.5333 | 
 | Wound Disruption | 0% | 0% | - | 
 | Pneumonia | 1.476% | 0% | 0.5573 | 
 | Reintubation | 0.9225% | 0% | 0.6436 | 
 | Urinary Infection | 0.1845% | 0% | 0.8366 | 
 | Deep Vein Thrombosis | 0.369% | 0% | 0.7704 | 
 | Renal Insufficiency | 0.1845% | 0% | 0.8366 | 
 | Pulmonary Embolism | 0.369% | 0% | 0.7704 | 
 | Ventilator | 0.9225% | 0% | 0.6436 | 
 | Acute Renal Failure | 0% | 4.348% | **1.182e-06** | 
 | CVA with Neurologic Deficit | 0% | 0% | - | 
 | Myocardial Infarction | 0% | 0% | - | 
 | Sepsis | 0.9225% | 0% | 0.6436 | 
 | Readmission | 4.428% | 4.348% | 0.9854 | 
 | Unplanned Readmission | 4.059% | 4.348% | 0.9453 | 


| | Non-COPD (N = 544.0) | COPD (N = 21.0) | p-value | 
| ------------- | ------------- | ------------- | ------------- |
 | Superficial SSI | 0.1838% | 0% | 0.8441 | 
 | Deep SSI | 0% | 0% | - | 
 | Organ/Space SSI | 1.471% | 4.762% | 0.2372 | 
 | Wound Disruption | 0% | 0% | - | 
 | Pneumonia | 1.287% | 4.762% | 0.186 | 
 | Reintubation | 0.7353% | 4.762% | 0.0532 | 
 | Urinary Infection | 0.1838% | 0% | 0.8441 | 
 | Deep Vein Thrombosis | 0.1838% | 4.762% | **0.000528** | 
 | Renal Insufficiency | 0% | 4.762% | **3.502e-07** | 
 | Pulmonary Embolism | 0.3676% | 0% | 0.7807 | 
 | Ventilator | 0.7353% | 4.762% | 0.0532 | 
 | Acute Renal Failure | 0% | 4.762% | **3.502e-07** | 
 | CVA with Neurologic Deficit | 0% | 0% | - | 
 | Myocardial Infarction | 0% | 0% | - | 
 | Sepsis | 0.5515% | 9.524% | **1.649e-05** | 
 | Readmission | 4.044% | 14.29% | **0.02513** | 
 | Unplanned Readmission | 3.676% | 14.29% | **0.01577** | 


| | Non-CGF (N = 562.0) | CGF (N = 3.0) | p-value | 
| ------------- | ------------- | ------------- | ------------- |
 | Superficial SSI | 0.1779% | 0% | 0.9417 | 
 | Deep SSI | 0% | 0% | - | 
 | Organ/Space SSI | 1.601% | 0% | 0.8251 | 
 | Wound Disruption | 0% | 0% | - | 
 | Pneumonia | 1.246% | 33.33% | **2.711e-06** | 
 | Reintubation | 0.7117% | 33.33% | **1.777e-09** | 
 | Urinary Infection | 0.1779% | 0% | 0.9417 | 
 | Deep Vein Thrombosis | 0.3559% | 0% | 0.9176 | 
 | Renal Insufficiency | 0.1779% | 0% | 0.9417 | 
 | Pulmonary Embolism | 0.3559% | 0% | 0.9176 | 
 | Ventilator | 0.8897% | 0% | 0.8697 | 
 | Acute Renal Failure | 0.1779% | 0% | 0.9417 | 
 | CVA with Neurologic Deficit | 0% | 0% | - | 
 | Myocardial Infarction | 0% | 0% | - | 
 | Sepsis | 0.8897% | 0% | 0.8697 | 
 | Readmission | 4.448% | 0% | 0.7086 | 
 | Unplanned Readmission | 4.093% | 0% | 0.7205 | 


| | Non-Disseminated Cancer (N = 551.0) | Disseminated Cancer (N = 14.0) | p-value | 
| ------------- | ------------- | ------------- | ------------- |
 | Superficial SSI | 0.1815% | 0% | 0.8732 | 
 | Deep SSI | 0% | 0% | - | 
 | Organ/Space SSI | 1.633% | 0% | 0.6298 | 
 | Wound Disruption | 0% | 0% | - | 
 | Pneumonia | 1.27% | 7.143% | 0.06627 | 
 | Reintubation | 0.9074% | 0% | 0.7203 | 
 | Urinary Infection | 0.1815% | 0% | 0.8732 | 
 | Deep Vein Thrombosis | 0.363% | 0% | 0.8213 | 
 | Renal Insufficiency | 0.1815% | 0% | 0.8732 | 
 | Pulmonary Embolism | 0.363% | 0% | 0.8213 | 
 | Ventilator | 0.726% | 7.143% | **0.01135** | 
 | Acute Renal Failure | 0% | 7.143% | **3.406e-10** | 
 | CVA with Neurologic Deficit | 0% | 0% | - | 
 | Myocardial Infarction | 0% | 0% | - | 
 | Sepsis | 0.9074% | 0% | 0.7203 | 
 | Readmission | 4.356% | 7.143% | 0.6165 | 
 | Unplanned Readmission | 3.993% | 7.143% | 0.5559 | 


| | Non-Steroid (N = 532.0) | Steroid (N = 33.0) | p-value | 
| ------------- | ------------- | ------------- | ------------- |
 | Superficial SSI | 0.188% | 0% | 0.8031 | 
 | Deep SSI | 0% | 0% | - | 
 | Organ/Space SSI | 1.316% | 6.061% | **0.03464** | 
 | Wound Disruption | 0% | 0% | - | 
 | Pneumonia | 1.316% | 3.03% | 0.4186 | 
 | Reintubation | 0.7519% | 3.03% | 0.1751 | 
 | Urinary Infection | 0.188% | 0% | 0.8031 | 
 | Deep Vein Thrombosis | 0.3759% | 0% | 0.7242 | 
 | Renal Insufficiency | 0.188% | 0% | 0.8031 | 
 | Pulmonary Embolism | 0.188% | 3.03% | **0.007636** | 
 | Ventilator | 0.5639% | 6.061% | **0.001069** | 
 | Acute Renal Failure | 0% | 3.03% | **5.852e-05** | 
 | CVA with Neurologic Deficit | 0% | 0% | - | 
 | Myocardial Infarction | 0% | 0% | - | 
 | Sepsis | 0.5639% | 6.061% | **0.001069** | 
 | Readmission | 4.699% | 0% | 0.2027 | 
 | Unplanned Readmission | 4.323% | 0% | 0.2226 | 


| | Non-Bleeding Disorder (N = 556.0) | Bleeding Disorder (N = 9.0) | p-value | 
| ------------- | ------------- | ------------- | ------------- |
 | Superficial SSI | 0.1799% | 0% | 0.8987 | 
 | Deep SSI | 0% | 0% | - | 
 | Organ/Space SSI | 1.619% | 0% | 0.7004 | 
 | Wound Disruption | 0% | 0% | - | 
 | Pneumonia | 1.439% | 0% | 0.717 | 
 | Reintubation | 0.8993% | 0% | 0.7751 | 
 | Urinary Infection | 0.1799% | 0% | 0.8987 | 
 | Deep Vein Thrombosis | 0.3597% | 0% | 0.857 | 
 | Renal Insufficiency | 0.1799% | 0% | 0.8987 | 
 | Pulmonary Embolism | 0.3597% | 0% | 0.857 | 
 | Ventilator | 0.7194% | 11.11% | **0.0009596** | 
 | Acute Renal Failure | 0% | 11.11% | **3.637e-15** | 
 | CVA with Neurologic Deficit | 0% | 0% | - | 
 | Myocardial Infarction | 0% | 0% | - | 
 | Sepsis | 0.8993% | 0% | 0.7751 | 
 | Readmission | 4.496% | 0% | 0.5152 | 
 | Unplanned Readmission | 4.137% | 0% | 0.5333 | 


| | Non-Independent Functional Health Status (N = 13.0) | Independent Functional Health Status (N = 552.0) | p-value | 
| ------------- | ------------- | ------------- | ------------- |
 | Superficial SSI | 0% | 0.1812% | 0.8779 | 
 | Deep SSI | 0% | 0% | - | 
 | Organ/Space SSI | 7.692% | 1.449% | 0.07556 | 
 | Wound Disruption | 0% | 0% | - | 
 | Pneumonia | 15.38% | 1.087% | **1.612e-05** | 
 | Reintubation | 15.38% | 0.5435% | **1.628e-08** | 
 | Urinary Infection | 0% | 0.1812% | 0.8779 | 
 | Deep Vein Thrombosis | 7.692% | 0.1812% | **6.57e-06** | 
 | Renal Insufficiency | 0% | 0.1812% | 0.8779 | 
 | Pulmonary Embolism | 0% | 0.3623% | 0.8279 | 
 | Ventilator | 15.38% | 0.5435% | **1.628e-08** | 
 | Acute Renal Failure | 0% | 0.1812% | 0.8779 | 
 | CVA with Neurologic Deficit | 0% | 0% | - | 
 | Myocardial Infarction | 0% | 0% | - | 
 | Sepsis | 0% | 0.9058% | 0.7303 | 
 | Readmission | 0% | 4.529% | 0.4325 | 
 | Unplanned Readmission | 0% | 4.167% | 0.4524 | 


| | Non-Totally or Partially Dependent Functional Health Status (N = 559.0) | Totally or Partially Dependent Functional Health Status (N = 6.0) | p-value | 
| ------------- | ------------- | ------------- | ------------- |
 | Superficial SSI | 0.1789% | 0% | 0.9174 | 
 | Deep SSI | 0% | 0% | - | 
 | Organ/Space SSI | 1.431% | 16.67% | **0.003028** | 
 | Wound Disruption | 0% | 0% | - | 
 | Pneumonia | 1.252% | 16.67% | **0.001479** | 
 | Reintubation | 0.7156% | 16.67% | **3.329e-05** | 
 | Urinary Infection | 0.1789% | 0% | 0.9174 | 
 | Deep Vein Thrombosis | 0.3578% | 0% | 0.8833 | 
 | Renal Insufficiency | 0.1789% | 0% | 0.9174 | 
 | Pulmonary Embolism | 0.3578% | 0% | 0.8833 | 
 | Ventilator | 0.7156% | 16.67% | **3.329e-05** | 
 | Acute Renal Failure | 0.1789% | 0% | 0.9174 | 
 | CVA with Neurologic Deficit | 0% | 0% | - | 
 | Myocardial Infarction | 0% | 0% | - | 
 | Sepsis | 0.8945% | 0% | 0.816 | 
 | Readmission | 4.472% | 0% | 0.5962 | 
 | Unplanned Readmission | 4.114% | 0% | 0.6119 | 
 
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
 | Ventilator | 0.00% | 0.00% | -|1.78% | 5.13% | 0.2178|
 | Acute Renal Failure | 0.00% | 0.00% | -|0.59% | 0.00% | 0.6301|
 | CVA with Neurologic Deficit | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Myocardial Infarction | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Sepsis | 0.31% | 0.00% | 0.7616|2.37% | 0.00% | 0.332|
 | Readmission | 3.67% | 3.33% | 0.925|5.33% | 7.69% | 0.5677|
 | Unplanned Readmission | 3.67% | 3.33% | 0.925|4.14% | 7.69% | 0.3502|


| | Outpatient Non-Smoke (N = 289) | Outpatient Smoke (N = 68) | p-value | Inpatient Non-Smoke (N = 162) | Inpatient Smoke (N = 46) | p-value |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
 | Superficial SSI | 0.00% | 0.00% | -|0.62% | 0.00% | 0.5932|
 | Deep SSI | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Organ/Space SSI | 0.69% | 0.00% | 0.4915|**1.23**% | **10.87**% | **0.001384**|
 | Wound Disruption | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Pneumonia | 0.00% | 0.00% | -|4.32% | 2.17% | 0.504|
 | Reintubation | 0.00% | 0.00% | -|2.47% | 2.17% | 0.9082|
 | Urinary Infection | 0.00% | 0.00% | -|0.62% | 0.00% | 0.5932|
 | Deep Vein Thrombosis | 0.00% | 0.00% | -|0.62% | 2.17% | 0.3397|
 | Renal Insufficiency | 0.35% | 0.00% | 0.6271|0.00% | 0.00% | -|
 | Pulmonary Embolism | 0.00% | 1.47% | **0.03898**|0.00% | 2.17% | 0.05995|
 | Ventilator | 0.00% | 0.00% | -|1.85% | 4.35% | 0.3294|
 | Acute Renal Failure | 0.00% | 0.00% | -|0.62% | 0.00% | 0.5932|
 | CVA with Neurologic Deficit | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Myocardial Infarction | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Sepsis | 0.35% | 0.00% | 0.6271|1.23% | 4.35% | 0.1748|
 | Readmission | 3.11% | 5.88% | 0.2729|4.94% | 8.70% | 0.3348|
 | Unplanned Readmission | 3.11% | 5.88% | 0.2729|4.32% | 6.52% | 0.5381|


| | Outpatient Non-Hypertension (N = 256) | Outpatient Hypertension (N = 101) | p-value | Inpatient Non-Hypertension (N = 112) | Inpatient Hypertension (N = 96) | p-value |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
 | Superficial SSI | 0.00% | 0.00% | -|0.00% | 1.04% | 0.2789|
 | Deep SSI | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Organ/Space SSI | 0.39% | 0.99% | 0.4943|2.68% | 4.17% | 0.553|
 | Wound Disruption | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Pneumonia | 0.00% | 0.00% | -|2.68% | 5.21% | 0.3443|
 | Reintubation | 0.00% | 0.00% | -|1.79% | 3.12% | 0.5296|
 | Urinary Infection | 0.00% | 0.00% | -|0.89% | 0.00% | 0.3534|
 | Deep Vein Thrombosis | 0.00% | 0.00% | -|0.89% | 1.04% | 0.9127|
 | Renal Insufficiency | 0.00% | 0.99% | 0.1109|0.00% | 0.00% | -|
 | Pulmonary Embolism | 0.39% | 0.00% | 0.5293|0.00% | 1.04% | 0.2789|
 | Ventilator | 0.00% | 0.00% | -|3.57% | 1.04% | 0.235|
 | Acute Renal Failure | 0.00% | 0.00% | -|0.00% | 1.04% | 0.2789|
 | CVA with Neurologic Deficit | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Myocardial Infarction | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Sepsis | 0.00% | 0.99% | 0.1109|0.89% | 3.12% | 0.2426|
 | Readmission | 3.12% | 4.95% | 0.4069|**1.79**% | **10.42**% | **0.007781**|
 | Unplanned Readmission | 3.12% | 4.95% | 0.4069|**1.79**% | **8.33**% | **0.02777**|


| | Outpatient Non-Dyspnea (N = 345) | Outpatient Dyspnea (N = 12) | p-value | Inpatient Non-Dyspnea (N = 197) | Inpatient Dyspnea (N = 11) | p-value |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
 | Superficial SSI | 0.00% | 0.00% | -|0.51% | 0.00% | 0.8128|
 | Deep SSI | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Organ/Space SSI | 0.58% | 0.00% | 0.7914|3.55% | 0.00% | 0.5248|
 | Wound Disruption | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Pneumonia | 0.00% | 0.00% | -|4.06% | 0.00% | 0.4955|
 | Reintubation | 0.00% | 0.00% | -|2.54% | 0.00% | 0.5928|
 | Urinary Infection | 0.00% | 0.00% | -|0.51% | 0.00% | 0.8128|
 | Deep Vein Thrombosis | 0.00% | 0.00% | -|1.02% | 0.00% | 0.737|
 | Renal Insufficiency | 0.29% | 0.00% | 0.8518|0.00% | 0.00% | -|
 | Pulmonary Embolism | 0.29% | 0.00% | 0.8518|0.51% | 0.00% | 0.8128|
 | Ventilator | 0.00% | 0.00% | -|2.54% | 0.00% | 0.5928|
 | Acute Renal Failure | 0.00% | 0.00% | -|**0.00**% | **9.09**% | **2.214e-05**|
 | CVA with Neurologic Deficit | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Myocardial Infarction | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Sepsis | 0.29% | 0.00% | 0.8518|2.03% | 0.00% | 0.6332|
 | Readmission | 3.77% | 0.00% | 0.4933|5.58% | 9.09% | 0.6273|
 | Unplanned Readmission | 3.77% | 0.00% | 0.4933|4.57% | 9.09% | 0.495|


| | Outpatient Non-COPD (N = 348) | Outpatient COPD (N = 9) | p-value | Inpatient Non-COPD (N = 196) | Inpatient COPD (N = 12) | p-value |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
 | Superficial SSI | 0.00% | 0.00% | -|0.51% | 0.00% | 0.8041|
 | Deep SSI | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Organ/Space SSI | 0.29% | 11.11% | **1.745e-05**|3.57% | 0.00% | 0.5054|
 | Wound Disruption | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Pneumonia | 0.00% | 0.00% | -|3.57% | 8.33% | 0.405|
 | Reintubation | 0.00% | 0.00% | -|2.04% | 8.33% | 0.1671|
 | Urinary Infection | 0.00% | 0.00% | -|0.51% | 0.00% | 0.8041|
 | Deep Vein Thrombosis | 0.00% | 0.00% | -|**0.51**% | **8.33**% | **0.007023**|
 | Renal Insufficiency | 0.00% | 11.11% | **4.755e-10**|0.00% | 0.00% | -|
 | Pulmonary Embolism | 0.29% | 0.00% | 0.8721|0.51% | 0.00% | 0.8041|
 | Ventilator | 0.00% | 0.00% | -|2.04% | 8.33% | 0.1671|
 | Acute Renal Failure | 0.00% | 0.00% | -|**0.00**% | **8.33**% | **5.096e-05**|
 | CVA with Neurologic Deficit | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Myocardial Infarction | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Sepsis | 0.00% | 11.11% | **4.755e-10**|1.53% | 8.33% | 0.09578|
 | Readmission | 3.45% | 11.11% | 0.2256|5.10% | 16.67% | 0.09534|
 | Unplanned Readmission | 3.45% | 11.11% | 0.2256|**4.08**% | **16.67**% | **0.04791**|


| | Outpatient Non-CGF (N = 355) | Outpatient CGF (N = 2) | p-value | Inpatient Non-CGF (N = 207) | Inpatient CGF (N = 1) | p-value |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
 | Superficial SSI | 0.00% | 0.00% | -|0.48% | 0.00% | 0.9445|
 | Deep SSI | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Organ/Space SSI | 0.56% | 0.00% | 0.9152|3.38% | 0.00% | 0.8516|
 | Wound Disruption | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Pneumonia | 0.00% | 0.00% | -|**3.38**% | **100.00**% | **5.385e-07**|
 | Reintubation | 0.00% | 0.00% | -|**1.93**% | **100.00**% | **1.69e-10**|
 | Urinary Infection | 0.00% | 0.00% | -|0.48% | 0.00% | 0.9445|
 | Deep Vein Thrombosis | 0.00% | 0.00% | -|0.97% | 0.00% | 0.9213|
 | Renal Insufficiency | 0.28% | 0.00% | 0.9401|0.00% | 0.00% | -|
 | Pulmonary Embolism | 0.28% | 0.00% | 0.9401|0.48% | 0.00% | 0.9445|
 | Ventilator | 0.00% | 0.00% | -|2.42% | 0.00% | 0.875|
 | Acute Renal Failure | 0.00% | 0.00% | -|0.48% | 0.00% | 0.9445|
 | CVA with Neurologic Deficit | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Myocardial Infarction | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Sepsis | 0.28% | 0.00% | 0.9401|1.93% | 0.00% | 0.8884|
 | Readmission | 3.66% | 0.00% | 0.7828|5.80% | 0.00% | 0.8041|
 | Unplanned Readmission | 3.66% | 0.00% | 0.7828|4.83% | 0.00% | 0.8218|


| | Outpatient Non-Disseminated Cancer (N = 356) | Outpatient Disseminated Cancer (N = 1) | p-value | Inpatient Non-Disseminated Cancer (N = 195) | Inpatient Disseminated Cancer (N = 13) | p-value |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
 | Superficial SSI | 0.00% | 0.00% | -|0.51% | 0.00% | 0.7958|
 | Deep SSI | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Organ/Space SSI | 0.56% | 0.00% | 0.9401|3.59% | 0.00% | 0.4871|
 | Wound Disruption | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Pneumonia | 0.00% | 0.00% | -|3.59% | 7.69% | 0.4564|
 | Reintubation | 0.00% | 0.00% | -|2.56% | 0.00% | 0.5589|
 | Urinary Infection | 0.00% | 0.00% | -|0.51% | 0.00% | 0.7958|
 | Deep Vein Thrombosis | 0.00% | 0.00% | -|1.03% | 0.00% | 0.7137|
 | Renal Insufficiency | 0.28% | 0.00% | 0.9577|0.00% | 0.00% | -|
 | Pulmonary Embolism | 0.28% | 0.00% | 0.9577|0.51% | 0.00% | 0.7958|
 | Ventilator | 0.00% | 0.00% | -|2.05% | 7.69% | 0.1985|
 | Acute Renal Failure | 0.00% | 0.00% | -|**0.00**% | **7.69**% | **0.0001035**|
 | CVA with Neurologic Deficit | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Myocardial Infarction | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Sepsis | 0.28% | 0.00% | 0.9577|2.05% | 0.00% | 0.6021|
 | Readmission | 3.65% | 0.00% | 0.8457|5.64% | 7.69% | 0.7587|
 | Unplanned Readmission | 3.65% | 0.00% | 0.8457|4.62% | 7.69% | 0.6156|


| | Outpatient Non-Steroid (N = 345) | Outpatient Steroid (N = 12) | p-value | Inpatient Non-Steroid (N = 187) | Inpatient Steroid (N = 21) | p-value |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
 | Superficial SSI | 0.00% | 0.00% | -|0.53% | 0.00% | 0.7369|
 | Deep SSI | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Organ/Space SSI | 0.58% | 0.00% | 0.7914|2.67% | 9.52% | 0.09885|
 | Wound Disruption | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Pneumonia | 0.00% | 0.00% | -|3.74% | 4.76% | 0.818|
 | Reintubation | 0.00% | 0.00% | -|2.14% | 4.76% | 0.4568|
 | Urinary Infection | 0.00% | 0.00% | -|0.53% | 0.00% | 0.7369|
 | Deep Vein Thrombosis | 0.00% | 0.00% | -|1.07% | 0.00% | 0.6339|
 | Renal Insufficiency | 0.29% | 0.00% | 0.8518|0.00% | 0.00% | -|
 | Pulmonary Embolism | 0.29% | 0.00% | 0.8518|**0.00**% | **4.76**% | **0.002778**|
 | Ventilator | 0.00% | 0.00% | -|**1.60**% | **9.52**% | **0.02466**|
 | Acute Renal Failure | 0.00% | 0.00% | -|**0.00**% | **4.76**% | **0.002778**|
 | CVA with Neurologic Deficit | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Myocardial Infarction | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Sepsis | 0.29% | 0.00% | 0.8518|**1.07**% | **9.52**% | **0.007477**|
 | Readmission | 3.77% | 0.00% | 0.4933|6.42% | 0.00% | 0.2317|
 | Unplanned Readmission | 3.77% | 0.00% | 0.4933|5.35% | 0.00% | 0.2774|


| | Outpatient Non-Bleeding Disorder (N = 354) | Outpatient Bleeding Disorder (N = 3) | p-value | Inpatient Non-Bleeding Disorder (N = 202) | Inpatient Bleeding Disorder (N = 6) | p-value |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
 | Superficial SSI | 0.00% | 0.00% | -|0.50% | 0.00% | 0.8628|
 | Deep SSI | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Organ/Space SSI | 0.56% | 0.00% | 0.8961|3.47% | 0.00% | 0.6428|
 | Wound Disruption | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Pneumonia | 0.00% | 0.00% | -|3.96% | 0.00% | 0.6191|
 | Reintubation | 0.00% | 0.00% | -|2.48% | 0.00% | 0.6965|
 | Urinary Infection | 0.00% | 0.00% | -|0.50% | 0.00% | 0.8628|
 | Deep Vein Thrombosis | 0.00% | 0.00% | -|0.99% | 0.00% | 0.8065|
 | Renal Insufficiency | 0.28% | 0.00% | 0.9265|0.00% | 0.00% | -|
 | Pulmonary Embolism | 0.28% | 0.00% | 0.9265|0.50% | 0.00% | 0.8628|
 | Ventilator | 0.00% | 0.00% | -|**1.98**% | **16.67**% | **0.02064**|
 | Acute Renal Failure | 0.00% | 0.00% | -|**0.00**% | **16.67**% | **6.017e-09**|
 | CVA with Neurologic Deficit | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Myocardial Infarction | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Sepsis | 0.28% | 0.00% | 0.9265|1.98% | 0.00% | 0.7278|
 | Readmission | 3.67% | 0.00% | 0.7353|5.94% | 0.00% | 0.5385|
 | Unplanned Readmission | 3.67% | 0.00% | 0.7353|4.95% | 0.00% | 0.5764|


| | Outpatient Non-Independent Functional Health Status (N = 5) | Outpatient Independent Functional Health Status (N = 352) | p-value | Inpatient Non-Independent Functional Health Status (N = 8) | Inpatient Independent Functional Health Status (N = 200) | p-value |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
 | Superficial SSI | 0.00% | 0.00% | -|0.00% | 0.50% | 0.8411|
 | Deep SSI | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Organ/Space SSI | 0.00% | 0.57% | 0.8658|12.50% | 3.00% | 0.144|
 | Wound Disruption | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Pneumonia | 0.00% | 0.00% | -|**25.00**% | **3.00**% | **0.001509**|
 | Reintubation | 0.00% | 0.00% | -|**25.00**% | **1.50**% | **2.088e-05**|
 | Urinary Infection | 0.00% | 0.00% | -|0.00% | 0.50% | 0.8411|
 | Deep Vein Thrombosis | 0.00% | 0.00% | -|**12.50**% | **0.50**% | **0.0006483**|
 | Renal Insufficiency | 0.00% | 0.28% | 0.905|0.00% | 0.00% | -|
 | Pulmonary Embolism | 0.00% | 0.28% | 0.905|0.00% | 0.50% | 0.8411|
 | Ventilator | 0.00% | 0.00% | -|**25.00**% | **1.50**% | **2.088e-05**|
 | Acute Renal Failure | 0.00% | 0.00% | -|0.00% | 0.50% | 0.8411|
 | CVA with Neurologic Deficit | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Myocardial Infarction | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Sepsis | 0.00% | 0.28% | 0.905|0.00% | 2.00% | 0.6863|
 | Readmission | 0.00% | 3.69% | 0.6616|0.00% | 6.00% | 0.4754|
 | Unplanned Readmission | 0.00% | 3.69% | 0.6616|0.00% | 5.00% | 0.5168|


| | Outpatient Non-Totally or Partially Dependent Functional Health Status (N = 355) | Outpatient Totally or Partially Dependent Functional Health Status (N = 2) | p-value | Inpatient Non-Totally or Partially Dependent Functional Health Status (N = 204) | Inpatient Totally or Partially Dependent Functional Health Status (N = 4) | p-value |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
 | Superficial SSI | 0.00% | 0.00% | -|0.49% | 0.00% | 0.8884|
 | Deep SSI | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Organ/Space SSI | 0.56% | 0.00% | 0.9152|**2.94**% | **25.00**% | **0.0154**|
 | Wound Disruption | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Pneumonia | 0.00% | 0.00% | -|**3.43**% | **25.00**% | **0.02632**|
 | Reintubation | 0.00% | 0.00% | -|**1.96**% | **25.00**% | **0.002889**|
 | Urinary Infection | 0.00% | 0.00% | -|0.49% | 0.00% | 0.8884|
 | Deep Vein Thrombosis | 0.00% | 0.00% | -|0.98% | 0.00% | 0.8423|
 | Renal Insufficiency | 0.28% | 0.00% | 0.9401|0.00% | 0.00% | -|
 | Pulmonary Embolism | 0.28% | 0.00% | 0.9401|0.49% | 0.00% | 0.8884|
 | Ventilator | 0.00% | 0.00% | -|**1.96**% | **25.00**% | **0.002889**|
 | Acute Renal Failure | 0.00% | 0.00% | -|0.49% | 0.00% | 0.8884|
 | CVA with Neurologic Deficit | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Myocardial Infarction | 0.00% | 0.00% | -|0.00% | 0.00% | -|
 | Sepsis | 0.28% | 0.00% | 0.9401|1.96% | 0.00% | 0.7773|
 | Readmission | 3.66% | 0.00% | 0.7828|5.88% | 0.00% | 0.6173|
 | Unplanned Readmission | 3.66% | 0.00% | 0.7828|4.90% | 0.00% | 0.6499|
 
 
 ### Notes
 I did not perform this analysis for Ventilator Dependent, Ascites, and Acute Renal Failure due to lack of patients with the conditions in both outpatient and inpatient settings. 

 ## Multivariate Logistic Regression
 
 Odds Ratio calculations made by including the variables: [Smoke]:

|   | Odds ratio (data) | 
| -------------  | ------------- | 
| Organ/Space SSI  | 5.1263 | 
| Pulmonary Embolism  | 193242590233598.4  | **this seems too high, looking into this further

 








