import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# https://wikidocs.net/7022



# letters가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력하세요.
# letters = 'python'
# 실행 예
# p t

'''
letters = 'python'
print(letters, type(letters))
print(letters[0], letters[2])
'''



# 자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하세요.
# license_plate = "24가 2210"

'''
license_plate = "24가 2210"
print(license_plate, type(license_plate))
print(license_plate[4 : ])
print(license_plate[-4 : ])
'''



# 아래의 문자열에서 '홀' 만 출력하세요.
# string = "홀짝홀짝홀짝"

'''
string = "홀짝홀짝홀짝"
print(string[::2])

# test[시작 : 끝 : 간격]
'''




# 문자열을 거꾸로 뒤집어 출력하세요.
# string = "PYTHON"

'''
string = "PYTHON"
print(string[::-1])
'''



# 아래의 전화번호에서 하이푼 ('-')을 제거하고 출력하세요.
# phone_number = "010-1111-2222"
# 실행 예
# 010 1111 2222

'''
phone_number = "010-1111-2222"
print(phone_number.replace("-", " "))
'''

# .replace를 사용하면 문자열의 일부를 치환 할 수 있다.



# 위 문제의 전화번호를 아래와 같이 모두 붙여 출력하세요.
# 실행 예
# 01011112222

'''
phone_number = "010-1111-2222"
print(phone_number.replace("-", ""))
'''



# url 에 저장된 웹 페이지 주소에서 도메인을 출력하세요.
# url = "http://sharebook.kr"
# 실행 예:
# kr

'''
url = "http://sharebook.kr"
print(url[-2:])

url_split = url.split('.')
print(url_split)
# ['http://sharebook', 'kr']

print(url_split[0])
print(url_split[-2])
# http://sharebook

print(url_split[1])
print(url_split[-1])
# kr
'''



# 아래 코드의 실행 결과를 예상해보세요.
# lang = 'python'
# lang[0] = 'P'
# print(lang)

'''
# TypeError: 'str' object does not support item assignment
# 문자열은 수정할 수 없다. 할당 메서드 지원하지 않는다.
'''



# 아래 문자열에서 소문자 'a'를 대문자 'A'로 변경하세요.
# string = 'abcdfe2a354a32a'

'''
string = 'abcdfe2a354a32a'
print(string.replace('a', 'A'))
'''



# 아래 코드의 실행 결과를 예상해보세요.\
# string = 'abcd'
# string.replace('b', 'B')
# print(string)

'''
# abcd라고 출력된다.
# aBcd로 출력되려면
# string = string.replace('b', 'B')
# print(string) 으로 하면 된다.
'''
