def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        max = 0
        for i in my_list:
            if max < i:
                max = i
        return max
    
my_list = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))

