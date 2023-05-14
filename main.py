class calculator():
  def __init__(self, num_1, num_2):
    self.num_1 = num_1
    self.num_2 = num_2
  def sum(self):
    return self.num_1 + self.num_2
  def minus(self):
    return self.num_1 - self.num_2
  def multiplication(self):
    return self.num_1 * self.num_2
  def division(self):
    return self.num_1 / self.num_2
  def power(self):
    return self.num_1 ** self.num_2
n = 5
m = 6
cal = calculator(n, m)
print(cal.sum())
