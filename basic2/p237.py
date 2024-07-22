# 딕셔너리
member = { 'name':'황예린', 'age':22, 'email':'yein@hanmail.net',"age":30 }
print( member['name'] )
print( member['age'] )
print( member['email'] )

score = dict([('국어', 80),('영어',90),('수학', 100), ('국어', 100)])
print(score)
print( score['국어'] )
# 국어점수를 90점으로 수정하기
score['국어'] = 90
print(score, '~~~')
score2 = dict([['국어', 80],['영어',90],['수학', 100], ['국어', 100]])
print(score2)
print( score2['수학'] )
# 국어점수를 90점으로 수정하기
score2['국어'] = 90
print(score2,'@@@')

# 교재 251쪽까지 문제 풀어 보기




