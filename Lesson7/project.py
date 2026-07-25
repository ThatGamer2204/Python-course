print("===========ASCII code checker============")
char=input("Enter EXACTLY ONE character :")
if len(char)==1:
    ascii_val=ord(char)
    print(f"\nCharacter is '{char}'")
    print(f"ASCII code for '{char}' is '{ascii_val}'.")

    print("\nCharacter Type :")
    if ascii_val>=65 and ascii_val<=90:
        print("Uppercase Letter")
    elif ascii_val>=97 and ascii_val<=122:
        print("Lowercase Letter")
    elif ascii_val>=48 and ascii_val<=57:
        print("Digit")
    elif ascii_val==32:
        print("Space")
    else:
        print("Special Character")
else:
    print("INVALID CHARACTER, Please Enter ONLY ONE CHARACTER!!!")