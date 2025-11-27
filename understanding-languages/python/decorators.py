# Purpose of decorators is to enhance the base function and then return the enhanced functions.

def timer_decorater(base_func):
  # Code to decorate.
  return enhanced_func


# @<decorator name> before a function, lets you enhance a base function without modifying its purpose. Helps in decoupling
# and separating usecases.

def brew_tea():
  # Code to brew.
