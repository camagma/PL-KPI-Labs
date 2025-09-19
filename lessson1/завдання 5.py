#5. Порахувати добуток цифр введеного числа.
x = int(input("введіть число: "))
d = 0
for i in str(x):
    d += int(i)
print(d)
