import math
import heapq

def dijkstra(matrix, source, destination):
    num_nodes = len(matrix)
    if source < 0 or source >= num_nodes or destination < 0 or destination >= num_nodes:
        return "Invalid source or destination index."
    
    distances = [math.inf] * num_nodes
    previous_nodes = [None] * num_nodes
    distances[source] = 0
    priority_queue = [(0, source)]
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_distance > distances[current_node]:
            continue
        for neighbor in range(num_nodes):
            weight = matrix[current_node][neighbor]
            if weight < math.inf:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(priority_queue, (distance, neighbor))
    
    if distances[destination] == math.inf:
        return f"No path exists from {chr(ord('A') + source)} to {chr(ord('A') + destination)}."
    
    path = []
    step = destination
    while step is not None:
        path.append(step)
        step = previous_nodes[step]
    path.reverse()
    if path[0] != source:
        return f"No path exists from {chr(ord('A') + source)} to {chr(ord('A') + destination)}."
    path_str = '->'.join(chr(ord('A') + node) for node in path)
    return f"The Shortest Path from {chr(ord('A') + source)} to {chr(ord('A') + destination)} is {path_str}\nShortest Distance from {chr(ord('A') + source)} to {chr(ord('A') + destination)} is: {distances[destination]}"
    
num_nodes = int(input("Enter the number of nodes: "))
matrix = []
print("Enter the adjacency matrix row by row. Use 'inf' for infinity.")
for i in range(num_nodes):
    row = input(f"Enter row {i+1}: ").strip().split()
    row = [math.inf if value.lower() == 'inf' else int(value) for value in row]
    matrix.append(row)
source = int(input("Enter the source node index: "))
destination = int(input("Enter the destination node index: "))
result = dijkstra(matrix, source, destination)
print(result)

#Output
"""Enter the number of nodes: 4
Enter the adjacency matrix row by row. Use 'inf' for infinity.
Enter row 1: 0 5 10 inf
Enter row 2: inf 0 2 7
Enter row 3: inf inf 0 1
Enter row 4: inf inf inf 0
Enter the source node index: 0
Enter the destination node index: 3
The Shortest Path from A to D is A->B->C->D
Shortest Distance from A to D is: 8"""
