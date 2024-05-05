import heapq

def dijkstra(graf, pocatecni):
    vzdalenost = {vrchol: float('infinity') for vrchol in graf}
    predchozi = {vrchol: '' for vrchol in graf}
    
    vzdalenost[pocatecni] = 0
    queue = [(0, pocatecni)]
    
    while queue:
        aktualni_vzdalenost, aktualni_vrchol = heapq.heappop(queue)

        if aktualni_vzdalenost > vzdalenost[aktualni_vrchol]:
            continue

        for soused, cena in graf[aktualni_vrchol].items():
            nova_vzdalenost = aktualni_vzdalenost + cena

            if nova_vzdalenost < vzdalenost[soused]:
                vzdalenost[soused] = nova_vzdalenost
                predchozi[soused] = aktualni_vrchol
                heapq.heappush(queue, (vzdalenost[soused], soused))

    return vzdalenost, predchozi


def najdiNejkratsiCestu(graph, start_vrchol, konec_vrchol):
    x, predchozi_od_startu = dijkstra(graph, start_vrchol)
        
    cesta = [konec_vrchol]
    while cesta[-1] != start_vrchol:
        cesta.append(predchozi_od_startu[cesta[-1]])
        
    return cesta[::-1]


def vzdalenostiACesty(graf):
    vzdalenosti_a_cesty = []
    for vrchol in graf:
        vzdal, pred = dijkstra(graf, vrchol)
        for bod in vzdal:
            vzdal[bod] = (vzdal[bod], najdiNejkratsiCestu(graf, vrchol, bod))
        vzdalenosti_a_cesty.append(vzdal)

    return vzdalenosti_a_cesty