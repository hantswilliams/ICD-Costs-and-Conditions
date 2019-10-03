<h1> <strong> ICD Costs and Conditions </strong> </h1>

## Description 

This repo contains a value set for associating financial cost ($ USD) with ICD-10 diagnostic/condition codes. 

To view the final mapping document (ICD10 individual costs to Episode Cost of Care), 
proceed to `OUTPUT` folder, there is a .csv and a .pkl (python) file that can be used quickly 


<h3> <strong> How was this created? </strong> </h3>


Information from the Beareu of Economic Analysis (BEA) now provides economic costs per ICD condition. See below for hyperlinks. 
This data includes a mapping of nearly chapter ICD10 chapter categories, subsetted by a CCS Category Number (CCS condition category number assigned by AHRQ) and a AHRQ Category (AHRQ Category). 

A second dataset, provided from hcup-us, has mapping from CCS10 to ICD10. This document (link below) was then utilized to merge 
together the BEA dataset with the HCUP dataset, to create a new dataset that has all economic information at the ICD10 level. 



This data originates from a couple different sources, all government and assumed reliable: <br>
http://www.bea.gov/data/special-topics/health-care <br> 
https://www.bea.gov/system/files/2019-03/Detail-Disease-Blended-forpub2.xlsx <br> 
https://apps.bea.gov/national/viz/diseases/index.htm <br> 
https://www.hcup-us.ahrq.gov/toolssoftware/ccs10/ccs10.jsp




