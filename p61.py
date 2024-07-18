score=80
print('성적'+str(score))

x='토끼'*10
print(x)

n=100*10 
print(n)

n100 = '100'*20
print(n100)

# 200숫자를 15번 반복해서 출력하기
n200 = 200
print( str(n200) * 15 )

# 64쪽 퀴즈
# 1
x='수학성적:'
print( type(x) ) 
y=80
print(type(y)) 
z = x + str(y) 
print( type(z) )

# 2번 교재 코드 실행해 보세요
date = "20220301"
year = date[0:4]
month = date[4:6]
day = date[6:]
date2 = year + "-" + month + "-" + day
print( date2 )

print(len(date))

# 자기이름 핸드폰번호 마지막자리의 갯수 반복하기 
# 정현희정현희정현희정현희 


'''
if len(phone1) == 15 :
   print( 'phone1은 한국 핸드폰번호입니다' )  
else :
   print( 'phone1은 한국 집번호입니다' )  

if len(phone2) == 15 :
   print( 'phone2은 한국 핸드폰번호입니다' )  
else :
   print( 'phone2은 한국 집번호입니다' ) 
'''
# 조건은 15글자이면 아니면 
# 결과
# phone1은 한국 핸드폰번호입니다
# 결과
# phone2은 한국 집번호입니다. 

# 힌트 글자길이 구하는 함수 len()
phone1 = '82-02-123-4567'
#15글자이면 한국 핸드폰번호
phone2 = '82-10-8744-3334'
#15글자 아니면 한국 집번호
if len(phone1) == 15 and len(phone2) == 15 :
    print( 'phone1은 핸드폰번호입니다')
    print( 'phone2는 핸드폰번호입니다.')
elif  len(phone1) == 15 and len(phone2) == 14 :   
    print( 'phone1은 핸드폰번호입니다')
    print( 'phone2는 집번호입니다.')
elif  len(phone1) == 14 and len(phone2) == 15 :   
    print( 'phone1은 집번호입니다')
    print( 'phone2는 핸드폰번호입니다.')
elif  len(phone1) == 14 and len(phone2) == 14 :   
    print( 'phone1은 집번호입니다')
    print( 'phone2는 집번호입니다.')
