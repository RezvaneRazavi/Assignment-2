x = int(input('Enter Number of class members: '))

class_list=[]
sum = 0

for i in range (x):
    num = float(input('enter score: '))
    class_list.append(num)

    sum += num

avg = sum / x

class_list.sort()
max = max(class_list)
min = min(class_list)

print(class_list, '\navg = ', avg, '\nmax= ', max, '\nmin= ', min)
