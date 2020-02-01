import matplotlib as mpl
from matplotlib import pyplot as plt
import matplotlib as mpl
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.patches as mpatch
import matplotlib.gridspec as gridspec


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
    Making it easier to observe distribution of a particular variable
    
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


def barplot(count_series, xlab, ylab, title, color, labels, figure_size = (12, 10), adjust = False, xrotation = 0):
    
    '''
    Function that creates barplot for pandas dataseries using the counts.
    
    Input
           : count_series -> type : pandas series
           : xlab -> name of the x axis -> type : string
           : ylab -> name of the y axis -> type : string
           : title -> title label -> type : string
           : color -> color(s) of the barplot -> type : any iterable object(list, string, tuple, etc)
           : labels -> labels in which order you want bars of the barplot -> type : list or tuple or any iterable
           : figure_size -> size of the figure -> type : tuple -> default : (12,10)
           : adjust -> adjusts the xaxis label if they are too big -> type : boolean -> default : False
    
    Output : Returns nothing
    '''

    # Creates an empty figure
    plt.figure(figsize = figure_size)
    
    # Creates an barplot
    plt.bar(count_series.index, count_series, color = color, edgecolor = "black")
    
    # Setting xticks and labels for xticks
    plt.xticks(count_series.index, labels, rotation = xrotation)
    
    # Setting title and label for both axis
    plt.ylabel(ylab)
    plt.xlabel(xlab)
    plt.title(title)
    
    # Adjust size of xaxis labels 
    if adjust:
        for tick in plt.gca().xaxis.get_major_ticks():
            tick.label.set_fontsize(10)
    
    plt.show()


def create_cluster_histo_and_box(var_name, values, xlab, ncluster = 4, color = ["royalblue", "tomato", "seagreen", "gold"], 
                        figsize = (20, 20)):

    fig = plt.figure(figsize = figsize)
    
    outer = gridspec.GridSpec(ncluster//2, ncluster//2, wspace = 0.2, hspace = 0.2)

    for i in range(ncluster):
        
        inner = gridspec.GridSpecFromSubplotSpec(2, 1, subplot_spec = outer[i], wspace = 0.1, hspace = 0.1)

        for j in range(ncluster//2):
            
            ax = plt.Subplot(fig, inner[j])
            
            if j == 0:
                
                ax.hist(values[i], edgecolor = "black", color = color[i])
                
                ax.set_xticks([])
                
                ax.set_title("Cluster" + str(i + 1), fontsize = 20)
            
            else:
                
                ax.boxplot(values[i], boxprops = dict(color = color[i]), vert = False)
                
                ax.set_yticks([])

            fig.add_subplot(ax)

    fig.text(0.5, 0.92, var_name + ' Across Various Cluster', horizontalalignment = 'center', verticalalignment = 'center', 
             fontsize = 22)
    
    fig.text(0.5, 0.1, xlab, horizontalalignment = 'center', verticalalignment = 'center', fontsize = 20)
    
    fig.text(0.085, 0.5, 'Frequency', horizontalalignment = 'center', verticalalignment = 'center', fontsize = 20, rotation = 90)
    
    #fig.show()
    
    
def create_cluster_bar(var_name, values, max_possible_val, xlab, ncluster = 4, color = ["royalblue", "tomato", "seagreen", "gold"], 
                        figsize = (20, 12)):
    
    fig, axes = plt.subplots(nrows = ncluster // 2, ncols = ncluster // 2, figsize = figsize)
    
    ax = axes.flatten()
    
    for i in range(ncluster):
        
        ax[i].bar(values[i].index, values[i], color = color[i], edgecolor = "black")
        
        ax[i].set_xticks(range(max_possible_val + 1))
        
        if i < 2:
            
            plt.setp(ax[i].get_xticklabels(), visible = False)
            
            ax[i].tick_params(axis = 'both', which = 'both', length = 0)
        
        ax[i].text(0.9, 0.9, "Cluster" + str(i + 1), horizontalalignment = 'center', verticalalignment = 'center', 
                   fontdict = {"color" : color[i], "size" : 22}, transform = ax[i].transAxes)
    
    
    fig.text(0.5, 0.92, var_name + ' Across Various Cluster', horizontalalignment = 'center', verticalalignment = 'center',
             fontsize = 22)
    
    fig.text(0.5, 0.080, "No of Children", horizontalalignment = 'center', verticalalignment = 'center', fontsize = 20)
    
    fig.text(0.085, 0.5, 'Counts', horizontalalignment = 'center', verticalalignment = 'center', fontsize = 20, rotation = 90)
    
    #fig.show()