import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# https://wikidocs.net/78556



# datetime 모듈을 사용해서 현재 시간을 화면에 출력해보세요.

'''
import datetime

now = datetime.datetime.now()

print(now)
'''



# datetime 모듈의 now 함수의 리턴 값의 타입을 화면에 출력해보세요.

'''
import datetime

now = datetime.datetime.now()

print(now, type(now))
'''



# datetime 모듈의 timedelta를 사용해서 오늘로부터 5일, 4일, 3일, 2일, 1일 전의 날짜를 화면에 출력해보세요.

'''
import datetime

now = datetime.datetime.now()

for day in range(5, 0, -1):
    delta = datetime.timedelta(days=day)
    date = now - delta
    print(date)
'''
