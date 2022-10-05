'''
Let us say your expense for every month are listed below,
January - 2200
February - 2350
March - 2600
April - 2130
May - 2190

Create a list to store these monthly expenses and using that find out,

1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this
'''

from traceback import print_tb


expense_per_month = [["January",2200],["February",2350],["March",2600],["April",2130],["May",2190]]

# 1. In Feb, how many dollars you spent extra compare to January?
print("In feb this much extra was spent compared to jan:",expense_per_month[1][1]-expense_per_month[0][1]) # 150

# 2. Find out your total expense in first quarter (first three months) of the year.
print("Expense for first quarter:",expense_per_month[1][1]+expense_per_month[0][1]+expense_per_month[2][1]) # 7150


# 3. Find out if you spent exactly 2000 dollars in any month
print("Did I spent 2000$ in any month? ", 2000 in expense_per_month) # False


# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list

expense_per_month.append(["june",1980])

# print all list
print(expense_per_month)