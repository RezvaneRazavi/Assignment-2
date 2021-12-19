weight = float(input('enter weghit(kg)= '))
height = float(input('enter height(m)= '))


BMI = weight / height ** 2
print("BMI=", BMI)


if BMI < 18.5:
    print('UNDERWEIGHT!')

elif BMI >= 18.5 and BMI <= 24.9:
    print('NORMAl!')

elif BMI >= 25 and BMI <= 29.9:
    print('OVERWIGHT!')

elif BMI >= 30 and BMI <= 34.9:
    print('OBESE!')

elif BMI >= 35:
    print('EXTREMELY OBESE!')
