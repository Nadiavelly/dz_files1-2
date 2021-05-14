def read_file(name_file):
    cook_book = dict()
    with open(name_file, encoding='utf-8') as f:
        data = f.readlines()
        k = 2
        name1 = data[0].strip()
        qu1 = int(data[1].strip())
        dish1 = []
        while data[k] != '\n':
            ingr = dict()
            s = data[k].split('|')
            ing = s[0].strip()
            qu = int(s[1].strip())
            meas = s[2].strip()
            ingr['ingredient_name'] = ing
            ingr['quantity'] = qu
            ingr['measure'] = meas
            dish1.append(ingr)
            k += 1
        cook_book[name1] = dish1
        n = k

        for i in data:
            if i == '\n':
                name = data[n + 1].strip()
                q = data[n + 2].strip()
                n += 3
                dish = []

                while n < len(data) and data[n] != '\n':
                    ingr = dict()
                    s = data[n].split('|')
                    ing = s[0].strip()
                    qu = int(s[1].strip())
                    meas = s[2].strip()
                    ingr['ingredient_name'] = ing
                    ingr['quantity'] = qu
                    ingr['measure'] = meas
                    dish.append(ingr)
                    n += 1
                cook_book[name] = dish
    return cook_book


def shop(dishes, person_count):
    cook_book = read_file('recipes.txt')
    shop_list = dict()
    for i in dishes:
        for ing in cook_book[i]:
            if ing['ingredient_name'] in dict.keys(shop_list):
                shop_list[ing['ingredient_name']]['quantity'] += ing['quantity']*person_count
            else:
                ing_dict = dict()
                ing_dict['measure'] = ing['measure']
                ing_dict['quantity'] = ing['quantity'] * person_count
                shop_list[ing['ingredient_name']] = ing_dict

    print(shop_list)


print(read_file('recipes.txt'))
dishes_list = ['Запеченный картофель', 'Омлет', 'Фахитос']
persons = 2
shop(dishes_list, persons)
