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

# convert from matice to ->
graf = {
  'A': {'B': 2, 'D': 6, 'E': 2},
  'B': {'A': 2, 'D': 3, 'E': 6},
  'C': {'D': 1},
  'D': {'A': 6, 'B': 3, 'C': 1, 'E': 2},
  'E': {'A': 2, 'B': 6, 'D': 2},
}

# make into function
cesty = cesty(vrcholy, 'A')
vzdalenosti_a_cesty = Dijikstra.vzdalenostiACesty(graf)
obchodni_cesty = {}

for cesta in cesty:
    trasa_cesty = []
    cena_cesty = 0
    
    i = 1
    while i < len(cesta):
        
        ceny_a_cesty_z_vrcholu = vzdalenosti_a_cesty[vrcholy_index[cesta[i - 1]]]
        vrchol = ceny_a_cesty_z_vrcholu[cesta[i]] 
        
        cena_cesty = cena_cesty + vrchol[0] 
        trasa_cesty.extend(vrchol[1]) 
        
        x = i
        while x < len(cesta):

            if cesta[x] in trasa_cesty and cesta[x] != cesta[i] and cesta[x] != cesta[-1]:
                cesta.pop(x)
            x += 1
        
        i += 1

    y = 1
    while y < len(trasa_cesty):
        if trasa_cesty[y] == trasa_cesty[y - 1]:
            trasa_cesty.pop(y)
        y += 1
        
    key = cena_cesty
    obchodni_cesty.setdefault(key, [])
    obchodni_cesty[cena_cesty].append(trasa_cesty)

# Remove duplicate paths
# Sort dicts. by key and show only the lowest
        
for cesta in obchodni_cesty:
    print(cesta, ":" , obchodni_cesty[cesta] , "\n")