from typing import List
def nastepny(n: int):
    tmp: List[int] = []
    for i in range(n, 2, -1):
        if i * i < n:
            tmp.append(i*i)
    return tmp

def foo(n, l_glowna):
    tmp = l_tmp.copy()
    while tmp.count(1)>= n:
        tmp.append(n)
        for _ in range(n):
            tmp.remove(1)    
        l_glowna.append(tmp.copy())


l_glowna: List[int] = []
n=113
l_jedynki: List[int] = []
for i in range(n):
    l_jedynki.append(1)
l_glowna.append(l_jedynki.copy())
l_tmp = l_jedynki.copy()

while l_tmp.count(1)>=4:            
            for el in nastepny(n):
                foo(el, l_glowna)                
            
            if l_tmp.count(1)>=4:
                tmp = l_tmp.copy() 
                l_tmp.append(4)
                for _ in range(4):
                    l_tmp.remove(1)                                
                l_glowna.append(l_tmp.copy()) 
l_glowna.append(nastepny(n))
l_glowna.append([n])

nastepny(25)

l_glowna = set(tuple(element) for element in l_glowna)

for i,el in enumerate(sorted(l_glowna),start=1):
    print(f'i={i}  =  {el}')
