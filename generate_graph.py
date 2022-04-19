import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("results.csv")
x = data['policies'].tolist()
y = data['mean_turnaround_times'].tolist()
plt.plot(x, y)
plt.title('Caching Policies Vs Mean Turnaround Times')
plt.xlabel('Caching Policies')
plt.ylabel('Average Turnaround Time')
plt.savefig('results-graph.png')
