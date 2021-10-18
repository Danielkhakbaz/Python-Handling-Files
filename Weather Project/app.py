import pandas as pd

data = pd.read_csv("weather_data.csv")

data_dict = {
    "names": ["Danial", "Behzad", "Ali"],
    "ages": [21, 20, 21]
}
    
new_data = pd.DataFrame(data_dict)

new_data.to_csv("best_friends.csv")