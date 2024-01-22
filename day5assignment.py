'''
univ = 'inha university'
counts_alphabet = {letter: univ.count(letter) for letter in univ} #dictionary comprehension
print(counts_alphabet) #{'i': 3, 'n': 2, 'h': 1, 'a': 1, ' ': 1, 'u': 1, 'v': 1, 'e': 1, 'r': 1, 's': 1, 't': 1, 'y': 1}
'''

'''
univ = 'inha university'
counts_alphabet = dict()
for letter in univ:
    counts_alphabet[letter] = univ.count(letter)
print(counts_alphabet)
'''

#assignment ex 8.10
squares = {n: pow(n,2) for n in range(10)} #key:0~9 value:key^2
print(squares)