# list1 = [3, 15, -12.5, '사과', '딸기', True, False]
# list2 = list(range(1,21,2))  # 1, 3, 5, 7, 9, 11, 13, 15, 17, 19
# print(list1)
# print(list2)
# for i in range(7) :
#    print( list1[6-i], end=" ")
# print('-'*50)   
# print( list2[: :2])
# print( list2[-1: :-2])

# #응용문제 100 110 120 .... 200 리스트를 만들어 보기
# list3 = list(range( 100, 201, 10 ))
# # 갯수를 세어 보기 답 11개
# cnt = 0
# sum = 0
# for i in list3 :
#    cnt = cnt + 1 
#    sum = sum + i
# print("리스트의 갯수는 %d"%cnt)   
# print("합계는 %d"%sum)
# # 합계를 구하기 

# print(len(list3)) #리스트의 갯수 구하기

# # 185페이지
# colors = ["빨", "파", "노", "검", "초"]
# for color in colors :
#     print("나는 %s를 좋아한다"%color) 

# colors = ["빨", "파", "노", "검", "초"]
# n = len(colors)
# for i in range( 0,n) :
#     print("나는 %s을 좋아한다"%colors[i])

# animal = ['코','호','사','펭','여']
# i=0
# while i<len(animal) :
#     print( animal[len(animal)-1 - i] )
#     i = i + 1

# 성적 프로그램 작성하기
list1 = ['홍길동', 50, 80]
list2 = ['이순신', 90, 75]
list3 = ['최경미', 100, 100]

print("이름  국어점수 수학점수 합계  평균")
print(list1[0], "  ", list1[1],"  ", list1[2], "  ", list1[1] + list1[2], " ", (list1[1] + list1[2])/2 )
print(list2[0], "  ", list2[1],"  ", list2[2], "  ", list2[1] + list2[2], " ", (list2[1] + list2[2])/2 )
print(list3[0], "  ", list3[1],"  ", list3[2], "  ", list3[1] + list3[2], " ", (list3[1] + list3[2])/2 )
print("우리반 이름 : %s %s %s"%(list1[0], list2[0],list3[0]) )
print("우리반 국어점수 합계 %d"%(list1[1] + list2[1] + list3[1]))
print("우리반 수학점수 합계 %d"%(list1[2] + list2[2] + list3[2]))

if   list1[1] > list2[1] and list1[1] > list3[1] :  # list1이 제일 큰 경우
     topKorName = list1
elif   list2[1] > list1[1] and list2[1] > list3[1] :  # list2이 제일 큰 경우
     topKorName = list2 
else :  # list3이 제일 큰 경우
     topKorName = list3     
print("우리반에서 국어점수 제일 잘 본 사람의 이름은? %s"%topKorName[0]) 

findName = input("찾고 싶은 사람은?")
if findName==list1[0] or findName==list2[0] or findName==list3[0] :
    print("우리반에 %s 있어요"%findName)
else :
    print("우리반에 %s 없어요"%findName) 


