import heapq

def dijkstra(graph, start):
    """
    Dijkstra's algorithm to find the shortest path from a starting node to all other nodes in a graph.
    
    Parameters:
    graph (dict): The graph in the form of adjacency list.
    start: The starting node.
    
    Returns:
    dict: A dictionary containing the shortest distances from the starting node to all other nodes.
    """
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# Test the function
graph = {
    'A': {'B': 3, 'C': 2},
    'B': {'A': 3, 'C': 1, 'D': 6},
    'C': {'A': 2, 'B': 1, 'D': 2},
    'D': {'B': 6, 'C': 2}
}

start_node = 'A'
shortest_distances = dijkstra(graph, start_node)

print("Shortest distances from node", start_node)
for node, distance in shortest_distances.items():
    print("Node:", node, "Distance:", distance)
