#%%
# 保存成Excel文件
import pandas as pd
df=pd.DataFrame(
{
    '编号':['1001','1002','1003'],
    '姓名':['张三','李四','王五']
})
df.to_excel(r'C:\Users\厉佳星\Desktop\数据导出-学生信息.xlsx',index=False,sheet_name='学生信息表') #index=False不导出索引
#%%
#导出到多个Sheet中
import pandas as pd
df=pd.DataFrame(
{
    '编号':['1001','1002','1003'],
    '姓名':['张三','李四','王五'],
    '总成绩':[740,658,543]
})
# 打开一个Excel文件
work=pd.ExcelWriter(r'C:\Users\厉佳星\Desktop\数据导出-多sheet.xlsx')

df.to_excel(work,sheet_name='学生成绩信息',index=False)  # 导出到名称为"学生成绩信息"的sheet页

df[['姓名','总成绩']].to_excel(work,sheet_name='成绩表',index=False)

# pandas2.0保存工作薄
work._save()
#%%
# 导出到csv文件中
import pandas as pd
df=pd.DataFrame(
{
    '编号':['1001','1002','1003'],
    '姓名':['张三','李四','王五'],
    '总成绩':[740.98,658.56,543.46]
})
df
df.to_csv('学生成绩.csv',index=False,columns=['姓名','总成绩'],float_format='%.1f')
#%%
