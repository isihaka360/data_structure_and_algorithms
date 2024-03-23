def factorize(number:int):
    assert number > 0 
    
    """The function will be working for printing factorization of a number
       function will require only one argument as factorial number"""
       
    factors = []
    divisor = 2
    while divisor <= number:
        
        if number % divisor == 0:
            factors.append(divisor)
            number //= divisor
        else:
            
            divisor += 1
            
    return factors 

if __name__ == "__main__":
    number = 129
    factors = factorize(number)
    print(f"The prime fctors of {number} are:{factors}")