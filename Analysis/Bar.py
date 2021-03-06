#!/usr/bin/env python
# -*- coding: utf-8 -*-
# a bar plot with errorbars
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as plt



def BarchartPlot(N,X,Y,xticks,title,xlabel,ylabel,xlegend,ylegend):
    ind=np.arange(N)   #the x locations for the groups
    width=.4          #the width of the bars

    fig,ax=plt.subplots(figsize=(20, 8))
    rects1=ax.bar(ind,X,width,color='g')
    rects2=ax.bar(ind+width,Y,width,color='r')

    #add some text for labels,title and axes ticks
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.set_xticks(ind + width)
    ax.set_xticklabels(xticks)
    ax.grid(True,which='both')

    ax.legend((rects1[0], rects2[0]), (xlegend, ylegend))
   
    autolabel(rects1,ax)
    autolabel(rects2,ax)
    plt.yticks(np.arange(1, 30, 2.0))
    plt.show()


def autolabel(rects,ax):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.1*height,
                '%d' % int(height),
                ha='center', va='bottom')

