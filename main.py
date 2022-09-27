import pandas as pd
from pandas import DatetimeIndex

df = pd.read_csv('temp_fuhlsbuettel_akt.txt', sep=';')
df = df[df.columns.difference(['eor'])]
print(df)

# d) column 'TT_TU' to Series
r = df[['TT_TU']]
my_series = r.squeeze()
# my_series = r.transpose()[0]

# e)
dt_range = pd.date_range(start='2016-03-22 00:00:00', end=' 2017-09-22 23:00:00', freq='60T')

# f)
my_series.index = dt_range
print(my_series)


# print(df[[dt_range, my_series]])
