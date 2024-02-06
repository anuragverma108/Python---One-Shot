lines_data = ['anurag\n','verma\n','is\n','great\n']

with open("dummyDat.txt",'w') as f:
    f.write("Anurag Verma\n")
    f.writelines(lines_data)
