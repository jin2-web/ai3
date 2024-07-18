# 구구단 만들기
# for i in range(1,10) :
#     for j in range(2,10) :
#         print("%2dX%2d=%2d"%(j, i, j*i), end=" ")
#     print()

# print("-"*50)    

# for i in range(2,10) :
#     for j in range(1,10) :
#         print("%2dX%2d=%2d"%(i, j, j*i), end=" ")
#     print()

# 소수구하기 
# 소수는 1과 자기 자신외에는 나누어 떨어지지 않는 수 
# 2 - 소수 4 - 소수가 아니다
# 179쪽 3번 문제
# 30 소수 2 나누어 보기 반복문 빠지기
# 31 소수 2 3 4 ... ... 30 31-1까지 나누어 보세요 31 == 30+1 소수다 
# 32 소수 2 
# 37 소수다 2 3 ... 36 나누어 보기 37 == 36+1 소수다

# 교재 있는 문제로 변형해서 풀기
# start=int( input("시작 수를 입력해 주세요") )
# end = int( input("끝 수를 입력해 주세요 "))
# for x in range( start, end+1) :
#     for i in range(2, x) :
#         if x % i == 0 :
#             break
#         if x == i+1 :
#             print("%d "%x, end=" ")
# x=start
# i=2
# flag=True
# while x < end :
#     i=2
#     while i < x :
#         if x % i == 0 :
#            flag==False
#            break  
#         i = i + 1   
#     if flag==False :
#         break
#     if x == i + 1 :
#         print("%d "%x, end=" ")
#     x = x + 1  

s = int(input('시작 : '))
e = int(input('끝 : '))
for i in range(s,e+1)  :
    if i%2!=0 and i%3 !=0 and i%5 != 0 and i%7 != 0 :
        print(i,end=' ')
        print("git study") 
