import pyexcel

# pip install pyexcel pyexcel-xlsx

data = [
    ["Imię", "Wiek"],
    ["Tomek", 38],
    ["Kasia", 38],
]
sheet = pyexcel.Sheet(data)
sheet.save_as('wyniki.xlsx')

# wczytanie
sheet = pyexcel.get_sheet(file_name="wyniki.xlsx")
print(sheet)

# pip install pyexcel-csv
# konwersja plikow: xlsx na csv
pyexcel.save_as(file_name="wyniki.xlsx",
                dest_file_name="wyniki.csv")