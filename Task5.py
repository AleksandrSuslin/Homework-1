revenue = int(input('Введите размер выручки: '))
cost = int(input('Введите  сумму издержек: '))

if cost> revenue:
    print(' У вас убыток')

else:
    profitability = (revenue - cost ) / revenue
    print('Ого, вы умудрились что-то заработать , ваша рентабельность: ',profitability )
    staff = int(input('Введите  кол-во сотрудников: '))
    profit_staff = (revenue - cost ) / staff
    print('Прибыль на одного сотрудника : ', profit_staff )