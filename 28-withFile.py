with open('27-data.txt','r') as file:
    print(file.read(10))    #shuru ke 10 character read karega
    print(file.read(10))    #fir next 10 charchter read karega
    #agr hum chahte h ki cursur firse shuru mei chla jaye o then we'll write file.seek(0)


    #opening file with 'with' and storing it as file object
    # for line in file:
    #     print(line)
        

#no need of writing close statement
