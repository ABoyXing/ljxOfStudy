'''
当然可以！以下是 NumPy 中数组元素的增删改查操作的简要总结：
# 增加
# append: 向数组末尾添加元素。np.append(arr, values, axis=0)
# insert: 在指定位置插入元素。 np.insert(arr, index, values, axis=0) values维度和arr一致
# vstack: 沿垂直方向（第一轴）堆叠数组。np.vstack(arr1,arr2)
# hstack: 沿水平方向（第二轴）堆叠数组。np.hstack(arr1,arr2)
# concatenate: 沿指定轴堆叠数组。np.concatenate(arr1,arr2,axis=0)
# axis=0 垂直方向，axis=1 水平方向

# 删除
# delete: 删除指定索引处的元素。np.delete(arr, index, axis=0)

# 修改
# 直接通过索引赋值可以修改数组中的元素。

# 查询
# where: 返回满足条件的元素索引。
    np.where(n>5) 解释：返回满足条件的元素索引。
    np.where(n>5,2,0) 解释：返回满足条件的元素索引，如果满足条件，则替换为2，否则替换为0。
'''
#%%
# insert补充
import numpy as np
n1=np.array([[1,2],[3,4],[5,6]])
arr=np.insert(n1,1,values=[10,20],axis=0)
print(arr)

#%%
# 
import numpy as np
n1=np.array([[1,2],[3,4],[5,6]])
# 创建第二个数组
n2=np.array([[10,20],[30,40],[50,60]])
# print(n1)
# print(n2)
#
# # 水平方向增加数据 (列数的增加)2列， 4列
# print(np.hstack((n1,n2)))
#
# #垂直方向增加数据(行数的增加) 3行，变为6行
# print(np.vstack((n1,n2)))
# 水平方向和垂直方向增加数据,axis=0 垂直方向，axis=1 水平方向
print(np.concatenate((n1,n2),axis=1))
#%%
#数组的删除操作
n1=np.array([[1,2],[3,4],[5,6]])
print(n1)

#删除第三行
n2=np.delete(n1,2,axis=0) # 2行索引为2的，轴是0
print(n2)

#删除第一列
n3=np.delete(n1,0,axis=1)
print(n3)

#删除第二行和第三行
n4=np.delete(n1,(1,2),axis=0)
print(n4)
#%%
#数组的修改操作
n1=np.array([[1,2],[3,4],[5,6]])
print(n1)
#修改操作
n1[1]=[30,40]
print(n1)

n1[2][1]=88
print(n1)
#%%
#数组的查询操作
n=np.arange(1,11)
print(n)

n2=n[np.where(n>5)] # 数组中所有大于5的元素
print(n2)

n3=np.where(n>5,2,0) # 数组中的元素大于5，输出2,否则输出0
print(n3)
#%%
