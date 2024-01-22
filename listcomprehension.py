def squares(*n) -> list:
    '''
    넘겨 받은 수치 데이터들의 거듭제곱 값을 리스트에 담아서 리턴
    :param n: tuple
    :return: list
    '''
    return [pow(i,2) for i in n]#list comprehension
    #return n*n

def run_function(f, *number) -> list:
    return f(*number)

print(squares(7,5,2))
print(run_function(squares, 9,10))