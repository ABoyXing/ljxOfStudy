#
#
# #%%
# # 帮我连接上这个mysql数据库：mysql://134.96.217.59:3333/db_iptv_10 username=huaxin password=Hxpti@123
# import pymysql
# conn = pymysql.connect(host='134.96.217.59', port=3333, user='huaxin', password='Hxpti@123', db='db_iptv_10')
# cursor = conn.cursor()
# # cursor.execute('select * FROM db_iptv_10.zwgd_gz_repeat_list_m_not_pre limit 100')
# # for row in cursor.fetchall():
# #     print(row)
#
# #%%
# # 帮我读取位于D盘的全量标准组织信息_2040808_原版.xlsx文件，并打印前100行
#
# import openpyxl
# import pandas as pd
# df = pd.read_excel('D:/全量标准组织信息_2040808_原版.xlsx')
# print(df.head(100))
#
# #%%
# # 综合上述的内容，帮我读取位于D盘的全量标准组织信息_2040808_原版.xlsx文件，同时将结果保存到myslq的db_iptv_10.org_info_full_std_2040808_test表中
# # 表结构:
# # CREATE TABLE `org_info_full_std_2040808_test` (
# #   `org_id` varchar(255) CHARACTER SET utf8 DEFAULT NULL COMMENT '组织ID',
# #   `org_name` varchar(255) CHARACTER SET utf8 DEFAULT NULL COMMENT '组织名称',
# #   `org_abbreviation` varchar(255) CHARACTER SET utf8 DEFAULT NULL COMMENT '组织简称',
# #   `parent_org_id` varchar(255) CHARACTER SET utf8 DEFAULT NULL COMMENT '父级组织ID',
# #   `parent_org_name` varchar(255) CHARACTER SET utf8 DEFAULT NULL COMMENT '父级组织名称',
# #   `org_order` varchar(255) CHARACTER SET utf8 DEFAULT NULL COMMENT '组织排序',
# #   `area_code` varchar(255) CHARACTER SET utf8 DEFAULT NULL COMMENT '区号',
# #   `area_code_name` varchar(255) CHARACTER SET utf8 DEFAULT NULL COMMENT '区号名称',
# #   `admin_area_code` varchar(255) CHARACTER SET utf8 DEFAULT NULL COMMENT '行政管理区域编码',
# #   `admin_area_name` varchar(255) CHARACTER SET utf8 DEFAULT NULL COMMENT '行政管理区域',
# #   `region_level_code` varchar(255) CHARACTER SET utf8 DEFAULT NULL COMMENT '区域层级编码',
# #   `region_level` varchar(255) CHARACTER SET utf8 DEFAULT NULL COMMENT '区域层级',
# #   `region_name` varchar(255) CHARACTER SET utf8 DEFAULT NULL COMMENT '区域名称',
# #   `org_id_path` varchar(255) CHARACTER SET utf8 DEFAULT NULL COMMENT '组织ID全路径',
# #   `org_name_path` varchar(255) CHARACTER SET utf8 DEFAULT NULL COMMENT '组织名称全路径',
# #   `branch_type_code` varchar(255) CHARACTER SET utf8 DEFAULT NULL COMMENT '支局类型编码',
# #   `branch_type` varchar(255) CHARACTER SET utf8 DEFAULT NULL COMMENT '支局类型',
# #   `branch_type_name` varchar(255) CHARACTER SET utf8 DEFAULT NULL COMMENT '支局类型名称',
# #   `Column19` varchar(50) DEFAULT NULL,
# #   `Column20` varchar(50) DEFAULT NULL
# # ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
# import openpyxl
# import pandas as pd
# df = pd.read_excel('D:/全量标准组织信息_2040808_原版.xlsx')
# for index, row in df.iterrows():
#     cursor.execute( )
#     )
