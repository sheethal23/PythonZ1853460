#!/usr/bin/env python3

# display a welcome message
print("The Miles Per Gallon program")
print()

# get input from the user
miles_driven= float(input("Enter miles driven:\t\t\t"))
gallons_used = float(input("Enter gallons of gas used:\t"))
cost_per_gallon = float(input("Enter cost per gallon:\t\t"))

# calculate miles per gallon
#mpg = miles_driven / gallons_used
mpg = round(miles_driven / gallons_used, 1)
total_gas_cost = (gallons_used * cost_per_gallon)
cost_per_mile = round((1/mpg)*cost_per_gallon, 1)
            
# format and display the result
print()
print("Miles Per Gallon:\t" + str(mpg))
print("Total Gas Cost:\t\t" + str(total_gas_cost))
print("Cost Per Mile:\t\t" + str(cost_per_mile))
print()
print("Bye")


