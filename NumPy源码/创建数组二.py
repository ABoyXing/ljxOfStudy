# 总结
"""
    # arange生成数组, arange(start,stop,step) 生成一个从start开始，到stop结束（不包括stop），步长为step的数组。
    # linespace生成数组, linespace(start,stop,num) 范围内的等差数列
    # logspace生成数组, logspace(start,stop,num,base=10,dtype=None) 等比数列
"""

#%%
#从数值范围创建数组
# 导入
import numpy as np
n1=np.arange(1,11,2) # 生成一个从1开始，到11结束（不包括11），步长为2的数组，即[1, 3, 5, 7, 9]。
# 打印
print(n1)
#%%
#
n2=np.linspace(7500,10000,6) # endporint=True表示包含stop(终止值)，6表示是创建6个
print(n2)
print(type(n2))
#%%
# 数组的元素是一个等比数列
n3=np.logspace(0,63,64,base=2,dtype='uint64')
print(n3)
#%%
