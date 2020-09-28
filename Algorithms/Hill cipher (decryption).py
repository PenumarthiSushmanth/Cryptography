import numpy as np
from math import sqrt
def modInverse(a, m) : 
    #a = a % m; 
    print(a,m)
    for x in range(1, m) : 
       #print("in the loop")
        if ((a * x) % m == 1) :
            return x 
    return 1
def correct_pt(key,pt):
    n = int(sqrt(len(key)))
    for i in range(len(pt)%n):
        pt+='x'
    return pt
def form_array(key):
    n = int(sqrt(len(key)))
    matrix =[]
    count = 0
    for i in range(n):          
        a =[] 
        for j in range(n):
             a.append((ord(key[count])%97))
             count+=1
        matrix.append(a) 
    arr = np.array(matrix)
    det = (np.linalg.det(arr))
    print("determinent is ",det)
    inv = modInverse(int(det),26)
    print("mod inverse of det is",inv)
    y = (np.linalg.inv(arr)*det*inv)
    return y
def hill_cipher(arr,ct):
    text = []
    pt = ''
    for i in range(len(ct)):
        text.append(ord(ct[i])%97)
    arr1 = np.array(text)
    arr2 = np.dot(arr,arr1)
    #print(arr2)
    for i in arr2:
        
        pt+=chr((int(round(i))%26)+97)
        
    return pt
ct = input("Enter the plain text ").replace(" ","").lower()
key = input("enter the key ").replace(" ","").lower()
arr = form_array(key)
print(arr)
#ct = correct_pt(key,ct)
pt =''
n = sqrt(len(key))
if n%1!=0:
    print("entered invalid key")
else:
    n = int(n)
    start = 0
    end = n
    for i in range(int(len(ct)/n)):
        text = ct[start:end]
        pt+=hill_cipher(arr,text)
        start+=n
        end+=n

    print(pt.upper())