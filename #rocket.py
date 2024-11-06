#rocket
'''def distance_to_miles():
    # Define the conversion factor
    conversion_factor = 0.621371
    # Get the distance from the user
    distance = float(input("Enter the distance in kilometers: "))
    # Convert the distance to miles
    miles = distance * conversion_factor
    return miles

distance_to_miles()'''

def distance_to_miles(distance):
  return distance / 1.609

answer = distance_to_miles(10000)
print(answer)