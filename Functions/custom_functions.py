import matplotlib as mpl
from matplotlib import pyplot as plt
import matplotlib as mpl
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.patches as mpatch


# Setting matplotlib parameters

## Change title size of a plot
mpl.rcParams['axes.titlesize'] = 22
## Change label size(x and y) of a plot
mpl.rcParams['axes.labelsize'] = 16
## Change xticks size of a plot
mpl.rcParams['xtick.labelsize'] = 15
## Change yticks size of a plot
mpl.rcParams['ytick.labelsize'] = 15




def create_histogram_plus_boxplot(series, var_name, color, ylabel, xlabel, size):
    
    '''
    Function that creates combination of histogram and boxplot for pandas dataseries.
    Making it easier to observe distribution of a particular varibale
    
    Input
           : series -> type : pandas series or list
           : var_name -> name of the variable (to display in the title of a plot) -> type : string
           : color -> color for both histogram and boxplot(border color) -> type : string
           : xlabel -> name of the x axis -> type : string
           : ylabel -> name of the y axis -> type : string
    
    Output : Returns nothing
    '''
    
    # Create a figure of width 10cm and height 11cm
    plt.figure(figsize = size)
    
    # plt.subplot(row, column, index)
    plt.subplot(2, 1, 1)
    # Plotting a histogram
    plt.hist(series, edgecolor = "black", color = color)  
    # Setting the title of histogram
    plt.title('Histogram of ' + var_name)
    # xticks = [] because both histogram and boxplot share same x axis (you can use sharex argument in plt.subplots function)
    plt.xticks([])
    
    # Setting label on y-axis
    plt.ylabel(ylabel)
    
    plt.subplot(2, 1, 2)
    # Plotting a boxplot
    plt.boxplot(series, boxprops = dict(color = color), vert = False)  
    # Setting labels on x-axis
    plt.xlabel(xlabel)
    # Setting the title of boxplot
    plt.title('Boxplot of ' + var_name)
    # No need of labels on y-axis(one variable)
    plt.yticks([])
    
    plt.show()
