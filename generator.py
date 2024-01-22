def my_range(first=0, last=5, step=1):
    number=first
    while number<last:
        yield  number
        number+=step
r = my_range()
print(r, type(r))

for x in r:
    print(x) #call generater
for x in r:
    print(x) #실행 X