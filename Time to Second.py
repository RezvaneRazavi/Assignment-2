hour = input("please enter Time: ").split(':')

seconds = int(hour[0]) * 3600 + int(hour[1]) * 60 + int(hour[2])

print('secons=', seconds)