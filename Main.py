from Cesty import obchodniCesty
from Convert import convert, convertIndex

def printAll(obchodni_cesty):
    for cesta in obchodni_cesty:
        print(cesta, ":" , obchodni_cesty[cesta] , "\n")
        
def printMin(obchodni_cesty):
    for cesta in obchodni_cesty:
        if len(obchodni_cesty[cesta]) > 1:
            print("Nejkratší cesty stojí" , cesta, "a jsou to:")
            for cesta in obchodni_cesty[cesta]:
                print(cesta , "\n")
            return
        else:
            print("Nejkratší cesta stojí" , cesta, "a je to:" , obchodni_cesty[cesta] , "\n")
            return


vrcholy = ['0', '1', '2', '3', '4']
start = '0'

matice1 = [
    [0, 10, 15, 20, 25],
    [10, 0, 35, 25, 30],
    [15, 35, 0, 30, 20],
    [20, 25, 30, 0, 10],
    [25, 30, 20, 10, 0]
]
graf1 = convert(matice1, vrcholy.copy())

matice2 = [
    [0, 10, 0, 0, 0],
    [10, 0, 2, 0, 2],
    [0, 2, 0, 2, 0],
    [0, 0, 2, 0, 2],
    [0, 2, 0, 2, 0]
]
graf2 = convert(matice2, vrcholy.copy())

matice3 = [
    [0, 10, 2, 2, 0],
    [10, 0, 0, 0, 0],
    [2, 0, 0, 800, 800],
    [2, 0, 800, 0, 2],
    [0, 0, 800, 2, 0]
]
graf3 = convert(matice3, vrcholy.copy())

obchodni_cesty1 = dict(sorted(obchodniCesty(vrcholy.copy(), convertIndex(vrcholy), start, graf1).items()))
obchodni_cesty2 = dict(sorted(obchodniCesty(vrcholy.copy(), convertIndex(vrcholy), start, graf2).items()))
obchodni_cesty3 = dict(sorted(obchodniCesty(vrcholy.copy(), convertIndex(vrcholy), start, graf3).items()))

printMin(obchodni_cesty1)
printMin(obchodni_cesty2)
printMin(obchodni_cesty3)