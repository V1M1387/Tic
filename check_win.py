def check_win(matrix, igrok):
    for row in matrix:
        if all(cell == igrok for cell in row):
            return True
    for col in range(3):
        if all(matrix[row][col] == igrok for row in range(3)):
            return True
    if all(matrix[i][i] == igrok for i in range(3)):
        return True
    if all(matrix[i][2 - i] == igrok for i in range(3)):
        return True
    return False