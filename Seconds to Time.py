seconds = int(input("please enter seconds: "))

hour = seconds // 3600
temp = seconds % 3600
minute = temp // 60
second = temp % 60

if hour < 10:
    hour = '0' + str(hour) 
if minute < 10:
    minute = '0' + str(minute)
if second < 10:
    second = '0' + str(second)

print(hour, ':', minute, ':', second)

