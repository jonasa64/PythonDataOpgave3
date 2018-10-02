# Description:
This program downloads a json-dataset from the NHCS, converts it to csv and retrieves information to answer these questions:  
1. Which state has the most deaths in the year of 2016? (All causes)
2. Which state has the least deaths in the year of 2016? (All causes)
3. Which state has had the smallest increase in deaths from 1999-2016? (All causes)
4. Which state has the most deaths caused by kidney disease in the year of 2005?
5. Which state has had the biggest increase in the death of Alzheimers from 1999-2016? Plot the increase year for year using matplotlib

# Requirements:
You need Python 3.x to run this program

# Dependencies:
This program depends on os, numpy, mathplotlib and urllib to run

# Installation:
Download this repository and launch main.py from your Python CLI 

# Results:
The program extracts data from the created csv-file
  * California has the most deaths in 2016
  * Alaska has the fewest
  * Pennsylvania has the smallest increase in deaths from 1999 to 2016, but the most kidney disease related deaths in 2005
    
# Output:
```
Downloading file ...  
Done  
Converting JSON-file to CSV ...  
Done  
Interpretating ...  
Done  
State with most deaths(2016): California  
State with least deaths(2016): Alaska  
State with the smallest increase in deaths(1999-2016): Pennsylvania  
State with most kidney disease related deaths(2005): Pennsylvania   
```
