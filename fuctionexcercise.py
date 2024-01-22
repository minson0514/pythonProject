#공프 문제풀이1 강노

#함수 #1
#특정값부터 특정값까지의 평균과 분산을 구해서 출력하는 프로그램을 함수를 이용하여 작성하시오
#(함수이름: avg_var).
# 단, 다음 제한 조건에 따라 프로그램을 작성 하시오.
# 1.평균과 분산 계산에 필요한 구간에 해당하는 값은 사용자가 셸에서 입력 하도록 하고,
# 이 값을 함수호출 시 전달 해야한다.
# 2.평균과 분산은 함수 밖에서 출력하되, 문자열 포맷팅을 이용한다.
'''
start = int(input("시작값 입력: "))
end = int(input("끝값 입력: "))
def avg_var(start, end):
    total_1 = 0
    for i in range(start, end+1): #end가 star보다 클 때 오류 생김
        total_1 = total_1+i
        i += 1
    average = total_1 / (end-start+1)

    total_2 = 0
    for j in range(start, end+1):
        total_2 = total_2 + pow((j-average), 2)
        j = j + 1
    var = total_2 / (end-start+1)
    return average, var
val = avg_var(start, end)
print(f"평균: {val[0]}, 분산: {val[1]}")
'''

#함수 #2
# 도, 분, 초를 도 단위로 변환하는 coord함수를 작성하고자 한다.
# 다음 구문과 실행결과를 보고 coord함수를 정의하시오.
'''
def coord(d, m=0, s=0):
    degree = d
    minute = d / 60.0
    second = d /3600.0
    a = degree + minute + second
    print(f"{d}도 {m}분 {s}초는 {a}도 입니다.")
coord(36)
coord(36,10)
coord(36,10,10)
'''

#함수 #3
#사용자로부터 원하는 개수의 정수를 입력 받아, 크기순으로 정렬해서 출력하는 프로그램을
#다음의 구조에 맞춰 3개의 함수를 이용하여 작성하시오.
#data 함수 정의: 입력 받은 값을 리스트의 요솟값으로
#sorting 함수 정의: sort 함수를 이용해 sorting
#output 함수 정의: 리스트 값 출력

n = int(input("원하는 자료 개수를 입력하세요: "))
def data(n):
    list=[]
    for i in range(1,n+1):
        word = int(input("%d번째 자료 값을 입력하세요: "%i))
        list.append(word)
    return list
def sorting(a):

a = data(n)
b = sorting(a)
#output(b)