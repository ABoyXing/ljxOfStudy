# 总结全文
# random.rand生成随机数组 random.rand()
"""
# random.randn 生成正态分布的随机数组
# random.randint 生成指定范围的随机int数组(整数)
# np.random.normal(0,0.1,size=(2,3)) # 均值为0，标准差为0.1 2行3列
# np.frombuffer(b'juanzijie',dtype='S1') # b'juanzijie'是一个字节数组，dtype='S1'表示每个元素是一个字节
# np.fromiter(iter,dtype='int') # 解释 iter是一个迭代器，dtype='int'表示每个元素是一个整数
"""
#%%
import numpy as np
n1=np.random.rand(5) # [0,1) 5个元素
print(n1)
#%%
n2=np.random.rand(2,4) #解释 2行4列
n2
#%%
# 用于从正态分布中返回随机生成的数组
n3=np.random.randn(10000000)
print(n3)
# 累加n3并打印
print(n3.sum()/n3.size) # 标准正态分布是一个均值为0（相对均值），标准差为1的正态分布。这个函数经常用于生成测试数据或者模拟一些随机过程。
#%%
n3=np.random.randn(3,4) #解释 3行4列
print(n3)
#%%
# 生成指定范围的随机数组
n4=np.random.randint(1,3,10) #[1,3)  ,产生10个元素
print(n4)
#%%
n4=np.random.randint(1,3,size=(2,3)) #[1,3)  
n4
#%%
# 生成正态分布 的随机数组
n5=np.random.normal(0,0.1,10) # 均值为0，标准差为0.1
print(n5)
#%%
n5=np.random.normal(0,0.1,size=(2,3)) # 均值为0，标准差为0.1 2行3列
n5
#%%
#asarray函数的使用
n1=np.asarray([1,2,3]) # 通过列表创建数组
n1 
#%%
# 通过列表的元组创建数组
n2=np.asarray([(1,2,3),(4,5,6)])
n2
#%%
# 通过元组创建数组
n3=np.asarray((1,2,3))
n3
#%%
# 通过元组的元组创建数组
n4=np.asarray(((1,2,3),(3,4,5)))
n4
#%%
# 通过元组的列表
n5=np.asarray(([1,2],[4,5]))
n5
#%%
# 动态数组
n1=np.frombuffer(b'juanzijie',dtype='S1') # b'juanzijie'是一个字节数组，dtype='S1'表示每个元素是一个字节
print(n1)
#%%
# 从迭代对象中创建数组对象
iter=(i for i in range(5))
n1=np.fromiter(iter,dtype='int') # 解释 iter是一个迭代器，dtype='int'表示每个元素是一个整数
print(n1)
#%%
#empty_like的使用
n=np.empty_like([[1,2],[3,4]])  # 创建一个2行2列的数组，因为给定的是2行2列
print(n)
#%%
n=np.zeros_like([[1,2],[3,4]])  # 创建以0填充的2行2列的数组
n
#%%
n=np.ones_like([[1,2],[3,4]])  # 创建以1填充的2行2列的数组
n
#%%
n=np.full_like([[1,2],[3,4]],8)  # 创建以8填充的2行2列的数组
n
#%%
