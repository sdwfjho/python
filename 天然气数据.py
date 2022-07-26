import pandas as pd
import os


# def readname():
#     name = os.listdir(path)
#     return name


# def merge():
#     path = 'd:\\github\\file\\'

#     names = os.listdir(path)

#     i = len(names)
#     for name in names:
#         df = pd.read_excel(path + name)
#         dfs = df.merge(dfs, df)
#         print('共', i, '已完成', index)
#     df = pd.concat(mc.df_list, ignore_index=True, sort=False, join='outer')
#     print('文件正在保存.....')
#     df1 = pd.read_excel(path + file1_name)
#     df2 = pd.read_excel(path + file2_name)
#     # df = df1.merge(df2.loc[:, ['用户号', '用户地址', '抄表时间','气量']], on='用户号',how='outer')
#     df = pd.merge(df1, df2, on='用户号', how='outer')
#     save(df, mc)


# def save(df, mc):
#     df.to_excel(mc.result_path + mc.result_name, index=False)
#     print('文件 ', mc.result_name + ' 保存完成')


# #########################  merge  ###############################################

# mc = Mc()
# mc.file1_name = '潍城区民用户-缴费信息.xls'
# mc.file2_name = '潍城区民用户-用气情况.xls'
# mc.file3_name = '潍城区民用户-欠费信息.xls'
# mc.join_list = [['用户号', '用户地址', '抄表时间', '气量'], 'outer']  # 合并列表参数
# mc.result_name = '潍城区.xlsx'  # 合并文件名称
# mc.result_path = 'd:\\github\\result\\'  # 合并文件保存路径

# ########################  concat  ###############################################

# mc.file_path = 'd:\\github\\file\\'  # 读取文件路径

# #################################################################################

path = 'd:\\github\\气\\'

names = os.listdir(path)

i = len(names)
dfs = pd.read_excel('d:\\github\\模板\\气.xls')
for name in names:
    if name == '潍城区民用户-缴费信息.xls':
        df = pd.read_excel(path + name,header=1,names=['户号','用户类型','缴费金额'])
        dfs = df.merge(dfs, df, on=['户号','用户类型','缴费金额'])
    elif name == '潍城区民用户-用气情况.xls':
        df = pd.read_excel(path + name,header=1,names=['户号','用户类型','用户地址','缴费时间','a','b','使用量'])
        dfs = df.merge(dfs, df, on=['户号','用户类型','用户地址','缴费时间','使用量'])
    elif name == '潍城区民用户-欠费信息.xls':
        df = pd.read_excel(path + name,header=1,names=['户号','法人单位名称（姓名）','用户地址','联系电话','i','使用量', '欠费时间','欠费金额'])
        dfs = df.merge(dfs, df, on=['户号','法人单位名称（姓名）','用户地址','联系电话','i','使用量', '欠费时间','欠费金额'])
    elif name == '潍城区工商户-法人缴费信息.xls':
        df = pd.read_excel(path + name, header=1, names=[
                           '序号', '抄表区名', '户号', '法人单位名称（姓名）', '用户类型', '用户地址', '使用量', '缴费金额', '缴费时间', '销帐金额（元）'])
        dfs = df.merge(dfs, df, on=[
                       '户号', '法人单位名称（姓名）', '用户类型', '用户地址', '使用量', '缴费金额', '缴费时间'])
    elif name == '潍城区工商户-法人欠费信息.xlsx':
        df = pd.read_excel(
            path + name, header=1, names=['户号', '法人单位名称（姓名）','用户状态', '用户地址', '联系电话', '最后抄表截止数','使用量', '欠费时间', '欠费金额','违约金额','总欠费金额'])
        dfs = df.merge(dfs, df, on=['户号', '法人单位名称（姓名）', '用户地址', '联系电话', '使用量', '欠费时间', '欠费金额'])
    elif name == '潍城区工商户-法人用气情况.xlsx':
        df = pd.read_excel(path + name, header=1,
                           names=['法人单位名称（姓名）', '户号','用户状态','区域','用气性质', '使用量'])
        dfs = df.merge(dfs, df, on=['法人单位名称（姓名）', '户号', '使用量'])
    else:
        dfs.to_excel('d:\\github\\result\\气汇总.xlsx',index=False)
        break
