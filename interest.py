# Compound interest calculator in Python

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time period in years: "))

interest = principal * rate * time
compound_interest = principal * (pow(1 + rate, time) - 1)

print(f"Simple interest: {interest}")
print(f"Compound interest: {compound_interest}")\
