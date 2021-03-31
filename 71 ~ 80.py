import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# https://wikidocs.net/7027


# tuple(튜플)이란 리스트처럼 여러 개의 데이터를 담아두는 데 사용.

# 튜플과 리스트의 차이점
# 1) 리스트는 선언을 할 때 '대괄호([])'를 사용하지만 튜플은 '소괄호(())'를 사용
# 2) 리스트는 리스트 내의 값을 생성, 삭제, 변경이 가능하지만 튜플은 그 값을 바꿀 수 없다.



# my_variable 이름의 비어있는 튜플을 만들라.

'''
my_variable = ()
print(type(my_variable))
'''



# 2016년 11월 영화 예매 순위 기준 top3는 다음과 같다.
# 영화 제목을 movie_rank 이름의 튜플에 저장하라. (순위 정보는 저장하지 않는다.)
# 순위	영화
# 1	    닥터 스트레인지
# 2	    스플릿
# 3	    럭키\

'''
movie_rank = ("닥터 스트레인지", "스플릿", "럭키")
print(movie_rank, type(movie_rank))
'''



# 숫자 1 이 저장된 튜플을 생성하라.

'''
num1 = (1, )

num2 = (1)

print(num1, type(num1))     # 하나의 데이터가 저장되는 경우, 쉼표를 입력해야 튜플로 정의

print(num2, type(num2))     # 쉼표를 입력하지 않아 정수로 정의
'''



# 다음 코드를 실행해보고 오류가 발생하는 원인을 설명하라.

# >> t = (1, 2, 3)
# >> t[0] = 'a'
# Traceback (most recent call last):
#   File "<pyshell#46>", line 1, in <module>
#     t[0] = 'a'
# TypeError: 'tuple' object does not support item assignment

'''
튜플은 원소의 값을 변경할 수 없다.
'''



# 아래와 같이 t에는 1, 2, 3, 4 데이터가 바인딩되어 있다.
# t가 바인딩하는 데이터 타입은 무엇인가?
# t = 1, 2, 3, 4

'''
t = 1, 2, 3, 4
print(t, type(t))

>> (1, 2, 3, 4) <class 'tuple'>

# 원칙적으로 튜플은 소괄호와 함께 데이터를 정의해야 하지만, 사용자 편의를 위해 괄호 없이도 동
'''



# 변수 t에는 아래와 같은 값이 저장되어 있다.
# 변수 t가 ('A', 'b', 'c') 튜플을 가리키도록 수정 하라.
# t = ('a', 'b', 'c')

'''
# 튜플의 값은 변경할 수 없기 때문에, 리스트와 달리 아래 코드는 동작하지 않는다.
t = ('a', 'b', 'c')
t[0] = 'A'
# 새로운 튜플을 만들고 t 라는 변수를 업데이트 해야 한다.
# 기존의 튜플 ('a', 'b', 'c')은 자동으로 삭제
'''



# 다음 튜플을 리스트로 변환하라.
# interest = ('삼성전자', 'LG전자', 'SK Hynix')

'''
interest = ('삼성전자', 'LG전자', 'SK Hynix')
convert = list(interest)

print(interest, type(interest))
print(convert, type(convert))
'''



# 다음 리스트를 튜플로 변경하라.
# interest = ['삼성전자', 'LG전자', 'SK Hynix']

'''
interest = ['삼성전자', 'LG전자', 'SK Hynix']
convert = tuple(interest)

print(interest, type(interest))
print(convert, type(convert))
'''



# 다음 코드의 실행 결과를 예상하라.
# temp = ('apple', 'banana', 'cake')
# a, b, c = temp
# print(a, b, c)

'''
temp = ('apple', 'banana', 'cake')
a, b, c = temp
a, b, c = ('apple', 'banana', 'cake')
# 비례식 같은 개념
a = apple, b = banana, c = cake
'''



# 1 부터 99까지의 정수 중 짝수만 저장된 튜플을 생성하라.
# ex) (2, 4, 6, 8 ... 98)

'''
even = tuple(range(2, 100, 2))
print(even)

# range(A, B, C)
# A 부터 C 숫자만큼의 간격으로 (B - 1) 까지의 정수 범위를 반환.
'''
