def main():
    # Create a dictionary with student IDs as
    # the keys and student names as the values.
    students_dict = {
        "42-039-4736": "Clint Huish",
        "61-315-0160": "Amelia Davis",
        "10-450-1203": "Ana Soares",
        "75-421-2310": "Abdul Ali",
        "07-103-5621": "Amelia Davis" }
    
    # Add an item to the dictionary
    students_dict["81-298-9238"] = "Sama Patel"
    # Remove an item from  the dictionary
    students_dict.pop("61-315-0160")
    # Get the length of the dictionary
    length = len(students_dict)
    # Print the length of the dictionary
    print(f"Length: {length}")
    # Print the entire dictionary
    print(students_dict)
    print()
    # Get the ID from the user 
    id = input("Enter the student ID ")
    #Check if the student ID is in the dictionary 
    #if id in students_dict:
        # Find the student ID  in the dictionary and
        # retrieve the corresponding student name
    name = students_dict[id]
        # print the student name
    print(name)
    #else:
    print("No such student")
    # call the main function to start the program
if __name__ =="__main__":
    main()
