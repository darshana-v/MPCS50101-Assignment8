# Problem 3
# gcd
# Darshana Venkatadasan

def greatest_common_divisor(a, b):
    if b == 0:
        return a
    else:
        return greatest_common_divisor(b, a % b)

'''
# testing the function
try:   
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(greatest_common_divisor(a, b))
except:
    print("Invalid input. Please enter integers only.")

'''
