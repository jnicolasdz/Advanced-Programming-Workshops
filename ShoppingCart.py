import string
import Product
from datetime import datetime

class ShoppingCart:

    def __init__(self) -> None:
        self.name = 'Shopping Cart'
        self.products_list = []

    
    def show_products(self) -> Product:
        return self.products_list
    
    def add_product(self, product : Product) -> None:
        self.products_list.append(product)
        

    def make_check_out(self, name : string, direction : string) -> string:
        checkout = f"Checkout:\nName: {name}\nDirection: {direction}\nDate: {datetime.now()}\nProducts\n"
        for i in self.products_list:
            checkout += f"{i.name}: f{i.amount}\n"
        return checkout;
