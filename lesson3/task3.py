#3. Знайти найбільший елемент списку.
import random
n = int(input("введіть довжину списку"))
lst = []
for i in range(n):
    lst.append(random.randint(0,100))
print(lst)
print("максимальне: ", max(lst))