#9. Обчислити різницю між найбільшим та найменшим елементом.
import random
n = int(input("введіть довжину списку"))
lst = []
newlst = []
for i in range(n):
    lst.append(random.randint(0,100))
print(lst, max(lst), min(lst))
print(max(lst)-min(lst))