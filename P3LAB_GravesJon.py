# Initialize the flag to determine if the year is a leap year
is_leap_year = False

# Read the input year   
input_year = int(input())

''' Type your code here. '''
# Check if the year is divisible by 4
if input_year % 4 == 0:
    # Check if the year is a century year
    if input_year % 100 == 0:
        # Check if the year is evenly divisible by 400
        if input_year % 400 == 0:
            is_leap_year = True
    else:
        is_leap_year = True

# Output the result
if is_leap_year:
    print(f"{input_year} - leap year")
else:
    print(f"{input_year} - not a leap year")