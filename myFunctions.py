# arb_args function
def arb_args(*args):
    for arg in args:
        print(arg)

# inner_func function
def inner_func(a, b):
    def add():
        return a + b

    def multiply():
        return a * b

    result = add() + multiply()
    print(result)

# lunch_lady function
def lunch_lady(student_name, lunch_preference="Mystery Meat"):
    print(student_name, lunch_preference)

# sum_n_product function
def sum_n_product(a, b):
    return a + b, a * b

# alias_arb_args function
alias_arb_args = arb_args

# arb_mean function
def arb_mean(*args):
    if args:
        average = sum(args) / len(args)
        print(average)
    else:
        print("No numbers provided")

# arb_longest_string function
def arb_longest_string(*args):
    if args:
        return max(args, key=len)
    else:
        return None
