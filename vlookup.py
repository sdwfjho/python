import pandas as pd
import os


class Mc:
    file1_name = ''  # 主文件名称
    file2_name = ''  # 副文件名称
    join_list = []  # 合并列表参数
    result_name = ''  # 合并文件名称
    result_path = ''
    file_path = ''


def readname(mc):
    name = os.listdir(mc.file_path)
    return name


def merge(mc):
    df1 = pd.read_excel(mc.file_path + mc.file1_name)
    df2 = pd.read_excel(mc.file_path + mc.file2_name)
    df = df1.merge(df2.loc[:, ['用户号', '用户地址', '抄表时间','气量']], on='用户号',how='outer')
    # df = pd.merge(df1,df2)
    save(df, mc)


def save(df, mc):
    df.to_excel(mc.result_path + mc.result_name,index=False)
    print('文件 ',mc.result_name + ' 保存完成')


def concat(mc):
    index = 0
    names = readname(mc)
    i = len(names)
    for name in names:
        mc.df_list.append(pd.read_excel(mc.file_path + name))
        index += 1
        print('共', i, '已完成', index)
    df = pd.concat(mc.df_list, ignore_index=True, sort=False, join='outer')
    print('文件正在保存.....')
    save(df, mc)


#########################  merge  ###############################################

mc = Mc()
mc.df_list = []   # df数组
mc.file1_name = '潍城区民用户-缴费信息.xls'  # 主文件名称
mc.file2_name = '潍城区民用户-用气情况.xls'  # 副文件名称
mc.join_list = [['用户号', '用户地址', '抄表时间','气量'], 'outer']  # 合并列表参数
mc.result_name = '使用情况副本.xlsx'  # 合并文件名称
mc.result_path = 'd:\\github\\result\\' # 合并文件保存路径

########################  concat  ###############################################

mc.file_path = 'd:\\github\\file\\'  #读取文件路径

#################################################################################

# concat(mc)
merge(mc)