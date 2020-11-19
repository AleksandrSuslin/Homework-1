start = int(input('Введите расстояние с которого начнёте тренеровку: '))
finish = int(input('Введите расстояние которое хотите пробежать  : '))
i = 1
result = start
while result <= finish:
    if result < finish:
        print(f' {i} день, вы пробежали - {result}км ')
        result = result * 1.1
        i += 1
print('Поздравляю, вы достигли желаемого результата ', round(result, 2),'км' , 'за :', i,
      'дней')
