import numpy as np

# запрос ввода размерности матрицы
n = int(input("Введите размерность матрицы: "))

# инициализация пустой матрицы
A = np.zeros((n,n))

# заполнение матрицы значениями, введенными пользователем
for i in range(n):
    for j in range(n):
        A[i,j] = float(input("Введите элемент A[{},{}]: ".format(i+1, j+1)))

# вычисляем обратную матрицу
try:
    A_inv = np.linalg.inv(A)
    print("Обратная матрица:")
    print(A_inv)
except np.linalg.LinAlgError:
    print("Обратной матрицы не существует")