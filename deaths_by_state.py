from datasetter import data as data
from datasetter import dataset_keys as keys

dataset = data.dataset

deaths = {}
kidney_deaths = {}
kidney = data.cause.index("Kidney disease")

for i in range(1,53):
    deaths[i] = sum(dataset[(dataset[:,0] == 2016) & (dataset[:,3] == i)][:,4])
    kidney_deaths[i] = sum(dataset[(dataset[:,0] == 2005) & (dataset[:,3] == i) & (dataset[:,2] == kidney)][:,4])

deaths_by_state_acd = sorted(deaths, key=deaths.__getitem__)
most_deaths_2016 = data.state[deaths_by_state_acd[-1]]
fewest_deaths_2016 = data.state[deaths_by_state_acd[1]]

print("State with most deaths(2016):",most_deaths_2016)
print("State with least deaths(2016):",fewest_deaths_2016)

kidney_deaths_by_state_acd = sorted(kidney_deaths, key=kidney_deaths.__getitem__)
print("State with most kidneys disease related deaths(2005):", data.state[kidney_deaths_by_state_acd[-1]])
