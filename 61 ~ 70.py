import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# https://wikidocs.net/7025



# price 변수에는 날짜와 종가 정보가 저장돼 있다.
# 날짜 정보를 제외하고 가격 정보만을 출력하라. (힌트 : 슬라이싱)

# price = ['20180728', 100, 130, 140, 150, 160, 170]
# 출력 예시:
# [100, 130, 140, 150, 160, 170]

'''
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])
'''



# 슬라이싱을 사용해서 홀수만 출력하라.
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 실행 예:
# [1, 3, 5, 7, 9]

'''
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])

# test[시작 : 끝 : 간격]
'''



# 슬라이싱을 사용해서 짝수만 출력하라.
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 실행 예:
# [2, 4, 6, 8, 10]

'''
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[1::2])

# test[시작 : 끝 : 간격]
'''



# 슬라이싱을 사용해서 리스트의 숫자를 역 방향으로 출력하라.
# nums = [1, 2, 3, 4, 5]
# 실행 예:
# [5, 4, 3, 2, 1]

'''
nums = [1, 2, 3, 4, 5]
print(nums[::-1])

# test[시작 : 끝 : 간격]
'''



# interest 리스트에는 아래의 데이터가 바인딩되어 있다.
# interest = ['삼성전자', 'LG전자', 'Naver']
# interest 리스트를 사용하여 아래와 같이 화면에 출력하라.
# 출력 예시:
# 삼성전자 Naver

'''
interest = ['삼성전자', 'LG전자', 'Naver']
del interest[1]
print(interest)
'''



# interest 리스트에는 아래의 데이터가 바인딩되어 있다.
# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# interest 리스트를 사용하여 아래와 같이 화면에 출력하라.
# 출력 예시:
# 삼성전자 LG전자 Naver SK하이닉스 미래에셋대우

'''
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(interest)
print(" ".join(interest))

# join 함수는 매개변수로 들어온 리스트에 있는 요소 하나하나를 합쳐서 하나의
# 문자열로 바꾸어 반환하는 함수
# .join(list)를 이용하면 매개변수로 들어온 ['a', 'b', 'c'] 이런 식의 리스트를
# 'abc'의 문자열로 합쳐서 반환해주는 함수
# 위의 print(" ".join(interest))중 " " 공백을 두어 각 합쳐진 문자열 사이에 공백을
# 넣어준다. 다른 기호 x를 넣어주면 각 요소가 합쳐지면서 x가 사이에 들어있게 된다.
'''



# interest 리스트에는 아래의 데이터가 바인딩되어 있다.
# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# interest 리스트를 사용하여 아래와 같이 화면에 출력하라.
# 출력 예시:
# 삼성전자/LG전자/Naver/SK하이닉스/미래에셋대우

'''
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print("/".join(interest))
'''



# interest 리스트에는 아래의 데이터가 바인딩되어 있다.
# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# join() 메서드를 사용해서 interest 리스트를 아래와 같이 화면에 출력하라.
# 출력 예시:
# 삼성전자
# LG전자
# Naver
# SK하이닉스
# 미래에셋대우

'''
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print("\n".join(interest))
'''



# 회사 이름이 슬래시 ('/')로 구분되어 하나의 문자열로 저장되어 있다.
# string = "삼성전자/LG전자/Naver"
# 이를 interest 이름의 리스트로 분리 저장하라.
# 실행 예시
# >> print(interest)
# ['삼성전자', 'LG전자', 'Naver']

'''
string = "삼성전자/LG전자/Naver"
interest = string.split("/")
print(interest)

# 문자열.split()을 사용하면, 문자열에 대해 공백을 구분자로 나누어 리스트를 생성
# .split("/") : "/"를 구분자로 나
'''



# 리스트에 있는 값을 오름차순으로 정렬하세요.
# data = [2, 4, 3, 1, 5, 10, 9]

'''
data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
print(data)
'''
