def factorial_repetition(n) -> int:
    '''
    반복문을 이용한 팩토리얼 함수
    :param n: 정수, int
    :return: 팩토리얼 값, int
    '''
    result = 1
    for i in range(2, n+1):
        result = result * i
    return result
import random

def factorial_recursion(n):
    '''
    재귀함수를 사용한 팩토리얼 함수
    :param n: 정수, int
    :return: function, int
    '''
    if n == 1:
        return n
    else:
        return n * factorial_recursion(n-1)
# numbers = list()
# for i in range(5):
#     numbers.append(random.randint(1, 100))
numbers = [random.randint(1, 100) for i in range(10)]
print(numbers)

number = int(input("number : "))
print(factorial_repetition(number))
print(factorial_recursion(number))
print(globals())
try:
    pick = int(input(f"Input index (0 ~ {len(numbers)-1}) : "))
    print(numbers[pick])
    #print(5/0)
except IndexError as err:
    print(f"Wrong index number\n{err}")
except ValueError as err:
    print(f"Input Only Number~\n{err}")
except ZeroDivisionError as err:
    print(f"The denominator cannot be 0.\n{err}")
except Exception as err:
    print(f"Error occurs : {err}")