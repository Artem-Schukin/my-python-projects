dishes = ["Салат", "Суп", "Котлеты"]

ingredients = [
    ["Лук", "Морковь", "Картофель"],   # для салата
    ["Лук", "Морковь", "Картофель"],   # для супа
    ["Лук", "Фарш"]                    # для котлет
]

norma = [
    [0.1, 0.05, 0.15],   # расход на 1 порцию салата
    [0.05, 0.05, 0.2],   # для супа
    [0.1, 0.15]          # для котлет
]
print(dishes)
bl = []
sklad = {}
for i in range (len(dishes)):
    print('Введите кол-во порций для', dishes[i])
    a = int(input())
    bl.append(a)
    for j in range(len(ingredients[i])):
        ing = ingredients[i][j]
        kol = bl[i]*norma[i][j]
        if ing in sklad:
          sklad[ing] = sklad[ing] + kol
        else:
           sklad[ing] = kol

print (sklad)
