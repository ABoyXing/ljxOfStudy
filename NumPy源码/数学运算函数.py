# 总结全文
"""
# 数学运算函数
# 数组的加减乘除
# 高纬度加减乘除低纬度
# 倒数 幂运算 求余数等

"""

#%%
import numpy as np
# 按1递增生成一个3*3*3的三维数组
n0=np.arange(27).reshape(3,3,3)
n1=np.array([[1,2,3],[4,5,6],[7,8,9]])
n2=np.array([10,10,10])
n3=np.array([1])
print(n0)
print(n1)
print(n2)
# 数组的加，减，乘，除
print(np.add(n1,n2))
print(n1+n2)
print(n1-n3)
print('实验：',n0-n1)

print('减:',np.subtract(n1,n2))
print('乘:',np.multiply(n1,n2))
print('除:',np.divide(n1,n2))
#%%
# 倒数
n1=np.array([0.25,1.75,2,100])
print(np.reciprocal(n1))
#%%
# 幂运算
n1=np.array([10,100,1000])  #n1这个数组的n2次幂
n2=np.array([1,2,3])

print(np.power(n1,n2))

#%%
# 求余
n1=np.array([10,20,30])

n2=np.array([4,5,-8])

print(np.mod(n1,n2))

# 30除以-8的余数 的公式   余=a-n*[a//n]      30//-(8) -3.75向下取整  为  -4   
                             #30-(-8)*(-4)
#%%
# 四舍五入
n=np.array([1.55,6.823,100,0.11897,3.1415926,-3.456])
print(n)
print(np.around(n)) # 四舍五入取整
print(np.around(n,decimals=2)) # 保留 小数点后2位
print(np.around(n,decimals=-1)) # 四舍五入取整到小数点的左侧
#%%
# 向上取整与向下取整
print(np.ceil(n))
print(np.floor(n))
#%%
# 三角函数
n=np.array([0,30,45,60,90])
# 不同角度的正弦值
print(np.sin(n*np.pi/180))

print(np.cos(n*np.pi/180))

print(np.tan(n*np.pi/180))
#%%
