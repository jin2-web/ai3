def hello() :
    print('hello') 

for i in range(20) :
#    print('hello')    
   hello()

# 1~100까지 합계 구하기 함수 정의하기
def uSum() : 
    sum=0
    for i in range(1,101) :
        sum += i
    print(sum)

def uSum1( uStart, uEnd   ) : 
    sum=0
    for i in range(uStart,uEnd + 1) :
        sum += i
    print(sum)

def hPrint() :
    print('-'*50)

def ifSum(n) :
    sum=0
    for i in range(1,101) :
        if sum >= n :
            break
        sum = sum + i
    print( '%d이상일때 항목의 %d값  합계 %d' %(n, i, sum))

# 만들어진 함수를 사용하는 쪽-비지니스로직
hPrint()
uSum() # 함수호출
# 합계 3000 넘는 순간 멈추고 합계, i값 출력하기 
ifSum(3000)
hPrint()
# 합계 4000 넘는 순간 멈추고 합계, i값 출력하기 
ifSum(4000)
uSum() # 함수호출
hPrint()
# 요구사항 입력 2개 받는다 
# 시작수? 50
# 끝수? 200
# 50~200까지 합을 출력하기 
start = int(input('시작수?'))
end = int(input('끝수?'))
uSum1( start, end )





