# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0
month = 0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    principal = principal * (1+rate/12) - payment
    total_paid += payment

    if(month >= extra_payment_start_month and month <= extra_payment_end_month):
        principal -= extra_payment
        total_paid += extra_payment

    if(principal < 0):
        overpayment = principal * -1
        principal = 0
        total_paid -= overpayment
    
    # print(month + 1, round(total_paid, 2), round(principal, 2))
    print(f'{month + 1:<6d} {round(total_paid, 2):<16f} {round(principal, 2)}')

    month += 1

print(f'\nTotal paid: {round(total_paid, 2)}')
print(f'Months: {month}')