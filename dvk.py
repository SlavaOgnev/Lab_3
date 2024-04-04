from datetime import datetime

# sПолучаем текущую дату
current_date = datetime.now()

# Получаем дату Нового года для текущего года
new_year = datetime(current_date.year + 1, 1, 1)

# Вычисляем количество дней до Нового года
days_left = (new_year - current_date).days

# Записываем результат в файл
with open('dvk.txt', 'w') as file:
file.write(f'До Нового года осталось {days_left} дней')
