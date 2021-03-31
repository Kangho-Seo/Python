import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# https://wikidocs.net/7024



# 아래 코드의 실행 결과를 예상해보세요.
# a = "3"
# b = "4"
# print(a + b)

'''
문자열에 덧셈 기호는 문자열의 연결
34 라고 출력
'''



# 아래 코드의 실행 결과를 예상해보세요.
# print("Hi" * 3)

'''
문자열에 곱셈 기호는 문자열의 반복
HiHiHi 라고 출력
'''


# 화면에 '-'를 80개 출력하세요.

'''
print("-" * 80)
'''



# 변수에 다음과 같은 문자열이 바인딩되어 있습니다.
# t1 = 'python'
# t2 = 'java'
# 변수에 문자열 더하기와 문자열 곱하기를 사용해서 아래와 같이 출력해보세요.
# 실행 예:
# python java python java python java python java


'''
t1 = 'python'
t2 = 'java'

t3 = t1 + ' ' + t2 + ' '

print(t3 * 4)
'''



# 변수에 다음과 같이 문자열과 정수가 바인딩되어 있을 때
# % formatting을 사용해서 다음과 같이 출력해보세요.

# name1 = "Kim"
# age1 = 10
# name2 = "Lee"
# age2 = 13

# name: Kim age: 10
# name: Lee age: 13

'''
name1 = "Kim"
age1 = 10
name2 = "Lee"
age2 = 13

print("name:, %s age: %d" % (name1, age1))
print("name:, %s age: %d" % (name2, age2))

# print formmating에서 %s는 문자열 데이터 타입의 값을 %d는
# 정수형 데이터 타입 값의 출력을 의미
'''



# 문자열의 format( ) 메서드를 사용해서 전 문제를 다시 풀어보세요.

'''
name1 = "Kim"
age1 = 10
name2 = "Lee"
age2 = 13

print("name: {} age: {}".format(name1, age1))
print("name: {} age: {}".format(name2, age2))
'''



# 삼성전자의 상장주식수가 다음과 같습니다. 컴마를 제거한 후 이를 정수 타입으로 변환해보세요.
# 상장주식수 = "5,969,782,550"

'''
상장주식수 = "5,969,782,550"
stock = 상장주식수.replace(",", "")
print(int(stock), type(int(stock)))
'''



# 다음과 같은 문자열에서 '2020/03'만 출력하세요.
# 분기 = "2020/03(E) (IFRS연결)"

'''
분기 = "2020/03(E) (IFRS연결)"
print(분기[:7])
'''



# 문자열의 좌우의 공백이 있을 때 이를 제거해보세요.
# data = "   삼성전자    "

'''
data = "   삼성전자    "
data1 = data.strip()

print(data)
print(data1)

# 문자열에서 .strip() 메서드를 사용하면 좌우의 공백을 제거할 수 있다. 이때 원본
# 문자열은 그대로 유지되고 공백이 제거된 새로운 문자열이 반환.
'''
