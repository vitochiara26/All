def dfs(adj_matrix, node_tag):
    stack = []
    visited = []
    stack.append(node_tag)
    
    while stack:
        current_node = stack.pop()
        if not current_node in visited:
            visited.append(current_node)
            for x in range(len(adj_matrix)):
                if adj_matrix[current_node][x] == 1:
                        stack.append(x)
                    

dfs([[0, 1, 0, 0]
   , [1, 0, 1, 0], 
     [0, 1, 0, 1], 
     [0, 0, 1, 0]], 
     1)