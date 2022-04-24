from re import M
import numpy as np
import pandas as pd

"""====================================== EXERCISE 1 ========================="""
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

print(avg_final_half_year)
print(avg_final_half_year2)

"""===================================================================="""

