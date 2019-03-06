import pandas as pd 
import numpy as np 


costs = pd.read_csv("/Users/hantswilliams/Dropbox/Biovirtua/Python_Projects/ICD10_Costs_Condition/Detail-Disease-Blended-forpub2.csv")
conversions = pd.read_csv("/Users/hantswilliams/Dropbox/Biovirtua/Python_Projects/ICD10_Costs_Condition/ICD_CSS_mapping/ccs_dx_icd10cm_2019_1 (2)/ccs_dx_icd10cm_2019_1.csv")


costs.columns=costs.columns.str.replace(" ","")
costs.columns=costs.columns.str.replace("/","")
costs = costs[costs.columns.drop(list(costs.filter(regex='Unnamed')))]
costs['Year'] = pd.to_numeric(costs['Year'], errors='coerce')
costs = costs[costs['Year'] == 2015]
costs['CCSCategoryNumber'] = costs['CCSCategoryNumber'].round(1)






conversions.columns=conversions.columns.str.replace("'","")
conversions.columns=conversions.columns.str.replace(" ","")
conversions.columns=conversions.columns.str.replace("-","")
##########                                  
conversions['ICD10CMCODE'] = conversions['ICD10CMCODE'].astype(str)
conversions['CCSCATEGORY'] = conversions['CCSCATEGORY'].astype(str)
conversions['MULTICCSLVL1'] = conversions['MULTICCSLVL1'].astype(str)
conversions['MULTICCSLVL2'] = conversions['MULTICCSLVL2'].astype(str)
conversions['ICD10CMCODE'] = conversions['ICD10CMCODE'].apply(lambda x: x.replace("'",''))
conversions['CCSCATEGORY'] = conversions['CCSCATEGORY'].apply(lambda x: x.replace("'",''))
conversions['MULTICCSLVL1'] = conversions['MULTICCSLVL1'].apply(lambda x: x.replace("'",''))
conversions['MULTICCSLVL2'] = conversions['MULTICCSLVL2'].apply(lambda x: x.replace("'",''))
conversions['CCSCATEGORY'] = conversions['CCSCATEGORY'].astype(int)


merged = conversions.merge(costs, how='left', left_on='CCSCATEGORY', right_on='CCSCategoryNumber')









merged.to_pickle("/Users/hantswilliams/Dropbox/Biovirtua/Python_Projects/ICD10_Costs_Condition/output/icd_costs.pkl")
merged.to_csv("/Users/hantswilliams/Dropbox/Biovirtua/Python_Projects/ICD10_Costs_Condition/output/icd_costs.csv", index=False)


