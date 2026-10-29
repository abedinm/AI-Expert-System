# Lab Activity 1 - Exercise 2: Tax calculator
# Tax brackets (each rate applies only to the part of the income inside that bracket):
#   up to $10,000            ->  5%
#   $10,001 to $50,000       -> 10%
#   $50,001 to $100,000      -> 20%
#   over $100,000            -> 30%
# Example: $60,000 -> 10,000*5% + 40,000*10% + 10,000*20% = 500 + 4,000 + 2,000 = $6,500

income = float(input("Enter your income: $"))

# (upper limit of the bracket, rate); None means "no upper limit"
brackets = [(10000, 0.05), (50000, 0.10), (100000, 0.20), (None, 0.30)]

total_tax = 0
lower = 0
for upper, rate in brackets:
    if income <= lower:
        break
    if upper is None or income < upper:
        taxable = income - lower
    else:
        taxable = upper - lower
    tax = taxable * rate
    total_tax = total_tax + tax
    print(f"  ${taxable:,.2f} taxed at {rate * 100:.0f}% = ${tax:,.2f}")
    if upper is None:
        break
    lower = upper

print(f"Total tax owed on ${income:,.2f}: ${total_tax:,.2f}")
