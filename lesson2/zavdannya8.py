import random
length = int(input("введіть довжину списку: "))
firstlst = []
newlst = []

for i in range(length):
    firstlst.append(random.randint(0, 100))

print("перший список:", firstlst)

for index in range(length):
    newindex = length - 1 - index
    newlst.append(firstlst[newindex])
print("новий список:", newlst)
