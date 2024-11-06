#TestClass
class City:
  def __init__(self, name, country, population, landmarks):
    self.name = name
    self.country = country
    self.population = population
    self.landmarks = landmarks

 
NewYork = City('New York',"America",100500200,"Statue of Liberty")

print(vars(NewYork))