# 정렬
data = [12,8,15,32,-3,-20,15,34,6]
print(data)
data.sort()
print(data)

data2 = ['a', '가', '@','1','ac']
print(data2)
data2.sort() #오름차순 정렬 유니코드 순서대로 정렬된다.
print(data2)
# 내림차순 정렬 하기
data2.sort(reverse=True)
print(data2)
# 오름차순 정렬 하기
data2.sort(reverse=False)
print(data2)

# 205
string1 = ["사과는 맛있다. 나는 사과를 제일 좋아한다"]
print(string1)

x = string1[0].replace("사과", "딸기", -1)
string1 = [x]
print(string1)

# 207 split() 문자열 쪼개기
hello = 'have-a-nice-day'
print(hello)

list1 = hello.split(" ")
print(list1)
print(type(list1))

for i in range(0, len(list1)) :
    print("list1[%d] :%s"%(i, list1[i]))
# a b c e f나누어 출력하기
list1 = 'a,b,c,d,e,f'
list1Sp = list1.split(',')
print( list1Sp )

# 나누세요
list2 = ['홍길동:100:20','이순신:90:80', '최수연:100:75' ]
# 출력 형식 list2[0] = ['홍길동:100:20']
# list22[0] = ['홍길동']
# list22[1] = ['100']
list22=[]
for i in list2:
    list10 = i.split(':') 
    print(list10)
    for j in list10 : 
        list22.append( j )   
print(list22)    

# 나누세요
print('-'*50)
list5 = [ 'kbs-사장-200, mbc-부장-100', 'kbs-사원-50, sbs-대리-80']

listSOk = []
for i in list5 :
    listHS = i.split('-')
    print(listHS )
    for j in listHS :
        listCS = j.split(',')
        print(listCS)
        for k in listCS :
          listSOk.append(k)
print('완성==>%s'%listSOk)          


# -----------------------------
# 데이터를 사이트에서 검색해 오기
# -----------------------------
# import  requests as req
# url = "http://search.naver.com/search.naver"
# rData = req.get(url,params = { 'query':'백일해 증상'})
# print(rData.text)

# 208
names = ['a','b','c']
x='-'.join(names)
print(x)

# 212쪽 2차원리스트
list2D = [ [1,2], [3,4,5], [1] ]
print( list2D[1][1] ) # 4
print( list2D[0][1] ) # 2 

list2DD = [ [1,2,3,4],[5,6,7] ]
# 7 출력
# print( list2DD[0][0] , end=" ")
# print( list2DD[0][1], end=" " )
# print( list2DD[0][2], end=" " )
# print( list2DD[0][3] , end=" ")
# print()
# print( list2DD[1][0] , end=" ")
# print( list2DD[1][1], end=" " )
# print( list2DD[1][2] , end=" ")

print( len(list2DD) ) # 2
print( len(list2DD[0])) # 4
print( len(list2DD[1])) # 3

for i in range(0, len(list2DD) ) :
    for j in range( 0, len(list2DD[i]) ) :
        print( list2DD[i][j], end=" ")
    print()

list3D = [ [ [1,2,3],[4,5] ], [ [6,7],[8] ] ]
# 8을 출력
print( list3D[1][1][0] )
# 1을 출력
print( list3D[0][0][0] )

# 218쪽 ~ 222쪽 문제 풀기




