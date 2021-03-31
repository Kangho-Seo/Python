import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# https://wikidocs.net/7039



# 입력된 문자열을 역순으로 출력하는 print_reverse 함수를 정의하라.

# print_reverse("python")

# nohtyp

'''
def print_reverse(string):
    print(string[ : : -1])

print_reverse("python")
'''



# 성적 리스트를 입력 받아 평균을 출력하는 print_score 함수를 정의하라.

# print_score ([1, 2, 3])

# 2.0

'''
def print_score(score_list):
    print(sum(score_list) / len(score_list))

print_score([1, 2, 3])
'''



# 하나의 리스트를 입력받아 짝수만 화면에 출력하는 print_even 함수를 정의하라.

# print_even ([1, 3, 2, 10, 12, 11, 15])

# 2
# 10
# 12

'''
def print_even(even):
    for i in even:
        if i % 2 == 0:
            print(i)

print_even ([1, 3, 2, 10, 12, 11, 15])
'''



# 하나의 딕셔너리를 입력받아 딕셔너리의 key 값을 화면에 출력하는 print_keys 함수를 정의하라.

# print_keys ({"이름":"김말똥", "나이":30, "성별":0})

# 이름
# 나이
# 성별

'''
def print_keys(dic):
    for i in dic.keys():
        print(i)

print_keys ({"이름":"김말똥", "나이":30, "성별":0})
'''



# my_dict에는 날짜를 키값으로 OHLC가 리스트로 저장돼 있다.

# my_dict = {"10/26" : [100, 130, 100, 100],
#            "10/27" : [10, 12, 10, 11]}

# my_dict와 날짜 키값을 입력받아 OHLC 리스트를 출력하는 print_value_by_key 함수를 정의하라.

# print_value_by_key  (my_dict, "10/26")

# [100, 130, 100, 100]

'''
my_dict = {"10/26" : [100, 130, 100, 100],
"10/27" : [10, 12, 10, 11]}

def print_value_by_key(my_dict, key):
    print(my_dict[key])

print_value_by_key(my_dict, "10/26")
'''



# 입력 문자열을 한 줄에 다섯글자씩 출력하는 print_5xn(string) 함수를 작성하라.

# print_5xn("아이엠어보이유알어걸")

# 아이엠어보
# 이유알어걸

'''
def print_5xn(line):
    chunk_num = int(len(line) / 5)
    for i in range(chunk_num + 1):
        print(line[i * 5: i * 5 + 5])

print_5xn("아이엠어보이유알어걸")
'''
