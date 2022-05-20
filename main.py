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
