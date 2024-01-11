def no_c(my_string):
    new_string = ''
    for i in range(len(my_string)):
        if 'c' == my_string[i] or 'C' == my_string[i]:
            continue
        new_string += my_string[i]
    return new_string
print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))
