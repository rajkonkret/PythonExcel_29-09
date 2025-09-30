import time
import numpy as np

lista = list(range(15_000_000))
lista_np = np.arange(15_000_000, dtype=np.int64)


# deklaracja funkcja
def sum_python():
    total = 0
    for i in lista:
        total += i
    print("Sum is:", total)


def sum_np():
    total = np.sum(lista_np)
    print("sum is:", total)


# funkcję musimy wywołac
start_d = time.time()
sum_python()
end_d = time.time()
print(end_d - start_d)

start_d = time.time()
sum_np()
end_d = time.time()
print(end_d - start_d)
# Sum is: 112499992500000
# 0.4727780818939209
# sum is: 112499992500000
# 0.00735783576965332
# https://pola.rs/
