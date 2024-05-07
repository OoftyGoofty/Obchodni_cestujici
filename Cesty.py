from Dijikstra import vzdalenostiACesty
from itertools import permutations

def cestyGen(vrcholy, start):
    vrcholy.remove(start)
    permutace = list(permutations(vrcholy))
    cesty = []
    
    ###
    for i in range (len(permutace)):
        cesty.append(list(permutace[i]))
        cesty[i].insert(0, start)
        cesty[i].append(start)
    ###
    
    return cesty

def odstranDuplikaty(obchodni_cesty):
    for cena in obchodni_cesty:
    
        ###
        i = 0
        while i < len(obchodni_cesty[cena]):
            cesty = obchodni_cesty[cena]
            
            ###
            y = 0
            while y < len(obchodni_cesty[cena]):
                if cesty[i] == cesty[y]:
                    if cesty[i] is not cesty[y]:
                        cesty.pop(y)
                        odstranDuplikaty(obchodni_cesty)
                        return
                y += 1
            ###
            
            i += 1    
        ###

def obchodniCesty(vrcholy, vrcholy_index, start, graf):
    cesty = cestyGen(vrcholy, start)
    vzdalenosti_a_cesty = vzdalenostiACesty(graf)
    obchodni_cesty = {}

    ### Projdi všechny permutace cest
    for cesta in cesty:
        trasa_cesty = []
        cena_cesty = 0
        
        ### 
        i = 1
        while i < len(cesta):
            
            ceny_a_cesty_z_vrcholu = vzdalenosti_a_cesty[vrcholy_index[cesta[i - 1]]]
            cil = ceny_a_cesty_z_vrcholu[cesta[i]] 
            
            cena_cesty = cena_cesty + cil[0] 
            trasa_cesty.extend(cil[1]) 
            
            ### Odstraň bod z cesty pokud jsme jím již prošli
            x = i
            while x < len(cesta):
                if cesta[x] in trasa_cesty and cesta[x] != cesta[i] and cesta[x] != cesta[-1]:
                    cesta.pop(x)
                x += 1
            ###
            
            i += 1
        ###
        
        ### Odstraň 2 opakované body vedle sebe
        y = 1
        while y < len(trasa_cesty):
            if trasa_cesty[y] == trasa_cesty[y - 1]:
                trasa_cesty.pop(y)
            y += 1
        ###
            
        klic = cena_cesty
        obchodni_cesty.setdefault(klic, [])
        obchodni_cesty[cena_cesty].append(trasa_cesty)
    ###
    
    odstranDuplikaty(obchodni_cesty)    
    
    return obchodni_cesty