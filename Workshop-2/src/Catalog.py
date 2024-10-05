"""
This module is for general Catalog which storages categories.

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
import Category

class Catalog:
    """This class is for storage categories"""
    def __init__(self) -> None:
        self.list_categories = []
        self.catalog = {}
    def add_Category(self, category : Category) -> None:

        """This method adds a product to the category
        Args:
            product (Product): product to add
        """
        self.list_categories.append(category)
        self.catalog[category.name] = category

    def show_categories(self) -> None:
        """This method shows the products of the category"
        Args:
            None
        Returns:
            None
        """
        index = 0
        for category in self.list_categories:
            index += 1
            print(index, category)
    def show_category(self, category_name : str) -> None:

        """This method shows the products of the category
        Args:
            category_name (str): name of the category
        Returns:
            None
        """

        print(self.catalog[category_name])
        self.catalog[category_name].show_products()
    def show_product(self, category_name : str, product_name : str) -> None:

        """This method shows the products of the category
        Args:
            category_name (str): name of the category
            product_name (str): name of the product
        Returns:
            None
        """
        print(self.catalog[category_name].get_product(product_name))