total_cost = float(input('Digite o valor do imóvel: \n'))

annual_salary = float(input('Digite o seu salário anual: \n'))

portion_saved = float(input('Digite a a porção mensal de salário economizada: \n'))

portion_down_payment = float(0.25)

down_payment = float(1 * total_cost)

current_savings = 0

r = 0.10

investments_return_monthly = float(r * current_savings / 12)

salary_saved_monthly = float(portion_saved * annual_salary / 12)

savings_total_monthly = float(salary_saved_monthly + investments_return_monthly)

months = 0

while current_savings < down_payment:
    current_savings = savings_total_monthly + current_savings
    investments_return_monthly = float(r * current_savings / 12)
    savings_total_monthly = float(salary_saved_monthly + investments_return_monthly)
    months = months + 1

print(months/12)

