order_name = input("Название заказа: ")
customer_name = input("Имя заказчика: ")

item1_name = input("\nНазвание позиции 1: ")
item1_qty = int(input("Количество позиции 1: "))
item1_price = float(input("Цена позиции 1 (руб.): "))

item2_name = input("\nНазвание позиции 2: ")
item2_qty = int(input("Количество позиции 2: "))
item2_price = float(input("Цена позиции 2 (руб.): "))

delivery = float(input("\nСтоимость доставки (руб.): "))
paid = float(input("Внесённая сумма (руб.): "))

item1_total = item1_qty * item1_price          
item2_total = item2_qty * item2_price         
goods_total = item1_total + item2_total        
order_total = goods_total + delivery          
total_qty = item1_qty + item2_qty              
change = paid - order_total                    

print("\n" + "=" * 52)
print(f"ЗАКАЗ: {order_name}")
print(f"Заказчик: {customer_name}")
print("=" * 52)
print(f"{item1_name} | {item1_qty} | {item1_price:.2f} | {item1_total:.2f}")
print(f"{item2_name} | {item2_qty} | {item2_price:.2f} | {item2_total:.2f}")
print("-" * 52)
print(f"Товары без доставки:  {goods_total:.2f} руб.")
print(f"Доставка:             {delivery:.2f} руб.")
print(f"ИТОГО с доставкой:    {order_total:.2f} руб.")
print(f"Всего единиц:         {total_qty}")
print(f"Сдача:                {change:.2f} руб.")
print("=" * 52)