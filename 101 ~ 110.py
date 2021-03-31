import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# https://wikidocs.net/7028



# 파이썬에서 True 혹은 False를 갖는 데이터 타입은 무엇인가?

'''
Boolean(bool)
'''



# 아래 코드의 출력 결과를 예상하라
# print(3 == 5)

'''
False
'''



# 아래 코드의 출력 결과를 예상하라
# print(3 < 5)

'''
True
'''



# 아래 코드의 결과를 예상하라.
# x = 4
# print(1 < x < 5)

'''
True
'''



# 아래 코드의 결과를 예상하라.
# print ((3 == 3) and (4 != 3))

'''
True
'''



# 아래 코드에서 에러가 발생하는 원인에 대해 설명하라.
# print(3 => 4)

'''
print(3 >= 4)
>> False
'''



# 아래 코드의 출력 결과를 예상하라
# if 4 < 3:
#    print("Hello World")

'''
조건이 맞지 않아 결과가 출력되지 않는다.
'''



# 아래 코드의 출력 결과를 예상하라
# if 4 < 3:
#    print("Hello World.")
# else:
#    print("Hi, there.")

'''
조건이 맞지 않아 Hi, there이 출력된다.
'''



# 아래 코드의 출력 결과를 예상하라
# if True :
#    print ("1")
#    print ("2")
# else :
#    print("3")
# print("4")

'''
1
2
4
'''



# 아래 코드의 출력 결과를 예상하라
# if True :
#    if False:
#        print("1")
#        print("2")
#    else:
#        print("3")
# else :
#    print("4")
# print("5")

'''
3
5
'''
