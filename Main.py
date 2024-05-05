import Dijikstra
import itertools

def cesty(pole, start):
    pole.remove(start)
    permutace = list(itertools.permutations(pole))
    cesty = []
    
    for i in range (len(permutace)):
        cesty.append(list(permutace[i]))
        cesty[i].insert(0, start)
        cesty[i].append(start)
    
    return cesty


vrcholy = ['A', 'B', 'C', 'D', 'E']
vrcholy_index = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4
}

graf = {
  'A': {'B': 2, 'D': 6},
  'B': {'A': 2, 'D': 3, 'E': 6},
  'C': {'D': 1},
  'D': {'A': 6, 'B': 3, 'C': 1, 'E': 2},
  'E': {'B': 6, 'D': 2},
}

#cesty = cesty(vrcholy, 'A')

cesty = [['A', 'B', 'C', 'D', 'E', 'A'],
         ['A', 'B', 'C', 'E', 'D', 'A']]

vzdalenosti_a_cesty = Dijikstra.vzdalenostiACesty(graf)
obchodni_cesty = {}

#for line in vzdalenosti_a_cesty:
#    print(line, "\n")
#for line in cesty:
#    print(line, "\n")

for cesta in cesty:
    trasa_cesty = []
    cena_cesty = 0
    
    i = 1
    while i < len(cesta): # 0 - 5
        
        #if cesta[i] not in trasa_cesty or cesta[i] == cesta[0]:
        ceny_a_cesty_z_vrcholu = vzdalenosti_a_cesty[vrcholy_index[cesta[i - 1]]] # {'A': (0, ['A']), 'B': (2, ['A', 'B']), 'C': (6, ['A', 'B', 'D', 'C']), 'D': (5, ['A', 'B', 'D']), 'E': (7, ['A', 'B', 'D', 'E'])}
        
        #print(ceny_a_cesty_z_vrcholu)
        
        #for item in ceny_a_cesty_z_vrcholu:
        #    print(ceny_a_cesty_z_vrcholu[item], "\n")
        
        vrchol = ceny_a_cesty_z_vrcholu[cesta[i]] # (2, ['A', 'B'])
        
        #print(vrchol, "\n")
        
        cena_cesty = cena_cesty + vrchol[0] # 2 = 0 + 2
        trasa_cesty.extend(vrchol[1]) # ['A', 'B']
        
        for x in range(i, len(cesta)):
            print(x)
        #    if cesta[x] in trasa_cesty and cesta[x] != cesta[-1]:
        #       cesta.pop(x)
        #        cesta.insert(0, 'X')
        
        print(cesta)
        
        #print(i, "\n")
            
        #else:
        #    cesta.pop(i)
        i += 1
    
    if cena_cesty in obchodni_cesty:        
        obchodni_cesty[cena_cesty] = [obchodni_cesty[cena_cesty], trasa_cesty]
    else:
        obchodni_cesty[cena_cesty] = trasa_cesty

        
for line in obchodni_cesty:
    print(line, ":" , obchodni_cesty[line] , "\n")