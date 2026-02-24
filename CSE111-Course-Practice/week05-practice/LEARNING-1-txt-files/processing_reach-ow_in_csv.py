import csv
#Indexes of some of the columns in the dentist.csv file.
COMPANY_NAME_INDEX = 0
NUM_EMPS_INDEX = 3
NUM_PATIENTS_INDEX = 4
def main():
# Open a file named dentists.csv and store a reference
    # to the opened file in a variable named dentists_file.
    with open("dentists.csv", "rt") as dentists_file:
        # Use the csv module to create a reader
            # object that will read from the opened file.
            reader = csv.reader(dentists_file)
        # The first row of the CSV file contains column
            # headings and not data about a dental office,
            # so this statement skips the first row of the
            # CSV file.
            next(reader)
            running_max = 0
            most_office = ""
        # Read each row in the CSV file one at a time.
            # The reader object returns each row as a list.
            for row_list in reader:
        # For the current row, retrieve the
                # values in columns 0, 3, and 4
                company = row_list[COMPANY_NAME_INDEX]
                num_of_employee = int(row_list[NUM_EMPS_INDEX])
                num_of_patients = int(row_list[NUM_PATIENTS_INDEX])
            # Compute the number of patients per
                # employee for the current dental office.
                patients_per_employee = num_of_patients/num_of_employee
            # If the current dental office has more
                # patients per employee than the running
                # maximum, assign running_max and most_office
                # to be the current dental office.
                if patients_per_employee > running_max:
                    running_max = patients_per_employee
                    most_office = company
            # Print the results for the user to see.
            print(f"{most_office} has {running_max} " "patient per employee")
            # Call the main function to start the program
if __name__ == "__main__":
      main()




                




