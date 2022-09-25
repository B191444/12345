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

x=np.arange(0,50,0.1)
y=np.sin(x)
plt.plot(x,y)

a=[1,2,3,4,5]
b=[5,20,7,8,9]
plt.plot(a,b)
plt.show()

r=[23,4,12,3,4]
v=[12,234,21,1,2]
plt.plot(r,v)
plt.show()

plt.plot(r,v,color="black",label="LINE1",linewidth=2,marker="*",markeredgecolor="green",
         markerfacecolor="red",markersize=20,linestyle="dotted")
plt.title("line graph")
plt.legend()
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()

plt.bar(r,v,color="blue")
plt.show()



plt.plot(r,v,color="blue")
plt.title("LINE GRAPH")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.show()

a=[1,2,3,4,5,6]
b=[5,6,7,8,9,9]
col=['r','g','b','y','w','k']
plt.scatter(a,b,c=col,marker="*",s=100,alpha=1)
plt.show()

hours=[8,2,4,6]
work=['sleep','food','college','leisure']
col=['yellow','blue','green','red']
plt.pie(hours,labels=work,colors=col,explode=[0,0,0,0],startangle=90)
plt.show()

x=['AA','BB','CC']
y=[10,200,20]
#plt.barh(x,y,color=['r','b','g'])
plt.barh(x,y)
plt.show()