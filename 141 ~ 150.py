import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# https://wikidocs.net/7020



# 다음과 같이 판매가가 저장된 리스트가 있을 때 부가세가 포함된 가격을 for 문을 사용해서 화면에 출력하라. 단 부가세는 10원으로 가정한다.

# 리스트 = [100, 200, 300]

# 110
# 210
# 310

'''
list = [100, 200, 300]

for i in list:
    print(i + 10)
'''



# for 문을 사용해서 리스트에 저장된 값을 다음과 같이 출력하라.

# 리스트 = ["김밥", "라면", "튀김"]

# 오늘의 메뉴: 김밥
# 오늘의 메뉴: 라면
# 오늘의 메뉴: 튀김

'''
list = ["김밥", "라면", "튀김"]

for i in list:
    print("menu : ", i)
'''



# 리스트에 주식 종목이름이 저장돼 있다.

# 리스트 = ["SK하이닉스", "삼성전자", "LG전자"]

# 저장된 문자열의 길이를 다음과 같이 출력하라.
# 6
# 4
# 4

'''
list = ["SK하이닉스", "삼성전자", "LG전자"]

for i in list:
    print(len(i))
'''



# 리스트에는 동물이름이 문자열로 저장돼 있다.

# 리스트 = ['dog', 'cat', 'parrot']

# 동물 이름과 글자수를 다음과 같이 출력하라.

# dog 3
# cat 3
# parrot 6

'''
list = ['dog', 'cat', 'parrot']

for i in list:
    print(i, len(i))
'''



# 리스트에 동물 이름 저장돼 있다.

# 리스트 = ['dog', 'cat', 'parrot']

# for문을 사용해서 동물 이름의 첫 글자만 출력하라.

# d
# c
# p

'''
list = ['dog', 'cat', 'parrot']

for i in list:
    print(i[0])
'''



# 리스트에는 세 개의 숫자가 바인딩돼 있다.

# 리스트 = [1, 2, 3]

# for문을 사용해서 다음과 같이 출력하라.

# 3 x 1
# 3 x 2
# 3 x 3

'''
list = [1, 2, 3]

for i in list:
    print("3 x", i)
'''



# 리스트에는 세 개의 숫자가 바인딩돼 있다.

# 리스트 = [1, 2, 3]

# for문을 사용해서 다음과 같이 출력하라.

# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9

'''
list = [1, 2, 3]

for i in list:
    print("3 x", i, "=", 3 * i)
'''



# 리스트에는 네 개의 문자열이 바인딩돼 있다.

# 리스트 = ["가", "나", "다", "라"]

# for문을 사용해서 다음과 같이 출력하라.

# 나
# 다
# 라

'''
list = ["가", "나", "다", "라"]

list1 = list[1:]

print(list1)

for i in list1:
    print(i)
'''



# 리스트에는 네 개의 문자열이 바인딩돼 있다.

# 리스트 = ["가", "나", "다", "라"]

# for문을 사용해서 다음과 같이 출력하라.

# 가
# 다

'''
list = ["가", "나", "다", "라"]

for i in list[ : : 2]:
    print(i)
'''



# 리스트에는 네 개의 문자열이 바인딩돼 있다.

# 리스트 = ["가", "나", "다", "라"]

# for문을 사용해서 다음과 같이 출력하라.

# 라
# 다
# 나
# 가

'''
list = ["가", "나", "다", "라"]

list1 = list[ : : -1]

for i in list1:
    print(i)
'''
