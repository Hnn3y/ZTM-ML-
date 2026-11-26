import pandas as pd

# Creating a series of car types
cars = pd.Series(["BMW", "Toyota", "Honda"])
print(f"{cars}")

# Creating a series of colours
colours = pd.Series(["Blue", "Red", "White"])
colours

# You can create a DataFrame by using pd.DataFrame() and passing it a Python dictionary.

# Creating a DataFrame of cars and colours
car_data = pd.DataFrame({"Car type": cars, 
                         "Colour": colours})
print(f"{car_data}")

#Note: Make sure your two Series are the same size before combining them in a DataFrame.