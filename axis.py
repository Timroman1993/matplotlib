#coding=utf-8
import matplotlib.pyplot as plt
import numpy as np 

x = np.linspace(-3,3,50) #-3~3中产生50个点

y1 = 2*x+1
y2 = x*x   

plt.figure()
plt.plot(x,y2)
plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--')

plt.xlim((-1,2)) #x轴的范围
plt.ylim((-2,3))  #y轴的范围

plt.xlabel('this is x') #坐标描述
plt.ylabel('this is y')

new_ticks = np.linspace(-1,2,5) #更换x的区间显示
print (new_ticks)
plt.xticks(new_ticks)

#plt.yticks([-2,-1,-0.5,1.2,3],['really bad','bad','normal','good','really good'])#一一对应，改变显示	
plt.yticks([-2,-1,-0.5,1.2,3],[r'$really\ bad\ \alpha$',r'$bad$',r'$normal$',r'$good$',r'$really\ good$']) #	显示的字体变好看点 \是转义字符 \alpha能直接打出那个

plt.show()

plt.figure(num=2) #在这里想让原点在中间一些-->改变原点位置
plt.plot(x,y2)
plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--')

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

