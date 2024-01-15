def multiply_by_2(a_dictionary):
    for key, value in a_dictionary.items():
        a_dictionary[key] = value *2
    return a_dictionary
        
a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
new_dict = multiply_by_2(a_dictionary)
print(new_dict)