# for x in range(5) :
#     print(x)
#     print("Hello")
# print("반복문 바깥")    

# 형식 range(초기값, 최종값-1, 증가값) 초기값(기본은 0)과 증가값(기본은 1)은 생략가능  
sum = 0
for i in range(0,11,2) : 
    sum = sum + i
    print("i의 값 : %d=>합계: %d"%(i, sum))  

for i in range(10):
    print(i, end=" ")
print()
# 149
# 5 10 15 20 ... 100
cnt = 0 # 갯수세기 
for i in range( 5, 101, 5 ) :
    print( i, end=" ")
    cnt = cnt + 1
print()    
print("갯수는 %d"%cnt)    
# 4 8 12 16 ... 200
print()
cnt = 0
for i in range( 4, 201, 4 ) :
    print( i, end=" ")
    cnt = cnt + 1
print()    
print("갯수는 %d"%cnt)    
# 200 150 100 50 0 -50 -100 -150 -200
print()
cnt = 0
for i in range( 200, -201,-50 ) :
    print( i, end=" ")    
    cnt = cnt + 1
print("갯수는 : %d"%cnt)     