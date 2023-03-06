import os


def make_cook_book():
    cook_book = {}
    with open("recipes.txt", encoding='UTF-8') as file:
        for string in file:
            ingredient_name = string.strip()
            quantity = int(file.readline())
            basket = []
            for i in range(quantity):
                ingr = file.readline().split(' | ')
                ingredients = {'ingredient_name': ingr[0].strip(), 'quantity': int(quantity),
                               'measure': ingr[-1].strip()}
                basket.append(ingredients)
            cook_book[ingredient_name] = basket
            file.readline()
    return cook_book


def get_shop_list_by_dishes(dishes: list, person_count=1):
    cook_book = make_cook_book()
    shop_list = {}
    for item in dishes:
        for ingredients in cook_book.get(item, []):
            if ingredients['ingredient_name'] in shop_list:
                shop_list[ingredients['ingredient_name']]['quantity'] += ingredients['quantity'] * person_count
            else:
                shop_list[ingredients['ingredient_name']] = {'quantity': ingredients['quantity'] * person_count,
                                                             'measure': ingredients['measure']}
    return shop_list


print(make_cook_book())
print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

path = 'C:\\Users\\denos\\Desktop\\Нетология\\ФАЙЛЫ\\'
path_2 = 'C:\\Users\\denos\\Desktop\\Нетология\\ФАЙЛЫ\\4.txt'


def create_files(path):
    files_list = os.listdir(path)
    files = {}
    for item in files_list:
        if item.rfind('.txt', -4) >= 0:
            with open(os.path.join(path, item), 'r', encoding='utf-8') as file:
                files[item] = file.readlines()
    with open(os.path.join(path_2), 'w', encoding='utf-8') as file:
        for file_name, rows in sorted(files.items(), key=lambda x: len(x[1])):
            file.write(file_name + '\n')
            file.write(str(len(rows)) + '\n')
            if '\n' not in rows[-1]:
                rows[-1] += '\n'
            file.write(''.join(rows))


create_files(path)
