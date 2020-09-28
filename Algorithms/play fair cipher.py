from math import ceil, sqrt
from collections import OrderedDict 
def removeDupWithOrder(str): 
    return "".join(OrderedDict.fromkeys(str))
def correct_pt(pt):
    cpt =''
    cpt =''
    for i in range(0,len(pt)):
        if i == 0:
            cpt+=pt[0]
        elif pt[i] == pt[i-1]:
            if(len(cpt)%2 != 0):
                cpt+='x'
                cpt+=pt[i]
            else:
                print("in else")
                cpt+=pt[i]
        else:
            cpt+=pt[i]
    if(len(cpt)%2 != 0):
        cpt+='x'
    return(cpt)
def form_key(key):
    List = []
    print(key)
    for i in range(5):
        List.append([])
    for i in range(25):
        if i <len(key):
            List[i%5].append(key[i]) 
        else:
            break
    count = i;
    for i in range(26):
        if key.find(chr(97+i)) != -1 or chr(97+i) == 'j':
            pass
        else:
            #print (count)
            List[count%5].append(chr(97+i))
            count+=1
    for i in List:   
        print(i)
    return List
def replace(List,e1,e2):
    r1,r2,c1,c2 = 0,0,0,0
    if e1 == 'i'and e2 =='j':
        for i in range(5):
            try:
                c1 = List[i].index(e1)
                r1 = i
            except Exception:
                pass
        return List[r1][c1-1],List[r1][c1+1]
    elif e1 =='j' and e2 =='i':
        for i in range(5):
            try:
                c1 = List[i].index(e1)
                r1 = i
            except Exception:
                pass
        return List[r1][c1+1],List[r1][c1-1]
    else:
        
        if e1 == 'j':
            e1 = 'i'
        if e2 =='j':
            e2 = 'i'
        for i in range(5):
            try:
                c1 = List[i].index(e1)
                r1 = i
            except Exception:
                pass
        for i in range(5):
            try:
                c2 = List[i].index(e2)
                r2 = i
            except Exception:
                pass
        if r1 == r2:
            c1+=1
            c2+=1
            
            return List[r1][(c1)%5],List[r2][(c2)%5]
        elif c1 == c2:
            return List[(r1+1)%5][c1],List[(r2+1)%5][c2]
        else:
            return List[r2][c1],List[r1][c2]
            
pt = input("enter the plain text ").replace(" ","")
key = input("enter key ")
key = removeDupWithOrder(key)
List = form_key(key)
pt = pt.lower()
pt = correct_pt(pt)
ct = ''
for i in range(0,len(pt),2):
    r1,r2 =replace(List,pt[i],pt[i+1])
    ct+=r1
    ct+=r2
    
print(ct)   
