import pandas as pd

foods = pd.Series(['Rice', 'Beans', 'Bread'])

values = pd.Series(['$1', '$5', "$10"])

data = pd.DataFrame({"Foods": foods,
                     "Dollar Values": values})
print(f"{data}")