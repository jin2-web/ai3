# 입력받기 '477569040'
'''
number=input("숫자를 입력하세요")
# 입력받은 문자(숫자)를 1개씩 가져다가 '4'
cnt = 0
for i in number :
    # 문자를 숫자로 변경한다. '4'-->4
    nVal=int(i)
    # 홀수인지 판단한다. 5 % 2 == 1
    if nVal % 2 == 1 :
        # 갯수 세기 cnt = cnt + 1
        cnt += 1
print("홀수의 갯수는 %d개입니다"%cnt)
'''
# 10 20 30 40 50 60 70 80 90 100 출력하기 
for k in range(5) :                # k = 0,    1,   2,    3,    4
    for i in range( 1, 6-k, 1) : #    1~5 6,  1~4 5 ,  1~3 4,    1~2 3,  1 2
        print( i, end=" ")
    print()    

for i in range(5) :
    for x in range(1+i,6) :
        print(x, end=' ')
    print()
for j in range(5) :
    k=6-j
    for i in range(1,k) :
        print(i, end=" ")
    print()  





