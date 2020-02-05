import matplotlib as mpl
from matplotlib import pyplot as plt
import matplotlib as mpl
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.patches as mpatch
import matplotlib.gridspec as gridspec
from matplotlib_venn import venn2


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
    
def create_cluster_stacked_bar(var_name, sizes, values, labels = ["Female", "Male"], ncluster = 4, fontsize = 22, 
                               colors_bar = ["royalblue", "pink"], colors_text = ["blue", "hotpink"], figsize = (15,10)):
    
    x = [i + 1 for i in range(ncluster)]
    
    plt.figure(figsize = figsize)
    
    plt.bar(x, height = sizes, color = colors_bar[1], label = labels[0])
    
    plt.bar(x, height = values, color = colors_bar[0], label = labels[1])
    
    plt.xticks(x)
    
    plt.xlabel("Clusters")
    
    plt.ylabel("Counts")
    
    plt.title(var_name + " Insights")
    
    for i in range(4):
        
        percentage = round(values[i] / sizes[i] * 100, 1)
        
        text1 = str(values[i]) + "(" + str(percentage) + "%)"
        
        text2 = str(sizes[i] - values[i]) + "(" + str(round(100 - percentage, 1)) + "%)"
        
        plt.text(i + 1, values[i] + 500, text1 , horizontalalignment = 'center', verticalalignment = 'center', 
                 fontdict = {"color" : colors_text[0] , "size" : fontsize})
        
        plt.text(i + 1, sizes[i] + 500, text2, horizontalalignment = 'center', verticalalignment = 'center', 
                 fontdict = {"color" : colors_text[1], "size" : fontsize})
    
    plt.legend(prop = {'size': 18}, fancybox = True)
    
    plt.show()


def create_cluster_donut_chart(var_name, values, labels = ["Card", "EFTPOS", "Cash", "Other"], ncluster = 4, 
         color = ["royalblue", "tomato", "seagreen", "gold"], figsize = (20, 12)):
    
    fig, axes = plt.subplots(nrows = ncluster // 2, ncols = ncluster // 2, figsize = figsize)
    
    ax = axes.flatten()
    
    for i in range(ncluster):
        
        leg = ax[i].pie(values[i], colors = ["royalblue", "tomato", "seagreen", "yellow"], autopct = '%1.1f%%', 
                  startangle = 90, pctdistance = 0.80, textprops = {"fontsize" : 16}, explode = (0.03,) * len(labels))
        
        ax[i].add_artist(plt.Circle((0, 0), 0.60, fc = 'white'))
        
        ax[i].set_title("Cluster" + str(i + 1), fontsize = 18)
    
    ax[i].legend(leg[0], labels, prop = {"size" : 18}, bbox_to_anchor = (-0.25, 1.4), fancybox = True)
    
    fig.text(0.5, 0.92, var_name + ' Across Various Cluster', horizontalalignment = 'center', verticalalignment = 'center',
             fontsize = 22)
    
    #fig.show()
    
def create_cluster_bar_side(var_name, values, labels = ["Yes", "No", "Unknown"], ncluster = 4, width = 0.5, 
         colors = ["royalblue", "tomato", "seagreen"], figsize = (20, 12)):
    
    for i in range(ncluster):
        plt.bar(i + 1, values[i][0], width = width/3, align = "center", edgecolor = "", color = colors[0])
        plt.bar(i + 1 - width/3, values[i][1], width = width/3, align = "center", edgecolor = "", color = colors[1])
        plt.bar(i + 1 + width/3, values[i][2], width = width/3, align = "center", edgecolor = "", color = colors[2])
    
    plt.xticks([i + 1 for i in range(ncluster)])
    
    patches = [ plt.plot([],[], marker = "s", ms = 10, ls = "", mec = None, color = colors[i], 
            label = labels[i])[0]  for i in range(len(colors)) ]
    
    plt.legend(handles = patches, loc = 'upper right', ncol = 1, prop = {"size" : 16})
    
    plt.xlabel("Clusters")
    
    plt.ylabel("Count/Frequency")
    
    plt.title(var_name + " Across Various Clusters")
    
    plt.show()
    

def create_cluster_venn_diagrams(dog_owners, cat_owners, both_owners, total, sizes, ncluster = 4, title = "Pets Insight", 
                                colors = ['blue', 'salmon', "#E1BCFF"], labels = ["Dog Owners", "Cat Owners", "BOTH"], 
                                figsize = (20,16)):


    fig, axes = plt.subplots(ncols = ncluster//2, nrows = ncluster//2, figsize = figsize)

    ax = axes.flatten()


    for i in range(ncluster):
        
        v2 = venn2(subsets = {
                                '10': dog_owners[i], '01': cat_owners[i], '11': both_owners[i]
                             },
                   set_colors = colors, alpha = 0.4, ax = ax[i])

        for idx, subset in enumerate(v2.set_labels):v2.set_labels[idx].set_visible(False)

        v2.get_label_by_id('10').set_text('%d\n(%.1f%%)' % (dog_owners[i], dog_owners[i] / total[i] * 100))
        v2.get_label_by_id('01').set_text('%d\n(%.1f%%)' % (cat_owners[i], cat_owners[i] / total[i] * 100))
        v2.get_label_by_id('11').set_text('%d\n(%.1f%%)' % (both_owners[i], both_owners[i] / total[i] * 100))

        ax[i].text(0.0, -0.55, "Total = " +  str(total[i]) + "\nCluster Size = " + str(sizes[i]), 
                   horizontalalignment = 'center', verticalalignment = 'center', fontsize = 20)

        ax[i].set_title("Cluster" + str(i + 1))

        for text in v2.set_labels:
            text.set_fontsize(18)

        for text in v2.subset_labels:
            text.set_fontsize(20)    


    patches = [ plt.plot([],[], marker = "o", ms = 18, ls = "", mec = None, color = colors[i], alpha = 0.4,
                label = labels[i])[0]  for i in range(len(colors)) ]

    plt.legend(patches, labels, prop = {"size" : 18}, bbox_to_anchor = (0.1, 1.3), fancybox = True)
    fig.text(0.47, 0.9, title, fontsize = 24)
    plt.show()
