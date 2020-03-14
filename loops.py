for i in range(1, 21, 2):
    print(i, end=' ')
print()
for j in range(0, 110, 10):
    print(j, end=' ')
print()
for k in range(20, 0, -1):
    print(k, end=' ')
print()
star_amount = float(input("Enter a number of stars: "))
l = 0
while l != star_amount:
    print("*", end ="")
    l = l + 1