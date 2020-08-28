import string
let = string.ascii_lowercase
ct = list(input("Enter cipher text: ").replace(" ","").lower())
k1 = int(input("Enter key1: "))
k2 = int(input("Enter key2:"))
index = dict()
for i in range(len(let)):
    index[let[i]]=i
index1 = {v:k for k,v in index.items()}

k1 = k1%26
for x in range(1, 26):
  if ((k1 * x) % 26 == 1):
    inv=x

for i in ct:
  x=((index.get(i)-k2)*inv)%26
  print(index1.get(x).upper(), end="")