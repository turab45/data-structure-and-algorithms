from re import M
import numpy as np
import pandas as pd

"""====================================== EXERCISE 1: Test Scores ========================="""
np.random.seed(0)

nums = np.random.randint(70, 100, 10)
months = "Sep Oct Nov Dec Jan Feb Mar Apr May Jun".split(" ")

s = pd.Series(nums, index=months)


# what is the students average test score for the entire year?
avg_entire_year = s.mean()

# what is the students average test score during the first half of the year?
avg_first_half_year = s.head(5).mean() # my logic -> also works fine
avg_first_half_year2 = s['Sep':'Jan'].mean()

# what is the students average test score during the final half of the year?
avg_final_half_year = s.tail(5).mean() # my logic -> also works fine
avg_final_half_year2 = s['Feb':'Jun'].mean()

# in which month he got higher marks?
higher_marks = s.max()
highest_marks_month = s[s == higher_marks].index[0]

# First five highest scores in the year?
highest_five_scores = []
s2 = s.copy()
for i in range(5):
    max_score =s2.max()
    highest_five_scores.append(max_score)
    idx = s2[s2 == max_score].index[0]
    s2.drop(idx, inplace=True)

# round score to nearesr 10
s = s.round(-1)
#print(s)

#print(avg_final_half_year)
#print(avg_final_half_year2)


# standard deviation of the series
std = s.std(ddof=0)
#print(std)

# beyond the exercise
np.random.seed(0)
months = "Sep Oct Nov Dec Jan Feb Mar Apr May Jun".split(" ")
vals = np.random.randint(40,60,10)
s =  pd.Series(vals, index=months)
mean = 85 - s.mean()
s = s+ mean
#print(s)


# exercise 3: counting 10's digits
s = pd.Series(np.random.randint(0,100,10))
s = (s/10).astype(np.int8)
#print(s)

s = pd.Series(np.random.randint(0,100,10))
#print(s[s<30])
s[s<= s.mean()] = 9999
#print(s)

"""Generate a series of 100,000 floats in a normal distribution, with a mean at 0 and a
    standard deviation of 100.
"""
np.random.seed(0)

s = pd.Series(np.random.normal(0,100,100_000))
#print(s.describe())
s[s == s.min()] = 5 * s.max()
#print(s.describe())

"""28 values of temperatues taken from a normal distribution with mean = 20 and standard deviation = 5, starts from Sun to Sat"""

np.random.seed(0)

days = "Sun Mon Tue Wed Thu Fri Sat".split(" ")
s = pd.Series(np.random.normal(20, 5, 28), index=days*4).round().astype(np.int8)

# what was the mean temperature on mondays?
monday_temp = s['Mon'].mean()

# what was the mean temperature on weekends (sat and sunday)? this is my logic
sat_temp = s['Sat'].mean()
weekend_temp = s['Sun'].mean() + sat_temp

# with fancy indexing
weekend_temp2 = s[['Sun','Sat']].mean()
print(weekend_temp2)
print(weekend_temp/2)

# common temperatures and how often does each appear?
common_temps = s.value_counts()
#print(common_temps)
