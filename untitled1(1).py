# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1X2-gXMX2QsjNlud-wH0uLLQhbTW6bR1B
"""

import numpy as np
import matplotlib.pyplot as plt
i=np.array([[[255,0,255]]])
plt.imshow(i)

x=np.arange(0,30,0.1)
y=np.sin(x)
plt.plot(x,y)