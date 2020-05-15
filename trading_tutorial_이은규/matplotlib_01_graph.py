import matplotlib.pyplot as plt

x = range(0, 100)
y = [v * v for v in x]

plt.plot(x, y)
plt.show()

plt.plot(x, y, 'ro')
plt.show()

plt.plot(x, y, 'b--')
plt.show()

'''
표 15.1 matplotlib의 주요 색상

문자	색상
b	blue(파란색)
g	green(녹색)
r	red(빨간색)
c	cyan(청록색)
m	magenta(마젠타색)
y	yellow(노란색)
k	black(검은색)
w	white(흰색)

표 15.2 matplotlib의 주요 마커

마커	의미
o	circle(원)
v	triangle_down(역 삼각형)
^	triangle_up(삼각형)
s	square(네모)
+	plus(플러스)
.	point(점)
'''