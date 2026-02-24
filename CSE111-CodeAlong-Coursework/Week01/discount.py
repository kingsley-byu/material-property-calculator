from datetime import datetime
DISCOUNT_DAYS = [1, 2]  # Tuesday and Wednesday
DISCOUNT_RATE = 0.10  # 10% discount
TAX_RATE = 0.06
dow = datetime.now().weekday()
quantity = 1
subtotal = 0
while quantity != 0:
   quantity = int(input("Enter the quantity: "))
   if quantity != 0: 
     price= float(input( "Enter the price: "))
     subtotal += quantity * price

print(f"Total Order: ${subtotal:.2f}")
discount = 0
if dow == 1 or dow == 2 :   # 1 = Tuesday 2 = wednesday
   # if dow  in [1,2]:  another way to write it
   #If dow in DISCOUNT_DAYS: another way to write it
   if subtotal >= 50:   
      discount = round(subtotal * DISCOUNT_RATE, 2)
      print(f"discount: ${discount:.2f}")
   else:
      short = 50 - subtotal 
      print(f"You can get a discount by ordering ${short:.2f} more!")
subtotal -= discount
tax = subtotal * TAX_RATE
total = subtotal + tax
print(f"tax: ${tax:.2f}")
print(f"total Due: ${total:.2f}")

