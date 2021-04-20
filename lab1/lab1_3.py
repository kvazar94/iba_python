# 5. Для каждого четного по номеру элемента списка A
# найти его сумму со следующим элементом и
# записать эти суммы в новый список B.
import random
inp = int(input("Enter list size: \n "))
B = []
A = [random.randint(0, 99) for i in range(inp)]
print("List A:", A)
for i in range(inp):
    if i % 2 == 0 and i != 0:
        b = A[i] + A[i+1]
        B.append(b)
print("List B:", B)
