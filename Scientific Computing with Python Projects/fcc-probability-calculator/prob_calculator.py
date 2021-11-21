import copy
import random
# Consider using the modules imported above.

class Hat:

  def __init__(self,**kwargs):
    contents=[]
    key_list = list(kwargs.keys())
    val_list = list(kwargs.values())
    for index, key  in enumerate(key_list):
      for i in range(val_list[index]):
        contents.append(key)


    self.contents=contents

  def draw(self,number):
    
    if number > len(self.contents):
      return self.contents

    results=random.sample(self.contents, number)
    
    for result in results:
      self.contents.remove(result)

    
    return results

    


def matchedDraw(expected_balls,draw):

  key_list = list(expected_balls.keys())
  val_list = list(expected_balls.values())
  contents=[]
  for index, key  in enumerate(key_list):
      for i in range(val_list[index]):
        contents.append(key)

  matches=True

  for ball in contents:
    if( ball in draw):
      draw.remove(ball)
      
    else:
      matches=False

  return matches

  
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  
  propabilty=0
  results=[]
  count=0
  for i in range(num_experiments):
    tempHat=copy.deepcopy(hat)
    drawn=tempHat.draw(num_balls_drawn)
    if(matchedDraw(expected_balls,drawn)):
      count+=1

  return count/num_experiments
  