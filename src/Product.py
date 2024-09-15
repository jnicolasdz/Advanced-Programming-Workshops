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


class Product():
    """This is the generic class for the products"""
    def __init__(self, name, amount) -> None:
        self.name = name
        self.amount = amount
        self.data = f"Product: {self.name} \nAvailables: {self.amount}\n"


    def show_data(self) -> str :
        """This method returns the data of the product
        Returns:
            str: data of the product
        """
        return self.data