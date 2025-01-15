# Function to calculate simple interest
def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

# User inputs
principal = int(input("Enter the Principal amount: $"))
rate = int(input("Enter the annual rate of interest (in %): "))
time = int(input("Enter the time period (in years): "))

# Calculate and display simple interest
simple_interest = calculate_simple_interest(principal, rate, time)
print(f'The Simple Interest is: ${simple_interest}')
