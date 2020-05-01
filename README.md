<p align="center">
<img src="https://raw.githubusercontent.com/jmv74211/matplotlib/master/images/matplotlib_logo.png" width="50%">
</p>

![Status](https://img.shields.io/badge/Status-building-orange.svg) ![Version](https://img.shields.io/badge/version-3.2.1-blue.svg)


# Introduction to matplotlib

Matplotlib is a Python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms.

**Considerations**:

- The figure is the window or general page in which everything is drawn. You can create multiple independent figures. A figure can have other things, like a subtitle, which is a centered title of the figure, a legend, a color bar...

- Axes are added to the figure. The axes are the area in which the data is graphed with functions such as `plot()` and `scatter()`, and can have associated labels.

- Each axis has an x-axis and a y-axis, and each contains a numbering.

   There are also the labels of the axes, the title, and the legend that must be taken into account when you want to customize the axes, but also taking into account that the scales of the axes and the grid lines can be useful.

- The vertebral lines are lines that connect the axis marks and designate the boundaries of the data area, in other words, they are the simple square that you can see when you have initialized.

- **matplotlib** is the entire Python data display package.

- **pyplot** is a module in the matplotlib package. The module provides an interface that allows you to create shapes and axes implicitly and automatically to achieve the desired frame.

- Machine learning **data** for graphing on matplotlib **should be structured under the numpy library**.

# How to create graphics with matplotlib

`Matplotlib` allows you to create different graphics. The possible types and examples links are mentioned below:

## Line diagram

Create a simple plot.

<p>
<img src="https://raw.githubusercontent.com/jmv74211/matplotlib/master/images/line_diagram_intro.png" width="50%">
</p>

> You can find examples [here](https://github.com/jmv74211/matplotlib/tree/master/1_line_diagram)


# References

- Matplotlib: Visualization with Python, available in https://matplotlib.org/

- Codebasics youtube channel, Matplotlib Tutorial, available in https://www.youtube.com/watch?v=qqwf4Vuj8oM&list=PLeo1K3hjS3uu4Lr8_kro2AqaO6CFYgKOl&index=1
