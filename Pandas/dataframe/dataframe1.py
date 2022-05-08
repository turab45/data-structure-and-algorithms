import pandas as pd

"""For this exercise, I want you to create a data frame that represents five different products sold by
a company. For each product, we’ll want to know the product ID number (any unique two-digit
integer will do), the product name, the wholesale price, the retail price, and the number of sales
of that product in the last month.
"""

# Task 1: Calculate how much net revenue you received from all of these sales.

df = pd.DataFrame([{'product_id':23, 'name':'computer', 'wholesale_price': 500,'retail_price':1000, 'sales':100},
{'product_id':96, 'name':'Python Workout', 'wholesale_price': 35,'retail_price':75, 'sales':1000},
{'product_id':97, 'name':'Pandas Workout', 'wholesale_price': 35,'retail_price':75, 'sales':500},
{'product_id':15, 'name':'banana', 'wholesale_price': 0.5,'retail_price':1, 'sales':200},
{'product_id':87, 'name':'sandwich', 'wholesale_price': 3,'retail_price':5, 'sales':300},])

net_rev = ((df['retail_price'] - df['wholesale_price']) * df['sales']).sum()
#print(net_rev)
# Beyond the exercise
# Task 2: On what products is our retail price more than twice the wholesale price?
task2 = df[df['retail_price'] >= 2*df['wholesale_price']]
#print(task2)

"""Because your store is doing so well, you’re able to negotiate a 30% discount on the
wholesale price of goods. Calculate the new net income."""

df['wholesale_price'] = (df['wholesale_price']/100) * 30
new_net_rev = ((df['retail_price'] - df['wholesale_price']) * df['sales']).sum()
#print(new_net_rev)