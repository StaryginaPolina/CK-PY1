salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

money_capital = 0  # количество денег, чтобы прожить 10 месяцев

for current_month in range(months):
    money_capital += spend - salary
    spend *= 1 + increase

print(round(money_capital))
