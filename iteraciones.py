
a = "platzi"

for i in a:
    print(i)


for i in range(10):
    print(i)


for i in range(30):
    if i % 3 == 0:
        print(i)
    elif i == 22:
        break

for i in range(30):
    if i % 3 != 0:
        continue
    else:
        print(i**2)
# -------------------------------------------------------------------------------
i = 10

while i > 0:
    print(i)
    i -= 1

