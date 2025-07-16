class StackArray:
  """A Stack class implemented using arrays in Python"""
  
  __slots__ = ['stack']

  def __init__(self, in_list=None):
    """Stack method to initialize an empty stack. Optionally accepts a list to populate the stack initially (bottom to top)."""
    self.stack = in_list if isinstance(in_list, list) else []

  # Dunder methods (basic container protocol)
  def __len__(self):
    """Returns the number of items in the stack."""
    return len(self.stack)

  def __contains__(self, parameter):
    """Checks if an item exists in the stack."""
    return parameter in self.stack

  def __eq__(self, other):
    """Checks equality between two StackArray instances based on content."""
    return isinstance(other, StackArray) and self.stack == other.stack

  def __iter__(self):
    """Returns an iterator over the stack from top to bottom (reversed)."""
    return iter(self.stack[::-1])

  def __repr__(self):
    """Dunder method that returns the string representation of the stack datastructure with the first '5' elements"""
    top_five = self.stack[-5:][::-1] # Top 5 elements, reversed
    return f"StackArray({top_five})  # Top → Bottom (first 5 of stack)"

  def __iadd__(self, other: 'StackArray'):
    """Adding Stack B to Stack A will give a combined stack with A at the bottom and B at the top, with the element order preserved"""
    if not isinstance(other, StackArray):
      raise TypeError("Cannot add non StackArray object to a StackArray object")
    
    self.stack.extend(other.stack)
    return self

  def __add__(self, other: 'StackArray') -> 'StackArray':
    """Adding Stack A + B will give a combined stackarray object with A at the bottom and B at the top, with the element order preserved"""
    if not isinstance(other, StackArray):
      raise TypeError("Cannot add non-stack object to stack object")

    return StackArray(self.stack + other.stack)

  def __getitem__(self, index):
    """Accesses an item by index (0 is bottom, -1 is top)."""
    return self.stack[index]
  
  # Stack-specific methods
  def push(self, item) -> None:
    """Pushes the item onto the topmost index of the Stack"""
    self.stack.append(item)

  def pop(self):
    """Removes the topmost item from the stack and returns it"""
    if self.is_empty():
      raise IndexError("You cannot pop from empty Stack")
    
    return self.stack.pop()

  def peek(self):
    """Returns the topmost value in the stack, but does it by reference"""
    if self.is_empty():
      raise AttributeError("You cannot peek on an empty Stack")
    
    return self.stack[-1]

  top = peek # Asigning an alias for the peek function.

  def clear(self) -> None:
    """Clears all items from the stack."""
    self.stack.clear()

  def is_empty(self) -> bool:
    """Checks if the stack is empty. Returns True if the stack is empty. False otherwise."""
    return not self.stack

  def size(self) -> int:
    """Returns the number of items present in the stack"""
    return len(self.stack)

  # def __bool__(self): Not going to define this because my class agrees with the len implementation for its truthiness
