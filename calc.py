def numbers(x,y):
    while True:
        print("Выбор математической операции: ")
        print("+ - Сложение;")
        print("- - Вычитание;")
        print("* - Умножение;")
        print("/ - Деление.")
        act = input()
        if act in ('+','-','*','/'):
            if act == '+':
                return x+y
            elif act == '-':
                return x-y
            elif act == '*':
                return x*y
            elif act == '/':
                if y != 0:
                    return x/y
                else:
                    print("Вы делите на ноль!")
        else:
            print("Неверный знак!")

def matrixPlus(A,B,C,m,n):
    for i in range(n):
        for j in range(m):
            C[i][j] = A[i][j] + B[i][j]
    return C

def matrixMultiply(m,n,A,q,B):
    C = []
    for i in range(m):
        row = []
        for j in range(q):
            row.append(0)
        C.append(row)
    for i in range(m):
        for j in range(q):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

def Number():
    x = input("Введите первое число: ")
    while True:
        try:
            x = float(x)
        except ValueError:
            x = input("Введите первое число: ")
        else: break
    y = input("Введите второе число: ")
    while True:
        try:
            y = float(y)
        except ValueError:
            y = input("Введите второе число: ")
        else: break
    c = numbers(x, y)
    print("%.2f" % (c))
    while True:
        print("Продолжить вычисления?")
        word = input()
        if word in ("Да", "Нет"):
            if word == "Да":
                print("Введите второе число")
                y = float(input())
                c = numbers(c, y)
                print("%.2f" % (c))
            elif word == "Нет":
                break
        else:
            print("Введите Да или Нет!")

def Matrix():
    print("Выбор математической операции: ")
    print("+ - Сложение;")
    print("* - Умножение;")
    act = input()
    if act in ('+', '*'):
        if act == '+':
            m = input("Введите кол-во столбцов матриц: ")
            while True:
                try:
                    m = int(m)
                except ValueError:
                    m = input("Введите кол-во столбцов матриц: ")
                else:
                    break
            n = input("Введите кол-во строк матриц: ")
            while True:
                try:
                    n = int(n)
                except ValueError:
                    n = input("Введите кол-во строк матриц: ")
                else:
                    break
            A = [[0] * m] * n
            B = [[0] * m] * n
            C = [[0] * m] * n
            print("Введите элементы матрицы А")
            for i in range(n):
                for j in range(m):
                    try:
                        A[i][j] = int(input())
                    except ValueError:
                        print("Введите цифру!")
                        A[i][j] = int(input())
            print("Введите элементы матрицы Б")
            for i in range(n):
                for j in range(m):
                    try:
                        B[i][j] = int(input())
                    except ValueError:
                        print("Введите цифру!")
                        B[i][j] = int(input())
            print(matrixPlus(A,B,C,m,n))
        elif act == '*':
            print("Введите размерность матрицы А:")
            try:
                m, n = list(map(int, input().split()))
            except ValueError:
                print("Используйте при вводе цифры!")
                m, n = list(map(int, input().split()))
            print("Введите размерность матрицы B:")
            try:
                p, q = list(map(int, input().split()))
            except ValueError:
                print("Используйте при вводе цифры!")
                p, q = list(map(int, input().split()))
            if n != p:
                print('Невозможно перемножить данные матрицы')
                Matrix()
            A = []
            for i in range(m):
                print("Введите значения матрицы А ", i, " строки:")
                try:
                    row = list(map(int, input().split()))
                except ValueError:
                    print("Используйте при вводе цифры!")
                    row = list(map(int, input().split()))
                A.append(row)
            B = []
            for j in range(p):
                print("Введите значения матрицы В ", j, " строки:")
                try:
                    row = list(map(int, input().split()))
                except ValueError:
                    print("Используйте при вводе цифры!")
                    row = list(map(int, input().split()))
                B.append(row)
            print(matrixMultiply(m,n,A,q,B))
    else:
        print("Неверный знак!")

def main():
    print("|" * 10, "Калькулятор", "|" * 10)
    while True:
        print("Выбор режима работы: ")
        print("1 - Операция с вещественными числами;")
        print("2 - Операция с матрицами.")
        mode = input()
        if mode in ('1', '2'):
            if mode == '1':
                Number()
            if mode == '2':
                Matrix()
        else:
            print("Попробуйте еще раз")

if __name__ == '__main__':
    main()