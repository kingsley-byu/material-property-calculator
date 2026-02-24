def main():
    province_list = read_list("provinces.txt")
    print(province_list)

    province_list.pop(0)
    province_list.pop()

    for i in range(len(province_list)):
        if province_list[i] == "AB":
            province_list[i] = "Alberta"

    count = province_list.count("Alberta")
    print()
    print(f" Alberta occurs {count} times in the list.")





def read_list(filename):
    list = []

    with open(filename, "rt") as text_file:
        for line in text_file:
           clean_line = line.strip()
           list.append(clean_line)

    return list
        
if __name__ =="__main__":
    main()


    

   
