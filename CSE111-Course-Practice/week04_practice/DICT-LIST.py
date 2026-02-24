# Example 7
def main():
    # Create a list that contains five student numbers.
    numbers_list = ["42-039-4736", "61-315-0160",
            "10-450-1203", "75-421-2310", "07-103-5621"]
    # Create a list that contains five student names.
    names_list = ["Clint Huish", "Amelia Davis",
            "Ana Soares", "Abdul Ali", "Amelia Davis"]
    # Convert the numbers and names lists into a dictionary

    student_dict = dict(zip(numbers_list, names_list))
    # print the entire student dictionary
    print("Dictionary:", student_dict)

    # Convert the student dictionary into
    # two lists named keys and values
    keys = list(student_dict.keys())
    values = list(student_dict.values())
    # print both list
    print("keys:", keys)
    print("values:", values)

    # call the main function to start the program
if __name__ == "__main__":
    main()



