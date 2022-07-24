import pandas as pd


class File:                            
    file_add = str
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
    print('=====' + file.file_name + '数据读取完成.=====')
    df = dict_data[0]
    return df

def Merge(df1,df2,loc1,loc2):
    df = df1.merge( df2.loc[:, [loc1,loc2]], how='left', on=loc1)
    return df

def Save(df_data,path):                #保存成EXCEL文件
    df_data.to_excel(path)
    print('\n文件保存完成。')
#################################################################################
file1_add = 'd:\\py123\\'
file1_name = '1.xlsx'

file2_add = 'd:\\py123\\'
file2_name = '123.xlsx'


loc1='卡口'
loc2='账户'
#################################################################################

file1 = New_file(file1_add, file1_name)
file2 = New_file(file2_add, file2_name)
df1 = Read_excel(file1)
df2 = Read_excel(file2)

result = Merge(df1,df2,loc1,loc2)
Save(result,'d:\\py123\\111.xlsx')
print(result)
