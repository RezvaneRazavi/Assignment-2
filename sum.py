
sum = 0

while True:
    x = input('enter number:')

    if x == 'exit':
        break
    sum += float(x)

print('sum=' + sum)