import pandas as pd


class File:
    file_path = str
    file_name = str
    usecols = list
    sheet_name = [0]
    header = 0
    index_col = 0
    skiprows = []


def New_file(str1, str2):
    s = File()
    s.file_add = str1
    s.file_name = str2
    s.usecols = list
    s.sheet_name = [0]
    s.header = 0
    s.index_col = 0
    s.skiprows = []
    return s


def Read_excel(file):
    dict_data = pd.read_excel(file.file_add + file.file_name, usecols=file.usecols, sheet_name=file.sheet_name,
                              header=file.header, index_col=file.index_col, skiprows=file.skiprows)
    print(file.file_name + '数据读取完成')
    df = dict_data[0]
    return df


def Merge(df1, df2, loc1, loc2):
    df = df1.merge(df2.loc[:, [loc1, loc2]], how='left', on=loc1)
    return df


def Save(df_data, result_path, result_name):  # 保存成EXCEL文件

    df_data.to_excel(result_path + result_name)
    print(result_name + '保存完成')


#################################################################################
file1_path = 'd:\\py123\\'  # 主文件路径
file1_name = '1.xlsx'  # 主文件名称

file2_path = 'd:\\py123\\'  # 副文件路径
file2_name = '123.xlsx'  # 副文件名称


loc1 = '卡口'  # 需要匹配的列
loc2 = '账户'  # 需要合并的列

result_path = ''  # 合并文件保存路径
result_name = ''  # 合并文件名称
#################################################################################

file1 = New_file(file1_path, file1_name)
file2 = New_file(file2_path, file2_name)
df1 = Read_excel(file1)
df2 = Read_excel(file2)

result = Merge(df1, df2, loc1, loc2)
Save(result, result_path, result_name)
print(result)
