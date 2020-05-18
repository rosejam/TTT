from pandas import Series, DataFrame

daeshin = {'open':  [11650, 11100, 11200, 11100, 11000],
           'high':  [12100, 11800, 11200, 11100, 11150],
           'low':  [11600, 11050, 10900, 10950, 10900],
           'close': [11900, 11600, 11000, 11100, 11050]}

daeshin_day = DataFrame(daeshin)
print(daeshin_day)

daeshin_day = DataFrame(daeshin, columns=['open', 'high', 'low', 'close'])

date = ['16.02.29', '16.02.26', '16.02.25', '16.02.24', '16.02.23']
daeshin_day = DataFrame(
    daeshin, columns=['open', 'high', 'low', 'close'], index=date)

day_data = daeshin_day.loc['16.02.24']
print(day_data)
print(type(day_data))

print(daeshin_day.columns)
print(daeshin_day.index)
