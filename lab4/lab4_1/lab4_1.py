#Создайте итерируемый объект, возвращающий генератор
# тридцати пяти чисел трибоначчи и выведите эти числа.
def tribonacci(param):
    f1, f2, f3 = 0, 0, 1
    for i in range(param):
        f1, f2, f3 = f2, f3, f1 + f2 + f3
        yield f1


f = tribonacci(35)
for i in range(35):
    print(next(f))
