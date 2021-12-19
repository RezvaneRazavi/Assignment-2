
sum = 0

while True:
    number = input('enter number or exit= ')

    if number == 'exit' or number == 'Exit':
        break
    else:
        sum += float(number)
    
print('sum= ', sum)

