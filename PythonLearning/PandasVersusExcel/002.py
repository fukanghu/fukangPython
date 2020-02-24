import pandas as pd

people = pd.read_excel('C:/Users/fukan/PycharmProjects/fukangPython/PandasVersusExcel/002/People.xlsx', header=1)
print(people.shape)
print(people.columns)
print(people.head(3))
print("*"*30)
print(people.tail(3))
print("*"*30)


# people = pd.read_excel('C:/Users/fukan/PycharmProjects/fukangPython/PandasVersusExcel/002/People.xlsx', header=None)
# people.columns = ['ID', 'Type', 'FirstName', 'MiddleName', 'LastName']
# print(people.columns)
# people.to_excel('C:/Users/fukan/PycharmProjects/fukangPython/PandasVersusExcel/002/output.xlsx')
# print('Done:')