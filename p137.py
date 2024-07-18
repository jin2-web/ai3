# number = input("수를 입력하세요 :") # '9' --> 9
# inputLength = len(number)
# number = int(number)
# if not(0<=number<=999) :  
#     print("오류! %s는 범위 0~999 이외의 숫자이다")
# elif inputLength == 1 :
#     print("%s은(는) 한자리 숫자이다")
# elif  inputLength == 2 :
#     print("%s은(는) 두자리 숫자이다")   
# elif  inputLength == 3 :
#     print("%s은(는) 세자리 숫자이다")     

# 137page E3-8 문제
# number1 = int( input("첫번째 숫자를 입력하세요"))
# number2 = int( input("두번째 숫자를 입력하세요"))
# print("원하는 연산은?")
# operater = input("+, -, *, / 중 하나를 선택하세요 : ")
# if not(operater == '+' or operater == '-' or operater == '*' or operater == '/') :
#     print("선택 오류!")
# elif operater=="+" :
#     print( "%d + %d = %d"%(number1, number2, number1+number2))
# elif operater=="-" :
#     print( "%d - %d = %d"%(number1, number2, number1-number2))
# elif operater=="*" :
#     print( "%d * %d = %d"%(number1, number2, number1*number2))
# elif operater=="/" :
#     print( "%d / %d = %d"%(number1, number2, number1/number2))
       
# S3-2
hour1 = int( input("첫번째 시간의 시를 입력하세요"))
minute1 = int( input("첫번째 시간의 분를 입력하세요"))
hour2 = int( input("두번째 시간의 시를 입력하세요"))
minute2 = int( input("두번째 시간의 분를 입력하세요"))

# 잘못 입력한 부분을 오류검출
# 조건문 
if not( 0<=hour1<=24 and 0<=hour2<=24 and 0<=minute1<=59 and 0<=minute2<=59 ) :
   print("시간과 분을 잘못입력하셨어요")
elif hour1 < hour2 :
    print( "빠른 시간 : %d:%d"%(hour1, minute1) )
    print("느린 시간 :%d:%d"%(hour2, minute2) ) 
elif  hour1 == hour2 and minute1 < minute2  :
    print( "빠른 시간 : %d:%d"%(hour1, minute1) )
    print("느린 시간 :%d:%d"%(hour2, minute2) ) 
elif hour1 == hour2 and minute1 > minute2 :
    print( "빠른 시간 : %d:%d"%(hour2, minute2) )
    print("느린 시간 :%d:%d"%(hour1, minute1) ) 
else :
    print( "빠른 시간 : %d:%d"%(hour2, minute2) )
    print("느린 시간 :%d:%d"%(hour1, minute1) )     






