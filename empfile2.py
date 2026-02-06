#find the total salary of the employees 

#working on file with tabular data(data arranged in rows and columns)
#table or matrix

empfile=open("E:/Rahul/emp.txt")
data=empfile.readlines()
empfile.close()

for x in data:
    w=x.split(',')
    print(w)