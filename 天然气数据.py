from cProfile import label
from email import header
import pandas as pd
import io

path_fk = 'd:\\github\\python\\fromwork\\'
path_file = 'd:\\github\\file\\'
path_result = 'd:\\github\\result\\'
kkk = pd.read_excel(path_fk + '空白模板.xls' )


haeder = pd.read_excel(path_fk + '潍城区工商户-法人缴费信息.xls',header=1)
df = pd.read_excel(path_file + '潍城区工商户-法人缴费信息.xls',header=1,names=haeder.columns)
kkk = kkk.merge(df.loc[:, ['户号', '用户名','用户类型','用户地址','使用量','缴费金额','缴费时间']], on=['户号', '用户名','用户类型','用户地址','使用量','缴费金额','缴费时间'],how='outer')

haeder = pd.read_excel(path_fk + '潍城区工商户-法人欠费信息.xlsx',header=1)
df = pd.read_excel(path_file + '潍城区工商户-法人欠费信息.xlsx',header=1,names=haeder.columns)
kkk = kkk.merge(df.loc[:, ['户号', '用户名',  '用户地址', '联系电话',  '使用量', '欠费时间', '欠费金额']], on= ['户号', '用户名',  '用户地址', '联系电话',  '使用量', '欠费时间', '欠费金额'],how='outer')


haeder = pd.read_excel(path_fk + '潍城区工商户-法人用气情况.xlsx',header=1)
df = pd.read_excel(path_file + '潍城区工商户-法人用气情况.xlsx',header=1,names=haeder.columns)
kkk = kkk.merge(df.loc[:, ['用户名', '户号', '使用量']], on=['用户名', '户号', '使用量'],how='outer')

haeder = pd.read_excel(path_fk + '潍城区民用户-缴费信息.xls',header=1)
df = pd.read_excel(path_file + '潍城区民用户-缴费信息.xls',header=1,names=haeder.columns)
kkk = kkk.merge(df.loc[:, ['户号', '用户类型', '缴费金额']], on=['户号', '用户类型', '缴费金额'],how='outer')

haeder = pd.read_excel(path_fk + '潍城区民用户-欠费信息.xls',header=1)
df = pd.read_excel(path_file + '潍城区民用户-欠费信息.xls',header=1,names=haeder.columns)
kkk = kkk.merge(df.loc[:, ['户号', '用户名', '用户地址', '联系电话', '使用量', '欠费时间', '欠费金额']], on=['户号', '用户名', '用户地址', '联系电话', '使用量', '欠费时间', '欠费金额'],how='outer')


haeder = pd.read_excel(path_fk + '潍城区民用户-用气情况.xls',header=1)
df = pd.read_excel(path_file + '潍城区民用户-用气情况.xls',header=1,names=haeder.columns)
kkk = kkk.merge(df.loc[:, ['户号', '用户类型', '用户地址', '使用量']], on=['户号', '用户类型', '用户地址', '使用量'],how='outer')


kkk.to_excel(path_result + '天然气副本.xlsx',index=False)