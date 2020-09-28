import numpy as np
from math import sqrt
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
    return arr
def hill_cipher(arr,pt):
    text = []
    ct = ''
    for i in range(len(pt)):
        text.append(ord(pt[i])%97)
    arr1 = np.array(text)
    arr2 = np.dot(arr,arr1)
    for i in arr2:
        ct+=chr((i%26)+97)
    return ct
pt = input("Enter the plain text ").replace(" ","").lower()
key = input("enter the key ").replace(" ","").lower()
arr = form_array(key)
pt = correct_pt(key,pt)
ct =''
n = sqrt(len(key))
if n%1!=0:
    print("entered invalid key")
else:
    n = int(n)
    start = 0
    end = n
    for i in range(int(len(pt)/n)):
        text = pt[start:end]
        ct+=hill_cipher(arr,text)
        start+=n
        end+=n

    print(ct.upper())