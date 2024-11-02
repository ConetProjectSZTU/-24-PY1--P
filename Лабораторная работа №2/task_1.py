salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

# Инициализация переменных
money_capital = 0
total_spend = 0

# Цикл для расчета суммарных расходов за 10 месяцев
for i in range(months):
    if i == 0:
        total_spend += spend
    else:
        spend *= (1 + increase)
        total_spend += spend

# Расчет необходимой подушки безопасности
money_capital = total_spend - (salary * months)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital))
