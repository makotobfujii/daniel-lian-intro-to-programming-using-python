def recursive(n):

    if n == 1: 
        return 1

    else:
        return n + recursive(n - 1)

while True: 
    try:    
        n = int(input("Enter a positive integer: "))
        if n > 0:
            break
        else: 
            print("Invalid input. Please enter a positive integer.")

    except ValueError:
        print("Invalid input. Please enter a positive integer.")

print(recursive(n))

