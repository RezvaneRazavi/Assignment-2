x = int(input('Enter number of class members: '))

class_List = []
sum = 0 


for i in range(x):
    number = float(input('enter score= '))
    class_List.append(number)

    sum += number


avg = sum / x


max = max(class_List)
min = min(class_List)


print('\n', class_List, '\navg= ', avg, '\nmax= ', max, '\nmin= ', min)
