from pprint import pprint

cook_book = {}

with open("recipe1.txt", 'r', encoding="utf-8") as file1:
    for line1 in file1:
        new_diches = line1.strip()
        quantity = int(file1.readline())
        recept = []
        cook_book[new_diches] = recept

        for ingr in range(quantity):
            quan_ingr = {}
            ingr = file1.readline().strip()
            ingr = ingr.split('|')
            quan_ingr['ingredient_name'] = ingr[0]
            quan_ingr['quantity'] = ingr[1]
            quan_ingr['measure'] = ingr[2]

            recept.append(quan_ingr)
        file1.readline()
pprint(cook_book)
print("***************************")


# pprint(cook_book['Омлет'])

def get_shop_list_by_dishes(dishes1, person_count):
    result = {}
    for dish in dishes1:

        ingrid = cook_book[dish]
        for ingr1 in ingrid:
            if ingr1['ingredient_name'] not in result.keys():
                ingr_name = ingr1['ingredient_name']
                ingr_quantity = int(ingr1['quantity'])* person_count
                ingr_measure = ['measure']
            else:
                ingr_quantity += int(ingr1['quantity']) * person_count

            result[ingr_name] = {'quantity': ingr_quantity, 'measure' : ingr_measure}

    return result



pprint(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2))
