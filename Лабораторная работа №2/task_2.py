money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
months = 0
current_balance = money_capital + salary

while current_balance >= spend:
    months += 1
    current_balance -= spend
    spend *= (1 + increase)  # Увеличиваем расходы на следующий месяц
    current_balance += salary

print("Количество месяцев, которое можно протянуть без долгов:", months)
