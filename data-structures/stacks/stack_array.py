class StackArray:
  """A Stack class implemented using arrays in Python"""

  def __init__(self, in_list):
    """Stack method to initialize an empty stack. Can take a list to insert into the initial stack by the ascending order of the index"""
    pass
  
  def push(self, item):
    """Pushes the item onto the topmost index of the Stack"""
    pass
  
  def pop(self):
    """Removes the topmost item from the stack and returns it"""
    pass
  
  def peek(self):
    """Returns the topmost value in the stack, but only by value and not reference"""
    pass

  top = peek #Asigning an alias for the peek function, so that stack.top() has the same behaviour.

  def is_empty(self):
    """Checks if the stack is empty. Returns False if it is not empty"""
    pass

  def size(self):
    """Returns the number of items present in the stack"""
    pass

  def __str__(self, n=5):
    """Dunder method that returns the string representation of the first 'n' stack elements, made for users"""
    pass
    
  def __repr__(self, n=5):
    """Dunder method that returns the string representation of the stack datastructure with the first 'n' elements"""
    pass

