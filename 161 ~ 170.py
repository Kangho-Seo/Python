import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# https://wikidocs.net/7033



# for문과 range 구문을 사용해서 0~99까지 한 라인에 하나씩 순차적으로 출력하는 프로그램을 작성하라.

'''
for i in range(100):
    print(i)
'''



# 월드컵은 4년에 한 번 개최된다. range()를 사용하여 2002~2050년까지 중 월드컵이 개최되는 연도를 출력하라.

# 2002
# 2006
# 2010
# ...
# 2042
# 2046
# 2050

# 참고) range의 세번 째 파라미터는 증감폭을 결정합니다.

# >> print(list(range(0, 10, 2)))
# [0, 2, 4, 6, 8]

'''
for i in range(2002, 2051, 4):
    print(i)
'''



# 1부터 30까지의 숫자 중 3의 배수를 출력하라.

'''
for i in range (3, 31, 3):
    print(i)
'''



# 99부터 0까지 1씩 감소하는 숫자들을, 한 라인에 하나씩 출력하라.

'''
for i in range(99, -1, -1):
    print(i)
'''



# for문을 사용해서 아래와 같이 출력하라.

# 0.0
# 0.1
# 0.2
# 0.3
# 0.4
# 0.5
# ...
# 0.9

'''
for i in range(10):
    print(i / 10)
'''



# 구구단 3단을 출력하라.

'''
for i in range(1, 10):
    print(3, "x", i, "=", i * 3)
'''



# 구구단 3단을 출력하라. 단 홀수 번째만 출력한다.

'''
for i in range(1, 10):
    if i % 2 != 0:
        print(3, "x", i, "=", i * 3)
'''



# 1~10까지의 숫자에 대해 모두 더한 값을 출력하는 프로그램을 for 문을 사용하여 작성하라.

'''
a = 0

for i in range(11):
    a += i
print(a)
'''



# 1~10까지의 숫자 중 모든 홀수의 합을 출력하는 프로그램을 for 문을 사용하여 작성하라.

'''
a = 0

for i in range(11):
    if i % 2 != 0:
        a += i
print(a)
'''



# 1~10까지의 숫자를 모두 곱한 값을 출력하는 프로그램을 for 문을 사용하여 작성하라.

'''
a = 1

for i in range(1, 11):
    a *= i
print(a)
'''
