def mult_list(lst):
    result = 1
    for num in lst:
        result *= num
    return result
print("Product of list is:",mult_list([1, 2, 3]))