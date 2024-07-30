import math

def dijkstra(matrix, source, destination):
    num_nodes = len(matrix)
    distances = [math.inf] * num_nodes
    distances[source] = 0
    unvisited = set(range(num_nodes))
    
    while unvisited:
        current_node = None
        for node in unvisited:
            if current_node is None or distances[node] < distances[current_node]:
                current_node = node
        if distances[current_node] == math.inf:
            break  
        for neighbor in range(num_nodes):
            weight = matrix[current_node][neighbor]
            if weight > 0: 
                distance = distances[current_node] + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
    
        unvisited.remove(current_node)
    return distances[destination] if distances[destination] != math.inf else "unreachable"

#Matrix to represent distances of travelling between nodes
adjacency_matrix = [
    [0, 5, 10, math.inf],  # Distances from node A
    [math.inf, 0, 2, 6],    # Distances from node B
    [math.inf, math.inf, 0, 1],  # Distances from node C
    [math.inf, math.inf, math.inf, 0]  # Distances from node D
]

source = 0 
destination = 3   
print(dijkstra(adjacency_matrix, source, destination))

#Output
#The Shortest Path from A to D is A->B->C->D
#Shortest Distance from A to D is: 5+2+1=8