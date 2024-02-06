#Creating lists

# list = [expression   for loop     if condition]

# a = [0,1,2,3,4,5,6,7,8,9]

a = [x for x in range(10)]
print(a)

b = [y for y in range(1,100,3)]
print(b)

#for printing only even numbers

c = [z for z in range(1,100) if z%2 == 0]
print(c)

#for printing only odd numbers

d = [p for p in range(1,100) if p%2 == 1]
print(d)

l = [5**x for x in range(11)]
print(l)