import pandas as pd

df = pd.read_excel('d:\\github\\file\\潍城区工商户-法人缴费信息.xls', header=1,names=['a','b','c','d'])
print(df)