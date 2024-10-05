"""
This module is for general Shopping Cart .

Copyright (C) 2024  Nicolás Diaz Salamanca <jndiasz@udistrital.edu.co>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import Product
from User import User
from datetime import datetime

class ShoppingCard :

    def __init__(self) -> None:
            self.list_products = []

    def show_products(self) :
        """This method shows the products of the shopping cart"""
        print('Shopping Cart:')
        for product in self.list_products:
            print(product)
    
    def add_product(self, product: Product) -> None:

        """This method adds a product to the shopping cart
        Args:
            product (Product): product to add
        """
        if product.is_available(1):
            product.change_stock(-1)
            self.list_products.append(product)
            product.amount += 1
            print(f"{product.name} added to the shopping cart")

        else: 
            print("Not enough stock")

    def make_checkout(self) -> str:
        
        """This method makes the checkout
        Args:
            None
        Returns:
            str: checkout
        """
        print("Enter your data to make the checkout\n")
        name = input("Enter your name: ")
        lastname = input("Enter your last name: ")
        direction = input("Enter your address: ")
        credit_card = input("Enter your credit card: ")
        country = input("Enter your country: ")
        user = User(name, lastname, direction, credit_card, country)
        checkout = f"Checkout:\nName: {user.name}\nCountry: {user.country}\nDirection: {user.address}\n \
        Date: {datetime.now()}\nProducts:\n"
        for i in self.list_products:
            checkout += f"{i.name}: {i.amount}\n"
        print(checkout)