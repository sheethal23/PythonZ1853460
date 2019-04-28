#!/usr/bin/env python3

from decimal import Decimal
from decimal import ROUND_HALF_UP
import locale as lc

# display a title
print("The Invoice program")
print()

choice = "y"
while choice == "y":
    
    # get user entry
    order_total = Decimal(input("Enter order total:     "))
    order_total = order_total.quantize(Decimal("1.00"), ROUND_HALF_UP)
    print()               

    # determine discount percent
    if order_total > 0 and order_total < 100:
        discount_percent = Decimal("0")
    elif order_total >= 100 and order_total < 250:
        discount_percent = Decimal(".1")
    elif order_total >= 250:
        discount_percent = Decimal(".2")

    # calculate results
    discount = order_total * discount_percent
    discount = discount.quantize(Decimal("1.00"), ROUND_HALF_UP)                                
    subtotal = order_total - discount
    Shippingcost = subtotal*Decimal("0.085")
    shippingcost = Shippingcost.quantize(Decimal("1.00"), ROUND_HALF_UP)
    tax_percent = Decimal(".05")
    sales_tax = subtotal * tax_percent
    sales_tax = sales_tax.quantize(Decimal("1.00"), ROUND_HALF_UP)                                 
    invoice_total = subtotal + sales_tax

    # display the results
    result = lc.setlocale(lc.LC_ALL, "")
    if result == "C":
        lc.setlocale(lc.LC_ALL, "en_US")
    line = "{:20}{:>10}"
    print(line.format("Order total:", lc.currency(order_total, grouping=True)))
    print(line.format("Discount amount:", discount))
    print(line.format("Subtotal:", subtotal))
    print(line.format("Shipping cost:", shippingcost))
    print(line.format("Sales tax:", sales_tax))
    print(line.format("Invoice total:", lc.currency(invoice_total, grouping=True)))
    print()

    choice = input("Continue? (y/n): ")    
    print()
    
print("Bye")
