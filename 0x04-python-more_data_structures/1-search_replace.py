def search_replace(my_list, search, replace):
    new_list = [replace if val == search else val for val in my_list]
    return new_list

my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
new_list = search_replace(my_list, 2, 89)

print(new_list)
print(my_list)