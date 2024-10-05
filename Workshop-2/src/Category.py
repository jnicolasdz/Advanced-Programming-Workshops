"""
This module is for Categories which storages products.

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

class Category: 

    """This class is for the categories of the products"""
    
    def __init__(self, name, list_products) -> None:
        self.name = name
        self.list_products = list_products
        self.category = {}

    def __str__(self) -> str:
        return f"Category: {self.name}"

    def add_product(self, product: Product) -> None:

        """This method adds a product to the category
        Args:
            product (Product): product to add
        """
        self.list_products.append(product)
        self.category[product.name] = product
    
    def get_product(self, name: str) -> Product:
        """This method returns the product with the given name
        Args:
            name (str): name of the product
        Returns:
            Product: product with the given name
        """
        return self.category[name]
    
    def show_products(self) -> None:
        """This method shows the products of the category
        Args:
            None
        Returns:
            None
        """
        index = 0
        for product in self.list_products:
            index += 1
            print(index, product)