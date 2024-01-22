#8장 딕셔너리와 셋
#8.1
'''
e2f={"dog": "chien", "cat": "chat","walrus": "morse"}
'''

#8.2
'''
e2f={"dog": "chien", "cat": "chat","walrus": "morse"}
print(e2f["walrus"]) #morse
'''

#8.3 *use item method
'''
e2f={"dog": "chien", "cat": "chat","walrus": "morse"}
#print(type(e2f.items()))#<class 'dict_items'>
#print(list(e2f.items()))
a=(list(e2f.items())) #key값이 tuple로 반환됨
eng=[]
for i in range(3):
    eng.append(a[i][0])
print(eng)

fre=[]
for j in range(3):
    fre.append(a[j][1])
print(fre)

print(fre[0])
f2e={}
for k in range(0,3):
    f2e[eng[i]]=fre[i]



#print(type(a))#<class 'list'>
'''
#정답
'''
e2f={"dog": "chien", "cat": "chat","walrus": "morse"}
f2e={}
for english, french in e2f.items():
    f2e[french]=english
print(f2e)
'''

#8.4
'''
print(f2e['chien'])
'''

#8.5
'''
e2f={"dog": "chien", "cat": "chat","walrus": "morse"}
print(e2f.keys()) #dict_keys(['dog', 'cat', 'walrus'])
'''

#8.10