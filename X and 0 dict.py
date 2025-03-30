lst_in = ['# x o', 'x # x', 'o o #']

list_conv = list(map(lambda x: [i for i in x if i!=' '], lst_in))

print(list_conv)

def is_free(lst):
    res = any(map(lambda x: [i for i in x if i == '#'], lst))
    return res

print(is_free(list_conv))