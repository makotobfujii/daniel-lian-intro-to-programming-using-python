def recursion(n):
    if n == 0: 
        return 1
    else:
        return 2 * recursion(n-1)        

def getN():
    while True:
        try:
            n = int(input("Please enter a positive integer: "))

            if n < 0: 
                print("Invalid input. Please enter a positive integer.")
            else: 
                return n
        
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

if __name__ == "__main__":
    n = getN()
    recursiveOutput = recursion(n)
    print(recursiveOutput)