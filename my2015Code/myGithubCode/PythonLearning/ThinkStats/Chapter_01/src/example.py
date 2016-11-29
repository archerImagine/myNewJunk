"""
!/usr/bin/env python
 -*- coding: utf-8 -*-
 This file contains code for use with "Think Stats",
 by Allen B. Downey, available from greenteapress.com

 Copyright 2014 Allen B. Downey
 License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
 @FileName: example.py
 @ProjectName : ThinkStats
 @Date:   2015-04-28 14:43:02
 @Last Modified time: 2015-04-29 12:46:15
"""
import numpy as np
import matplotlib.cm as cm
from matplotlib.pyplot import figure, show

fig = figure(figsize=(8, 8))
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8], polar=True)
N = 20
theta = np.arange(0.0, 2*np.pi, 2*np.pi/N)
radii = 10*np.random.rand(N)
width = np.pi/4*np.random.rand(N)
bars = ax.bar(theta, radii, width=width, bottom=0.0)
for r, bar in zip(radii, bars):
    bar.set_facecolor(cm.jet(r/10.))
    bar.set_alpha(0.5)

show()
