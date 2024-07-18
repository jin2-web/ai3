'''name = input("이름은")
print( name )

age = input("당신의 나이는?")
print( "당신의 나이는 %s살입니다"%age)
print( "당신의 나이는 %d살입니다"%int(age))

birthYear = input("당신이 태어난 년도는?")
age = 2024-int(birthYear)
print("당신의 나이는 %d살입니다."%age)
'''
# 73page quiz 풀기
a=int(input('첫번째 정수를 입력하세요 : '))
b=int(input('두번째 정수를 입력하세요 :'))
c=int(input('세번째 정수를 입력하세요 :'))

if a>b and a > c :
    print( a )
elif b>a and b>c :
    print(b)
elif c>a and c>b :
    print(c)     
       