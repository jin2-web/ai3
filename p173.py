# 1~200 출력하기
# for문
for i in range(1,201, 1) :
    if i==100 :
        continue
    print( i, end=" ")
print()
print("-" * 100)    
# while문  
i=1
while i<200 :
    i = i+1 
    if i==100 :
        continue
    print( i, end=" ")
    
# 100이면 빠지기 
# 100이면 찍지 않고 건너 뛰기(반복문 계속) 101 찍기 