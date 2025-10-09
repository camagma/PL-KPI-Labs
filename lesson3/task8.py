#8. Вивести новий список тільки з додатних чисел.
import random
n = int(input("введіть довжину списку"))
lst = []
newlst = []
for i in range(n):
    lst.append(random.randint(-100,100))
print(lst)
for i in lst:
    if i > 0:
        newlst.append(i)
print(newlst)