time =int(input('Введите время в секундах: '))
hours = time // 3600
minuts = (time//60) % 60
seconds = time % 60
print(f'{hours}часов, {minuts}минут , {seconds}секунд')

