#
char=str(input("Enter a character"))
if 'a'<='z':
    print(f"{char} is a capital letter.")
elif'a'<=char<='z':
    print(f"{char} is a small letter.")
else:
    print(f"{char} is not a letter.")