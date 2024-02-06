#dictionary ->Heterogenous in nature

dict ={'a':1, 'b':2, 'c':3}
print(dict)

marks = {'anurag': 99, 'amrit':78, 'soham':55}
print(marks)
print(marks['anurag'])

#Iterating through a Dictionary 
#hum key pr iterate krte h dictionary mein

squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
for i in squares:
    print(i,end=' ,')
    print(squares[i])


#updating elements in dictionary
my_dict = {'name':'Jack', 'age': 26}
my_dict['age'] = 27

#adding new elements
my_dict['gender'] = 'male'
print(my_dict)

