"""
This module is for general form menu in CLI .

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

class Product:
    """This is the generic class for the products"""
    def __init__(self, name : str, brand : str, stock : int, price :\
                  float, details : str) -> None:
        """This is the constructor of the class
        Args:
            name (str): name of the product
            id (str): id of the product
            brand (str): brand of the product
            price (float): price of the product
            details (str): details of the product
        """
        self.name = name
        self.brand = brand
        self.__stock = stock
        self.price = price
        self.details = details
        self.amount = 0
    
    def __str__(self) -> str:
        """This method returns the string representation of the object
        Returns:
            str: string representation of the object
        """
        return f"Name: {self.name}\nBrand: {self.brand}\nPrice: {self.price}\
        \nDetails: {self.details}\n"
    
    def change_stock(self, quantity : int) -> None:
        """This method increases the stock of the product
        Args:
            quantity (int): quantity to increase
        """
        self.__stock += quantity

    def is_available(self, quantity : int) -> bool:
        """This method checks if the given quantity is aviable
        Args:
            quantity (int): quantity to check
        Returns:
            bool: True if the quantity is aviable, False otherwise
        """
        return self.__stock >= quantity
    
