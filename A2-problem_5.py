# Problem 5
# divisibility by 11
# Darshana Venkatadasan

def divisible_by_11(number):
    # args: number (int)
    # returns (bool): True if the number is divisible by 11, False otherwise

    # check if input is a valid number
    # isinstance checks if the input is an integer
    if not isinstance(number, int):
        return False

    number_str = str(number)
    # calculating alternate sum of the digits
    alternating_sum = 0
    for i, digit in enumerate(number_str):
        # i = count, digit = value
        if (i%2 == 0):
            alternating_sum += int(digit)
        else:
            alternating_sum -= int(digit)

    return (alternating_sum%11 == 0)

# to implement the function
if __name__ == "__main__":
    try:
        n = int(input("Enter the number: "))
        if(divisible_by_11(n)):
            print("Divisible by 11!")
        else:
            print("Not divisible by 11")
    except:
        print("Invalid Input! Please enter a positive integer.")
