#file handling

# open ----> read ----> close


file =  open('27-data.txt','r')       #The first argument is the file name, and the second argument is the mode ("r" for reading).
                                    #it returna file object


#we can use readline() method to read individual lines of a file. This method reads a file till the
# newline, including the newline character.

# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())

for line in file:
    print(line)

file.close()