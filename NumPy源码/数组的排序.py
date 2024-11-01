'''
# np.sort(arr,axis=None,kind='quicksort',order=None)
    arr：需要排序的数组。
    axis：沿哪个轴排序，默认为 1(按列)。
    kind：排序算法类型，默认为 'quicksort'。
    order：若数组包含多个字段，则按照哪个字段排序
# np.argsort()
# np.lexsort()
'''



#%%
#数组的排序
import numpy as np
n=np.array([[4,7,3],[2,8,5],[9,1,6]])
print(n)
#%%
print('数组排序',np.sort(n))
#%%
#按行排序
print(np.sort(n,axis=0))
#%%
#按列排序
print(np.sort(n,axis=1))
#%%
#argsort()排序
x=np.array([9,5,3,4,2,1,6,8])
#排序
y=np.argsort(x) # 返回一个由排序后的元素索引组成的数组y
print(y)
#排序后的重构数组
print(x[y])
#%%
#lexsort()排序
math=np.array([101,109,115,108,118,118]) # 数学成绩

en=np.array([117,105,118,108,98,109]) # 英语成绩

total=np.array([621,623,620,620,615,615]) # 总成绩

#排序
sort_total=np.lexsort((en,math,total)) # 排序的顺序  总-->数学-->英语

print(sort_total) # 排序后的索引值

lst=[  [total[i],math[i],en[i]   ]for i in sort_total]

n=np.array(lst)
print(n)
#%%
