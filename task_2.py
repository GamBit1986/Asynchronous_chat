import json


list_of_orders = []


def write_order_to_json(item, quantity, price, buyer, date):
    with open("orders_1.json", "r", encoding="UTF-8") as f:
        data = json.load(f)

    with open("orders_1.json", "w", encoding="UTF-8") as f:
        list_of_orders = data["orders"]
        print(list_of_orders)
        order = {'item': item, 'quantity': quantity,
                 'price': price, 'buyer': buyer, 'date': date}
        list_of_orders.append(order)
        json.dump(data, f, indent=4, ensure_ascii=False)


write_order_to_json("холодильник", 10, 10000, 'Петров А.С.', "15.01.2023")
write_order_to_json("мухобойка", 100, 100, 'Сидоров С.С.', "15.05.2021")


