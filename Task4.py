number = int(input('Введите положительное число (двухзначное и более): '))
max = number % 10
number = number//10
while number > 0:
    if number % 10 > max:
        max = number % 10
    number = number//10
print(max)