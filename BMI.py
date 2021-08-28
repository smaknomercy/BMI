height = float(input("Введіть свій ріст в см: "))
weight = float(input("Введіть свою вагу в кг: "))
BMI = float("{0:.2f}".format(weight /((height / 100) * (height /100))))
print(f"Ваш ІМТ {BMI}")
if(BMI > 40):
    print("Ожиріння ІІІ степені")
elif(BMI >= 35):
    print("Ожиріння ІІ степені")
elif(BMI >= 30):
    print("Ожиріння І степені")
elif(BMI >= 25):
    print("Надлишкова вага")
elif(BMI >= 18.5):
    print("Нормальна вага")
else:
    print("Недостатня вага")