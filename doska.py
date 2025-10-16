def doska(matrix):
    for row in matrix:
        print(" | ".join(row))
        print("-" * 9)