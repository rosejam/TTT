from pandas import Series

# Series 객체: 값과 각 값에 연결된 인덱스값 저장
kakao = Series([92600, 92400, 92100, 94300, 92300])
print(kakao)
print(kakao[0])

# 인덱스값을 문자열로 지정
kakao2 = Series([92600, 92400, 92100, 94300, 92300], index=['2016-02-19',
                                                            '2016-02-18',
                                                            '2016-02-17',
                                                            '2016-02-16',
                                                            '2016-02-15'])
print(kakao2)
print(kakao2['2016-02-19'])

# 인덱스만 출력
print(kakao2.index)
for date in kakao2.index:
    print(date)

# 값만 출력
print(kakao2.values)
for ending_price in kakao2.values:
    print(ending_price)

# Series 덧셈
mine   = Series([10, 20, 30], index=['naver', 'sk', 'kt'])
friend = Series([10, 30, 20], index=['kt', 'naver', 'sk'])
merge = mine + friend   # 인덱싱이 같은 값끼리 덧셈 연산을 수행
print(merge)