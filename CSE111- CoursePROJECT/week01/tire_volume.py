import math
from datetime import date
# Write a program that will accept user input that describes a tire
# 
#  then calculate and display the tire's volume. Record the tire information in a log file.

#1 Have the user enter a tire width in mm.
#2 Have the user enter the aspect ratio.
#3 Have the user enter the diameter of the wheel in inches.
#4 Calculate and display the tire's volume.
#5 Log the information in a text file.
     # I.   current date (Do NOT include time)
     #  II. width of the tire
     #  III.aspect ratio of the tire
     #  IV. diameter of the wheel
     # V.   volume of the tire (rounded to two decimal places)
w = float(input("Enter the width of the tire in mm (ex 205): "))
a = float(input("Enter the aspect ratio (ex 50): "))
d = float(input("Enter the diameter of the wheel in inches (ex 14): "))



# formula for calculating the tire volume
V = (math.pi * w**2 *a *(w*a + 2540 * d))/10**10
# w is the width of the tire in millimeters
# a is  is the aspect ratio of the tire
# d is the diameter of the wheel in inches.
print(f"The volume of the tire is: {V:.2f} Litres")
today = date.today()
# Ask the user if she wants to buy tire and if "yes" ask for her
# phone number and save to file
phone_number = "N/A"
country_code = "N/A"
to_buy_tire = input("Do you want to buy this tire with the Dimensions entered? (YES/NO): ").strip().lower()
if to_buy_tire == "yes" :
    country_code = int(input("Please enter your country code (e.g., +1, +44, +234): "))
    phone_number = int(input("Please enter your phone number: "))

else:
    print("Goodbye!!")


with open ("volume.txt", "at") as tire_file:
    print(f"{today}, {w}, {a}, {d}, {V:.2f}, {country_code}-{phone_number}", file=tire_file)

# To find the price of four different tires
# he program calculates the tire volume, and the price is 
# an estimated value based on similar tire sizes obtained 
# from online retailers.

small_price = 61.97 
medium_price = 84.37
large_price = 100
extra_large_price = 125.99
sales_tax = 0.07
price = 0
if V <= 34.12:
   price = small_price +small_price*sales_tax
   print("Small tire selected")
elif V <= 37.50:
    price = medium_price + medium_price*sales_tax
    print("Medium tire selected")
elif V <= 39.50:
    price = large_price + large_price*sales_tax
    print("Large tire selected")
else:
     price = extra_large_price + extra_large_price*sales_tax
     print("Extra large tire selected")
print(f"Price of tire is ${price:.2f}" )
     
