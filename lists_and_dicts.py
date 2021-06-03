def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Moises", "lastname": "Cruz"}

    super_list = [
        {"firstname": "Moises", "lastname": "Cruz"},
        {"firstname": "Miguel", "lastname": "Torres"},
        {"firstname": "Pepe", "lastname": "Rodelo"},
        {"firstname": "Susana", "lastname": "Martinez"},
        {"firstname": "Monica", "lastname": "Onofre"},
    ]

    super_dict ={
        "natural_nums": [1,2,3,4,5],
        "integers_nums": [-1,-2,0,1,2],
        "floating_nums": [1.1,4.5,6.43],
    }

    for key, value in super_dict.items():
        print(f"{key} - {value}")

    for values in super_list:
        for keys, values in values.items():
            print(f"{keys} - {values}")


if __name__ == '__main__':  
    run()