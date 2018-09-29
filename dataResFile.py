start_year = 1999
end_year = 2016
state = 'Alaska'
cause = "Alzheimer's disease"

years = range(start_year, end_year+1)

death_arr = [data[3] for year in years for data in dataset if data[0] == year and data[2] == state and data[1] == cause]                    
  
end_years = np.array(death_arr[1:])
start_years = np.array(death_arr[:-1])
increase_arr = end_years - start_years


xs = years[1:]
ys = increase_arr
xlabels = [f'{year}-{year+1}' for year in years]
 
 
plt.title(f"Annual increase in deaths for\n '{cause}' in '{state}'", fontsize=14)
plt.xlabel("Time period", fontsize=12)
plt.ylabel("Deaths", fontsize=12) 
plt.xticks(xs, xlabels, rotation='vertical')
plt.tight_layout(pad=2.0)
plt.plot(xs, ys, linewidth=5)

plt.show()
plt.close()
  
