# 总结全文
"""
# array创建数组 可以指定数据类型、指定维度、真假复制
# empty zero ones 创建数组 可以制定维度，以空、0、1来填充
# full创建数组 可以指定维度和形状，并指定填充数
"""
#%%
import numpy as np # 导入numpy
n1=np.array([1,2,3])
print(n1)
#%%
# 创建一个带小数点的数组
n2=np.array([0.1,0.2,0.3])
n2
#%%
# 创建一个二维数组
n3=np.array([[1,2],[3,4]])
n3
#%%
# 创建数组时指定数据类型
lst=[1,2,3]
n4=np.array(lst,dtype=float)
print(n4)
print(n4.dtype)
print(type(n4))
print(type(n4[0]))
#%%
# 数组复制
n5=np.array([1,2,3])
n6=np.array(n5,copy=True)
n6[0]=100
n6[2]=200
print(n5)
print(n6)
#%%
# 指定维数
lst=[1,2,3]
n7=np.array(lst,ndmin=3) # 最小维数，创建三维数组
print(n7)
#%%
# 不同方式创建数组
#n8=np.empty([4,3])
n8=np.empty([4,3],dtype=int)  #[4,3]表示是4行3列
print(n8)
#%%
# 创建指定维度，以0填充
n9=np.zeros(3)
# 打印
print(n9)
n9  #输出结果默认是浮点类型
#%%
# 创建指定维度，以1填充
n10=np.ones(3)
# 打印
print(n10)
n10
#%%
# 创建指定维度，以指定的数值填充
n11=np.full(3,8)  # 创建一维数组，以8填充3个
# 打印
print(n11)
n11
#%%
n12=np.full((3,4),8)  # 创建二维数组，3行4列，以8填充
print(n12)
n12
#%%
n13=np.full((3,4,5),8)  # 创建三维数组，3行4列5列，以8填充
print(n13)
