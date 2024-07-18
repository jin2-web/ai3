word="I am Happy"
for i in word:
    print(i, end="")

phone="010-5744-5554"
print(phone)
# 핸드폰 번호안에서 5가 있나요? 답 없습니다. 
flag = 0
for i in phone :
   if i=="5":
     flag = 1
if flag == 0 :
    print("없어요")
else :
    print("있어요")       
# 영어문장에 "a"글자가 있나요?
word="apple"
# 답은 1개 있어요
word="an/a"
# 답은 2개 있어요
word="book"
#답은 없어요
for j in range(0,3,1) :
    word = input("영어 단어는")
    flag = 0 # 있으면 1로 없으면 0으로 됨 
    cnt = 0 # a의 갯수를 세어주는 변수 
    for i in word :
        if i == 'a' :
            flag=1
            cnt += 1
    if flag == 0 :
        print("a가 없어요")       
    else :
        print("%d개 있습니다"%cnt)

