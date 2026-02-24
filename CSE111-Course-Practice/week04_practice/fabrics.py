def main():
    # create an empty list ti hold the fabrics names.
    fabrics = []
    # add 3 element at the end of the fabrics list
    fabrics.append("velvet")
    fabrics.append("denim")
    fabrics.append("gingham")
    # insert an element at the beginning of the fabrics list
    fabrics.insert(0, "chiffon")
    print(fabrics)
    # determine if gingham is in the fabrics list
    if "gingham" in fabrics:
        print("gingham is in the fabrics list")
    else:
        print("gingham is NOT in the fabrics list")
    # get the index where velvet is store in the list
    i = fabrics.index("velvet")
    # replace the velvet with taffeta
    fabrics[i] = "taffeta"
    # remove the last element from the list
    fabrics.pop()
    # remove denim from the list
    fabrics.remove("denim")
    # get the length of the fabrics list
    length = len(fabrics)
    print(f"fabrics list contains {length} elements")
    print(fabrics)

       # Count from zero to nine by one.
    for i in range(10):
        print(i)
    print()
    # Count from five to nine by one.
    for i in range(5, 10):
        print(i)
    print()
    # Count from zero to eight by two.
    for i in range(0, 10, 2):
        print(i)
    print()
    # Count from 100 down to 70 by three.
    for i in range(100, 69, -3):
        print(i)

    # call the main function to start the program
if __name__ == "__main__":
    main()

