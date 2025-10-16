def esli_full(matrix):
    return all(all(cell != " " for cell in row) for row in matrix)