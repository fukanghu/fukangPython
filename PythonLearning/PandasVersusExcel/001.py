# 如何使用pandas创建excel文件于文件夹

import pandas as pd

df = pd.DataFrame({'ID':[1, 2, 3, 4], 'Name':['Tim', 'Victor', 'Nick', 'Fukang']})
df = df.set_index('ID')

df.to_excel('C:/Users/fukan/Desktop/output.xlsx')
print("Done!")