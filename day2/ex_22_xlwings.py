# xlwings  - praca z plikami excel, wymaga excela !!!

import xlwings as xw
import pandas as pd
import numpy as np

df = pd.DataFrame(data=np.random.randn(100, 5),
                  columns=[f'Próba {i}' for i in range(1, 6)])

print(df)
print(df.head()) # 5 pierwszych
print(df.tail()) # 5 ostatnich

xw.view(df)