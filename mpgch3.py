#!/usr/bin/env python3

# display a welcome message
print("The Miles Per Gallon application")
print()

choice = "y"

while choice == "y":
    # get input from the user
    miles_driven = float(input("Enter miles driven:         "))
    gallons_used = float(input("Enter gallons of gas used:  "))
    cost_per_gallon = float(input("Enter cost per gallon:\t\t"))

    if miles_driven <= 0:
        print("Miles driven must be greater than zero. Please try again.")
    elif gallons_used <= 0:
        print("Gallons used must be greater than zero. Please try again.")
    else:
        # calculate and display miles per gallon
        mpg = round((miles_driven / gallons_used), 2)
        total_gas_cost = (gallons_used * cost_per_gallon)
        cost_per_mile = round((1 / mpg) * cost_per_gallon, 1)

        print()
        print("Miles Per Gallon:          ", mpg)
        print("Total Gas Cost:\t\t\t\t" + str(total_gas_cost))
        print("Cost Per Mile:\t\t\t\t" + str(cost_per_mile))

        choice = input("Get entries for another trip (y/n) : ")


print("\nBye")




