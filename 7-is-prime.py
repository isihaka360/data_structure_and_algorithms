def is_prime(number):
    #checks whether a given integer is prime or not
    if number < 2:
        return False
    for i in  range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
if __name__ == "__main__":
    number = 19
    if is_prime(number):
         print(f"{number} is prime")
    else:
        print(f"{number} is not prime")