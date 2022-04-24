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
print(s)

#print(avg_final_half_year)
#print(avg_final_half_year2)


"""====================================== EXERCISE 1: Test Scores ========================="""


