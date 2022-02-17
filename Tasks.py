#1
def payment():
    working_hours = float(input("Enter hours: "))
    rate_of_wage = float(input("Enter rate: "))
    pay = working_hours * rate_of_wage
    print(f"Pay: {pay}")


#2
def numbers():
    sum = count = 0
    while True:
        number = input("Enter a number:")
        if number == "done":
            break
        try:
            float(number)
            sum += float(number)
            count += 1
        except:
            print("Invalid input")
    print(f"Sum:{sum}, count:{count}, mean:{sum / count}")


#3
def letter():
    letter = input("Enter the letter: ")
    lst_vowel = ["a","e","i","o","u"]
    lst_consonant = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z']
    if letter == "y":
        print("Letter is vowel and consonant")
    elif letter in lst_vowel:
        print("Letter is vowel")
    elif letter in lst_consonant:
        print("Letter is consonant")
    else:
        print("Wrong input")


#4
def chess_color():
    letters = ['a','b','c','d','e','f','g','h']
    letter = input("Enter letter coord: ").lower()
    dig = int(input("Enter digital coord: "))
    if letter in letters and 0 < dig < 9:
        index = letters.index(letter)
        if (index + 1) % 2 == dig % 2:
            print("Color is black")
        else:
            print("Color is white")
    else:
        print("Wrong input")


#5
def fahrenheit_to_celsius():
    fahr = float(input("Enter temperature in fahrenheits: "))
    celsius = (fahr - 32) / 1.8
    print(f"Temperature in celsius is {celsius}:")









