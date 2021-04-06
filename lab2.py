#2. Торговая фирма в первый день работы реализовала товаров на P тыс. руб.,
# а затем ежедневно увеличивала выручку на 3%.
# Какой будет выручка фирмы в тот день, когда она впервые превысит заданное значение Q?
# Сколько дней придется торговать фирме для достижения этого результата?
import random
P = random.randint(1000, 9999)
Q = int(input("Введите значение Q: \n "))
daily_earn = []
counter = P
print("День 1:", P)
day = 2
while counter < Q:
    counter = counter + (counter*0.03)
    daily_earn.append(counter)
    print("День",day,"-", '%.2f' % counter)
    day+=1
print("Выручка привышает Q на", len(daily_earn) + 1, "день и составит", '%.2f' % daily_earn[-1])