#BackShot BUrgers


class Resturant:
  name = ''
  category = ''
  raiting = 0.0
  delivery = False

backshot_burgers = Resturant()
backshot_burgers.name = "BackShot Burgers"
backshot_burgers.category = "Fast Food Diner"
backshot_burgers.raiting = 4.5
backshot_burgers.delivery = True

kahfali = Resturant()
kahfali.name = "Kahfali"
kahfali.category = "Dine in"
kahfali.raiting = 4
kahfali.delivery = False
print(vars(backshot_burgers))
print(vars(kahfali))