"""
This module is for general form menu in CLI .

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

class Menu:

    """This class is for general form menu in CLI"""

    def __init__(self, content : str) -> None:
        self.content = content
        self.options = []
        
    def set_exit_option(self, option : int) -> None:

        """This method sets the exit option of the menu
        Args:
            option (int): exit option
        Returns:
            None
        """
        self.exit_option = option
    
    def set_options(self, options : list) -> None:

        """This method sets the options of the menu
        Args:
            options (list): options of the menu
        Returns:
            None
        """

        self.options = options
    
    def get_input(self) -> int:

        """This method gets the input of the user
        Args:
            None
        Returns:
            int: user choice
        """
        
        self.display()
        try:
            user_choice = int(input('Enter a choice: '))
            while user_choice != self.exit_option and user_choice not in self.options:
                print('Invalid choice')
                user_choice = int(input('Enter a choice: '))
            return user_choice
        except Exception : 
            print('ERROR: Please enter only numbers')
            return self.get_input()
            
    def display(self) -> None:

        """This method display the menu
        Args:
            None
        Returns:
            None
        """
        
        print(self.content)

