def get_data(file_name):
    # global dish, cook_book, dish_count
    dish = []
    cook_book = {}
    dish_count = -1

    with open(file_name) as file:
        for line in file:
            dish.append(line.strip())
            dish_count += 1
            cook_book[dish[dish_count]] = []
            ingredients_quantity = int(file.readline().strip())
            for ingredient in range(ingredients_quantity):
                component = file.readline().strip().split(' | ')
                cook_book[dish[dish_count]].append({'ingredient_name': component[0],
                                                    'quantity': component[1], 'measure': component[2]})
            file.readline()

    return cook_book

result = get_data('recipes.txt')


print(result)
for key, value in result.items():
     print(key)
     for i in range(len(value)):
         print(value[i])


print('___________________Разделитель_______далее задача №2___________')

dishes_list = ['Омлет', 'Фахитос']
person = 2


def get_shop_list_by_dishes(dishes, person_count):
    dish_list = {}
    for k in range(len(dishes)):
        for i in range(len(result[dishes[k]])):
            if dish_list.get(result[dishes[k]][i]['ingredient_name']):
                quantity_count = (dish_list[result[dishes[k]][i]['ingredient_name']]['quantity'])
                dish_list[result[dishes[k]][i]['ingredient_name']] = {'measure': result[dishes[k]][i]['measure'],
                                      'quantity': int(result[dishes[k]][i]['quantity']) * person_count + quantity_count}
            else:
                dish_list[result[dishes[k]][i]['ingredient_name']] = {'measure': result[dishes[k]][i]['measure'],
                                                          'quantity': int(result[dishes[k]][i]['quantity']) * person_count}
    return dish_list

dish_list = get_shop_list_by_dishes(dishes_list, person)

print(dish_list)

for key, value in dish_list.items():
    print(f'{key} : {value}')
