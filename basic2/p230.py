animals = ('토끼','거북이','사자','여우')
print(animals)

numbers  = tuple(range(10))
print(numbers)

# 출력하기
print( animals[0] )
print( numbers[:3] )

# 수정하기
# animals[2] = '호랑이' 안됨

anNu = animals + numbers 
print(anNu)

# for문
s = 0
n2 = tuple(range(101)) 
for i in n2 :
   s += i 
print( s  )
print( sum(n2 ) )   


