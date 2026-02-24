LOWER=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS=["0","1","2","3","4","5","6","7","8","9"]
SPECIAL=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", "\"", ",", ".", "<", ">", "?", "/", "\\","`", "~"]

def word_in_file(word, filename, case_sensitive=False):
    """This function reads a file (specified by the filename parameter) in which each line of the file contains
      a single word. If the word passed in the word parameter matches a word in the file the function returns a
        true otherwise it returns a false. If the parameter case_sensitive is true a case sensitive match is performed.
          If case_sensitive is false a case insensitive match is performed. The case_sensitive parameter should default to False
          Parameters
        word, filename, case_sensitive
        Return Type: Boolean"""
    with open(filename, "r",encoding="utf-8") as file1:
        for line in file1:
            current_word = line.strip()
            if case_sensitive:
                if current_word == word:  
                  return  True
            
            else:
                if current_word.lower() == word.lower():   
                  return True
            
    return False



def word_has_character(word, character_list):
    """This function loops through each character in the string passed in the word parameter to see if that character is in the
      list of characters passed in the character_list parameter. If any of the characters in the word are present in the character
        list return a true, If none of the characters in the word are in the character list return false
        Parameters: word, character_list
        Return Type: Boolean"""
    for i in word:
        if i in character_list:
            return True
    return False

def word_complexity(word):
    """This function creates a numeric complexity value based on the types of characters the word parameter contains. One point of
       complexity is given for each type of character in the word. The function calls the word_has_character function for each of
       the 4 kinds of characters (LOWER, UPPER, DIGITS, SPECIAL). If the word has that kind of character a point is added to 
       complexity rating. Since there are 4 kinds of characters the complexity rating will range from 0 to 4. (0 would be
       returned only if word contained no characters or only contains characters that are not in any of the lists.)
       Parameters: word
       Return Tpe:Integer"""
    
    complexity_rating = 0
    if word_has_character(word, LOWER):
        complexity_rating += 1
    if word_has_character(word, UPPER):
       complexity_rating += 1

    if word_has_character(word, DIGITS):
        complexity_rating += 1
    if word_has_character(word, SPECIAL):
         complexity_rating += 1
    return complexity_rating

def password_strength(password, min_length=10, strong_length=16):
    DICTIONARY_FILE = "wordlist.txt"
    TOP_PASSWORD_FILE = "toppasswords.txt"
    if word_in_file(password, DICTIONARY_FILE, case_sensitive=False):
        print("Password is a dictionary word and is not secure.")
        return 0

    if word_in_file(password, TOP_PASSWORD_FILE, case_sensitive=True):
        print("Password is a commonly used password and is not secure.")
        return 0
    
    if len(password) < min_length:
        
        print("Password is too short and not secure.")
        return 1
    
    if len(password) >= strong_length:
        print("Password is long, length trumps complexity; this is a good password.")
        return 5

    
    complexity_rating =  word_complexity(password)
    strength = complexity_rating + 1
    print(f"The password strength based on complexity is {strength}")
    if strength > 5:
        strength = 5
    return strength


# This function describe the strength rating of the password the user entered, 
# and display either very week, weak, fair, strong and very strong
def describe_strength(strength):
    """This function check if password is:
    - very weak
    - weak
    - fair
    - strong
    - very strong
    and return the strength of the password based on the rating (from 1 to 5)"""
    if strength <= 1:
        return "❌ very weak"
    elif strength == 2:
        return "😒 weak"
    elif strength == 3:
        return "Fair 🙁🙁"
    elif strength == 4:
        return "Strong 💪✅"
    else:
        return "Very strong 💪💪✅✅"




def main():
    while True:
        password = input("Enter a password to test('q' or 'Q' to quit): ")
        if password.lower() == "q":
            print("Have a good day")
            break
        else:
            strength = password_strength(password)
            print(f"Password strength rating: {strength} {describe_strength(strength)}")


if __name__ == "__main__":
    main()