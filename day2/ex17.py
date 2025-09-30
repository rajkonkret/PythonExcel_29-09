import pandas as pd

df = pd.read_excel("excel_with_multiple_sheets.xlsx", sheet_name=2)  # indeks 2, marks
print("the dataframe is:")
print(df)
# the dataframe is:
#      Name  Marks
# 0  Aditya    179
# 1  Sammer    180
# 2  Darwin    170
# 3    Anna    167

df = pd.read_excel("excel_with_multiple_sheets.xlsx", sheet_name="marks")  # indeks 2, marks
print("the dataframe is:")
print(df)
#      Name  Marks
# 0  Aditya    179
# 1  Sammer    180
# 2  Darwin    170
# 3    Anna    167

dane = pd.ExcelFile("excel_with_multiple_sheets.xlsx")
print(dane.sheet_names)  # ['height', 'weight', 'marks']

df = pd.read_excel("excel_with_multiple_sheets.xlsx", sheet_name=dane.sheet_names[0])
print("the dataframe is:")
print(df)
# the dataframe is:
#      Name  Height
# 0  Aditya     179
# 1  Sammer     180
# 2  Darwin     170
# 3    Anna     167

# wczytanie konkretnej kolumny
# usecols=['Name'] - kolumny, które chcemy wczytać
df = pd.read_excel("excel_with_multiple_sheets.xlsx", sheet_name="marks", usecols=['Name'])
print("the dataframe is:")
print(df)
# the dataframe is:
#      Name
# 0  Aditya
# 1  Sammer
# 2  Darwin
# 3    Anna
