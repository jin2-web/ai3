# 20 22 24 26 ... 50 출력하기
cnt=0
sum=0
for i in range(20, 51, 2) :
    print( i, end=" ")
    cnt = cnt + 1
    sum = sum + i
print()  
print("20~50까지의 2개씩 증가 숫자 갯수 %d"%cnt)
print("20~50까지의 2개씩 증가 숫자의 합계 %d"%sum)

# 100 95 90 ... 0 출력하기
cnt=0
sum=0
for i in range( 100, -1, -5) :
    print(i, end=" ")
    cnt += 1
    sum += i
print()
print("100~0까지의 -5개씩 감소 숫자 갯수 %d"%cnt)
print("100~0까지의 -5개씩 감소 숫자의 합계 %d"%sum)
print("100~0까지의 -5개씩 감소 숫자의 평균 %d"%int(sum//cnt))

# 1~100까지 숫자의 합을 구하되 400이 넘으면 멈추기 
# 1단계 1~100까지 합 구하기
sum=0
for i in range(1, 101, 1) :
    if sum >= 400 :
        print("합계가 400넘는 순간 i값은 %d"%i)
        break 
    sum += i
print("1~100까지 합에서 400이 넘는 순간까지 합은 %d"%sum) 

# 200~500까지 3개 증가하는 수를 출력하기
# 갯수가 20개일때 멈추기 
cnt = 0
for i in range( 200, 501, 3) :
    print( i, end=" ")
    cnt += 1
    if cnt == 20 :
        break
print()
print( "20개일 때 i값 %d"%i)

# 5~500까지 5의 배수를 출력하기
# 합계가 1000이상이거나 갯수가 30개 이상면 멈추기
#
cnt=0
sum=0 
for i in range(5, 501, 5) :
    print( i , end=" ")
    cnt += 1
    sum += i
    if sum >= 1000 or cnt >= 30 :
        break
print()
print("합계가 1000이상이거나 갯수가 30개 이상일때 멈추기 멈춘값 : %d %d %d "%(i, cnt, sum) )    
