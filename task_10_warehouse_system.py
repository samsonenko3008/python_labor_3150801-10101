# Задача 10: Система учёта склада

# 1. Создание базы данных материалов (вложенные словари)
warehouse = {
    "Кирпич": {"quantity": 5000, "price": 12.50, "min_quantity": 1000},
    "Цемент": {"quantity": 120, "price": 450.00, "min_quantity": 50},
    "Песок": {"quantity": 8, "price": 800.00, "min_quantity": 10},
    "Арматура": {"quantity": 30, "price": 48000.00, "min_quantity": 20},
    "Бетон": {"quantity": 45, "price": 4200.00, "min_quantity": 15}
}

# 2. Расчет общей стоимости и поиск самого дорогого товара
total_warehouse_value = 0
most_expensive_name = ""
max_item_cost = 0
critical_items = []

for name, data in warehouse.items():
    item_cost = data["quantity"] * data["price"]
    total_warehouse_value += item_cost
    
    # Поиск самого дорогого запаса
    if item_cost > max_item_cost:
        max_item_cost = item_cost
        most_expensive_name = name
        
    # Проверка критических остатков
    if data["quantity"] < data["min_quantity"]:
        critical_items.append(f"{name}: {data['quantity']} < {data['min_quantity']}")


# 3. Таблица
print("=" * 65)
print("СИСТЕМА УЧЁТА СКЛАДА")
print("=" * 65)
# Заголовки согласно заданию
print(f"{'Материал':<12} | {'Кол-во':<8} | {'Цена':<8} | {'Мин.':<6} | {'Стоимость'}")
print("-" * 65)

for name, data in warehouse.items():
    # Считаем стоимость для каждой позиции
    item_cost = data["quantity"] * data["price"]
    
    # Определяем, нужен ли восклицательный знак (критический остаток)
    status_mark = "!!!" if data["quantity"] < data["min_quantity"] else ""
    
    # Печать строки таблицы
    print(f"{name:<12} | {data['quantity']:<8} | {data['price']:<8.2f} | {data['min_quantity']:<6} | {item_cost:<10.2f} {status_mark}")

print("=" * 65)
print(f"ОБЩАЯ СТОИМОСТЬ: {total_warehouse_value:.2f}")
print(f"Самый дорогой: {most_expensive_name}")

if critical_items:
    print("\nКРИТИЧЕСКИЕ ОСТАТКИ:")
    for item in critical_items:
        print(item)

# Имитация выдачи
print("\n=== ВЫДАЧА МАТЕРИАЛА ===")
print(f"Выдано 25 ед. Цемент")
warehouse["Цемент"]["quantity"] -= 25
print(f"Новый остаток: {warehouse['Цемент']['quantity']}")








   
