# 8. Дано натуральное четырехзначное число n.
# Верно ли, что все его цифры различны?
import random
N = random.randint(1000, 9999)
n = 4
print("Число n:", N)
check = []
for d in str(N):
    check.append(int(d))
for i in range(n - 1):
    for j in range(i + 1, n):
        if check[i] == check[j]:
            print("Число n имеет одинаковые цифры")
            quit()
print("Все цифры уникальны")
