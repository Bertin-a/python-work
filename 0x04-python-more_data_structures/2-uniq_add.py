def uniq_add(my_list=[]):
    s = set(my_list)
    my_list = list(s)
    return sum(my_list)
my_list = [1, 2, 3, 1, 4, 2, 5]
result = uniq_add(my_list)
print("Result: {:d}".format(result))
