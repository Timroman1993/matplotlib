#coding=utf-8
#练习一下标注
#coding=utf-8
import matplotlib.pyplot as plt
import numpy as np 

x = np.linspace(-3,3,50) #-3~3中产生50个点

y = 2*x+1

plt.figure(figsize=(8,5))
plt.plot(x,y)
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))

ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

#显示一个点并加标注
x0 = 1
y0 = 2*x0+1
plt.scatter(x0,y0,s=30,color='red') #显示出点
plt.plot([x0,x0],[y0,0],'k--',lw=1)#做垂线段 [a,c],[b,d]是指（a,b),(c,d)之间的连线 k--是黑色虚线
#plt.annotate(r'$(1,%s)$' % y0, xy=(x0,y0))
#plt.annotate(r'$(1,%s)$' % y0, xy=(x0,y0), xycoords='data',xytext=(+30, -30),textcoords='offset points') #从点上移动点距离
plt.annotate(r'$(1,%s)$' % y0, xy=(x0,y0), xycoords='data',xytext=(+30, -30),textcoords='offset points',fontsize=16,arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.2")) 
plt.text(-3,3,r'$this\ is\ \alpha\ balabala... \ $',fontdict={'size': 16, 'color': 'r'})
plt.show()