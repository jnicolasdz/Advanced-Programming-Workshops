"""
This module is an example of an abstract class to define a calculator operations.

Copyright (C) 2024  Carlos Andres Sierra <cavirguezs@udistrital.edu.co>

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
from datetime import datetime

class ShoppingCart:
    """this class represent a concrete shopping cart that can be used to add products and make a checkout"""
    def __init__(self) -> None:
        self.name = 'Shopping Cart'
        self.products_list = []

    def show_products(self) -> Product:
        """This method return the list of products in the shopping cart
        Args:
            None  
        Returns:
            Product: list of products in the shopping cart
        """
        return self.products_list
    
    def add_product(self, product : Product) -> None:
        """This method add a product to the shopping cart
        Args:
            product (Product): product to add to the shopping cart
        Returns:    
            None"""

        self.products_list.append(product)
        

    def make_check_out(self, name : str, direction : str) -> str:
        """This method make a checkout of the shopping cart
        Args:
            name (str): name of the client
            direction (str): direction of the client
            Returns:
                str: checkout of the shopping cart"""
        checkout = f"Checkout:\nName: {name}\nDirection: {direction}\nDate: {datetime.now()}\nProducts\n"
        for i in self.products_list:
            checkout += f"{i.name}: f{i.amount}\n"
        return checkout
