from Cesty import obchodniCesty
from Convert import convert, convertIndex

def printAll(obchodni_cesty):
    for cesta in obchodni_cesty:
        print(cesta, ":" , obchodni_cesty[cesta] , "\n")
        
def printMin(obchodni_cesty):
    for cesta in obchodni_cesty:
        if len(obchodni_cesty[cesta]) > 1:
            print("Nejkratší cesty stojí" , cesta, "a jsou:" , obchodni_cesty[cesta] , "\n")
            return
        else:
            print("Nejkratší cesta stojí" , cesta, "a je:" , obchodni_cesty[cesta] , "\n")
            return


vrcholy = ['A', 'B', 'C', 'D', 'E']
start = 'A'
matice = [
    [0, 2, 6, 0, 10],
    [2, 0, 0, 5, 0],
    [6, 0, 0, 8, 0],
    [0, 5, 8, 0, 10],
    [10, 0, 0, 10, 0]
]
graf = convert(matice, vrcholy)

obchodni_cesty = dict(sorted(obchodniCesty(vrcholy, convertIndex(vrcholy), start, graf).items()))

#printAll(obchodni_cesty)
printMin(obchodni_cesty)