def recursive(x,n):
    """
    Prompt: Write arecursive mathematical definition for computing x^n for a positive integer "n" & a real number "x"
    """

    # Base Case 1: If "n" equals 0, return 1. Based on exponent rule where x^0 = 1
    if n == 0: 
        return 1

    # Base Case 2: If "n" equals 1, return x. Based on exponent rule where x^1 = x
    #elif n == 1: 
    #    return x

    # Recursive Case: If "n" is greater than 1, x^n = x * x^(n-1)
    else:    
        return x * recursive(x, n-1)

def get_xVal():
    while True:
        try:
            return float(input("Please enter a real number: "))
        except ValueError:
            print("Invalid input, please enter a valid real number.")

def get_nVal():
    while True:
        try:
            nVal = int(input("Please enter a positive integer: "))
            if nVal < 0:
                print("Please enter a non-negative integer.")
            else:
                return nVal
            
        except ValueError:
            print("Invalid input, Please enter a positive integer: ")

if __name__ == "__main__":
    # Galling methods to get inputs for recursive function
    x = get_xVal()
    n = get_nVal()

    # Calling recursive function and passing user defined input values
    output = recursive(x,n)
    print(output)

    
    