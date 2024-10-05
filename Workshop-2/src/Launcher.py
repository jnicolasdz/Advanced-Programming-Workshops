
"""
This is the main module of the system

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

from Product import Product
from Category import Category
from Catalog import Catalog
from Menu import Menu
from ShoppingCart import ShoppingCard

class Launcher:
    """This class is the main class of the system"""
    def __init__(self) -> None:
        
        self.stock = 5
        self.shopping_cart = ShoppingCard()
        self.menu_1 = Menu("Welcome to the electronic catalog!\nSelect an option:\n0. Exit\n1. See Catalog")
        self.menu_1.set_exit_option(0)
        self.menu_2 = Menu("Select a Category\n0.Exit\n")
        self.menu_2.set_exit_option(0)
        self.menu_3 = Menu("Select a product typing number product\n0.Exit\n")
        self.menu_3.set_exit_option(0)
        self.menu_4 = Menu("0.Exit\n1.Add product to shopping cart\n")
        self.menu_4.set_exit_option(0)
        self.menu_5 = Menu("Checkout:\n1.Exit\n2.Process order\n")
        self.menu_5.set_exit_option(1)        

        self.components_products = [Product('Microcontroller', 'Microcontroller Brand', self.stock, 1345.78, 'Microcontroller'),
                       Product('Pickit programmer', 'Pickit Brand', self.stock, 1345.78, 'Pickit programmer'),
                       Product('Rasperry Pi', 'Rasperry Brand', self.stock, 1345.78, 'Rasperry Pi')]
        
        self.peripherials_products = [Product('Keyboard', 'Keyboard Brand', self.stock, 1345.78, 'Keyboard'),
                         Product('Graphic Tablet', 'Graphic Tablet Brand', self.stock, 1345.78, 'Graphic Tablet'),
                         Product('Multiple Charger', 'Multiple Charger Brand', self.stock, 1345.78, 'Multiple Charger'),
                         Product('Baffle', 'Baffle Brand', self.stock, 1345.78, 'Baffle')]

        self.technology_home_products = [Product('TV', 'TV Brand', self.stock, 1345.78, 'TV'),
                            Product('Blender', 'Blender Brand', self.stock, 1345.78, 'Blender'),
                            Product('Fridge', 'Fridge Brand', self.stock, 1345.78, 'Fridge'),
                            Product('Washing Machine', 'Washing Machine Brand', 5, 1345.78, 'Washing Machine')]
        
        self.technology_devices_products = [Product('Laptop without OS', ' free Laptop Brand', self.stock, 1345.78, 'Laptop'),
                               Product('Mac Laptop', 'Apple', self.stock, 1345.78, 'Laptop'),             
                               Product('Tablet', 'Tablet Brand', self.stock, 1345.78, 'Tablet'),
                               Product('Smartwatch', 'Smartwatch Brand', self.stock, 1345.78, 'Smartwatch'),
                               Product('Smartphone', 'Smartphone Brand', self.stock, 1345.78, 'Smartphone')]
        
        self.category_list = [Category('Components', self.components_products),
                              Category('Peripherials', self.peripherials_products),
                              Category('Technology Home', self.technology_home_products),
                              Category('Technology Devices', self.technology_devices_products)]
        
        self.catalog = Catalog()
        for category in self.category_list:
            self.catalog.add_Category(category)

    def main(self) -> None :
        """This is the principal method of the system"
        Args:
            None
        Returns:
            None"""

        self.menu_1.set_options([1])
        user_choice = self.menu_1.get_input()
        if user_choice == 1:
            self.menu_2.set_options([1, 2, 3, 4])
            self.catalog.show_categories()
            user_choice = self.menu_2.get_input()

            if user_choice == 1:
                self.menu_3.set_options([1,2,3])
                self.catalog.show_category('Components')
                user_choice = self.menu_3.get_input()
                for i  in self.menu_3.options:
                    if user_choice == i:
                        self.menu_4.set_options([1])
                        print(self.catalog.catalog['Components'].list_products[i-1])
                        user_choice = self.menu_4.get_input()
                        if user_choice == 1:
                            self.shopping_cart.add_product(self.catalog.catalog['Components'].list_products[i-1])
                            self.shopping_cart.make_checkout()
                            
            elif user_choice == 2:
                self.menu_3.set_options([1,2,3,4])
                self.catalog.show_category('Peripherials')
                user_choice = self.menu_3.get_input()
                for i  in self.menu_3.options:
                    if user_choice == i:
                        self.menu_4.set_options([1])
                        print(self.catalog.catalog['Components'].list_products[i-1])
                        user_choice = self.menu_4.get_input()
                        if user_choice == 1:
                            self.shopping_cart.add_product(self.catalog.catalog['Components'].list_products[i-1])
                            self.shopping_cart.make_checkout()

            elif user_choice == 3:
                self.menu_3.set_options([1,2,3,4])
                self.catalog.show_category('Technology Home')
                user_choice = self.menu_3.get_input()
                for i  in self.menu_3.options:
                    if user_choice == i:
                        self.menu_4.set_options([1])
                        print(self.catalog.catalog['Components'].list_products[i-1])
                        user_choice = self.menu_4.get_input()
                        if user_choice == 1:
                            self.shopping_cart.add_product(self.catalog.catalog['Components'].list_products[i-1])
                            self.shopping_cart.make_checkout()

            elif user_choice == 4:
                self.menu_3.set_options([1,2,3,4,5])
                self.catalog.show_category('Technology Devices')
                user_choice = self.menu_3.get_input()
                for i  in self.menu_3.options:
                    if user_choice == i:
                        self.menu_4.set_options([1])
                        print(self.catalog.catalog['Components'].list_products[i-1])
                        user_choice = self.menu_4.get_input()
                        if user_choice == 1:
                            self.shopping_cart.add_product(self.catalog.catalog['Components'].list_products[i-1])
                            self.shopping_cart.make_checkout()

if __name__ == '__main__':
    launcher = Launcher()
    launcher.main()








        




