import random
words = ['big', 'red', 'funny', 'baby', 'yellow', 'wait', 'python', 'joseph']
def main():
    numbers = [16.2, 75.1, 52.3]
    word_list = []
    print(numbers)
    append_random_numbers(numbers)
    print(numbers)
    append_random_numbers(numbers, 3)
    print(numbers)
    
    append_word_list(word_list)
    print(word_list)
    append_word_list(word_list, 4)
    print(word_list)

def append_word_list(w_list, quantity=1):
    for _ in range(quantity):
        w_list.append(random.choice(words))


def  append_random_numbers(numbers_list, quantity=1):
    for _ in range(quantity):
        num = random.uniform(0,100)
        num = round(num, 1)
        numbers_list.append(num)

if __name__ == "__main__":
    main()


    
