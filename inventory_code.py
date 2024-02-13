import datetime

class Product:
    def __init__(self, name, description, price, quantity, supplier):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        self.supplier = supplier

class Sale:
    def __init__(self, product_name, quantity_sold, total_amount):
        self.product_name = product_name
        self.quantity_sold = quantity_sold
        self.total_amount = total_amount
        self.timestamp = datetime.datetime.now()

class InventoryManagementSystem:
    def __init__(self):
        self.products = []
        self.sales = []
    
    def add_product(self, product):
        self.products.append(product)
    
    def update_product(self, product_name, new_price):
        for product in self.products:
            if product.name == product_name:
                product.price = new_price
                return True
        return False
    
    def remove_product(self, product_name):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                return True
        return False
    
    def sell_product(self, product_name, quantity_sold):
        for product in self.products:
            if product.name == product_name:
                if product.quantity >= quantity_sold:
                    product.quantity -= quantity_sold
                    sale_amount = product.price * quantity_sold
                    sale_record = Sale(product.name, quantity_sold, sale_amount)
                    self.sales.append(sale_record)
                    return True
                else:
                    print("Error: Not enough quantity in stock.")
                    return False
        print("Error: Product not found.")
        return False
    
    def generate_sales_report(self):
        # Generate a simple sales report
        print("Sales Report:")
        for sale in self.sales:
            print(f"Product: {sale.product_name}, Quantity Sold: {sale.quantity_sold}, Total Amount: {sale.total_amount}, Time: {sale.timestamp}")
    
    def generate_low_stock_notification(self, threshold):
        # Generate low stock notifications
        for product in self.products:
            if product.quantity < threshold:
                print(f"Low stock notification for {product.name}")
    
    def record_stock(self):
        # Record current stock levels
        print("Stock Record:")
        for product in self.products:
            print(f"Product: {product.name}, Quantity: {product.quantity}")

# Example usage:
if __name__ == "__main__":
    inventory_system = InventoryManagementSystem()
    
    # Adding products
    product1 = Product("Laptop", "Dell XPS 15", 1500, 10, "Dell")
    product2 = Product("Smartphone", "iPhone 13", 999, 20, "Apple")
    inventory_system.add_product(product1)
    inventory_system.add_product(product2)
    
    # Selling products
    inventory_system.sell_product("Laptop", 5)
    inventory_system.sell_product("Smartphone", 15)
    
    # Updating product price
    inventory_system.update_product("Laptop", 1600)
    
    # Generating sales report
    inventory_system.generate_sales_report()
    
    # Generating low stock notification
    inventory_system.generate_low_stock_notification(10)
    
    # Recording current stock levels
    inventory_system.record_stock()

