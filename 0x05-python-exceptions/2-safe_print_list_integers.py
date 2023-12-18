#!/user/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    integer = 0
    try:
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                integer += 1
    except IndexError:
        pass
    finally:
        print()
        return integer
    
