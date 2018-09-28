# PythonDataOpgave3

Når vi bruger "import datasetter", kan vi tilgå variablen dataset_keys: *datasetter.dataset_keys*  
Den er nemt at indexere dataene efter.

Et godt udgangspunkt kunne være:  
```python
from datasetter import data as data
from datasetter import dataset_keys as keys

dataset = data.dataset
```

*data* er en initialiseret klasse, hvorfra vi kan hente listerne *icd*,*cause* og *state*
*state* har *"United States"* som index 0, da *"United States"* optræder som en stat i datasettet, og naturligvis ikke skal medregnes når man undersøger noget fra de forskellige stater. 

# Rune
1. Which state has the most deaths in the year of 2016? (All causes)
2. Which state has the least deaths in the year of 2016? (All causes)

# Anders

3. Which state has had the smallest increase in deaths from 1999-2016? (All causes)
4. Which state has the most deaths caused by kidney disease in the year of 2005?

# Jonas

5. Which state has had the biggest increase in the death of Alzheimers from 1999-2016? Plot the increase year for year using matplotlib
