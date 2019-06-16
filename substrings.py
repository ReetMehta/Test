word=input("Enter the word:")
w=[]
for i in word:
    w.append(i) 
n=0

for i in range(0,len(w)):
    counter=0
    pointer=i
    for j in range(0,len(w)-i):
        if w[pointer] is w[j]:
            pointer+=1
            counter+=1
        else: break
    n+=counter

print(n)
print("sdfzv")