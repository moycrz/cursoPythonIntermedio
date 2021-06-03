def divisors(num):
    divisors = [i for i in range(1, num +1) if num % i == 0]
    # for i in range(1, num + 1):
    #     if num % i == 1:
    #         divisors.append(i)
    return divisors

def run():
    num = input('Enter a number: ')
    assert num.isnumeric() and int(num) >= 0, "You can't use strings or negative numbers" 
    #.isnumeric() it's a special moddle of strings
    
    print(divisors(int(num)))
    print("End of progam...")   


if __name__ == '__main__':
    run()