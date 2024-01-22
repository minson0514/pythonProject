#dictionary
#mutable data structure
sugang = dict(python='kim', cpp='sung', db='kang')
#TypeError: unhashable type: 'dict' -> {} 로 dict를 묶으면 에러

#get items
'''
print(sugang)
sugang['datastructure'] = "kim"
print(sugang)
sugang['datastructure'] = 'park'
print(sugang) #type: dictionary
print(sugang['db']) #kang
print(sugang.get('db')) #kang
print(sugang.get('opensource')) #None
print(sugang.get('opensource', 'not exist'))
'''

#Print items
'''
for subjet, professor in sugang.items():
    print("%s 과목 담당교수는 %s 입니다."%(subjet,professor)) #print key and value

#for k in sugang.keys():
for k in sugang: #key -> default
    print(k) #print key
for v in sugang.values():
    print(v) #print value

for s in sugang.items():
    print(s) #print key and value in tuple
'''