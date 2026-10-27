
import csv
count = int(input("Сколько деталей?"))
total_all = 0
max_price = 0
min_price = float('inf')

if count <= 0:
    print ('Ошибка: кол-вл не может быть отрицательным')
    exit()
file = open('otchet.txt', 'w',
encoding='cp1251')
file.write('Отчёт\n')
file.write('=' *30 + '\n')
all_price = []
with open('otchet.csv', 'w' , newline='', encoding='cp1251') as f:
    writer = csv.writer(f, delimiter=";")
    writer.writerow(['Номер', 'Полощадь', "Слои", "Цена без скидки", "Скидка", "Итог"])
for i in range(count):
    print('---Деталь №', {i+1}, ' ---')
    leng = float(input('Длинна детали в м: '))
    if leng<=0:
        print ('Ошибка: размеры не могут быть отрицательными')
        exit()
    sir = float(input('Ширина детали в м: '))
    if sir<=0:
        print ('Ошибка: размеры не могут быть отрицательными')
        exit()
    sloy = int(input('Количество слоёв: '))
    if sloy<= 0:
        print ('Ошибка: кол-вл не может быть отрицательным')
        exit()
    price = int(input('Cтоиммость слоя за кв/м: '))
    if price<=0:
        print("Ошибка: стоимость не может быть отрицательной")
        exit()
    s = leng * sir
    total = s*sloy*price
    metr = price * sloy
    if s>20:
        discount = 0.9
        print ('Скидка 10%')
    elif s>10:
        discount = 0.95
        print ('Скидка 5%')
    else:
        print('Скидки нет')
        discount = 1
    print('Площадь детали', s)
    file.write('Площадь детали: ' + str(s) + '\n')
    print('Общая стоимость покраски без скидки: ', total, 'руб')
    file.write('Общая стоимость покраски без скидки: ' + str(total) + 'руб\n')
    print ('Стоимость покраски 1 квадратного метра с учётом всех слоев: ', metr, 'руб')
    file.write('Стоимость покраски 1 квадратного метра с учётом всех слоев: ' + str(metr) + 'руб\n')
    total_with_discount = total * discount
    with open('otchet.csv', 'a', newline='', encoding='cp1251') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow([i+1, s, sloy, total, discount, total_with_discount])
    all_price.append(total_with_discount)
    print('Итоговая стоимость с учётом скидки: ', total_with_discount, 'руб')
    file.write('Итоговая стоимость с учётом скидки:' + str(total_with_discount) + 'руб\n')

    
    if total_with_discount > max_price:
        max_price = total_with_discount
    if total_with_discount < min_price:
        min_price = total_with_discount
    

    
    


    total_all = total_all + total_with_discount
print('--- Итоговые стоимости всех деталей ---')
for i in range(len(all_price)):
    print (f'деталь №{i+1}: {all_price[i]} руб.')


file.close()    
print ('Общая стоимость всех деталей:', total_all)
print ('Самая дорогая деталь', max_price)
print ('самая дешевая деталь', min_price)
