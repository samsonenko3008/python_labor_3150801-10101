# Задача 4: Рабочий график

# Задаем номер дня недели от 1 до 7 (1 — Понедельник, 7 — Воскресенье)
day_number = 3  # Любое число от 1 до 7

# Определение дня недели
if day_number == 1: day_name = "Понедельник"
elif day_number == 2: day_name = "Вторник"
elif day_number == 3: day_name = "Среда"
elif day_number == 4: day_name = "Четверг"
elif day_number == 5: day_name = "Пятница"
elif day_number == 6: day_name = "Суббота"
elif day_number == 7: day_name = "Воскресенье"
else: day_name = "Неизвестный день"

# Определение режима работы
if 1 <= day_number <= 5:
    status = "Рабочий день"
    schedule = "8:00 начало смены"
elif 6 <= day_number <= 7:
    status = "Выходной"
    schedule = "Отдых"
else:
    status = "Ошибка"
    schedule = "Неверный ввод"


# Вывод результатов
print(f"=== ГРАФИК РАБОТЫ ===")
print(f"День №{day_number}: {day_name}")
print(f"Статус: {status}")
print(f"Режим: {schedule}")
