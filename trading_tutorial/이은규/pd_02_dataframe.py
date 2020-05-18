from pandas import Series, DataFrame

# colX: 키값
# 각 키는 리스트 타입의 값을 가짐
# DataFrame 객체는 'col0', 'col1', 'col2'라는 세 개의 Series 객체로 구성됨(인덱스는 서로 동일)
raw_data = {'col0': [1, 2, 3, 4],
            'col1': [10, 20, 30, 40],
            'col2': [100, 200, 300, 400]}

data = DataFrame(raw_data)
print(data)
print(data['col0'])

daeshin = {'open':  [11650, 11100, 11200, 11100, 11000],
           'high':  [12100, 11800, 11200, 11100, 11150],
           'low' :  [11600, 11050, 10900, 10950, 10900],
           'close': [11900, 11600, 11000, 11100, 11050]}

daeshin_day = DataFrame(daeshin)
print(daeshin_day)

daeshin_day = DataFrame(daeshin, columns=['open', 'close', 'high', 'low'])  # DataFrame 객체 생성할 때 컬럼 순서 지정 가능
print(daeshin_day)

date = ['16.02.29', '16.02.26', '16.02.25', '16.02.24', '16.02.23']
daeshin_day = DataFrame(daeshin, columns=['open', 'high', 'low', 'close'], index=date)  # 인덱스도 지정 가능
print(daeshin_day)

close = daeshin_day['close']    # DF[키값(컬럼)]
print(close)

day_data = daeshin_day.loc['16.02.24']  # DF.loc[인덱스값(로우)]
print(day_data)
print(type(day_data))

print(daeshin_day.columns)
print(daeshin_day.index)