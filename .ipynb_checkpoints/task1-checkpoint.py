%matplotlib inline

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statistics

#from Assignment 12, task 2:

# creating the array with income values for 10 months
income = np.array([500,1000,2500,3300,4700,15600,13000,9000,27000, 30900])

# multiplying every value in the array by 0.7 to get the amount before tax
income_without_tax = income*0.7

# creating the array with expense values for 10 months
expenses = np.array([500,500,600,900,3000,5000,3400,900,7000,15000])


# creating a data frame based on expenses and income

# first, making a list with all the months names
months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct"]

# second, creating the dictionary as the foundation for the data frame
data = {'Month': months, 'Income without tax': income_without_tax, 'Expenses':expenses}

# data frame itself
df = pd.DataFrame(data)
print()


df["Savings"] = df["Income without tax"] - df["Expenses"]
df["Profit"] = df["Savings"]>0
   
# now, outputting it; using to_string to get rid of the index column
print("Income/Expenses/Savings/Profit Data Frame:")
print("----------------------------------------------------")
print(df.to_string(index=False))

# selecting the first 3 months (indexes 0,1,2)
quarter = df.iloc[0:3]      
print()
print()
# outputting the data for the first quarter
print("First Quarter Only:")
print("----------------------------------------------------")
print(quarter.to_string(index=False))




# Assignment 13 ->


# plotting income by month
plt.plot(df['Month'], income_without_tax, marker='.', linestyle='-', color='m')
plt.title('Income by Month')
plt.xlabel('Month')
plt.ylabel('Income')
plt.show()

# creating a column chart diagram to show savings for each month
plt.bar(df['Month'],df['Savings'], color='c')
plt.title('Savings by Month')
plt.xlabel('Month')
plt.ylabel('Savings')
plt.show()


# making a pie chart diagram
positive_savings = df['Savings'][df['Savings'] > 0]
plt.pie(positive_savings, labels=df['Month'][df['Savings'] > 0], colors = plt.cm.Pastel1.colors)
plt.title('Monthly Savings in Total Yearly Savings')
plt.show()

# outputting the average income for quarters
quarter_incomes = [df.iloc[0:3],df.iloc[3:6],df.iloc[6:9],df.iloc[9:10]]


print("Average Income by Quarter:")
print()
k=1
for i in quarter_incomes:
    print(f'Quarter {k} average = {statistics.mean(i["Income without tax"]):.2f}')
    k += 1
