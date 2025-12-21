import time

# Purpose of decorators is to enhance the base function and then return the enhanced functions.

def timer_decorater(base_func):
  
  def enhanced_function:
    start_time = time.timer()
    base_func()
    end_time = time.stop()
    print(f"Task time: {end_time-start_time}" seconds)
  
  return enhanced_func


# @<decorator name> before a function, lets you enhance a base function without modifying its purpose. Helps in decoupling
# and applying the single responsibility rule to make the code reuasble.
@timer_decorator
def brew_tea():
  print("Brewing Tea")
  time.sleep(1)
  print("Tea finished brewing")
