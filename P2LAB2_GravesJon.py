num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())

''' Type your code here. '''
# Multiply all the inputs.
product_all=num1*num2*num3*num4
# Add up all the inputs.
sum_all=num1+num2+num3+num4

# Output the product and sum with 0 decimal places.
print(f"{product_all:.0f} {sum_all/4:.0f}")
# Output the product and sum with 3 decimal places.
print(f"{product_all:.3f} {sum_all/4:.3f}")