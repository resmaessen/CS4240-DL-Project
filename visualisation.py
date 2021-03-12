# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 11:43:09 2021

@author: maxim
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle
import matplotlib.image as img 
import numpy as np


# Import images
apple_1 = img.imread('apples/images/20130320T004354.277980.Cam6_41.png')
apple_2 = img.imread('apples/images/20130320T004853.331815.Cam6_63.png')
apple_3 = img.imread('apples/images/20130320T005036.762582.Cam6_52.png')
mango_1 = img.imread('mangoes/images/20151124T024358.594842_i2107j1191.png')
mango_2 = img.imread('mangoes/images/20151124T024519.396151_i1924j1228.png')
mango_3 = img.imread('mangoes/images/20151124T024640.797688_i2604j637.png')
almond_1 = img.imread('almonds/images/fromEast_56_53_IMG_4373_i1200j2400.png')
almond_2 = img.imread('almonds/images/fromEast_57_57_IMG_4375_i600j3300.png')
almond_3 = img.imread('almonds/images/fromEast_59_06_IMG_4420_i1200j2100.png')


# Import annotations
csv_apple_1='apples/annotations/20130320T004354.277980.Cam6_41.csv'
csv_apple_2='apples/annotations/20130320T004853.331815.Cam6_63.csv'
csv_apple_3='apples/annotations/20130320T005036.762582.Cam6_52.csv'
csv_mango_1='mangoes/annotations/20151124T024358.594842_i2107j1191.csv'
csv_mango_2='mangoes/annotations/20151124T024519.396151_i1924j1228.csv'
csv_mango_3='mangoes/annotations/20151124T024640.797688_i2604j637.csv'
csv_almond_1='almonds/annotations/fromEast_56_53_IMG_4373_i1200j2400.csv'
csv_almond_2='almonds/annotations/fromEast_57_57_IMG_4375_i600j3300.csv'
csv_almond_3='almonds/annotations/fromEast_59_06_IMG_4420_i1200j2100.csv'


# Apple
csv_file = list([csv_apple_1, csv_apple_2, csv_apple_3])
im = list([apple_1, apple_2, apple_3])

for j in range(len(csv_file)): 
    data = pd.read_csv(csv_file[j])

    c_x = np.array(data["c-x"])
    c_y = np.array(data["c-y"])
    radius = np.array(data["radius"])

    fig,ax = plt.subplots(1)
    ax.set_aspect('equal')

    ax.imshow(im[j])

    for i in range(len(c_x)):
        circle = Circle((c_x[i], c_y[i]), radius[i], color='r', fill=False)
        ax.add_patch(circle)
    
    plt.show()


# Mango & Almond
csv_file = list([csv_mango_1, csv_mango_2, csv_mango_3, csv_almond_1, csv_almond_2, csv_almond_3]) 
im = list([mango_1, mango_2, mango_3, almond_1, almond_2, almond_3]) 

for j in range(len(csv_file)):
    data = pd.read_csv(csv_file[j])

    x = np.array(data["x"])
    y = np.array(data["y"])
    dx = np.array(data["dx"])
    dy = np.array(data["dy"])

    fig,ax = plt.subplots(1)

    ax.imshow(im[j])

    for i in range(len(x)):
        rectangle = Rectangle((x[i],y[i]), dx[i], dy[i], color='r', fill=False)
        ax.add_patch(rectangle)
    
    plt.show()
