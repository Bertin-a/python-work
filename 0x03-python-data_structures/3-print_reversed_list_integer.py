def print_reversed_list_integer(my_list=[]):
    my_list.sort(reverse = True)
    for item in my_list:
        print('{:d}'.format(item))

my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)