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
from Product import *
import Constants

class Microcontroller(Product):
    """This class is an inherance of the Product class, it is used to create a Microcontroller object"""
    def __init__(self) -> None:
        """Modificed constructor to add name of the product and amount respectively"""
        self.name = 'Microcontroller'
        self.amount = Constants.AMOUNT

        super().__init__(self.name, self.amount)


class Pickit(Product):
    """This class is an inherance of the Product class, it is used to create a Pickit object"""
    def __init__(self) -> None:
        """Modificed constructor to add name of the product and amount respectively"""
        self.name = 'Pickit programmer'
        self.amount = Constants.AMOUNT

        super().__init__(self.name, self.amount)


class RasperryPi(Product):
    """This class is an inherance of the Product class, it is used to create a Rasperry pi object"""
    def __init__(self) -> None:
        """Modificed constructor to add name of the product and amount respectively"""
        self.name = 'Rasperry Pi'
        self.amount = Constants.AMOUNT

        super().__init__(self.name, self.amount)


