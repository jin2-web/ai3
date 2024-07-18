s = "안녕하세요. 반갑습니다."
print(s)
print( s[0] + s[1] )
print( s[ 0 : 2 ])
print( s[ 7 : 10 ]) 

jumin="991013-3201253"
# 99년 10월 13일
sex= jumin[7]
print( sex )
# 1, 3인경우 남자 출력 2, 4인 경우 여자 출력
if sex=='1' or sex=='3' :
    print('남자')
else :
    print('여자')
# 주민번호 제일 마지막 부분에 짝수이면 '맞는 주민번호'출력
# 홀수이면 '틀린 주민번호'출력     
# 1단계 주민번호 제일 마지막 부분을 가지고 온다
end = jumin[-1] # 또는 jumin[13]
print( end )
# 2단계 '6'을 연산하기 위해서 숫자 6으로 형변환
endInt = int(end) #'6' --> 6
# 3단계 조건문 주민번호 오류 검출하기
if endInt % 2 == 0 : 
    print('맞는 주민번호')
else :
    print('틀린 주민번호')    
     