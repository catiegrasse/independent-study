## Analysis
#### Source: "Effect of diabetes mellitus on postoperative endoscopic sinus surgery outcomes"  
This paper analyzed the NSQIP database from the years 2005 - 2013 (our data: 2014 - 2016)  
From this group in the database, found 644 patients identified as having undergone ESS  (our data: 565 patients (approx .02% of total database)))
- Paper: 85/644 (13.2%) had DM vs Our data: 69/565 (12.2%) had DM 
- Paper: DM patients were significantly older than non-DM patients vs Our data: average age of patient with DM = 54 vs average age of patient without DM = 44
## Findings
|   | Non - Diabetics (N = 496) | Diabetics (N = 69) |
| ------------- | ------------- | ------------- |
| <= 40 years  | 43.15%  | 17.39 % |
| 41-60 years  | 37.90%  | 33.33% |
| 61-80 years  | 16.73%  | 46.38% |
| > 80 years   | 2.22%   | 2.90%  |
| Male | 47.18% | 44.93% |
| Female | 52.82% | 55.07% |
| White | 73.79% | 68.11% |
| Black | 11.90% | 18.84% |
| Other | 5.44% | 7.25% |
| Unknown | 8.87% | 5.80% |
| Smoking | 20.16% | 20.28% |
| Dyspnea | 3.63% | 7.24% |
| Hypertension | 29.03% | 76.81% |
| Unplanned Readmission | 3.83% | 5.79% |  

- Dyspnea (difficulty breathing) and hypertension were the only statistically significant comorbidities according to the paper

## Odds Ratio
Feature Columns = ["Age", "Sex", "Race", "Diabetes", "Smoking", "Dyspnea", "Hypertension"]
Dependent Variable: Unplanned Readmission
Odds Ratio: 
[[ 1.00548339  0.85197126  1.0763642   0.89472254  1.01183143  0.59995999
   1.12781509]]
*Not sure how to get a single odds ratio from this analysis*
