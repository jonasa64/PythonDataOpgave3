from datasetter import data as data
from datasetter import dataset_keys as keys

deaths = {}
dataset = data.dataset

for i in range(1, 52):
    deaths[i] = sum(dataset[(dataset[:, 0] == 2016) & (dataset[:, 3] == i)][:, 4])

deaths_by_state_acd = sorted(deaths, key=deaths.__getitem__)

print("State with most deaths(2016):", data.state[deaths_by_state_acd[-1]])
print("State with least deaths(2016):", data.state[deaths_by_state_acd[1]])
