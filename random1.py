import random

print(random.random())



list = []
for num in range(1, 9):
    list.append(num)

test = int(random.choice(list))

if test > 5:
    print(f"UR num is {test} so lucky!")
else:
    print(f"UR num {test}, so Sad")
