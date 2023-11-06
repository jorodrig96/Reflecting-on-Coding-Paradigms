def flat_and_sort(number_list):
  list  = []
  for item in number_list:
    for i in item:
      list.append(i)
  return sorted(list)
  
print(flat_and_sort([[2,3], [10, 1], [6,9,4], [5,8,7], [11]]))

"""
1. this function ensures data mutability by the function having its inputs within itself 
and not having to rely on other external variable/functions.

2. the function is pure because it only ouputs what is given within
and doesnt change anything external.

3. this can be a HOF. its "inheritance" can be used in other functions or 
pieces of code. 

4. im sure by habit some other developer would have placed the "list" variable outside of 
the function. which would have no longer made it pure. I wouldve done it before i had 
learned this functional method, which is a much more organized way of coding. 

5. its makes a helpful paradimn by having its variable "list" within the function. If it 
was outside of the function, you can run the chance of calling another "list" or even 
itterating through something else.
"""

class Podracer:
  def __init__(self, max_speed, condition, price):
    self.max_speed = max_speed
    self.condition = condition 
    self.price = price
    

  def podracer_repair(self):
    self.condition = "repaired"
    return f"The podracer is {self.condition} and ready to get back to work!"


p = Podracer(200, "new", "expensive")

print(p.max_speed, p.condition, p.price)
print(p.podracer_repair())

class AnakinsPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)
  
    def boost(self):
        self.max_speed *= 2
        return f"AnakinsPod just received some boost. Its max speed is now {self.max_speed}"

a = AnakinsPod(150, "new", "expensive")

print(a.max_speed, a.condition, a.price)
print(a.boost())

class SebulbasPod(Podracer):
  def __init__(self, max_speed, condition, price):
    super().__init__(max_speed, condition, price)

  def flame_jet(self, other): #got help from the solution code on this one.
    other.condition = "trashed"
    return f"{type(self).__name__} just got {other.condition}"

s = SebulbasPod(200, "new", "expensive")

print(s.flame_jet(p))

"""
1. the code above demonstrates only some of the pillars of OOP. it has encapsulation, 
inheritance, and polymorphism. it bundles information by allowing other classes to 
callbacks from high order functions. its lets classes use the same interface with the 
same process an inheritance heirarchy.

2. if we were to use functional programming it would have been even longer code than it
already is because we have to repeat the same code for every class.

3. using OOP assisted because of the callbacks. Reusing the same code for the classes
using callbacks helped save so many lines of code.
"""

"""
REFLECTION QEUSTIONS

1. No. They're both useful. Personally, im not sure if im right or wrong cause im still 
learning. But,  i think both styles are used in all code. I think it depends on what 
you are trying to do and get done. Both styles are great but one style takes a longer
than the other. But like i said, it all depends on what are you are getting done.

2. OOP seems more appealing to me. Being able to get data from different sets of code is
so much helpful. It might cause more bugs but it does seem more flexible.

3. the flat_and_sort function. The list variable would be better defined outside of it 
because you can pull in data from other functions and use it in different ways.

4. I still think it depends on what you are trying to get done. But, if i had to choose,
i would say OOP. Only because you have to look at many pieces of code to understand.
"""

