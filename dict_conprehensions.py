def run():
    my_dict = {key:key**2 for key in range(1,101) if key % 3 != 0}
    print(my_dict)


if __name__ == '__main__':
    run()