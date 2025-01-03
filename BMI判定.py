
def bmi_cal(height_cm, weight):
    height = height_cm/100
    bmi = round(weight / height**2)
    return bmi

def bmi_check(bmi):
    if 40 <= bmi:
        result = '肥満度4'
    elif 35 <= bmi < 40:
        result = '肥満度3'
    elif 30 <= bmi < 35:
        result = '肥満度2'
    elif 25 <= bmi < 30:
        result = '肥満度1'
    elif 18.5 <= bmi < 25:
        result = '普通体重'
    else:
        result = '低体重'   
    return result


height_cm = int(input('身長を入力してください。（単位cm）:'))
weight = int(input('体重を入力してください。（単位kg）:'))

bmi = bmi_cal(height_cm, weight)
result = bmi_check(bmi)


print('BMIは' + str(bmi) + 'です。判定結果は'+ result + 'です。')