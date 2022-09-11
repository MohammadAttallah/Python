# 1- import string module
# 2- store all characters in list (upper/lower case, digits, punctuations)
# 3- take number of character from user
# 4 - make sure the number of character is 8 or more
# 5 - shuffle all lists
# 6 - calculate 30% and 20% of number of characters
# 7 - create password 60% letters and 40% digits and punctuations

def password_generator(characters_number):
    import string
    import random

    lowerlist = list(string.ascii_lowercase)
    upperlist = list(string.ascii_uppercase)
    digitlist = list(string.digits)
    punclist = list(string.punctuation)
    ##test if the input is valid or not
    while True:
        try:
            characters_number = int(characters_number)  # convert the input to int
            if characters_number < 8:
                print("you need at least 8 characters")
                characters_number = input("please enter the number again:  ")
            else:
                break
        except:
            print("please enter number only")
            characters_number = input("How many characters for the password?:  ")

    random.shuffle(lowerlist)
    random.shuffle(upperlist)
    random.shuffle(digitlist)
    random.shuffle(punclist)

    part1 = round(characters_number * 0.3) # calculate the lower and upper part
    part2 = round(characters_number * 0.2) # calculate the digit and punc part


    password = []
    for x in range(part1):
        password.append(lowerlist[x])
        password.append(upperlist[x])

    for x in range(part2):
        password.append(digitlist[x])
        password.append(punclist[x])

    random.shuffle(password)
    password = "".join(password[0:])
    return password



characters_number = input("How many characters for the password?:  ")

print(password_generator(characters_number))
