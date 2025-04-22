import datetime

class GroceryStore: 
    def __init__(self): 
        self.stock = {} 
        self.sales = []

    def add_item(self, item_name, quantity, price, expiry_date=None):
     if item_name in self.stock:
        self.stock[item_name]['quantity'] += quantity
     else:
        self.stock[item_name] = {
            'quantity': quantity,
            'price': price,
            'expiry_date': expiry_date
        }
     print(f"Added {quantity} of {item_name} at Rs.{price} each. Expiry: {expiry_date if expiry_date else 'N/A'}")

    def update_stock(self, item_name, quantity):
     if item_name in self.stock:
        self.stock[item_name]['quantity'] += quantity
        print(f"Updated stock: {item_name} now has {self.stock[item_name]['quantity']} units.")
     else:
        print("Item not found in stock.")

    def purchase_item(self, item_name, quantity):
     if item_name in self.stock and self.stock[item_name]['quantity'] >= quantity:
        total_price = self.stock[item_name]['price'] * quantity
        self.stock[item_name]['quantity'] -= quantity
        sale_record = {
            'item': item_name,
            'quantity': quantity,
            'total_price': total_price,
            'date': datetime.datetime.now()
        }
        self.sales.append(sale_record)
        print(f"Purchased {quantity} of {item_name} for ${total_price:.2f}. Remaining stock: {self.stock[item_name]['quantity']}.")
     else:
        print("Insufficient stock or item not found.")

    def display_stock(self):
     print("\nCurrent Stock:")
     for item, details in self.stock.items():
        expiry = details['expiry_date'] if details['expiry_date'] else 'N/A'
        print(f"{item}: {details['quantity']} units, Price: Rs.{details['price']} each, Expiry: {expiry}")

    def display_expired_items(self):
     print("\nExpired Items:")
     today = datetime.date.today()
     for item, details in self.stock.items():
        if details['expiry_date']:
            expiry_date = datetime.datetime.strptime(details['expiry_date'], '%Y-%m-%d').date()
            if expiry_date < today:
                print(f"{item} expired on {details['expiry_date']}")

    def display_sales_report(self):
     print("\nSales Report:")
     total_income = 0
     for sale in self.sales:
        print(f"{sale['date']}: Sold {sale['quantity']} of {sale['item']} for Rs.{sale['total_price']:.2f}")
        total_income += sale['total_price']

store = GroceryStore()


store.add_item("Milk", 10, 30, "2025-04-21")
store.add_item("Bread", 15, 25, "2025-04-23")
store.add_item("Rice", 50, 60)  # No expiry


store.purchase_item("Milk", 2)
store.purchase_item("Bread", 1)


store.display_stock()


store.display_expired_items()


store.display_sales_report()
