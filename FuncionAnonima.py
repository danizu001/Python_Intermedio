from functools import reduce

my_list=[1,4,5,6,9,13,19,21]
mul=[2,2,2,2,2]
palindromo = lambda palabra:palabra==palabra[::1]
odd=list(filter(lambda x:x%2!=0,my_list))
squares=list(map(lambda x:x**2,my_list))
allm=reduce(lambda a,b:b*a,mul)
print(palindromo('ana'))
print(odd)
print(squares)
print(allm)