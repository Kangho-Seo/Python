import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# https://wikidocs.net/78563



# 아래의 표에서, 아이스크림 이름을 키값으로, (가격, 재고) 리스트를
# 딕셔너리의 값으로 저장하라. 딕셔너리의 이름은 inventory로 한다.

# 이름	가격	재고
# 메로나	300	 20
# 비비빅	400	 3
# 죠스바	250	 100

'''
inventory = {"메로나" : [300, 20],
            "비비빅" : [400, 3],
            "죠스바" : [250, 100]}

print(inventory, type(inventory))
'''



# inventory 딕셔너리에서 메로나의 가격을 화면에 출력하라.
# inventory = {"메로나": [300, 20],
#               "비비빅": [400, 3],
#               "죠스바": [250, 100]}

# 실행 예시:
# 300 원

'''
inventory = {"메로나": [300, 20],
              "비비빅": [400, 3],
              "죠스바": [250, 100]}

print(inventory["메로나"][0], "원")
'''



# inventory 딕셔너리에서 메로나의 재고를 화면에 출력하라.
# inventory = {"메로나": [300, 20],
#               "비비빅": [400, 3],
#               "죠스바": [250, 100]}
# 실행 예시:
# 20 개

'''
inventory = {"메로나": [300, 20],
              "비비빅": [400, 3],
              "죠스바": [250, 100]}

print(inventory["메로나"][1], "개")
'''



# inventory 딕셔너리에 아래 데이터를 추가하라.
# inventory = {"메로나": [300, 20],
#              "비비빅": [400, 3],
#              "죠스바": [250, 100]}
#     이름	가격	재고
#    월드콘   500	  7

# 실행 예시:
# >> print(inventory)
# {'메로나': [300, 20], '비비빅': [400, 3], '죠스바': [250, 100], '월드콘': [500, 7]}

'''
inventory = {"메로나": [300, 20],
              "비비빅": [400, 3],
              "죠스바": [250, 100]}

inventory["월드콘"] = [500, 7]

print(inventory, type(inventory))
'''



# 다음의 딕셔너리로부터 key 값으로만 구성된 리스트를 생성하라.
# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}

'''
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
ice = list(icecream.keys())
print(ice, type(ice))
'''



# 다음의 딕셔너리에서 values 값으로만 구성된 리스트를 생성하라.
# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}

'''
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
ice = list(icecream.values())
print(ice, type(ice))
'''



# icecream 딕셔너리에서 아이스크림 판매 금액의 총합을 출력하라.
# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}

# 출력 예시:
# 6700

'''
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}\

ice = list(icecream.values())
print(sum(ice))
'''



# 아래의 new_product 딕셔너리를 다음 icecream 딕셔너리에 추가하라.
# new_product = {'팥빙수':2700, '아맛나':1000}
# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}

# 실행 예시:
# >> print(icecream)
# {'탱크보이': 1200,  '폴라포': 1200,  '빵빠레': 1800,  '월드콘': 1500,  '메로나': 1000,  '팥빙수':2700, '아맛나':1000}

'''
new_product = {'팥빙수':2700, '아맛나':1000}
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}

icecream.update(new_product)
print(icecream)
'''



# 아래 두 개의 튜플을 하나의 딕셔너리로 변환하라. keys를 키로,
# vals를 값으로 result 이름의 딕셔너리로 저장한다.

# keys = ("apple", "pear", "peach")
# vals = (300, 250, 400)

# 실행 예시:
# >> print(result)
# {'apple': 300, 'pear': 250, 'peach': 400}

'''
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
result = dict(zip(keys, vals))
print(result)

# zip은 [key1, key2], [value1, value2]를 (key1, value1), (key2, value2)와 같이
# 묶어주는 기능을 한다. zip을 사용해 묶어서 키 - 값 쌍을 만들어주고 dict로 딕셔너리 형태로 변환.
# dict 대신 list를 사용하면 리스트 형태로 변환되는 것을 확인할 수 있다.
'''



# date와 close_price 두 개의 리스트를 close_table 이름의 딕셔너리로 생성하라.

# date = ['09/05', '09/06', '09/07', '09/08', '09/09']
# close_price = [10500, 10300, 10100, 10800, 11000]

# 실행 예시:
# >> print(close_table)
# {'09/05': 10500, '09/06': 10300, '09/07': 10100, '09/08': 10800, '09/09': 11000}

date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]

close_table = dict(zip(date, close_price))
print(close_table)
