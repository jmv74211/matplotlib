# Line diagram

## Basic example

Create a simple plot.

```python
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
ax.grid()

fig.savefig("test.png")
plt.show()
```

<p align="center">
<img src="https://raw.githubusercontent.com/jmv74211/matplotlib/master/images/line_diagram_intro.png" width="55%">
</p>

---

## More examples

### Import library

```python
import matplotlib.pyplot as plt
```

### Define your data

```python
days = [1,2,3,4,5,6,7]
max_t = [50,51,52,48,47,49,46]
min_t = [43,42,40,44,33,35,37]
avg_t = [45,48,48,46,40,42,41]
```

### Configure the axes limits

```python
axes = plt.axes()
axes.set_ylim([30,60])
axes.set_xlim([min(days), max(days)])
```

### Define the chart labels

```python
plt.xlabel("Days")
plt.ylabel("Temperature")
plt.title("Weather")
```

### Plot the line diagrams with labels

```python
plt.plot(days,max_t, label="Max")
plt.plot(days,min_t, label="Min")
plt.plot(days,avg_t, label="Avg")
```

### Plot the labels as legend

```python
plt.legend(shadow=True, fontsize='small')
```

### Plot a grid

```python
plt.grid()
```

### Show the graphic

```
plt.show()
```

<p align="center">
<img src="https://raw.githubusercontent.com/jmv74211/matplotlib/master/images/line_diagram_example_1.png" width="70%">
</p>

> See full code [here](https://github.com/jmv74211/matplotlib/blob/master/1_line_diagram/example_axes_labels_legend_grid.py)

## Load data from csv with pandas and plot it

### Load csv data to dataframe

```python
DATA_FILE = 'example_data/weight.csv'
df = pd.read_csv(DATA_FILE)
```

### Plot using dataframe data

```python
plt.plot(df['week'], df['jmv74211'], label= 'User1', linewidth = 1, color = 'blue')
plt.plot(df['week'], df['vpc'], label= 'User2', linewidth = 1, color = 'red')
```

<p align="center">
<img src="https://raw.githubusercontent.com/jmv74211/matplotlib/master/images/line_diagram_example_2.png" width="70%">
</p>

> See full code [here](https://github.com/jmv74211/matplotlib/blob/master/1_line_diagram/example_loading_data_with_pandas.py)