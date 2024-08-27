
import pprint

def make_cook_book(file):
    with open (file, "r", encoding='utf-8') as f:
        name_dish = []
        ingridient_list_all = []
        ingridient_nums = []
        new_list = []
        n1 = 0
        n = 0

        for line in f:

            line_n = line.strip()
            if '1' not in line_n and '2' not in line_n and '3' not in line_n and '4' not in line_n and '5' not in line_n and '6' not in line_n and '7' not in line_n and '8' not in line_n and '9' not in line_n and '0' not in line_n and len(line_n) != 0:
                name_dish.append(line_n)
            elif ' | ' in line_n:
                parts = line_n.split(' | ')
                ingridients = {'ingridient_name': parts[0], 'quantity': parts[1], 'measure': parts[2]}
                ingridient_list_all.append(ingridients)
            elif len(line_n) == 1:
                ingridient_nums.append(int(line_n) + n)
                n = int(line_n) + n
        for ns in ingridient_nums:
            new_list.append(ingridient_list_all[n1:ns])
            n1 = ns

        cook_Book = dict(zip(name_dish, new_list))
        return cook_Book


def get_shop_list_by_dishes(dishes, person_count):
    my_cook_book = make_cook_book('recipe.txt')
    ingridients_dict = {}
    for dish in dishes:
        if dish in my_cook_book.keys():
            for item in my_cook_book[dish]:
                if item['ingridient_name'] not in ingridients_dict.keys():
                    ingridients_dict[item['ingridient_name']] = {
                            'measure': item['measure'],
                            'quantity': 0
                        }
                ingridients_dict[item['ingridient_name']]['quantity'] += int(item['quantity']) * person_count
    return ingridients_dict

print(make_cook_book('recipe.txt'))

pprint.pp(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2))



def read_and_sort(files, file):
    merged_text = {}
    for items in files:
        with open(items, 'r', encoding="utf-8") as f:
            lines = f.readlines()
            merged_text[len(lines)] = f'{items}\n{len(lines)}\n{"".join(lines)}\n'

    sorted_merged_text = dict(sorted(merged_text.items()))

    with open(file, 'w') as f:
        for key, value in sorted_merged_text.items():
            f.writelines(f'{value}')

    return 0

read_and_sort(['1.txt', '2.txt', '3.txt'], 'final.txt')





