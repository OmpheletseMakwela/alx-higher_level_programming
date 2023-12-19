#!/user/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    i = 0

    while i < x:
        try:
            value = my_list[i]
            if isinstance(value, int):
                print("{:d}".format(value), end="")
                count += 1
        except IndexError as e:
            print()
            raise e
        i += 1

    print()
    return count
