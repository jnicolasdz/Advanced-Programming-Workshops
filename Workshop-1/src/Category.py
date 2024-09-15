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

from abc import ABC, abstractmethod

from Product import *

class Category(ABC):
    """This is an abstract clase to define concretes categoiries"""
    def __init__(self, name, productlist) -> None:
        self.name = name
        self.products_list = productlist

    def show_products(self) -> Product:
        """This method returns the products of the category
        Returns:
            Product: products of the category
        """
        return self.products_list
    
    
    

    
    

    

