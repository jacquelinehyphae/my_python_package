import pandas
from exampleHelper import subtract_helper

class Example:
  def __init__(self, x=1, y=2):
    self.x = x
    self.y = y

  def add(self):
    result = self.y + self.x
    return result

  def subtract(self):
    return subtract_helper(self.x, self.y)
