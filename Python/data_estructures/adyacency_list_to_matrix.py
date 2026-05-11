def adjacency_list_to_matrix(dic):

    matrix = []
    for _ in range(len(dic)):
        matrix.append([0]*len(dic)) 
    
    for key in range(len(dic)):
        for value in dic[key]:
            matrix[key][value] = 1
    
    matrix_str = ''
    for row in matrix:
        matrix_str += str(row)
        matrix_str += '\n'
    
    print(matrix_str)
    return matrix


adjacency_list_to_matrix({0: [2], 1: [2, 3], 2: [0, 1, 3], 3: [1, 2]})