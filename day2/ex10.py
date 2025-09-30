# pandas - biblioteka do przetwarzania danych
import pandas as pd  # alias

# pip list - lista zainstalowanych bibliotek
# pip install pandas

# tworzymy tabelki w pamięci
writer = pd.ExcelWriter('empty_excel.xlsx')
empty_dataframe = pd.DataFrame()  # tablice/macierze w pandas

# zapisanie ddanych do pliku excel
empty_dataframe.to_excel(writer, sheet_name='empty')
writer.close()  # jak uzywamy excelwriter musimy uzyc close()
