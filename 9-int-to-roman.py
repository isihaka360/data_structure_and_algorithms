#function def ........
def int_to_roman(n):
    numbers = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
    roman = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
    i=12
    roman_numerals = ""
    while n!=0:
        if numbers[i]<=n:
            roman_numerals+=roman[i]
            n=n-numbers[i]
        else:
            i-=1
    return roman_numerals

# user input button.....
user_input_button=int(input("Enter number:"))
print("The number entered is equivalent to ", int_to_roman(user_input_button),"roman numeral")