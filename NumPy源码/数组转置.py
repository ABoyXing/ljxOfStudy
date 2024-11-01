'''
# arr.reshape(列数,行数)
# arr.T  转置
# arr.transpose() 转置

'''


#%%
import numpy as np
n=np.arange(24).reshape(4,6)
print(n)
# 转置
n2=n.T
print(n2)

# 转置
n3=n.transpose()
print(n3)
#%%
#转置练习
n=np.array([['A',100],['B',200],['C',300],['D',400],['E',500]])
print(n)

newa=n.T
print(newa)
#%%
