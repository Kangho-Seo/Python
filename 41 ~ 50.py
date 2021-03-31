import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# https://wikidocs.net/78558



# 다음과 같은 문자열이 있을 때 이를 대문자 BTC_KRW로 변경하세요.
# ticker = "btc_krw"

'''
ticker = "btc_krw"
print(ticker.upper())

# .upper 메서드를 호출하면 문자열을 대문자로 만들 수 있다.
'''



# 다음과 같은 문자열이 있을 때 이를 소문자 btc_krw로 변경하세요.
# ticker = "BTC_KRW"

'''
ticker = "BTC_KRW"
print(ticker.lower())

# .lower 메서드를 호출하면 문자열을 소문자로 만들 수 있다.
'''



# 문자열 'hello'가 있을 때 이를 'Hello'로 변경해보세요.

'''
a = 'hello'
print(a.capitalize())

# .capitalize 메서드를 호출하면 주어진 문자열에서 맨 첫 글자를 대문자로 변환
'''



# 파일 이름이 문자열로 저장되어 있을 때 endswith 메서드를
# 사용해서 파일 이름이 'xlsx'로 끝나는지 확인해보세요.
# file_name = "보고서.xlsx"

'''
file_name = "보고서.xlsx"
print(file_name.endswith("xlsx"))

# endwith는 문자열이 특정 문자로 끝나는지 여부(True, False)를 알려준다.
'''



# 파일 이름이 문자열로 저장되어 있을 때 startswith
# 메서드를 사용해서 파일 이름이 '2020'로 시작하는지 확인해보세요.
# file_name = "2020_보고서.xlsx"

'''
file_name = "2020_보고서.xlsx"
print(file_name.startswith("2020"))

# startswith는 문자열이 특정 문자로 시작하는지 여부(True, False)를 알려준다.
'''



# 다음과 같은 문자열이 있을 때 공백을 기준으로 문자열을 나눠보세요.
# a = "hello world"

'''
a = "hello , world"
print(a.split(''))

# 문자열의 split() 메서드를 사용하면 문자열에서 공백을 기준으로 분리
'''



# 다음과 같이 문자열이 있을 때 btc와 krw로 나눠보세요.
# ticker = "btc_krw"

'''
ticker = "btc_krw"
print(ticker.split('_'))
'''



# 다음과 같이 날짜를 표현하는 문자열이 있을 때 연도, 월, 일로 나눠보세요.
# date = "2020-05-01"

'''
date = "2020-05-01"
print(date.split('-'))
'''



# 문자열의 오른쪽에 공백이 있을 때 이를 제거해보세요.
# data = "039490     "

'''
data = "039490     "
print(data.rstrip())

# strip : 좌, 우 공백 제거
# lstrip : 좌 공백 제거
# rstip : 우 공백 제거
'''
