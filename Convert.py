def convert(matice, vrcholy):
    vrcholy_index = {y: x for x, y in convertIndex(vrcholy).items()}
    graf = {}
    
    ###
    for i in range(len(matice)):
        graf[vrcholy[i]] = {}
        rad = {}
        
        ###
        for j in range(len(matice[i])):
            if matice[i][j] != 0:
                rad[vrcholy_index[j]] = matice[i][j]
        ###
        graf[vrcholy[i]] = rad
    ###
    
    return graf

def convertIndex(vrcholy):
    vrcholy_index = {}
    
    ###
    i = 0
    for vrchol in vrcholy:
        vrcholy_index[vrchol] = i
        i += 1
    ###
    
    return vrcholy_index