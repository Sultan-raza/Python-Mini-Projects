print("Welcome to the Currency Converter!\n")

# User inputs
amount = float(input("Enter the amount to convert: "))
print("Available currencies: USD, EUR, GBP")
source_currency = input("Enter the source currency (e.g., USD): ").upper()
target_currency = input("Enter the target currency (e.g., EUR): ").upper()

# Conversion rates
conversion_rates = {
    "USD": {"EUR": 0.85, "GBP": 0.75},
    "EUR": {"USD": 1.18, "GBP": 0.88},
    "GBP": {"USD": 1.34, "EUR": 1.14}
}

# Currency conversion
if source_currency in conversion_rates and target_currency in conversion_rates[source_currency]:
    converted_amount = amount * conversion_rates[source_currency][target_currency]
    print(f"{amount} {source_currency} is equal to {converted_amount:.2f} {target_currency}")
else:
    print("Invalid currency input!")
