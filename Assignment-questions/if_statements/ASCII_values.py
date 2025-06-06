ch = input("Enter a single character: ")

if len(ch) != 1:
    print("Please enter exactly one character.")
else:
    ascii_val = ord(ch)  

    if 65 <= ascii_val <= 90:
        print("It is an UPPERCASE letter.")
    elif 97 <= ascii_val <= 122:
        print("It is a LOWERCASE letter.")
    elif 48 <= ascii_val <= 57:
        print("It is a DIGIT.")
    else:
        print("It is a SPECIAL SYMBOL.")
