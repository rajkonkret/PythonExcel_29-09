# pep8
# https://peps.python.org/pep-0008/
# snake_case
import sys  # import biblioteki

print()  # wypisz/wydrukuj
# ctrl alt l - formatowanie kodu

# Process finished with exit code 0 - program działa poprawnie

print("Radek")
# Radek
print('Radek')

# ctrl / - komentowanie
# print("radek')
#   File "C:\Users\cscomarch\PycharmProjects\PythonExcel_29-09\day1\pierwszy.py", line 14
#     print("radek')
#           ^
# SyntaxError: unterminated string literal (detected at line 14)

print('dalsza część programu')
print(type('radek'))  # wypisanie typu danych, <class 'str'>, string, tekstowe

print(type(45))  # <class 'int'>, integer, liczba całkowita
print(sys.int_info)
# sys.int_info(bits_per_digit=30, sizeof_digit=4,
#              default_max_str_digits=4300, str_digits_check_threshold=640)

print("34" + "19")  # 3419, konkatenacja, łączenie stringów
print(34 + 19)  # 53
# print("34" + 19) # TypeError: can only concatenate str (not "int") to str

# liczby zmiennoprzecinkowe
print(4.56)  # 4.56
print(type(4.56))  # <class 'float'>
print(sys.float_info)
# sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021,
#                min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)

print(0.1 + 0.2)  # 0.30000000000000004
print(0.1 + 0.9)  # 1.0

# zmienna - pudełko na dane
# typowanie dynamiczne
zmienna = 90
name = "Radek"
print(type(name))
print(name)
# <class 'str'>
# Radek
name = 90
print(name)  # 90

# hint - podpowiedz dla programisty
name: str = "Radek"
name = 90
print(name)
# 90
# 90

# # rzutowanie - zamiana na właściwy typ danych
a = "1"
b = 0
# print(a + b) 3 TypeError: can only concatenate str (not "int") to str
# int() - rzutowanie na int
print(int(a) + int(b))

# teksty są niemutowalne
tekst = "Witaj Świecie"
print(type(tekst))

tekst.upper()
print(tekst)  # Witaj Świecie
# """ Return a copy of the string converted to uppercase. """
print(tekst.upper())  # WITAJ ŚWIECIE
nowy_tekst = tekst.upper()
print(nowy_tekst)  # WITAJ ŚWIECIE

zmienna1 = "GROSS"
zmienna2 = "groẞ"
print(zmienna1.lower() == zmienna2.lower())  # False
print(zmienna1.casefold() == zmienna2.casefold())  # True

# zmienna logiczna, True, False
print(1 != 0)  # różne, True

name = "Radek"
# f - string, sformatowany tekst
print(f"Nazywam się {name}")  # Nazywam się Radek

a = 4.567
print(f"Liczba: {a}")  # Liczba: 4.567
# ctrl d - duplikacja linii
print(f"Liczba: {a:.2f}")  # Liczba: 4.57

print("liczba:", a)  # liczba: 4.567

# %f - float
print("Liczba: %f" % a)  # Liczba: 4.567000
print("Liczba: %.2f" % a)  # Liczba: 4.57
# print("Liczba: %f" % "Radek") # TypeError: must be real number, not str

print("""
Tekst
    wielolinijkowy
    """)
# "
# Tekst
#     wielolinijkowy"

# komentarz dokumentacyjny
"""Komentarz 
wielolinijkowy"""

print(100 / 3)  # dzielenie, 33.333333333333336
print(100 // 3)  # część całkowita, 33
print(100 % 3)  # reszta z dzielenia, 1
print(10 % 3)  # reszta 1, modulo

zysk = 890123456654
print(f"Nasza duża liczba: {zysk:,}")  # Nasza duża liczba: 890,123,456,654
print(f"Nasza duża liczba: {zysk:_}")  # Nasza duża liczba: 890_123_456_654
print(f"Nasza duża liczba: {zysk:_}".replace("_", " "))  # Nasza duża liczba: 890 123 456 654

liczba = 15_000_000_000
print(liczba)
print(type(liczba))  # <class 'int'>
