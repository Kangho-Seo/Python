import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# https://wikidocs.net/78562



# for문의 실행결과를 예측하라.
# 과일 = ["사과", "귤", "수박"]
# for 변수 in 과일:
#     print(변수)

'''
사과
귤
수박
'''



# for문의 실행결과를 예측하라.
# 과일 = ["사과", "귤", "수박"]
# for 변수 in 과일:
#   print("#####")

'''
#####
#####
#####
'''



# 다음 코드를 for문으로 작성하라.
# 변수 = 10
# print(변수)
# 변수 = 20
# print(변수)
# 변수 = 30
# print(변수)

'''
num = ["10", "20", "30"]
for i in num:
    print(i)
'''



# 다음 코드를 for문으로 작성하라.
# print(10)
# print("-------")
# print(20)
# print("-------")
# print(30)
# print("-------")

'''
num = ["10", "20", "30"]

for i in num:
    print(i)
    print("------")
'''



# 다음 코드를 for문으로 작성하라.
# print("++++")
# print(10)
# print(20)
# print(30)

'''
num = ["10", "20", "30"]

print("++++")
for i in num:
    print(i)
'''



# 다음 코드를 for문으로 작성하라.
# print("-------")
# print("-------")
# print("-------")
# print("-------")

'''
num = ["1", "2", "3", "4"]

for i in num:
    print("-------")
'''
