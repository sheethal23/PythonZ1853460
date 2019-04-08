#!/usr/bin/env python3


def calculate_future_value(monthly_investment, yearly_interest, years):
    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest / 12 / 100
    months = years * 12

    # calculate future value
    future_value = 0.0
    for i in range(0, months):
        future_value += monthly_investment
        monthly_interest = future_value * monthly_interest_rate
        future_value += monthly_interest

    return future_value


def get_float():
    # monthly_investment = float(input("Enter monthly investment:\t"))
    count = 1
    while True:
        monthly_investment = float(input("Enter monthly investment:\t"))
        if monthly_investment > 0 and monthly_investment <= 1000:
            count += 1
            return monthly_investment
        else:
            print("Entry must be greater than 0 and less than or equal to 1000")
            count += 1


def get_float2():
    count = 1
    while True:
        yearly_interest_rate = float(input("Enter yearly interest rate:\t"))
        if yearly_interest_rate > 0 and yearly_interest_rate <= 15:
            count += 1
            return yearly_interest_rate
        else:
            print("Entry must be greater than 0 and less than or equal to 15")
            count += 1


def get_int():
    count = 1
    while True:
        years = int(input("Enter number of years:\t\t"))
        if years > 0 and years <= 50:
            count += 1
            return years
        else:
            print("Entry must be greater than 0 and less than or equal to 1000")
            count += 1


def main():
    choice = "y"
    while choice.lower() == "y":
        # get input from the user
        monthly_investment = get_float()
        yearly_interest_rate = get_float2()
        years = get_int()

        monthly_interest_rate = yearly_interest_rate / 12 / 100
        months = years * 12

        # calculate future value
        future_value = 0.0
        for i in range(0, months):
            future_value += monthly_investment
            monthly_interest = future_value * monthly_interest_rate
            future_value += monthly_interest

        print("Future value:\t\t\t" + str(round(future_value, 2)))
        print()

        # see if the user wants to continue
        choice = input("Continue? (y/n): ")
        print()

    print("Bye!")


if __name__ == "__main__":
    main()
