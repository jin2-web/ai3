def average( *args ) :
    print( len( args ) )

def func( food ) :
    for x in food :
        print(x, end=" ")
#비지니스로직 부분(실제 코드 수행 부분) 함수 호출
average(85,96,87) 
average(77,93,85,97,72)

fruits = ['사과','오렌지','바나나']
func( fruits )