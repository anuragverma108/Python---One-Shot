a = [1,2,7,5,3,4]
print(a)

#append - element is inserted from the last
a.append(6)
print(a)

#insert - list.insert(index at which elemmennt to be inserted, element to be inserted)
a.insert(3,3.5)
print(a)

#sort - use to sort a list in ascending order
a.sort()
print(a)

#pop - pop(index of element to be removed)
a.pop(4)
print(a)

#clear - empty the whole list
b = [3,45,56,7,8]
print(b)
b.clear()
print(b)

#reverse 
a.reverse()
print(a)

#index      #used to find index of a element
q = a.index(3.5)
print(q)

#count      #used to find the no. of times a element has been repeated
z = a.count(5)
print(z)


