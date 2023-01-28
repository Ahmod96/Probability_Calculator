import copy
import random
class Hat():
    def __init__(self, **args):
      self.args = args
      self.contents = []
      for arg in args:
          n_arg = 1
          while n_arg <= args[arg]:
              self.contents.append(arg)
              n_arg += 1
    def draw(self, n_draw):
      if n_draw > len(self.contents):
          return self.contents
      else:
          random_index = random.sample(range(0, len(self.contents)), n_draw)
          withdraw_list = []
          for value in random_index:
              withdraw_list.append(self.contents[value])
          for value in sorted(random_index, reverse = True):
              del self.contents[value]
      return withdraw_list

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    
    expected_balls_list = []
    for ball in expected_balls:
      ball_value = 1
      while ball_value <= expected_balls[ball]:
          expected_balls_list.append(ball)
          ball_value += 1
    
    M = 0
    for num in range(0, num_experiments):
      hat_copy = copy.deepcopy(hat)
      withdraw_list = hat_copy.draw(num_balls_drawn)
      
      count = 0
      expected_balls_copy = copy.deepcopy(expected_balls_list)
      for ball in withdraw_list:
          if ball in expected_balls_copy:
              count += 1
              del expected_balls_copy[expected_balls_copy.index(ball)]
              
      if count == len(expected_balls_list):
          M += 1
    probability = M/num_experiments
    return probability
