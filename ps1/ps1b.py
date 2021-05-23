#saving, with a raise
#factoring in a raise every six month

annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
total_cost = float(input('Enter the cost of your dream home: '))
semi_annual_raise = float(input('Enter the semi-annual raise, as a decimal: '))


portion_down_payment = total_cost * 0.25
monthly_salary = annual_salary / 12
current_saving = 0.0
r = 0.04
month = 0

while current_saving <= portion_down_payment:
    current_saving += current_saving * r/12
    current_saving += monthly_salary * portion_saved
    month += 1
    if month%6 == 0:
        monthly_salary += monthly_salary * semi_annual_raise 

print(f'Number of months: {month}')