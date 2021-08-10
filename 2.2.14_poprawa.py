import numpy as np
n = 51
ones = np.ones(n).astype('int')
ones = list(ones)
ones.count(1)
squares = [x**2 for x in range(51) if x**2 < 51 and x**2>1]
main = [ones]

def foo(lista, main, squares):
    for el in squares:
        tmp = lista.copy()
        if tmp.count(1) < el:
            continue
        if tmp.count(1) >= 4:
            podmianka(tmp, el, main)
            foo(tmp, main,squares)
            
def podmianka(lista, el, main):
    if lista.count(1) >= el:
        lista.append(el)
        for _ in range(el):
            lista.remove(1)
        #print(lista)
        lista.sort()
        main.append(lista)
        
foo(ones, main,squares)

main_set = set(tuple(el) for el in main)
len(main_set)
for i,el in enumerate(sorted(main_set),start=1):
    print(f'{i}:{el}')
