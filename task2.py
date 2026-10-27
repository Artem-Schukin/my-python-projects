ewe = []
count = int(input('Сколько всего чисел?'))
for i in range (count):
    num = float(input(f'Введите число{i+1}:'))
    ewe.append(num)

print(ewe)
print(sum(ewe))
total = sum(ewe)
average = total/count
print(average)