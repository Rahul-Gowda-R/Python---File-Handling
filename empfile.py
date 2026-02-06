#working on file with tabular data(data arranged in rows and columns)
#table or matrix

empfile=open("E:/Rahul/emp.txt")
data=empfile.readlines()
empfile.close()

for x in data:
    print(x.strip())
    #(type(x))