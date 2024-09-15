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


import Category
import Constants
import sys
from CategoriesProducts import *
from ShoppingCart import *

class Menu: 
    """This class is used to create a menu object, which has the responsability to connect the rest
    of objects in order to communicate with the user requests"""
    def __init__(self) -> None:
        """The constructor agregates a shopping cart object"""
        self.shopping_cart = ShoppingCart()

    def back(self, option):
        """This method is used to return to the main menu
        Args:   
            option: int
                The option selected by the user
        Returns:        
            None"""
        if (option == 1):
            self.display("Thanks for visiting us")
            sys.exit()
    
    def get_input(self, text) -> str:
        """This method is used to get the input from the user
        Args:
            text: string
                The text to display to the user, if it is None, the method will not display anything.
                so it can be used to get input and print a message if it is neccesary
        Returns:    
            str"""
        if (text == None):
            return input()
        else :
            return input(text)
        

    def display(self, text : str) -> None:
        """This method is used to display a message to the user
        Args:
            text: string
                The text to display to the user
        Returns:
            None""" 
        print(text)

    
    def display_categories(self, categories : Category) -> None:
        """This method is used to display the categories of the products
        Args:
            categories: Category
                The categories of the products
        Returns:
            None"""
        self.display(Constants.MENU_2)
        for i in range(0, len(categories)):
            self.display(f"{i+2}. {categories[i].name}\n")


    def display_products(self, category : Category) -> None:
        """This method is used to display the products of a category
        Args:
            category: Category
                The category of the products
        Returns:
            None"""
        index = 1
        for i in category.show_products():
            index += 1
            self.display(f"{index}. {i.show_data()}")

    
    def display_menu(self) -> None:
        """This method is used to display the main menu
        Returns:
            None"""
        self.display(Constants.MENU_1)

    
    def getClientData(self) -> None:
        """This method is used to get the client data
        Returns:
            None"""
        name = self.get_input("Type your name")
        direction = self.get_input("Type your direction")
        self.display(self.shopping_cart.make_check_out(name, direction))
        
    

    def process_cycle(self) -> None:
        """This method is used to process the main cycle of the program, work as the main method of the program
        Returns:
            None"""
        categories = [CategoryCamera(), CategoryComponents(), CategoryPeripherials(), CategoryTecnologyDevices(),CategoryTechnologyHome()]
        self.display_menu()

        while True:
            option = int(self.get_input(None))
            self.back(option)
            if (option == 2):
                self.display_categories(categories)
                option = int(self.get_input(None))
                self.back(option)
                self.display(Constants.MENU_3)
                for i in range(1, len(categories)+1):
                    if (option == i+1):
                        self.display_products(categories[i-1])
                        category_selected = categories[i-1]
                while option != 1 and option != 2:
                    option = int(self.get_input(None))
                    for i in range(3, len(categories)+3):
                        if(option == i):
                            self.shopping_cart.add_product(category_selected.products_list[i-4])
                            self.display(f"Added to shopping cart {category_selected.products_list[i-4].name}")
                            category_selected.products_list[i-4].amount -= 1
                            self.display(Constants.MENU_3)
                            self.display_products(category_selected)
                if(option == 3):
                    self.display(Constants.MENU_4)
                    self.display(self.shopping_cart.products_list)
                    option = int(self.get_input(None))
                    self.back(option)
                    if(option == 2):
                        self.display(Constants.MENU_4)
                        option = int(self.get_input(None))
                        self.back(option)
                        if(option == 2):
                            name = self.get_input(f"Insert your name")
                            direction = self.get_input(f"Inser your directions")
                            self.display(self.shopping_cart.make_check_out(name, direction))
                            option = int(self.get_input(None))
                            self.back(option)
"""Execution of the program"""
if __name__ == "__main__":
    menu = Menu()
    menu.process_cycle()




                        

                            

               
                    
            




                    


                
                 




