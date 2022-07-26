import pandas as pd


def Read_excel(file_name):
    df = pd.read_excel('d:\\github\\file\\' + file_name)
    print(file_name + '读取完成.')
    return df

def Merge(df1, df2):
    df = df1.merge(df2.loc[:, ['户号', '使用量','应收']], how='outer')
    return df

def Save(df,result_name):  
    df.to_excel('d:\\github\\file\\result\\' + result_name)
    print(result_name + '保存完成')
    
def Star(file1_name,file2_name,result_name):
    df1 = Read_excel(file1_name)
    df2 = Read_excel(file2_name)
    result = Merge(df1, df2)
    Save(result, result_name)

def Concat(df1,df2):
    df.concat([df1,df2],ignore_index =True,sort=False)#只合并相同列添加join='inner'参数。




#################################################################################
file1_name = 'a.xls'  # 主文件名称
file2_name = 'b.xls'  # 副文件名称
result_name = '使用情况副本.xlsx'  # 合并文件名称
#################################################################################

# Star(file1_name,file2_name,result_name)
