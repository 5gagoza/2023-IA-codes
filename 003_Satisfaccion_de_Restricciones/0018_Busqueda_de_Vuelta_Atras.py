def backtrack_search(n):
    # Crear un tablero vacío de tamaño n x n
    board = [[0 for _ in range(n)] for _ in range(n)]
    # Llamar a la función auxiliar para iniciar la búsqueda
    return backtrack(board, n, 0)

def backtrack(board, n, row):
    # Si ya se han colocado todas las reinas, retornar el tablero como solución
    if row == n:
        return board
    # Para cada columna, intentar colocar una reina en la fila actual
    for col in range(n):
        if is_valid(board, n, row, col):
            # Si es una posición válida, colocar la reina en el tablero
            board[row][col] = 1
            # Llamar recursivamente a la función backtrack para la siguiente fila
            result = backtrack(board, n, row + 1)
            if result is not None:
                # Si se encuentra una solución, retornarla
                return result
            # Si no hay solución, deshacer el movimiento (quitar la reina del tablero)
            board[row][col] = 0
    # Si no se pudo colocar una reina en ninguna columna, retornar None para indicar fracaso
    return None

def is_valid(board, n, row, col):
    # Revisar si hay otra reina en la misma fila o columna
    for i in range(n):
        if board[row][i] == 1 or board[i][col] == 1:
            return False
    # Revisar las diagonales
    for i in range(n):
        for j in range(n):
            if (i+j == row+col) or (i-j == row-col):
                if board[i][j] == 1:
                    return False
    # Si no hay conflictos, la posición es válida
    return True

solution = backtrack_search(8)
if solution is not None:
    print("Solución encontrada:")
    for row in solution:
        print(row)
else:
    print("No se encontró solución.")
