import pandas as pd
import numpy as np

data = pd.read_csv("taxi-passanger-count.csv", squeeze=True, header=None)

#print(data[data==1].count())
#print(data[data==6].count())

q1 = data.value_counts(normalize=True)[[1,6]] * 100

# What proportion of taxi rides are for 3, 4, 5, or 6 passengers?
q2 = data.value_counts(normalize=True)[[3,4,5,6]] * 100


data2 = pd.read_csv("taxi-distance.csv", header=None)
print(data2)

data2.dropna(inplace=True)
print(data2)
# show no of rides in short 2, greater than 2 but no 10 and greater than 10.

#q3_1 = data2[data2 < 2.0]

#print(data2.value_counts())
#print(q3_1)