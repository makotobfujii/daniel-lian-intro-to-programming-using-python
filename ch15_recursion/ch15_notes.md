# Chapter 15 - Recursion

## Notes
- Recursive functions require a base case aka a stopping condition as well as a recursive case
- Recursive functions need to be reduced down to a stopping case to terminate
- **Direct Recursion:** Recursive function that invokes itself
- **Indirect Recursion:** When function A invokes function B, which in turn invokes function A etc. Can involve more than just 2 functions. 
- **Infinite Recursion:** Where a recursive function does not reduce the problem down to the base case

## Checkpoint 1 Questions
#### 15.1 What is a recursive function?
```
A function that calls itself
```
#### 15.2 How many times would the factorial function in Listing 15.1 be invoked for factorial(6)?
```
7
```
#### 15.6 What is an infinite recursion? What is a direct recursion? What is an indirect recursion?
```
Direct Recursion: Recursive function that invokes itself
Indirect Recursion: When function A invokes function B, which in turn invokes function A etc. Can involve more than just 2 functions. 
Infinite Recursion: Where a recursive function does not reduce the problem down to the base case
```
#### 15.7 How many times would the fib() function in ComputeFibonacci.py be invoked for fib(6)?
```
fib(6)
├── fib(5)
│   ├── fib(4)
│   │   ├── fib(3)
│   │   │   ├── fib(2)
│   │   │   │   ├── fib(1)
│   │   │   │   └── fib(0)
│   │   │   └── fib(1)
│   │   └── fib(2)
│   │       ├── fib(1)
│   │       └── fib(0)
│   └── fib(3)
│       ├── fib(2)
│       │   ├── fib(1)
│       │   └── fib(0)
│       └── fib(1)
└── fib(4)
    ├── fib(3)
    │   ├── fib(2)
    │   │   ├── fib(1)
    │   │   └── fib(0)
    │   └── fib(1)
    └── fib(2)
        ├── fib(1)
        └── fib(0)

fib(6) is called once.
fib(5) is called once.
fib(4) is called twice.
fib(3) is called three times.
fib(2) is called five times.
fib(1) is called eight times.
fib(0) is called five times.

Summing these up, the total number of calls is 1 + 1 + 2 + 3 + 5 + 8 + 5 = 25.

So, the function fib() will be called 25 times for fib(6)
```
#### 15.8 Show the output of the following programs and identify their base cases and recursive calls:
```python
def f(n):
    if n == 1:
        return 1
    else:
        return n + f(n - 1)
print("Sum is", f(5))

# OUTPUT: Sum is 15
# BASE CASE: if n == 1: return 1
```
```python
def f(n):
    if n > 0:
        print(n % 10)
    f(n // 10)
f(1234567)

# OUTPUT: RecursionError: maximum recursion depth exceeded in comparison
# BASE CASE: The base case is missing because the f(n // 10) is outside of the condtion if n > 0. Therefore, the recursive call of f(n // 10) still runs when n == 0. To correct this the proper code with a base case would be:
def f(n):
    if n > 0: 
        print(n % 10)
        f(n // 10) # This will properly reduce n to the base case and stop the recursion once n == 0 
```