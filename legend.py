#coding=utf-8
import matplotlib.pyplot as plt
import numpy as np 

x = np.linspace(-3,3,50) #-3~3中产生50个点

y1 = 2*x+1
y2 = x*x   


plt.figure() #打上那个线表示哪个
plt.plot(x,y2,label = 'power')
plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--',label = 'linear')
plt.legend(loc='best')#best会自己找一个比较好的位置


plt.xlim((-1,2)) #x轴的范围
plt.ylim((-2,3))  #y轴的范围

#gca = 'get current axis'，figure的每个框边都是一条脊（spines）
ax = plt.gca()
ax.spines['right'].set_color('none') #隐去右边框
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom') #将下边框设置成x轴
ax.yaxis.set_ticks_position('left')#将左边框设置成x轴
ax.spines['bottom'].set_position(('data',-1)) #对应移到y的-1处
ax.spines['left'].set_position(('data',-0.25))#对应移到x的-0.5处
plt.show()