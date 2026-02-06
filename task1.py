#task : create a text mytext.txt, type few lines
#read the file and find the biggest word in the file



file=open("E:/Rahul/mytext.txt")
text=file.read()
file.close()

words=text.split()

biggest=words[0]

for word in words:
    if len(word)>len(biggest):
        biggest=word

print("Biggest word:",biggest)