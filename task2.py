#task : create a text mytext.txt, type few lines
#find all the words which dose not start with vowels


file=open("mytext.txt")
text=file.read()
file.close()

words = text.split()

vowels="aeiouAEIOU"

results=[]

for word in words:
    if word[0] not in vowels:
        results.append(word)

print("Words  not starting with vowels")
print(results)