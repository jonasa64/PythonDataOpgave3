
with open('deathdata.csv', 'r') as csvFile:

    reader = csv.DictReader(csvFile)   

    
    data_kidney_2005 = {}
    
    for row in reader:
	    if row['Year'] == '2005' and row['Cause Name'] == 'Kidney disease' and row['State'] != 'United States':
                data_kidney_2005[row['State']] = int(row['Deaths'])
                    
    print(max(data_kidney_2005,key=data_kidney_2005.get))
