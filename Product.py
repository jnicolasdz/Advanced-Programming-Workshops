
import string

class Product():

    def __init__(self, name, amount) -> None:
        self.name = name
        self.amount = amount
        self.data = f"Product: {name} \nAvailables: {amount}\n"


    def show_data(self) -> string :
        return self.data