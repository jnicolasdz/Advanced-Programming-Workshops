"""
This is a class to create passive object that storage user data.

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
class User:
    """This is an abstract class to define any kind of users"""

    def __init__(self, name : str, lastname : str, address : str, credit_card : str, country : str) -> None:

        self.name = name
        self.lastname = lastname
        self.address = address
        self.credit_card = credit_card
        self.country = country
    