from datasetter import data as data
from datasetter import dataset_keys as keys #keys are unused, but contains a usefull data-indexing-list

dataset = data.dataset # Get the dataset from datasetter.py

deaths = {}
death_increase = {}
kidney_deaths = {}
kidney = data.cause.index("Kidney disease") # Get the index key of "Kidney disease" in the cause-collection

for i in range(1,len(data.state)): #loop through all states(i), to extract data
    deaths[i] = sum(dataset[(dataset[:,0] == 2016) & (dataset[:,3] == i)][:,4]) #summarize deaths in the preceding state where the year is 2016 
    death_increase[i] = deaths[i] - sum(dataset[(dataset[:,0] == 1999) & (dataset[:,3] == i)][:,4]) #summarize deaths in preceding state where the year is 1999 and substract from the previously collect 2016-sum
    kidney_deaths[i] = sum(dataset[(dataset[:,0] == 2005) & (dataset[:,3] == i) & (dataset[:,2] == kidney)][:,4]) #summarize deaths in the preciding state where the year is 2005 and the cause is the index key of "Kidney disease"

    
deaths_by_state_acd = sorted(deaths, key=deaths.__getitem__) # sort 2016 deaths-sum ascending
most_deaths_2016 = data.state[deaths_by_state_acd[-1]] # retrieve the last entry of the sorted deaths-sums (highest number)
fewest_deaths_2016 = data.state[deaths_by_state_acd[0]] # retrieve the first entry of the sorted deaths-sums (lowest number)


#print these results
print("State with most deaths(2016):",most_deaths_2016) 
print("State with least deaths(2016):",fewest_deaths_2016)


death_increase_by_state_acd = sorted(death_increase, key=death_increase.__getitem__) # sort the 1999-2016 death increases ascending
smallest_death_increase = data.state[death_increase_by_state_acd[0]] # retrieve the first entry of the sorted deaths-sums (lowest)

#print the result
print("State with the smallest increase in deaths(1999-2016):", smallest_death_increase)


kidney_deaths_by_state_acd = sorted(kidney_deaths, key=kidney_deaths.__getitem__) #sort 2005 kidney disease related deaths-sum ascending
most_kidney_deaths = data.state[kidney_deaths_by_state_acd[-1]] # retrieve the last entry of the sorted deaths-sums (highest)

#print the result
print("State with most kidney disease related deaths(2005):", most_kidney_deaths)
