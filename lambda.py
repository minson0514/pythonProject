#map
#lambda
def squares(n):
    return n * n

even_numbers = [i for i in range(1,51) if i % 2 == 0]
print(even_numbers)
print(tuple(map(squares, even_numbers))) #map(함수이름, sequence type 자료구조)
print(tuple(map(lambda x : x**2, even_numbers))) #lambda 함수이름 : 수식, sequence type 자료구조

z=lambda  x: pow(x,2)
print(tuple(map(z,even_numbers)))