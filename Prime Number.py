print("Welcome to the Prime Number Checker!")

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

number = int(input("Enter your number: "))

if is_prime(number):
    print(f"{number} is a Prime Number.")
else:
    print(f"{number} is Not a Prime Number.")
