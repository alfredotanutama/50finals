from helper import*

def dbg_dis1(categories, rice, vegetable, protein, other):
    print(f'----------')
    print(f'Categories are {categories}') # -- ['Rice', 'Vegetable', 'Protein', 'Other']
    print(f'----------')
    print(f'rice: {rice}')
    print(f'----------')
    print(f'vegetable: {vegetable}')
    print(f'----------')
    print(f'protein: {protein}')
    print(f'----------')
    print(f'other: {other}')
    print(f'----------')

def dbg_dis3(list):
    print('Display Selected List!!')
    print(list)
    print('Display Price From Each List!!')
    for item in list:
        print(item[0])
        # get_price_from_db(item[0])

