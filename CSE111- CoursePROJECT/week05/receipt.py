import csv
from datetime import datetime, timedelta
def main():
    try:
        KEY_INDEX = 0
        # Call the read_dictionary function , store the return dictionary in the variable products_dict
        products_dict = read_dictionary("products.csv", KEY_INDEX)
        
        PRODUCT_INDEX = 1
        PRODUCT_PRICE = 2
        # Open the request.csv file for reading
        with open("request.csv", "rt") as request_file:
            # Use the csv.reader to read the file
            reader = csv.reader(request_file)
            # Skip the first line
            next(reader)
            print("MR BIGG'S GROCERY STORE".center(30))
            print("="*30)
            #total price of item
            total_due_price = 0
            total_item_count = 0
            sales_tax_rate = 0.06
            total_amount_due = 0
            # Use a loop to read and process each row
            for product in reader:
                product_number = product[0]
                quantity = int(product[1])
            
                # store each row in the product dictionary
                product_info = products_dict[product_number]
                # Get the product information from the products.csv file
                product_name = product_info[PRODUCT_INDEX]
                product_price = float(product_info[PRODUCT_PRICE])
                
                # Print the product name, requested quantity, and product price.
                print(f"{product_name}: {quantity} @ {product_price}")       

                # Count the total item 
                total_item_count += quantity

                #  multiply each product by their price and sum the total price for all the quantity purchased
                total_due_price += product_price *quantity

                # To compute the the sales tax amount of 6% as the sales tax rate
                sales_tax_amount = total_due_price* sales_tax_rate

                # Compute the total amount due
                total_amount_due = total_due_price + sales_tax_amount
            # print an empty line
            print()
            #print the total item
            print(f"The total item ordered: {total_item_count}")
            # print the total price
            print(f"The Subtotal: {total_due_price:.2f}")

            # print the sales tax amount
            print(f"The sales tax amount: {sales_tax_amount:.2f}")

            # print the total amount due
            print(f"Total: {total_amount_due:.2f}")

            # Print a thank you message 
            print("Thank you for your patronage🥰")

            # Get the current date and time from your computer’s operating system 
            # and print the current date and time.
            now = datetime.now()
            print(now.strftime("%Y-%m-%d %H:%M:%S"))
        
            # this code print a reminder of how many days until the New Years Sale 
            # begins (Jan 1) at the bottom of the receipt.
            new_year = datetime(now.year + 1, 1, 1)
            days_left = new_year - now
            print(f"New year sales begins in {days_left.days} days ")
            
            # Write code to print a "return by" date that is 9:00 PM 30 days in the 
            # future at the bottom of the receipt.
            return_by = now + timedelta(days=30)
            return_by = return_by.replace(hour=21, minute=0, second=0)
            print(f"Return by: {return_by.strftime('%Y-%m-%d %I:%M %p')}")

            print("="*30)

    except FileNotFoundError as not_found_err:
        print("Error: Missing file")
        print(not_found_err)
        
    except KeyError as key_err:
        print(f"Error: unknown product ID in the request.csv file")
        print(key_err)

    except PermissionError as perm_err:
        print(perm_err)

    


            


def read_dictionary(filename, key_column_index):
    """This function reads the product data from the csv file
    passed to the function in the filename parameter. The dictionary
    key is contained in the csv data column indicated by the 
    key_column_index parameter, the value of each dictionary item 
    is the list derived from the values in the row of the csv file.
    parameter:
    - filename
    key_index_column 
    Return:
    a dictionary of products"""
    
    # create a dictionary to hold the content of the csv file
    compound_list = {}
    # Open the csv file for reading  and populate the compound 
    # dictionary with the content of the products.csv file
    with open(filename, "rt") as csv_file:
            #  use the csv.reader to read each row and store it in a variable 
        reader = csv.reader(csv_file)
        # skip the first line of the file
        next(reader)
        # Loop through line by line
        for content in reader:
            key = content[key_column_index]
            compound_list[key] = content
        return compound_list
    
if __name__ == "__main__":
    main()

