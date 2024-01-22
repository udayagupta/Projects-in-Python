import datetime as dt
import os

class Bakery:
    def __init__(self, order_items: list) -> None:
        self.total_orders = {}
        self.order_items = order_items
        
    def add_order(self, customerName: str, orderItem: str, orderQuantity: int, due_date: str):
        length_total_order = len(self.total_orders)
        order_id = length_total_order + 1
        order = Order(customerName, orderItem, orderQuantity, order_id, due_date)
        self.total_orders[order_id] = order        

    def view_order(self, orderId: int):
        if orderId in self.total_orders:
            return self.total_orders[orderId]
        else:
            return False
    
    def display_orders(self):
        print("BAKERY'S ORDERS".center(70, "-"))
        for _ , order in self.total_orders.items():
            print_order_details(order)


class Order:
    def __init__(self, customer_name: str, order_item: str, order_quantity: int, order_id: int, due_date: str) -> None:
        datetime = dt.datetime.now()
        date = datetime.date().strftime("%d-%m-%Y")
        time = datetime.time().strftime("%I:%M %p")
        self.customer_name = customer_name or "N/A"
        self.order_item = order_item
        self.order_quantity = order_quantity
        self.order_id = order_id
        self.date = date
        self.time = time
        self.due_date = due_date


def print_order_details(order):

    print(f"Customer Name: {order.customer_name}")
    print(f"Order Item: {order.order_item}")
    print(f"Order Quantity: {order.order_quantity}")
    print(f"Order ID: {order.order_id}")
    print(f"Date: {order.date}")
    print(f"Time: {order.time}")
    print(f"Due Date: {order.due_date}")
    print("-"*70)


def clear_screen():
    os.system("cls")


def make_order() -> dict:

    name = input("Customer Name: ").strip()

    print("Bakery Items".center(70, "-"))
    for index, item in enumerate(order_items, start=1):
        print(f"{index}: {item}")
    print("Bakery Items".center(70, "-"))
    
    order_item = input("Order Item: ")
    
    while not order_item.isdigit() or int(order_item) > len(order_items):
        order_item = input("Invalid!\nOrder Item: ")

    quantity = input("Order Quantity: ")

    while not quantity.isdigit():
        quantity = input("Invalid!\nOrder Quantity: ")

    quantity = int(quantity)

    while True:
        try:
            due_date = input("Date Format: 'dd-mm-yyyy(full-year)'\nDue Date: ")
            due_date = dt.datetime.strptime(due_date, "%d-%m-%Y").strftime("%d-%m-%Y")
            break
        except:
            print("Wrong Date Format!")


    return {"customerName": name,
            "orderItem": order_items[int(order_item)-1],
            "orderQuantity": quantity,
            "due_date": due_date}


def display_orders():
    bakery.display_orders()

def view_order():
    orderID = input("Order ID: ")
    
    while not orderID.isdigit():
        orderID = input("Invalid!\nOrder ID: ")
    
    order_to_view = bakery.view_order(int(orderID))
    if order_to_view:
        print_order_details(order_to_view)
    else:
        print("Wrong ID")

def _continue_():
    input("Press Enter to Continue...")

# You can add more items
order_items = ["Cake", "Pastry", "Pan Cake"]

bakery = Bakery(order_items)


while True:
    clear_screen()
    print(f"BAKERY MANAGEMENT SYSTEM".center(70, "-"))
    print("1. MAKE A ORDER")
    print("2. VIEW ORDER BY ID")
    print("3. DISPLAY ALL THE ORDER")

    choice = input("Enter your choice: ").strip()

    
    match choice:
        case "1":
            customer_order = make_order()
            bakery.add_order(customer_order["customerName"],
                             customer_order["orderItem"],
                             customer_order["orderQuantity"],
                             customer_order["due_date"])
            print("Order Added")
            _continue_()
        case "2":
            if not len(bakery.total_orders):
                print("No orders have been made yet")
            else:
                view_order() 
            _continue_()
        case "3":
            if not len(bakery.total_orders):
                print("No orders have been made yet")
            else:
                display_orders()
            _continue_()

        case _:
            print("Invalid Input!")

