# 예제 4-8 
# for i in range(5) :
#     phone = input("하이픈(-)을 포함한 휴대폰 번호를 입력하세요")

#     for x in phone :
#         if x != "-" :
#             print("%s"%x, end="")
#     print()

# 1단계 키보드입력을 받는다
hp = input("핸드폰번호를 입력해 주세요") # 51-*
# 2단계 한글자를 가져와서 숫자인지 비교한다
for i in hp :
   # 3단계 숫자이면 출력한다 아니면 다시 2단계로 간다 
  if  '가'<=i<='힣':
    print("%s"%i, end="")
  # 3-1단계 대문자만 출력한다.   