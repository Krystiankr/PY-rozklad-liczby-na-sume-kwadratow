import numpy as np

def foo(lista, main, squares):
    for el in squares:
        tmp = lista.copy()
        if tmp.count(1) < el:
            continue
        if tmp.count(1) >= 4:
            replace(tmp, el, main)
            foo(tmp, main,squares)
           
def replace(lista, el, main):
    if lista.count(1) >= el:
        lista.append(el)
        for _ in range(el):
            lista.remove(1)
        lista.sort()
        main.append(lista)

n = 34
ones = list(np.ones(n).astype('int'))
squares = [x**2 for x in range(n) if x**2 < n and x**2>1]
main = [ones]
        
foo(ones, main,squares)

main_set = set(tuple(el) for el in main)
for i,el in enumerate(sorted(main_set),start=1):
    print(f'{i}:{el}')
