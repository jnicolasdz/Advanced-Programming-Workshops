
import string
import Category
import Constants
import sys
from CategoriesProducts import *
from ShoppingCart import *

class Menu: 

    def __init__(self) -> None:
        

        self.shopping_cart = ShoppingCart()

    def back(self, option, index):
        if (option == 1 and index-1 >= 0):
            self.display(Constants.MENU_LIST[index-1])

        elif(option == 1):
            self.display("Thanks for visiting us")
            sys.exit()
    
    def get_input(self, text) -> string:
        if (text == None):
            return input()
        else :
            return input(text)
        

    def display(self, text : string) -> None: 
        print(text)

    
    def display_categories(self, categories : Category) -> None:
        self.display(Constants.MENU_2)
        for i in range(0, len(categories)):
            self.display(f"{i+2}. {categories[i].name}\n")


    def display_products(self, category : Category) -> None:
        index = 1
        for i in category.show_products():
            index += 1
            self.display(f"{index}. {i.show_data()}")

    
    def display_menu(self) -> None:
        self.display(Constants.MENU_1)

    
    def getClientData(self) -> None:
        name = self.get_input("Type your name")
        direction = self.get_input("Type your direction")
        self.display(self.shopping_cart.make_check_out(name, direction))
        
    

    def process_cycle(self) -> None:

        index = 0
        categories = [CategoryCamera(), CategoryComponents(), CategoryPeripherials(), CategoryTecnologyDevices(),CategoryTechnologyHome()]
        option = int(self.get_input(self.display_menu()))
        while (option != 9):
            self.back(option, index)
            if (option == 2):
                index += 1
                option = int(self.get_input(self.display_categories(categories)))
                self.back(option, index)
                for i in range(0, len(categories)):
                    if (categories[i] == option) :
                        index += 1
                        self.display(Constants.MENU_3)
                        self.display_products(categories[i])
                        category_selected = categories[i]
                option = int(self.get_input(None))
                self.back(option, index)
                while option != 1 or option != 3:
                    option = int(self.get_input(None))
                    self.back(option, index)
                    for i in range(1, len(category_selected)+1):
                        if(option == i+2):
                            self.shopping_cart.add_product(category_selected.product_list[i+2])
                if(option == 3):
                    self.display(Constants.MENU_4)
                    index += 1
                    self.display(self.shopping_cart.products_list)
                    option = int(self.get_input(None))
                    self.back(option, index)
                    if(option == 2):
                        self.display(Constants.MENU_4)
                        option = int(self.get_input(None))
                        index += 1
                        self.back(option,index)
                        if(option == 2):
                            name = self.get_input(f"Insert your name")
                            direction = self.get_input(f"Inser your directions")
                            self.display(self.shopping_cart.make_check_out(name, direction))
                            option = int(self.get_input(None))
                            self.back(option, index)
                  


                    


                
                 




