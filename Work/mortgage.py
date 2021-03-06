# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0

while principal > 0:
    principal = principal * (1 + rate/12) - payment
    total_paid = total_paid + payment
    month = month + 1
    if month % 12 == 0:
        print(f'Sum paid after {month} months is {round(total_paid, 2)}')

print(f'Total paid is {total_paid} or rounded to two decimals {round(total_paid, 2)}')
