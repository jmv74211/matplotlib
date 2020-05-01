import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Load data
DATA_FILE = 'example_data/weight.csv'
df = pd.read_csv(DATA_FILE)

# Plot configuration vars
weight_range = [70,80]
x_increment = 1.0
y_increment = 2.0

# Set axes range
axes = plt.axes()
axes.set_ylim(weight_range)
axes.set_xlim([min(df['week']), max(df['week'])])

# Configure the characteristics of the chart
plt.plot(df['week'], df['jmv74211'], label= 'User1', linewidth = 1, color = 'blue')
plt.plot(df['week'], df['vpc'], label= 'User2', linewidth = 1, color = 'red')

# Set axes marker interval
plt.xticks(np.arange(min(df['week']), max(df['week'])+1, x_increment))
plt.yticks(np.arange(min(weight_range), max(weight_range)+1, y_increment))

# Define title and name of axes
plt.title('Weight diagram')
plt.ylabel('Weight')
plt.xlabel('Weeks')

# Show legend, grid and figure
plt.legend()
plt.grid()
plt.show()