def func(c) :
    x = c + 5
    return x

r = func(100)
print(r) # 105
#함수정의
def inchToCm(inch) :
    cm = []
    for i in range(inch, 31, 10) : # 10 20 30 
        k = i * 2.54
        cm.append(k)
    return cm

# 함수 호출
result = inchToCm(10) # 25.4   50.8   76.2
print(result)

# 
def p(n) :
   result = [] 
   answer = 1 
   for i in range(n, 0, -1) :
       answer = answer * i
   result.append(answer)
   answer = 0
   for i in range(1, n+1 ) :
       answer = answer + i
   result.append(answer)    
   answer = 0
   for i in range(1, n+1 ) :
       answer = answer + 1
   result.append(answer)  
   return result    

print( p(5) ) # 결과 120 5*4*3*2*1 
# 결과 5!결과 ==> 120, 1~5까지 합 ==> 15, 1~5까지 길이 ==>  5
def p(x) :
    a = 1
    b = 0
    cnt=0
    for i in range (x,0,-1) :
        a = a * i
        b += i
        cnt+=1
    list1 = [a,b,cnt]
    return list1

print(p(5))
        

