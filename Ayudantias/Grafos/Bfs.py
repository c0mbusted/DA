"""graph = {'A': ['B', 'C', 'E'],
         'B': ['A','D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B'],
         'E': ['A', 'B','D'],
         'F': ['C'],
         'G': ['C']}"""
graph= [34, 4, 2, 22, 15, 31,50,90]
         
         
def bfs(graph, initial):
    
    visited = []
    
    queue = [initial]
 
    while queue:
        
        node = queue.pop(0)
        if node not in visited:
            
            visited.append(node)
            neighbours = graph[node]
 
            
            for neighbour in neighbours:
                queue.append(neighbour)
    return visited
 
print(bfs(graph,22))