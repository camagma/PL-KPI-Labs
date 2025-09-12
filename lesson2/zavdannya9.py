import random

length = int(input("введіть довжину списку: "))
lst = []

for i in range(length):
    lst.append(random.randint(0, 10))
print(lst)
print(sum(lst) / length)