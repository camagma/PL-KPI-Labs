#3. Вивести всі числа від 1 до 50, які діляться на 5.
count = 0
for i in range(50):
    if count % 5 == 0:
        print(count)
    count +=1
