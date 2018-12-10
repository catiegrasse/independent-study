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







