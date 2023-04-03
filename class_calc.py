from random import randint
import numpy as np

class Matrix(object):

    def __init__(self, a=0, b=0):
        self.matrix = []
        self.m = a
        self.n = b
        self.init_matrix(self.m, self.n)

    def init_matrix(self, n, m):
        if (self.m == 0 and self.n == 0):
            print("Введите размерность матрицы:")
            try:
                m, n = list(map(int, input().split()))
            except ValueError:
                return 'ERROR \n'

            print("Введите элементы матрицы")
            try:
                self.matrix = [[input() for j in range(m)] for i in range(n)]
            except ValueError:
                return 'ERROR \n'
        else:
            try:
                self.matrix = [[randint(0, 10) for j in range(self.m)] for i in range(self.n)]
            except ValueError:
                return 'ERROR \n'
    
    def __add__(self, other):
        try:
            a = np.array(self.matrix)
            b = np.array(other.matrix)
            return a + b
        except ValueError:
            return "ERROR \n" 

    def __str__(self):
        strings = []
        for row in self.matrix:
            strings.append(str(row))
        return '\n'.join(strings)

    def __mul__(self, other):
        if isinstance(other, Matrix):
            try:
                a = np.array(self.matrix)
                b = np.array(other.matrix)
                return b.dot(a)
            except ValueError:
                return "ERROR \n"  
        return np.array([[num*other for num in row] for row in self.matrix]) 

    def __sub__(self, other):
        try:
            a = np.array(self.matrix)
            b = np.array(other.matrix)
            return a - b
        except ValueError:
            return "ERROR \n"

    def matrixTranspose(self):
        try:
            return (np.array(self.matrix)).transpose()
        except ValueError:
            return "ERROR \n"

m1 = Matrix()
print('Матрица: \n', m1)

m1 = Matrix(2,2)
m2 = Matrix(2,2)
print('Матрица А: \n', m1)
print('Матрица Б: \n', m2)
print('СЛОЖЕНИЕ \n', m1+m2)
print('ВЫЧИТАНИЕ \n', m1-m2, '\n')

m1 = Matrix(2, 3)
m2 = Matrix(3, 5)
print('Матрица А: \n', m1)
print('Матрица Б: \n', m2)
print('УМНОЖЕНИЕ МАТРИЦ \n', m1*m2, '\n')

m1 = Matrix(2, 3)
m2 = Matrix(4, 5)
print('Матрица А: \n', m1)
print('Матрица Б: \n', m2)
print('ОШИБКА ПЕРЕМНОЖЕНИЯ \n', m1*m2)

m1 = Matrix(2, 3)
print('Матрица: \n', m1)
print('ТРАНСПОНИРОВАНИЕ \n', m1.matrixTranspose(), '\n')

m1 = Matrix(2, 2)
print('Матрица: \n', m1)
print('УМНОЖЕНИЕ \n', m1*5, '\n')
