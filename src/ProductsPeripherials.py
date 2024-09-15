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

class Keyboard(Product):
    """This class is an inherantance of the Product class,  it is used to create a Keyboard object"""
    def __init__(self) -> None:
        """Modificed constructor to add name of the product and amount respectively"""
        self.name = 'Keyboard'
        self.amount = Constants.AMOUNT

        super().__init__(self.name, self.amount)


class GraphicTablet(Product):
    """This class is an inherantance of the Product class,  it is used to create a Graphic Tablet object"""
    def __init__(self) -> None:
        """Modificed constructor to add name of the product and amount respectively"""
        self.name = 'Graphical drawing tablet'
        self.amount = Constants.AMOUNT

        super().__init__(self.name, self.amount)


class MultipleCharger(Product):
    """This class is an inherantance of the Product class,  it is used to create a Multiple Charger object"""
    def __init__(self) -> None:
        """Modificed constructor to add name of the product and amount respectively"""
        self.name = 'Multiple charger'
        self.amount = Constants.AMOUNT

        super().__init__(self.name, self.amount)


class Baffle(Product):
    """This class is an inherantance of the Product class,  it is used to create a Baffle object"""
    def __init__(self) -> None:
        """Modificed constructor to add name of the product and amount respectively"""
        self.name = 'Baffle'
        self.amount = Constants.AMOUNT

        super().__init__(self.name, self.amount)


