
height_cm = int(input('身長を入力してください。（単位cm）:'))
weight = int(input('体重を入力してください。（単位kg）:'))

height = height_cm/100

bmi = round(weight / height**2)

print('BMIは' + str(bmi) + 'です。')

if 40 <= bmi:
    print('肥満度4')
elif 35 <= bmi < 40:
    print('肥満度3')
elif 30 <= bmi < 35:
    print('肥満度2')
elif 25 <= bmi < 30:
    print('肥満度1')
elif 18.5 <= bmi < 25:
    print('普通体重')
else:
    print('低体重') 