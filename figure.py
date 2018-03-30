#coding=utf-8
import matplotlib.pyplot as plt
import numpy as np 

x = np.linspace(-3,3,50) #-3~3中产生50个点

y1 = 2*x+1
y2 = x*x   

plt.figure()  #figure中显示y1. 
plt.plot(x,y1)
plt.show()

plt.figure(num=2,figsize=(8,5))#一个figure管一段 
plt.plot(x,y2)

plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--')
plt.show()

