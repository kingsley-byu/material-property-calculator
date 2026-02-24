import csv
def read_dictionary(filename, key_column_index):
    student_dictionary = {}
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
            key_value = row[key_column_index]
            student_dictionary[key_value] = row
    return student_dictionary
def main():
    KEY_INDEX = 0
    NAME_INDEX = 1
    students = read_dictionary("students.csv", KEY_INDEX)
    ID = input("Please enter the student ID: ")
    ID = ID.replace("-", "")
    if not ID.isdigit():
        print("Invalid I-Number")

    elif len(ID) < 9:
        print("Invalid ID Number: too few digits")
    
    elif len(ID) > 9:
        print("Invalid ID Number: Too many digits")
        

    else:

        if ID in students:

            student = students[ID]
            name = student[NAME_INDEX]
            print(f"The student name is {name}")
        else:
            print("No such student")
if __name__  =="__main__":
    main()