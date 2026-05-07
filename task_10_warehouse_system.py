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
