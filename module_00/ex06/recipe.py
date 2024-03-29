#!/usr/bin/env python3
"""
recipe
"""

COOKBOOK = {
        'sandwich': {
            'ingredients': [
                'ham',
                'bread',
                'cheese',
                'tomatoes'
                ],
            'meal': 'lunch',
            'prep_time': '10'
            },
        'cake': {
            'ingredients': [
                'flour',
                'sugar',
                'eggs'
                ],
            'meal': 'dessert',
            'prep_time': '60'
            },
        'salad': {
            'ingredients': [
                'avocado',
                'arugula',
                'tomatoes',
                'spinach'
                ],
            'meal': 'lunch',
            'prep_time': '15'
            }
    }


def quit_fn():
    """quit"""
    raise SystemExit


def print_a_recipe():
    """Print recipe"""
    try:
        name = input('Please enter the recipe\'s\
 name to get its details:\n>> ')
        print(f"Recipe for {name}:\nIngredients list:\
 {COOKBOOK[name]['ingredients']}\nTo be eaten for\
 {COOKBOOK[name]['meal']}.\nTakes {COOKBOOK[name]['prep_time']}\
 minutes of cooking.", end='\n')
    except KeyError:
        print(name + ' is not in the cookbook.', end='\n')


def delete_a_recipe():
    """Delete recipe"""
    name = input('What recipe do you want to delete ?\n>> ')
    try:
        del COOKBOOK[name]
    except KeyError:
        print(name + ' is not in the cookbook.', end='\n')


def add_a_new_recipe():
    """Add a recipe"""
    name = input('Recipe name\n>> ')
    ingredients = input('List ingredients\n>> ')
    meal = input('What dish or meal time is it for ?\n>> ')
    prep_time = input('How long does it take to cook it ?\n>> ')
    COOKBOOK[name] = {
        'ingredients': ingredients,
        'meal': meal,
        'prep_time': prep_time
    }


def print_all_recipe_name():
    """Display all recipe"""
    for recipe in COOKBOOK:
        print(recipe)


MENU = {
        '1': ('Add a recipe', add_a_new_recipe),
        '2': ('Delete a recipe', delete_a_recipe),
        '3': ('Print a recipe', print_a_recipe),
        '4': ('Print the cookbook', print_all_recipe_name),
        '5': ('Quit', quit_fn)
    }


if __name__ == '__main__':
    while True:
        print('Please select an option by typing the corresponding number:')
        for item in MENU.items():
            print(item[0], item[1][0], sep=': ', end='\n')
        CHOICE = input('>> ')
        try:
            MENU[CHOICE][1]()
        except KeyError:
            print('This option does not exist, please type the\
 corresponding number.\nTo exit, enter 5.', end='\n')
