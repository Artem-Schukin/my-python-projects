n = []
count = int(input('Введите числа?'))
for i in range (count):
    num = float(input(f'Введите числа{i+1}:'))
    n.append(num)

print(n[-1])
