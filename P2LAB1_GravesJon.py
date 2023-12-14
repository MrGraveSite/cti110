''' Type your code here. '''
mile_per_gallon = float(input())
dollar_per_gallon = float(input())

#Calculate the unit cost.
unit_cost = dollar_per_gallon / mile_per_gallon

#Evaluate the cost for the 20 miles.
your_value1 = unit_cost * 20

#Evaluate the cost for 75 miles
your_value2 = unit_cost * 75

#Evaluate the cist for 500 miles
your_value3 = unit_cost * 500

#Print the result and format the out put up to 2 decimal places.
print(f'{your_value1:.2f} {your_value2:.2f} {your_value3:.2f}')