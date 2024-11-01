#%%
#
import numpy as np
n=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(n)
print(n.sum()) #整个数组求和

#数组元素行的和
print(n.sum(axis=0))

#数组元素列的和
print(n.sum(axis=1))
#%%
#平均值
print(n.mean())

print('行的平均值')
print(n.mean(axis=0))

print('列的平均值')
print(n.mean(axis=1))
#%%
# 数组中的最大值和最小值
print(n.max())

print('行的最大值',n.max(axis=0))

print('列的最大值',n.max(axis=1))
print(n.min())


print('行的最小值',n.min(axis=0))

print('列的最小值',n.min(axis=1))
#%%
#加权平均
# 一组数据与出现的次数相乘再平均计算，加权平均
n1=np.array([1,2,3,4,5])  # 数组中的数据
n2=np.array([10,20,30,40,50]) # n2表示的是n1数组中数据出现的次数
print(np.average(n1,weights=n2))  # (1*10+2*20+3*30+4*40+5*50)/(10+20+30+40+50)

#%%
#中位数  (前掉是数组有序)
n1=np.array([1,2,3,4,5,6]) #(3+4)/2
print(np.median(n1))

n1=np.array([1,2,3,4,5,288])
print(np.median(n1))
#%%
#方差  :各组数据与它们的平均数的差的平方

n=np.array([1,2,3])  # 平均数为2  ，（1-2）=-1   （2-2）=0  （3-2)=1
print(n.var())
 
#标准差 :均方差，方差的平方根
print(n.std())
#%%
