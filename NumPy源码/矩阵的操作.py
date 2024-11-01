#%%
import numpy as np
a=np.mat('5 6;7 8') # 创建矩阵的方式
print(a)

b=np.mat([[5,6],[7,8]])
print(b)

print(type(a),type(b))

n1=np.array([[5,6],[7,8]])
print(type(n1))
#%%
# 使用mat函数创建常见的矩阵
#创建一个3*3的零矩阵
d1=np.mat(np.zeros((3,3)))
print(d1)
#%%
# 创建一个2*4的1矩阵
d2=np.mat(np.ones((2,4)))
print(d2)
#%%
nd3=np.mat(np.random.rand(3,3)) # 0-1之间的随机数
print(nd3)
#%%
#  1-8之间的随机数
d4=np.mat(np.random.randint(1,8,size=(3,5)))
print(d4)
#%%
# 对角矩阵
nd5=np.mat(np.eye(2,2),dtype=int)
print(nd5)

nd6=np.mat(np.eye(4,4),dtype=int)
print(nd6)
#%%
# 对角线矩阵
a=[1,2,3]
data1=np.mat(np.diag(a))   # 对象线是1，2，3
print(data1)
#%%
b=[7,8,9]
data1=np.mat(np.diag(b))   # 对象线是7，8，9
print(data1)
#%%
