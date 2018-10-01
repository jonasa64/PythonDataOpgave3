from datasetter import data as data
from datasetter import dataset_keys as keys

dataset = data.dataset

deaths = {}
death_increase = {}
kidney_deaths = {}
kidney = data.cause.index("Kidney disease")

for i in range(1,53):
    deaths[i] = sum(dataset[(dataset[:,0] == 2016) & (dataset[:,3] == i)][:,4])
    death_increase[i] = sum(dataset[(dataset[:,0] == 1999) & (dataset[:,3] == i)][:,4]) - deaths[i]
    kidney_deaths[i] = sum(dataset[(dataset[:,0] == 2005) & (dataset[:,3] == i) & (dataset[:,2] == kidney)][:,4])
    
deaths_by_state_acd = sorted(deaths, key=deaths.__getitem__)
most_deaths_2016 = data.state[deaths_by_state_acd[-1]]
fewest_deaths_2016 = data.state[deaths_by_state_acd[1]]

print("State with most deaths(2016):",most_deaths_2016)
print("State with least deaths(2016):",fewest_deaths_2016)


death_increase_by_state_acd = sorted(death_increase, key=death_increase.__getitem__)
smallest_death_increase = data.state[death_increase_by_state_acd[1]]

print("State with the smallest increse in deaths(1999-2016):", smallest_death_increase)


kidney_deaths_by_state_acd = sorted(kidney_deaths, key=kidney_deaths.__getitem__)
most_kidney_deaths = data.state[kidney_deaths_by_state_acd[-1]]

print("State with most kidneys disease related deaths(2005):", most_kidney_deaths)
