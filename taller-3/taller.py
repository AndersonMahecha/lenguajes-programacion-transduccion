import numpy as np
SYMBOL_CHAR = {'{', '}', '(', ')', ',', '[', ']', ':', '=', '==', '!=', '!'}
ARITHMETIC_CHAR = {'+', '-', '/', '*', '%'}
LOGICAL_CHAR = {'or', 'and', 'not'}
ESPACIO = {' '}
KEY_CHAR = {'if', 'for', 'in', 'range', 'else', 'def', 'return', 'while', 'elif', 'print', 'len'}


def perform_matrix_operation(operator, matrix1, matrix2):
    if operator == '+':
        return add_matrices(matrix1, matrix2)
    elif operator == '-':
        return subtract_matrices(matrix1, matrix2)
    elif operator == '*':
        return multiply_matrices(matrix1, matrix2)
    else:
        raise ValueError("Operador no válido")


def add_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Las matrices deben tener las mismas dimensiones")

    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)

    return result


def subtract_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Las matrices deben tener las mismas dimensiones")

    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] - matrix2[i][j])
        result.append(row)

    return result


def multiply_matrices(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        raise ValueError(
            "El número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz")

    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            total = 0
            for k in range(len(matrix2)):
                total += matrix1[i][k] * matrix2[k][j]
            row.append(total)
        result.append(row)

    return result


def transpose(matrix):
    result = []
    for i in range(len(matrix)):
        result.insert(i, [])
        for j in range(len(matrix[i])):
            result[i].insert(j, matrix[j][i])
    return result


def show_matrix(matrix):
    for i in matrix:
        for j in i:
            print(f" {(str(j)).center(8)} ", end='')
        print()


# Ejemplo de uso
matrix1 = [[1, 2, 3], [4, 5, 5], [7, 8, 9]]
matrix2 = [[5, 9, 6], [7, 8, 1], [5, 3, 7]]
show_matrix(matrix1)
print("-" * 50)
show_matrix(matrix2)
print("-" * 50)
operator = '+'
result = (perform_matrix_operation(operator, matrix1, matrix2))
show_matrix(result)
print("-" * 50)
result = transpose(result)
show_matrix(result)
print("-" * 50)
