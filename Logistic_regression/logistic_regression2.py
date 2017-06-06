# -*- coding: utf-8 -*-
"""
Created on Wed May  3 13:59:39 2017

@author: rogue
"""

#logistic 回归，通过求偏导来实现参数求解

import matplotlib.pyplot as plt
from scipy.optimize import minimize
import numpy as np

#定义读取数据函数
import matplotlib.pyplot as plt
from scipy.optimize import minimize

def loaddata(file, delimeter):
    data = np.loadtxt(file, delimiter=delimeter)
    print('Dimensions: ',data.shape)
    print(data[1:6,:])
    return(data)

def plotData(data, label_x, label_y, label_pos, label_neg, axes=None):
    neg = data[:,2] == -1
    pos = data[:,2] == 1

    if axes == None:
        axes = plt.gca()
        axes.scatter(data[pos][:,0], data[pos][:,1], marker='+', c='k', s=60, linewidth=2, label=label_pos)
        axes.scatter(data[neg][:,0], data[neg][:,1], c='y', s=60, label=label_neg)
        axes.set_xlabel(label_x)
        axes.set_ylabel(label_y)
        axes.legend(frameon= True, fancybox = True);
		
data = loaddata('data1.txt','\t')
 
plotData(data, 'Exam 1 score', 'Exam 2 score', 'Pass', 'Fail')

