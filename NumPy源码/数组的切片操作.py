'''
# 1.切片函数list[star:end] 单个引号意味着从0开始，到end-1结束
# 2.切片函数list[star:end:step] 获取数组中指定步数的元素  star、end也可以是负数，-1代表末尾。
# 3.切片函数list[::] 获取数组中的所有元素
# 4.切片函数list[::step] 获取数组中的所有元素，步长默认为1

# np的array数组切片是引用类型，修改切片会影响原始数组。
# python自带的list数组的切片则是真是复制，修改切片不会影响。

# array二维数组的切片表达：
    # arr[行：列]
    # arr[star:end,star:end] 行的起始，列的起始 star或end如果为空，就以为着从起点或者末尾
    #也可以是arr[行,star：end] 这样就是某行 及 范围内的列
'''


#%%
import numpy as np
n=np.array([10,20,30,40,50,60,70,80,90])
print(n)
print(n[0:5:2])

#%%
print(n[:3]) # 省略起始位置，那么默认从0开始 [0,3), 步长默认为1
#%%
print(n[3:6]) # [3,6)
#%%
print(n[6:]) 
#%%
print(n[6:9])
#%%
print(n[::]) # 获取数组中的的所有元素
#%%
#修改步长
print(n[0::2]) # 0,2,4,6,8,
#%%
print(n[1::5])
#%%
# 步长还可以为负数
print(n[::-1])
#%%
print(n[-1:-10:-1])
#%%
print(n[-5:-8:-2])
#%%
# 列表的切片操作与数组的切片操作的区别
array=np.array([10,20,30,40])
print(array)
arr1=array[1:4]
print(arr1)
# 对切片之后的数组进行修改
arr1[0]=100
print(arr1)
print(array)
#%%
lst=[10,20,30,40]
lst1=lst[1:4]
print(lst1)
lst1[0]=100
print(lst1)
print(lst)
#%%
# 二维数组的切片操作
arr=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(arr)
#%%
print(arr[1,2]) # 1表示的是索引为1的行， 2表示的是索引为2的列
#%%
print(arr[:2,1:]) # 从索引为0的行到索引为2的行，不包含2，从索引为1的列开始，一直到最后的列
#%%
print(arr[1,:2]) # 逗 号之前表示行，索引为1的行，到索引为2的列结束，不包含2
#%%
print(arr[:2,2])
#%%
print(arr[:,:1])
#%%

#%%
