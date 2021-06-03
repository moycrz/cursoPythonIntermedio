def run():
    # squares = []
    # for num in range(1, 101):
    #     if num % 3 != 0:
    #         squares.append(num**2)
    #     else:
    #         continue
    ### We can replace all the code above this line, with the following line of code.
    # squares = [i**2 for i in range(1,101) if i % 3 != 0]
    # print(squares)

    ##The next line is a class exercise.
    challenge = [i for i in range(1, 10000) if i%4 == 0 and i%6==0 and i%9 ==0]
    print(challenge)


if __name__ == '__main__':
    run()