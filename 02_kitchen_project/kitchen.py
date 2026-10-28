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
zakaz = []
total_zakaz = []
for i in range (len(dishes)):
    print('Введите кол-во порций для', dishes[i])
    a = int(input())
    bl.append(a)
    for j in range(len(ingredients[i])):
        ing = ingredients[i][j]
        kol = bl[i]*norma[i][j]
        if ing in zakaz:
            index = zakaz.index(ing)
            total_zakaz[index] = total_zakaz[index] + kol
        else:
            zakaz.append(ing)
            total_zakaz.append(kol)


print (total_zakaz)
print (zakaz)
