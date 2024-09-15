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
from Category import *
from ProductsCamera import *
from ProductsComponents import *
from ProductsPeripherials import *
from ProductsTechnologyDevices import *
from ProductsTechnologyHome import *

class CategoryCamera(Category):
    """this class works as a category for the camera products"""
    def __init__(self) -> None:
        """Modified constructor to add the name and the products list of camera"""
        self.name = 'Camera'
        self.products_list = [Camera(),CameraPro()]
        super().__init__(self.name, self.products_list)


class CategoryComponents(Category):
    """this class works as a category for the electronic components products"""
    def __init__(self) -> None:
        """Modified constructor to add the name and the products list of electronic components"""
        self.name = 'Electronic components'
        self.products_list = [Microcontroller(),Pickit(), RasperryPi()]
        super().__init__(self.name, self.products_list)

class CategoryPeripherials(Category):
    """this class works as a category for the peripherials products"""
    def __init__(self) -> None:
        """Modified constructor to add the name and the products list of peripherials"""
        self.name = 'Peripherials devices'
        self.products_list = [Keyboard(),GraphicTablet(), MultipleCharger(), Baffle()]
        super().__init__(self.name, self.products_list)

class CategoryTecnologyDevices(Category):
    """this class works as a category for the technology devices products"""
    def __init__(self) -> None:
        """Modified constructor to add the name and the products list of technology devices"""
        self.name = 'Technology devices'
        self.products_list = [LaptopNoOS(),MacLatop(), Tablet(), Smartwatch()]
        super().__init__(self.name, self.products_list)

class CategoryTechnologyHome(Category):
    """this class works as a category for the technology home products"""
    def __init__(self) -> None:
        """Modified constructor to add the name and the products list of technology home"""
        self.name = 'Technology home devices'
        self.products_list = [TV(),Blender()]
        super().__init__(self.name, self.products_list)