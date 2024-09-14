
import string
import Category
import Constants
import sys
from CategoriesProducts import *
from ShoppingCart import *

class Menu: 

    def __init__(self) -> None:
        

        self.shopping_cart = ShoppingCart()

    def back(self, option):
        if (option == 1):
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




                        

                            

               
                    
            




                    


                
                 




