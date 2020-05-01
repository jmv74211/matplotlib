import matplotlib.pyplot as plt

# Data
days = [1,2,3,4,5,6,7]
max_t = [50,51,52,48,47,49,46]
min_t = [43,42,40,44,33,35,37]
avg_t = [45,48,48,46,40,42,41]

# Axes limits
axes = plt.axes()
axes.set_ylim([30,60])
axes.set_xlim([min(days), max(days)])

# Chart labels
plt.xlabel("Days")
plt.ylabel("Temperature")
plt.title("Weather")

# Plot line diagram
plt.plot(days,max_t, label="Max")
plt.plot(days,min_t, label="Min")
plt.plot(days,avg_t, label="Avg")

# Show legend
plt.legend(shadow=True, fontsize='small')

# Show grid
plt.grid()

# Show figure
plt.show()