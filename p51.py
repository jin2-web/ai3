# a,b에 각각 5,7을 할당하고
a, b = 5, 7
# 곱셉을 한 값을 변수 result에 저장하여
result = a * b
# 출력하는 프로그램
print( result )

# 2
portion = 12345 // 789
the_rest = 12345 % 789
print( '몫 : ', portion, '나머지 : ', the_rest )

# 3
#  x, y에 각각 11, 22를 할당하고
x, y = 11, 22
z = x
x = y
y = z
print("x=", x, "y=", y)


# 3-1 파이썬에서 변수 값 교환하기
x, y = 100,200
x, y = y, x
print("x=", x, "y=", y)

# 4
r=7 # 반지름 
# 원넓이 구하기 반지름*반지름*3.14
area = r*r*3.14
print( r, '의 반지름의 원넓이는 ', area)
