# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

# pays extra 1000$/month on these months
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000
months = 0

while principal > 0:
    months += 1
    if extra_payment_start_month <= months <= extra_payment_end_month:
        extra_payment = 1000
    else:
        extra_payment = 0
    if principal*(1+rate/12) < (payment + extra_payment):
        payment = principal*(1+rate/12)
        extra_payment = 0
    principal = principal * (1 + rate / 12) - payment - extra_payment

    total_paid = total_paid + payment + extra_payment
    print(months, round(total_paid, 2), round(principal, 2))


print('Total paid', total_paid)
print('Total months', months)
