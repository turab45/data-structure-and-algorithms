import pandas as pd

data = pd.read_csv(r'C:\Users\USER\OneDrive\Desktop\yellow_tripdata_2022-01.csv')

data['trip_distance'].to_csv('taxi-distance.csv')