def get_products_of_all_ints_except_at_index(int_list):
    # Make a list with the products
    products = []
    p = 1
    if len(int_list) < 2:
        raise IndexError('Getting the product of numbers at other '
                         'indices requires at least 2 numbers')
    for i in range(len(int_list)):
        products.insert(i, p)
        p = p * int_list[i]

    p = 1
    for i in range(len(int_list) - 1, -1, -1):
        products[i] = products[i] * p
        p = p * int_list[i]

    return products


li=[1,2,3]
print(get_products_of_all_ints_except_at_index(li))