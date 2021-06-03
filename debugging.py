def divisors(num):
    divisors = [i for i in range(1, num +1) if num % i == 0]
    # for i in range(1, num + 1):
    #     if num % i == 1:
    #         divisors.append(i)
    return divisors

def run():
    try:
        num = int(input('Enter a number: '))
        if num < 0:
            raise Exception("Negative number is invalid")
        print(divisors(num))
        print("End of progam...")   

    except ValueError:
        print("You can only add numbers")
    except Exception as ve:
        print(ve)

if __name__ == '__main__':
    run()