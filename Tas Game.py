import random

while True:
    num = random.randint(1, 6)
    print('Number Tas:', num)
    if num == 6:
        num = random.randint(1, 6)
        print('Award user:', num)
        break
    else:
        break