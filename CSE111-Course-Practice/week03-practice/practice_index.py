def main():
    """
    this program
    """
    full_address(country, state, city, state_code)

def full_address(country, state, city, state_code):
    address = f"Nigeria, Edo state, Benin city, 10231"
    index_position = address.index(", ")
    print("{index_position}")

if __name__ == "__main__":
    main()