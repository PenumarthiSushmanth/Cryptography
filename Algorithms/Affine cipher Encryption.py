import string
pt = list(input("Enter the plain text: ").replace(" ","").lower())
k1 = int(input("Enter key1: "))
k2 = int(input("Enter key2: "))
lst = string.ascii_lowercase
index = dict()
for i in range(len(lst)):
    index[lst[i]]=i
index1 = {v:k for k,v in index.items()}
for i in pt:
    x = ((index.get(i) * k1)+k2)%26
    print(index1.get(x).upper(), end="")
