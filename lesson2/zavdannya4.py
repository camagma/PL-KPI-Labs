#4. Роздрукувати таблицю множення для числа (n) (задати користувачем).
a = int(input("введіть число для таблиці множення: "))
count = 0

for i in range(10):
    result = count * a
    print(f"{a} * {count} = {result}")
    count+=1
    

    
