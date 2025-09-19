#3. Вивести всі числа від 1 до 200, кратні 3.
count = 1
for i in range(1, 200):
    if count % 3 == 0:
        print(count)
    count += 1
