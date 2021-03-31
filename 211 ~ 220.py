import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# https://wikidocs.net/23907



# 함수의 호출 결과를 예측하라.

# def 함수(문자열) :
#     print(문자열)

# 함수("안녕")
# 함수("Hi")

'''
안녕
Hi
'''



# 함수의 호출 결과를 예측하라.

# def 함수(a, b) :
#     print(a + b)

# 함수(3, 4)
# 함수(7, 8)

'''
7
15
'''



# 아래와 같은 에러가 발생하는 원인을 설명하라.

# def 함수(문자열) :
#     print(문자열)

# 함수()
# TypeError: 함수() missing 1 required positional argument: '문자열'

'''
함수에 정의와 다르게 함수를 호출하고 있다. 함수를 호출할 때 하나의 파라미터를 입력해야한다.
'''



# 아래와 같은 에러가 발생하는 원인을 설명하라.

# def 함수(a, b) :
#     print(a + b)

# 함수("안녕", 3)

# TypeError: must be str, not int

'''
덧셈 연산을 하려고 설계, 문자열과 숫자는 더할 수 없다.
'''



# 하나의 문자를 입력받아 문자열 끝에 ":D" 스마일 문자열을 이어 붙여 출력하는 print_with_smile 함수를 정의하라.\

# 정의한 함수를 호출하라. 파라미터는 "test"로 입력하라.

'''
def print_with_smile(str):
    print(str + ":D")

print_with_smile("test")
'''



# 현재 가격을 입력 받아 상한가 (30%)를 출력하는 print_upper_price 함수를 정의하라

'''
def print_upper_price(price):
    print(price * 1.3)

print_upper_price(10)
'''



# 두 개의 숫자를 입력받아 두 수의 합을 출력하는 print_sum 함수를 정의하라.

'''
def print_sum(a, b):
    print(a + b)

print_sum(3 ,4)
'''



# 두 개의 숫자를 입력받아 합/차/곱/나눗셈을 출력하는 print_arithmetic_operation 함수를 작성하라.

# print_arithmetic_operation(3, 4)

# 3 + 4 = 7
# 3 - 4 = -1
# 3 * 4 = 12
# 3 / 4 = 0.75

'''
def print_arithmetic_operation(a, b):
    print(a, "+", b, "=", a + b)
    print(a, "-", b, "=", a - b)
    print(a, "*", b, "=", a * b)
    print(a, "/", b, "=", a / b)

print_arithmetic_operation(3, 4)
'''



# 세 개의 숫자를 입력받아 가장 큰수를 출력하는 print_max 함수를 정의하라. 단 if 문을 사용해서 수를 비교하라.

'''
def print_max(a, b, c):
    x = 0
    if a > x:
        x = a
    if b > x:
        x = b
    if c > x:
        x = c
    print(x)

print_max(1, 2, 3)
'''
