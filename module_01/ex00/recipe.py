"""
Recipe Class Definition
"""

DISHTYPES = ('starter', 'lunch', 'dessert')


def notfalsy(something):
    """Check whether argument is falsy"""
    if something:
        return something
    raise ValueError('Value must not be empty')


def only_str(string):
    """Check whether it is string"""
    if isinstance(string, str):
        return str(string)
    raise ValueError('Value must be a string')


def only_int(number):
    """Check whether it is integer"""
    if isinstance(number, int):
        return int(number)
    raise ValueError('Value must be an integer')


def only_strlist(lst):
    """Check whether it is a list"""
    if (isinstance(lst, list)
            and all(isinstance(item, str) for item in lst)):
        return list(lst)
    raise ValueError('Value must be list containing only strings')


def btwrange(number):
    """Check whether number is in range"""
    number = only_int(number)
    if int(number) in range(1, 6):
        return number
    raise ValueError('Value must be an integer between 1 to 5')


def uptoinf(number):
    """Check whether the number is greater than 0"""
    number = only_int(number)
    if int(number) >= 0:
        return number
    raise ValueError('Value must be an integer between 0 to +inf')


def isdish(string):
    """Check whether it is a dish"""
    string = only_str(string)
    if string in DISHTYPES:
        return string
    raise ValueError('Not a valid dish')


class Recipe:
    """Recipe class
    Init name, cooking_lvl, cooking_time, ingredients, description and type
    """

    # pylint: disable=too-many-arguments
    def __init__(
            self, name, cooking_lvl, cooking_time, ingredients,
            description, recipe_type
            ):
        self.__name = notfalsy(only_str(name))
        self.__cooking_lvl = btwrange(cooking_lvl)
        self.__cooking_time = uptoinf(cooking_time)
        self.__ingredients = only_strlist(ingredients)
        self.__description = only_str(description)
        self.__recipe_type = isdish(recipe_type)

    def __str__(self):
        """Return the string to print with the recipe info"""
        return f"Name: {self.__name}\
\nLevel: {self.__cooking_lvl}/5\
\nTime: {self.__cooking_time}min\
\nIngredients: {', '.join(self.__ingredients)}\
\nDescription: {self.__description}\
\nType: {self.__recipe_type}"

    @property
    def name(self):
        """'Name' property"""
        return self.__name

    @property
    def cooking_lvl(self):
        """'Cooking level' property"""
        return self.__cooking_lvl

    @property
    def cooking_time(self):
        """'Cooking time' property"""
        return self.__cooking_time

    @property
    def ingredients(self):
        """'Ingredients' property"""
        return self.__ingredients

    @property
    def description(self):
        """'Description' property"""
        return self.__description

    @property
    def recipe_type(self):
        """'Recipe type' property"""
        return self.__recipe_type

    @name.setter
    def name(self, name):
        self.__name = only_str(name)

    @cooking_lvl.setter
    def cooking_lvl(self, cooking_lvl):
        self.__cooking_lvl = btwrange(cooking_lvl)

    @cooking_time.setter
    def cooking_time(self, cooking_time):
        self.__cooking_time = only_int(cooking_time)

    @ingredients.setter
    def ingredients(self, ingredients):
        self.__ingredients = only_strlist(ingredients)

    @description.setter
    def description(self, description):
        self.__description = only_str(description)

    @recipe_type.setter
    def recipe_type(self, recipe_type):
        self.__recipe_type = isdish(recipe_type)
