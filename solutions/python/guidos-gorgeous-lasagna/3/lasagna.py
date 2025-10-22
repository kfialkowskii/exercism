"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""
#Constants below
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time
    

def preparation_time_in_minutes(number_of_layers):
    """Calculate preparation time by number of layers.
    
    :param number_of_layers: int - number of layers in lasagna
    :return: int - minutes needed to prepare lasagna
    
    Function that takes number of layers in lasagna as arument and returns 
    minutes needed to prepare whole thing based on PREPARATION_TIME constant.
    """
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate time spent in the kitchen.
    
    :param number_of_layers: int - number of layers in lasagna.
    :param elapsed_bake_time: int - number of minutes lasagna has spent baking already.
    :return: int - total minutes spent in the kitchen making lasagna.
    
    Function that takes number of layers in lasagna and elapse bake time 
    as arguments and returns total minutes needed to make lasagna.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
